"""L29 — Triaging suspicious usage in an AI service (M17, Intermediate).

Goal: rank principals by behavioural signals, show that the ranking surfaces the incident, and write the triage
note that turns a score into an investigation.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd

from labkit import check, load_csv, report

# === WORK STARTS HERE ===
# STEP 1: aggregate the logs per principal.
logs = load_csv("api_logs.csv")
logs["ts"] = pd.to_datetime(logs["ts"])
features = (logs.groupby("principal")
            .agg(requests=("status", "size"),
                 failure_rate=("status", lambda s: float((s == 401).mean())),
                 exports=("endpoint", lambda s: int((s == "/export").sum())),
                 bytes_out=("bytes_out", "sum"),
                 off_hours=("ts", lambda s: int((s.dt.hour < 6).sum())))
            .reset_index())
print(features.sort_values("requests", ascending=False).head().to_string(index=False))

# STEP 2: robust z-scores per signal, then a transparent sum.
signals = ["failure_rate", "exports", "bytes_out", "requests"]
scored = features.copy()
for name in signals:
    values = scored[name].to_numpy(dtype=float)
    median = np.median(values)
    mad = np.median(np.abs(values - median)) + 1e-9
    scored[f"z_{name}"] = (values - median) / (1.4826 * mad)
scored["signals_fired"] = (scored[[f"z_{n}" for n in signals]] > 3.0).sum(axis=1)
scored["score"] = scored[[f"z_{n}" for n in signals]].clip(lower=0).sum(axis=1)
ranked = scored.sort_values("score", ascending=False).reset_index(drop=True)
report("top suspects", ranked.head(5)[["principal", "score", "signals_fired", "failure_rate", "exports",
                                       "bytes_out"]].round(2))

# STEP 3: the incident is the top row, and it fires on more than one signal.
check(ranked.loc[0, "principal"] == "user-13", "the ranking must surface the incident principal")
check(ranked.loc[0, "signals_fired"] >= 2, "a single signal is not enough to open a case")
check(ranked.loc[0, "exports"] > 10, "the export burst must be visible in the ranking")

# STEP 4: triage note template — what an analyst records before acting.
note = pd.DataFrame([
    {"field": "principal", "value": ranked.loc[0, "principal"]},
    {"field": "first seen", "value": str(logs[logs.principal == ranked.loc[0, "principal"]].ts.min())},
    {"field": "evidence", "value": "401 burst then /export burst, 4800 bytes per call"},
    {"field": "hypothesis", "value": "credential stuffing followed by data exfiltration"},
    {"field": "next step", "value": "revoke key, check downstream copies, preserve logs"},
])
report("triage note", note)

# STEP 5: what the score cannot tell you.
print("\nThe score ranks behaviour; it does not establish intent. user-13 could be a broken integration.")
print("A triage note states the hypothesis and the next step, and never states the conclusion as fact.")
