"""L04 — Least-privilege access control for a data platform (M03, Intermediate).

Goal: implement a deny-by-default policy engine over roles, resources and actions, then prove with a test
matrix that the interesting failures are denied for the right reason.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

from labkit import check, report

PRINCIPALS = {
    "ana": {"team": "analytics", "roles": ["analyst"], "spend": 0},
    "ben": {"team": "support", "roles": ["support"], "spend": 50},
    "cara": {"team": "analytics", "roles": ["manager"], "spend": 500},
}
RESOURCES = {
    "dataset:raw": {"team": "analytics", "sensitive": True},
    "dataset:curated": {"team": "analytics", "sensitive": False},
    "ticket:4412": {"team": "support", "sensitive": False},
    "model:prod": {"team": "analytics", "sensitive": True},
}
POLICY = [
    {"action": "read", "roles": ["analyst", "manager"], "scope": "same_team"},
    {"action": "write", "roles": ["manager"], "scope": "same_team"},
    {"action": "export", "roles": ["manager"], "scope": "same_team", "requires": "sensitive_ok"},
    {"action": "refund", "roles": ["support", "manager"], "scope": "same_team"},
]


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L04/solution.py (open it only after trying).

# STEP 1: write the decision function. Deny is the default; every allow needs a reason.
# TODO 1: implement this step.

# STEP 2: run a matrix that contains both permitted and forbidden work.
# TODO 2: implement this step.

# STEP 3: deny-by-default must hold for an unknown principal and an unknown action.
# TODO 3: implement this step.

# STEP 4: least privilege — the support role cannot read a sensitive analytics dataset.
# TODO 4: implement this step.

# STEP 5: separate the two reasons a denial can have: identity and authority.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
