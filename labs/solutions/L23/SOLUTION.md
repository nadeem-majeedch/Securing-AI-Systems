# L23 — Solution: Authorising an AI agent's tool calls

**Module:** M14  |  **Difficulty:** Intermediate  |  **Time:** 75 minutes

## Approach

The solution implements a deny-by-default engine with six ordered checks, evaluates the ten requests, and tables decisions plus rules. Assertions pin the cross-tenant, amount, unknown-action and unknown-principal cases.

## Reference results

**7 of 10** requests are denied. Allowed: q01 and q02 (alice, alpha), q05 (carol refund 20), q09 is denied on recipient tenant. Denials: q03, q04, q07 cross-tenant resource; q06 amount 900 over the 200 limit; q08 unknown action `delete_file`; q09 cross-tenant recipient; q10 unknown principal.

## Why this works

The prompt said the same things the policy says. The difference is that the policy cannot be talked out of a decision: q03 fails because bob's tenant is beta, no matter how persuasive the conversation was. Deny-by-default also handles the cases nobody wrote a prompt for, such as `delete_file`.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L23/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- `string indices must be integers` — you iterated the dict instead of `['requests']`.
- Everything allowed — you read the tenant from the request instead of the principal.
- q08 crashes — unknown tools have no policy entry; handle the missing key before indexing.
- All denied — the roles sets do not intersect because of a typo in the policy keys.

## Marking rubric (100 marks)

- 40 marks — policy engine correct and ordered.
- 25 marks — audit fields and reasons complete.
- 20 marks — separation of duties explained.
- 15 marks — design note is specific.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Authorisation belongs in code the model cannot edit.
- Deny by default is what covers the cases you did not imagine.
- A decision without a rule and a reason is not auditable.
