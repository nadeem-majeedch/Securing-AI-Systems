"""L23 — Authorising an AI agent's tool calls (M14, Intermediate).

Goal: replace prompt-level trust with an explicit policy engine, evaluate ten synthetic requests, and produce an
audit record for every decision.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import pandas as pd

from labkit import check, load_json, report

PRINCIPALS = {
    "alice": {"tenant": "alpha", "roles": {"support"}},
    "bob": {"tenant": "beta", "roles": {"support"}},
    "carol": {"tenant": "beta", "roles": {"support"}},
    "svc_agent": {"tenant": "alpha", "roles": {"automation"}},
}
POLICY = {
    "read_file": {"roles": {"support", "automation"}, "max_amount": None},
    "refund": {"roles": {"support"}, "max_amount": 200},
    "send_email": {"roles": {"support"}, "max_amount": None},
}


def resource_tenant(request):
    parts = str(request.get("resource", "")).split(":")
    return parts[1] if len(parts) > 1 else None


def authorise(request):
    """Deny by default; every branch names the rule it applied."""
    principal = PRINCIPALS.get(request["principal"])
    if principal is None:
        return "deny", "unknown_principal", "principal_exists"
    rule = POLICY.get(request["tool"])
    if rule is None:
        return "deny", "unknown_action", "action_allowlisted"
    if not (principal["roles"] & rule["roles"]):
        return "deny", "role_not_permitted", "role_in_allowlist"
    if resource_tenant(request) != principal["tenant"]:
        return "deny", "cross_tenant_resource", "resource_tenant_match"
    if rule["max_amount"] is not None and request.get("amount", 0) > rule["max_amount"]:
        return "deny", "amount_over_limit", "amount_limit"
    if request["tool"] == "send_email" and request.get("recipient_tenant") != principal["tenant"]:
        return "deny", "cross_tenant_recipient", "recipient_tenant_match"
    return "allow", "policy_satisfied", "all_checks_passed"


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L23/solution.py (open it only after trying).

# STEP 1: read the synthetic request log (tool calls an agent attempted).
# TODO 1: implement this step.

# STEP 2: counts and the reason distribution.
# TODO 2: implement this step.

# STEP 3: assertions — default deny, explicit reasons, and the important cases caught.
# TODO 3: implement this step.

# STEP 4: the audit entry a reviewer needs.
# TODO 4: implement this step.

# STEP 5: separation of duties.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
