"""L32 — A release gate that reads evidence (M20, Challenge).

Goal: assemble the evidence an earlier lab produced into one gate, make the decision mechanical, and show that a
missing or failed item blocks the release with a reason.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import pandas as pd

from labkit import check, report

# === WORK STARTS HERE ===
# STEP 1: the gate specification — required items, thresholds and the lab that produces each one.
SPEC = [
    {"id": "G1", "item": "utility", "metric": "accuracy", "threshold": 0.75, "produced_by": "L02"},
    {"id": "G2", "item": "robustness", "metric": "accuracy_under_pgd", "threshold": 0.15, "produced_by": "L12"},
    {"id": "G3", "item": "privacy", "metric": "membership_2auc_minus_1", "threshold": 0.25, "produced_by": "L14",
     "direction": "below"},
    {"id": "G4", "item": "injection", "metric": "tool_call_asr", "threshold": 0.0, "produced_by": "L19",
     "direction": "below"},
    {"id": "G5", "item": "retrieval ACL", "metric": "suite_pass_rate", "threshold": 1.0, "produced_by": "L22"},
    {"id": "G6", "item": "artefact integrity", "metric": "manifest_match", "threshold": 1.0, "produced_by": "L24"},
    {"id": "G7", "item": "agent authorisation", "metric": "unauthorised_allows", "threshold": 0.0, "produced_by": "L23",
     "direction": "below"},
    {"id": "G8", "item": "red-team coverage", "metric": "cells_reproduced_ratio", "threshold": 0.8,
     "produced_by": "L28"},
]


def evaluate(evidence):
    """Return (decision, rows). Missing evidence is a block, never a warning."""
    rows = []
    for gate in SPEC:
        record = evidence.get(gate["id"])
        if record is None:
            rows.append({"id": gate["id"], "item": gate["item"], "value": None, "status": "blocked",
                         "reason": "evidence missing"})
            continue
        value = record["value"]
        direction = gate.get("direction", "above")
        passed = value >= gate["threshold"] if direction == "above" else value <= gate["threshold"]
        rows.append({"id": gate["id"], "item": gate["item"], "value": value,
                     "status": "pass" if passed else "blocked",
                     "reason": f"{direction} {gate['threshold']}"})
    table = pd.DataFrame(rows)
    return ("release" if (table.status == "pass").all() else "block"), table


# STEP 2: the candidate release, with every item present and passing.
complete = {
    "G1": {"value": 0.839, "source": "labs/solutions/L02/solution.py stdout"},
    "G2": {"value": 0.234, "source": "labs/solutions/L13/solution.py stdout"},
    "G3": {"value": 0.054, "source": "labs/solutions/L14/solution.py stdout"},
    "G4": {"value": 0.00, "source": "labs/solutions/L19/solution.py stdout"},
    "G5": {"value": 1.00, "source": "labs/solutions/L22/solution.py stdout"},
    "G6": {"value": 1.00, "source": "labs/solutions/L24/solution.py stdout"},
    "G7": {"value": 0.00, "source": "labs/solutions/L23/solution.py stdout"},
    "G8": {"value": 1.00, "source": "labs/solutions/L28/solution.py stdout"},
}
decision, table = evaluate(complete)
report("complete evidence", table)
print("decision:", decision)
check(decision == "release", "complete passing evidence must release")

# STEP 3: three ways the same gate blocks — missing, below threshold, and the wrong direction.
missing = {k: v for k, v in complete.items() if k != "G5"}
decision_missing, table_missing = evaluate(missing)
weak = {**complete, "G2": {"value": 0.07, "source": "labs/solutions/L13/solution.py stdout"}}
decision_weak, table_weak = evaluate(weak)
leaky = {**complete, "G3": {"value": 0.42, "source": "labs/solutions/L14/solution.py stdout"}}
decision_leaky, table_leaky = evaluate(leaky)
report("blocked cases", pd.concat([
    table_missing[table_missing.status == "blocked"].assign(case="missing"),
    table_weak[table_weak.status == "blocked"].assign(case="weak robustness"),
    table_leaky[table_leaky.status == "blocked"].assign(case="privacy"),
]))
check(decision_missing == "block" and decision_weak == "block" and decision_leaky == "block",
      "missing, weak and leaky evidence must all block")

# STEP 4: a gate needs an accountable owner and an expiry.
governance = pd.DataFrame([
    {"field": "evidence path", "why": "the reviewer can open the artefact"},
    {"field": "producing lab and commit", "why": "the result is reproducible"},
    {"field": "threshold and direction", "why": "the rule is not negotiable at release time"},
    {"field": "owner and expiry", "why": "stale evidence is re-run, not inherited"},
])
report("evidence record", governance)

# STEP 5: the statement the gate lets you make.
print("\nThe gate does not say the system is safe. It says eight specific claims were tested, by named"
      " methods, against declared thresholds, on this build — and that a reviewer can check each one.")
