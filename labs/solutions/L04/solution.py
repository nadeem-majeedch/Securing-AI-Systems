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
# STEP 1: write the decision function. Deny is the default; every allow needs a reason.
def decide(principal, action, resource, amount=0):
    person = PRINCIPALS.get(principal)
    if person is None:
        return False, "unknown principal"
    rule = next((r for r in POLICY if r["action"] == action), None)
    if rule is None:
        return False, "unknown action"
    if not set(rule["roles"]) & set(person["roles"]):
        return False, "role not permitted"
    resource_meta = RESOURCES.get(resource)
    if resource_meta is None:
        return False, "unknown resource"
    if rule["scope"] == "same_team" and resource_meta["team"] != person["team"]:
        return False, "cross-team resource"
    if rule.get("requires") == "sensitive_ok" and resource_meta["sensitive"] and person["spend"] < 100:
        return False, "sensitive export requires elevated approval"
    if amount > person["spend"]:
        return False, "spend limit exceeded"
    return True, "allowed"


# STEP 2: run a matrix that contains both permitted and forbidden work.
cases = [
    ("ana", "read", "dataset:curated"),
    ("ana", "read", "dataset:raw"),
    ("ana", "write", "dataset:curated"),
    ("ben", "read", "ticket:4412"),
    ("ben", "read", "dataset:curated"),
    ("cara", "export", "dataset:raw"),
    ("cara", "export", "model:prod"),
    ("cara", "refund", "ticket:4412"),
    ("ben", "refund", "ticket:4412"),
    ("mallory", "read", "dataset:curated"),
]
rows = []
for principal, action, resource in cases:
    allowed, reason = decide(principal, action, resource)
    rows.append({"principal": principal, "action": action, "resource": resource,
                 "decision": "allow" if allowed else "deny", "reason": reason})
report("access decisions", rows)

# STEP 3: deny-by-default must hold for an unknown principal and an unknown action.
check(decide("mallory", "read", "dataset:curated")[1] == "unknown principal", "unknown principal must be denied")
check(decide("cara", "delete", "dataset:raw")[1] == "unknown action", "unknown action must be denied")

# STEP 4: least privilege — the support role cannot read a sensitive analytics dataset.
check(not decide("ben", "read", "dataset:curated")[0], "cross-team read must be denied")
check(decide("cara", "export", "dataset:raw")[0], "manager export of own sensitive data is allowed")

# STEP 5: separate the two reasons a denial can have: identity and authority.
denials = [row for row in rows if row["decision"] == "deny"]
report("denial reasons", denials)
check({row["reason"] for row in denials} >= {"role not permitted", "cross-team resource", "unknown principal"},
      "the matrix should exercise at least three denial paths")
print("\nEvery denial names the check that failed, which is what makes the log usable in an incident.")
