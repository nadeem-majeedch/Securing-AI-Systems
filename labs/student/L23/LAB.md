# L23 — Authorising an AI agent's tool calls

| | |
|---|---|
| **Module** | M14 |
| **Difficulty** | Intermediate |
| **Estimated time** | 75 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A support agent can read documents, issue refunds and send email. The agent's prompt says it must stay within the customer's tenant and never refund more than 200. A red-team transcript shows the agent agreeing to do both, because the instruction was in the prompt, not in the tool layer.

## 2. Problem statement

Move the rules out of the prompt and into a policy engine: evaluate ten synthetic tool requests, deny by default, and record a rule and reason for every decision.

## 3. Learning objectives

- Enforce tenant, role and amount constraints outside the model.
- Apply deny-by-default with explicit rules.
- Produce an audit record per decision.
- Explain separation between proposal and authorisation.

## 4. Prerequisites

- L19, L21.

## 5. Required software

- Python 3.12+
- pandas

## 6. Dataset and input files

- `labs/datasets/tool_requests.json` — ten tool calls from four principals.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L23/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L23/starter.py
```

1. Define principals with tenant and roles, and a policy per tool.
2. Implement `authorise(request)` returning decision, reason and rule.
3. Check in order: principal exists, tool allowlisted, role permitted, resource tenant, amount, recipient.
4. Evaluate all ten requests and table the decisions.
5. Summarise counts by decision and reason.
6. Assert at least five denials, no empty reasons, and the specific cross-tenant, amount and unknown-action cases.
7. Table the four audit fields a reviewer needs.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L23/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

**7 of 10** requests are denied. Allowed: q01 and q02 (alice, alpha), q05 (carol refund 20), q09 is denied on recipient tenant. Denials: q03, q04, q07 cross-tenant resource; q06 amount 900 over the 200 limit; q08 unknown action `delete_file`; q09 cross-tenant recipient; q10 unknown principal.

## 10. Interpretation of results

The prompt said the same things the policy says. The difference is that the policy cannot be talked out of a decision: q03 fails because bob's tenant is beta, no matter how persuasive the conversation was. Deny-by-default also handles the cases nobody wrote a prompt for, such as `delete_file`.

## 11. Student tasks

1. Report which requests would have succeeded without the resource-tenant check.
2. Explain why principal existence is checked before the action.
3. Add a fifth principal with the automation role and describe what changes.
4. Write the one-paragraph design note for the agent team.

## 12. Challenge exercises

1. Add a per-session budget so repeated refunds cannot exceed 200 in total.
2. Add an approval step for amounts over 200 and model it as a decision state.
3. Design the alert that fires when a principal accumulates three denials in a minute.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Parse the resource tenant from `doc:<tenant>:<n>`.
2. Check the cheapest, most decisive rule first and return on denial.
3. Never derive the tenant from the request; take it from the authenticated principal.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L23/solution.py
labs/solutions/L23/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- `string indices must be integers` — you iterated the dict instead of `['requests']`.
- Everything allowed — you read the tenant from the request instead of the principal.
- q08 crashes — unknown tools have no policy entry; handle the missing key before indexing.
- All denied — the roles sets do not intersect because of a typo in the policy keys.

## 16. Security lessons learned

- Authorisation belongs in code the model cannot edit.
- Deny by default is what covers the cases you did not imagine.
- A decision without a rule and a reason is not auditable.

## 17. Submission requirements

- The completed script and decision table.
- The design note.
- Answers to the tasks.
- One paragraph on what you would log beyond the four fields.

## 18. Acceptable use

Evaluate the policy engine against `tool_requests.json` and the mock executor. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Never connect the agent to a real email, refund, payment or shell tool. The executor only records decisions and performs no action.

## 20. Data handling

Ten synthetic tool calls from four invented principals. No tokens, endpoints or customer identifiers appear.

## 21. Cleanup

Delete decision logs you exported. If you extended the lab with test credentials in a real system, revoke them.

## 22. Restoring your environment

Core stack only; no agent process is left running.
