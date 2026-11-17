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
# STEP 1: read the synthetic request log (tool calls an agent attempted).
requests = load_json("tool_requests.json")["requests"]
rows = []
for request in requests:
    decision, reason, rule = authorise(request)
    rows.append({"id": request["id"], "principal": request["principal"], "tool": request["tool"],
                 "tenant": PRINCIPALS.get(request["principal"], {}).get("tenant"),
                 "decision": decision, "reason": reason, "rule": rule})
log = pd.DataFrame(rows)
report("authorisation decisions", log)

# STEP 2: counts and the reason distribution.
summary = log.groupby(["decision", "reason"]).size().reset_index(name="count")
report("decision summary", summary)
denied = int((log.decision == "deny").sum())
print(f"\n{denied}/{len(log)} requests denied; every denial names a rule.")

# STEP 3: assertions — default deny, explicit reasons, and the important cases caught.
check(denied >= 5, "most of this request set should be denied")
check((log.reason != "").all(), "every decision needs a reason")
check(set(log[log.reason == "cross_tenant_resource"].id) >= {"q03", "q04", "q07"},
      "every cross-tenant resource access must be denied")
check(set(log[log.reason == "amount_over_limit"].id) >= {"q06"}, "the amount limit must be enforced")
check(set(log[log.reason == "unknown_action"].id) >= {"q08"}, "an unknown tool must be denied, not ignored")
check(set(log[log.decision == "allow"].id) >= {"q01", "q02"}, "legitimate requests must still pass")

# STEP 4: the audit entry a reviewer needs.
audit_fields = pd.DataFrame([
    {"field": "request id and timestamp", "why": "links the decision to the conversation"},
    {"field": "principal and tenant", "why": "makes the subject explicit"},
    {"field": "tool and arguments", "why": "the policy was evaluated on these values"},
    {"field": "decision, rule and reason", "why": "explains a deny without re-running the agent"},
])
report("audit fields", audit_fields)

# STEP 5: separation of duties.
print("\nThe model proposes; the policy engine disposes. A prompt is not an authorisation boundary, and an"
      " agent that can call a refund tool will eventually call it with the wrong amount.")
