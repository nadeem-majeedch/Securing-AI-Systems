"""L01 — Security properties audit of a clinical triage assistant (M01, Beginner).

Goal: classify the assistant's assets against confidentiality, integrity and availability, then find the
records in the referral feed that already violate the stated policy.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

from labkit import check, load_csv, report

ALLOWED_TRIAGE = {"green", "amber", "red"}
INJECTION_MARKERS = ("ignore previous instructions", "system:", "disregard")

# === WORK STARTS HERE ===
# STEP 1: load the referral feed and show its shape.
df = load_csv("referrals.csv")
print(f"referrals: {len(df)} rows, columns: {list(df.columns)}")

# STEP 2: map each asset to the security property it depends on.
assets = [
    {"asset": "referral notes", "property": "confidentiality", "why": "contain patient health detail"},
    {"asset": "triage label", "property": "integrity", "why": "drives the urgency decision"},
    {"asset": "summariser endpoint", "property": "availability", "why": "clinicians depend on it during a shift"},
    {"asset": "audit trail", "property": "integrity", "why": "evidence after a bad decision"},
]
report("asset to property map", assets)

# STEP 3: flag records that break the policy.
def issues(row):
    found = []
    if str(row["triage"]).strip().lower() not in ALLOWED_TRIAGE:
        found.append("unknown triage value")
    if str(row["triage"]) != str(row["triage"]).strip():
        found.append("padded triage label")
    if not 0 < int(row["age"]) < 120:
        found.append("implausible age")
    text = str(row["note"]).lower()
    if any(marker in text for marker in INJECTION_MARKERS):
        found.append("instruction in note")
    return "; ".join(found)

df["issues"] = df.apply(issues, axis=1)
flagged = df[df.issues != ""]

# STEP 4: summarise which property each defect threatens.
summary = [
    {"defect": "instruction in note", "property": "integrity", "count": int(df.issues.str.contains("instruction").sum())},
    {"defect": "implausible age", "property": "integrity", "count": int(df.issues.str.contains("age").sum())},
    {"defect": "padded triage label", "property": "integrity", "count": int(df.issues.str.contains("padded").sum())},
    {"defect": "unknown triage value", "property": "integrity", "count": int(df.issues.str.contains("unknown").sum())},
]
report("defects by property", summary)
print(flagged[["referral_id", "triage", "age", "issues"]].to_string(index=False))

# STEP 5: assert the audit found the seeded defects.
check(len(flagged) >= 3, "expected at least three policy-breaking rows")
check(summary[0]["count"] >= 2, "expected at least two injected notes")
print("\nAudit complete: every defect names the property it threatens, so each can be routed to a control.")
