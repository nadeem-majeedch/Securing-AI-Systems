# L04 — Solution: Least privilege for an analytics platform

**Module:** M03  |  **Difficulty:** Intermediate  |  **Time:** 60 minutes

## Approach

The solution encodes the policy as a list of rules and evaluates six checks in a fixed order, returning the first failure with a reason. The matrix is deliberately mixed: five legitimate requests pass, five fail on four different checks.

## Reference results

The matrix produces **five allows and five denials**. Denials cover `role not permitted` (analyst writing, support reading), `cross-team resource` (manager refunding a support ticket), `unknown principal` (mallory) and `sensitive export requires elevated approval` is available as a path you can exercise by lowering the manager's spend limit.

## Why this works

The interesting cases are not the obvious denials but the ones that look reasonable: a support agent reading a curated table to answer a ticket, and a manager exporting a sensitive table. Both fail a check that exists for a reason. Reasons in the output are what make the policy reviewable — "denied" alone tells an auditor nothing.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L04/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Everything allowed — you probably wrote `return True` before the checks.
- `TypeError: unhashable` — you compared lists with `&`; convert both to sets.
- Cross-team denial never triggers — the resource key is misspelt and hits `unknown resource` first.
- Spend limit never triggers — pass `amount` as an int, not a string.

## Marking rubric (100 marks)

- 40 marks — engine is deny-by-default and reasons are specific.
- 25 marks — matrix covers legitimate and forbidden work.
- 20 marks — the two assertions on privilege boundaries hold.
- 15 marks — written policy note is specific about export conditions.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Policy belongs in data so it can be diffed, tested and reviewed.
- Deny-by-default is a code shape, not an intention.
- A denial without a reason cannot be investigated or appealed.
