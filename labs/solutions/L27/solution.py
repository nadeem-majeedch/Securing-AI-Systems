"""L27 — Rate limits and abuse controls on a prediction API (M17, Intermediate).

Goal: read real-shaped gateway logs, apply fixed-window and token-bucket limits per principal, and measure the
trade between blocking an abusive client and inconveniencing honest ones.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd

from labkit import check, load_csv, report

ABUSIVE = "user-13"

# === WORK STARTS HERE ===
# STEP 1: load the logs and confirm the incident is visible before any control.
logs = load_csv("api_logs.csv")
logs["ts"] = pd.to_datetime(logs["ts"])
logs["window"] = logs["ts"].dt.floor("10min")
print(f"{len(logs)} requests, {logs.principal.nunique()} principals, "
      f"{logs.ts.min()} to {logs.ts.max()}")

per_principal = (logs.groupby("principal")
                 .agg(requests=("status", "size"), failures=("status", lambda s: int((s == 401).sum())),
                      bytes_out=("bytes_out", "sum"), exports=("endpoint", lambda s: int((s == "/export").sum())))
                 .sort_values("requests", ascending=False))
per_principal["failure_rate"] = (per_principal.failures / per_principal.requests).round(3)
report("top principals", per_principal.head(8).reset_index())

# STEP 2: fixed-window limit per principal per 10 minutes. A 1-minute window is too coarse for 2 req/min bursts.
LIMIT = 8
window_counts = logs.groupby(["principal", "window"]).size().rename("count").reset_index()
blocked = window_counts[window_counts["count"] > LIMIT].copy()
blocked["blocked_requests"] = blocked["count"] - LIMIT
print(f"\nfixed window {LIMIT}/10min: {int(blocked.blocked_requests.sum())} requests blocked "
      f"across {blocked.principal.nunique()} principals")

# STEP 3: honest-user cost, measured rather than assumed.
honest = blocked[blocked.principal != ABUSIVE]
print(f"honest principals affected: {honest.principal.nunique()}; "
      f"worst honest minute: {int(honest.blocked_requests.max()) if len(honest) else 0} requests over")

# STEP 4: token bucket with a burst allowance and a separate export quota.
CAPACITY, REFILL = 6.0, 1.5          # tokens, tokens per minute
state = {}
blocked_bucket, blocked_export = 0, 0
export_seen = {}
for row in logs.itertuples():
    tokens, last = state.get(row.principal, (CAPACITY, row.ts))
    elapsed = max((row.ts - last).total_seconds() / 60.0, 0.0)
    tokens = min(CAPACITY, tokens + elapsed * REFILL)
    export_seen[row.principal] = export_seen.get(row.principal, 0)
    if row.endpoint == "/export" and export_seen[row.principal] >= 3:
        blocked_export += 1
        tokens -= 1.0
    elif tokens < 1.0:
        blocked_bucket += 1
    else:
        tokens -= 1.0
        if row.endpoint == "/export":
            export_seen[row.principal] += 1
    state[row.principal] = (max(tokens, 0.0), row.ts)

print(f"token bucket: {blocked_bucket} blocked by rate, {blocked_export} blocked by export quota")

# STEP 5: compare the two controls on the same evidence.
abusive_fixed = int(blocked[blocked.principal == ABUSIVE].blocked_requests.sum())
report("control comparison", [
    {"control": f"fixed window {LIMIT}/10min", "abusive_blocked": abusive_fixed,
     "honest_principals_affected": int(honest.principal.nunique())},
    {"control": "token bucket + export quota", "abusive_blocked": blocked_bucket + blocked_export,
     "honest_principals_affected": 0},
])
check(abusive_fixed > 0, "the fixed window must catch the burst")
check(int(honest.principal.nunique()) <= 2, "the fixed window should barely touch honest traffic")
check(blocked_export >= 5, "the export quota must bite on the exfiltration burst")

# STEP 6: the limits are a policy decision, not a code decision.
print("\nA fixed window is easy to explain and easy to game at the boundary; a bucket tolerates legitimate"
      " bursts. Neither replaces an export quota, because the damage here is per megabyte, not per request.")
