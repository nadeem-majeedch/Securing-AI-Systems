"""L06 — Intake validation and quarantine for patient referrals (M05, Beginner).

Goal: reject dirty rows at the boundary with a stated reason, without silently dropping anything. The count
accepted plus the count quarantined must equal the input count.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import pandas as pd

from labkit import check, load_csv, report

ALLOWED_TRIAGE = {"green", "amber", "red"}
INJECTION = ("ignore previous instructions", "system:", "disregard")


# === WORK STARTS HERE ===
# STEP 1: load raw input and record the original count.
raw = load_csv("referrals.csv")
print(f"received {len(raw)} referrals")

# STEP 2: define one validator per column, each returning a reason or None.
def validate_row(row):
    reasons = []
    if not 0 < int(row["age"]) < 120:
        reasons.append("age out of range")
    triage = str(row["triage"])
    if triage != triage.strip():
        reasons.append("triage has surrounding whitespace")
    if triage.strip().lower() not in ALLOWED_TRIAGE:
        reasons.append("triage value not in allowlist")
    if str(row["source"]) not in {"portal", "fax", "email"}:
        reasons.append("unknown source")
    note = str(row["note"]).lower()
    if any(marker in note for marker in INJECTION):
        reasons.append("instruction-like text in note")
        return "; ".join(reasons)          # never normalise an injected note: quarantine it
    if len(note) < 5:
        reasons.append("note too short to summarise")
    return "; ".join(reasons)


# STEP 3: partition into accepted and quarantined, keeping the reason.
rows = raw.to_dict("records")
accepted, quarantined = [], []
for row in rows:
    reason = validate_row(row)
    if reason:
        quarantined.append({**row, "reason": reason})
    else:
        accepted.append(row)

print(f"accepted {len(accepted)} | quarantined {len(quarantined)}")
check(len(accepted) + len(quarantined) == len(raw), "no row may be silently dropped")

# STEP 4: summarise the reasons so the source team can fix the feed.
report("quarantine reasons", [
    {"reason": reason, "rows": int(count)}
    for reason, count in pd.Series([q["reason"] for q in quarantined]).value_counts().items()
])
print(pd.DataFrame(quarantined)[["referral_id", "source", "reason"]].to_string(index=False))

# STEP 5: assert the policy outcomes that matter.
check(any("instruction-like" in q["reason"] for q in quarantined), "injected notes must be quarantined")
check(any("age out of range" in q["reason"] for q in quarantined), "the implausible age must be caught")
check(all(str(a["triage"]) == str(a["triage"]).strip() for a in accepted), "accepted labels are clean")
print("\nAccept + quarantine = input. The reason column is the message the supplier needs to fix the feed.")
