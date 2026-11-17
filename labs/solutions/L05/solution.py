"""L05 — Threat model and risk ranking for a hospital summariser (M04, Beginner).

Goal: turn a vague worry ("the AI could be attacked") into a ranked, evidenced threat register where every
row has an asset, a STRIDE category, a control and a way to test that control.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

from labkit import check, load_csv, report

# === WORK STARTS HERE ===
# STEP 1: state the system under assessment precisely enough to be wrong about it.
system = "clinical triage assistant: summarises referrals and suggests an urgency label"
referrals = load_csv("referrals.csv")
print("target system:", system)
print(f"in scope: {len(referrals)} referrals, fields {list(referrals.columns)}")

# STEP 2: build the register. Impact and likelihood are 1-5; residual_factor is what remains after the control.
threats = [
    {"id": "T1", "asset": "referral note", "stride": "Tampering", "atlas": "AML.T0051",
     "threat": "instruction in a referral changes the urgency label", "impact": 5, "likelihood": 4,
     "control": "treat note text as data; validate the urgency label", "residual_factor": 0.4,
     "test": "inject a payload in staging and assert the label is unchanged"},
    {"id": "T2", "asset": "model artefact", "stride": "Tampering", "atlas": "AML.T0010",
     "threat": "unsigned model file is deployed", "impact": 5, "likelihood": 2,
     "control": "signed hash manifest checked at load", "residual_factor": 0.2,
     "test": "swap one byte and assert the loader refuses"},
    {"id": "T3", "asset": "patient identifiers", "stride": "Information disclosure", "atlas": "AML.T0057",
     "threat": "identifiers leak into the summary", "impact": 5, "likelihood": 2,
     "control": "identifier allowlist before generation", "residual_factor": 0.3,
     "test": "run 100 summaries and grep for names and postcodes"},
    {"id": "T4", "asset": "audit log", "stride": "Repudiation", "atlas": "AML.T0024",
     "threat": "log edited after a bad decision", "impact": 4, "likelihood": 2,
     "control": "hash-chained, off-host log", "residual_factor": 0.2, "test": "edit a record and assert verification fails"},
    {"id": "T5", "asset": "summariser endpoint", "stride": "Denial of service", "atlas": "AML.T0029",
     "threat": "max-length requests exhaust the service", "impact": 3, "likelihood": 4,
     "control": "per-principal quota and input bound", "residual_factor": 0.5,
     "test": "send 50 max-length requests and expect 429"},
    {"id": "T6", "asset": "clinician decision", "stride": "Elevation of privilege", "atlas": "—",
     "threat": "clinician accepts a wrong summary without review", "impact": 5, "likelihood": 4,
     "control": "show source spans and require acknowledgement", "residual_factor": 0.6,
     "test": "usability review measures acknowledgement rate"},
]

# STEP 3: compute inherent and residual risk.
for row in threats:
    row["risk"] = row["impact"] * row["likelihood"]
    row["residual"] = round(row["risk"] * row["residual_factor"], 1)
ranked = sorted(threats, key=lambda r: -r["residual"])
report("ranked register", [
    {"id": r["id"], "threat": r["threat"][:52], "stride": r["stride"], "risk": r["risk"], "residual": r["residual"]}
    for r in ranked
])

# STEP 4: a register is only useful if every row can be tested and owned.
check(all(r["test"] for r in threats), "every threat needs a test")
check(all(r["control"] for r in threats), "every threat needs a control")
check(all(r["residual"] <= r["risk"] for r in threats), "a control must not increase risk")
check(ranked[0]["id"] == "T6", "the human-factors threat should top the residual ranking here")

# STEP 5: state what the ranking implies for budget.
top = ranked[0]
print(f"\nTop residual risk: {top['id']} — {top['threat']} ({top['residual']})")
print("Budget implication: the largest residual is a workflow control, not a model control.")
print("That is the normal result: the model is often the easiest part to harden.")
