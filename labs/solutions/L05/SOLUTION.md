# L05 — Solution: Threat modelling and risk ranking for a hospital summariser

**Module:** M04  |  **Difficulty:** Beginner  |  **Time:** 50 minutes

## Approach

The solution defines six threats with explicit impact, likelihood and residual factors, computes both scores in one loop, then ranks. Four assertions enforce register quality: every row testable, every row controlled, residual never above inherent, and the expected top risk.

## Reference results

Six threats are ranked. **T6 (clinician accepts a wrong summary) leads with residual 12.0**, followed by T1 (instruction in a referral, 8.0) and T5 (endpoint exhaustion, 6.0). Inherent risk for T6 and T1 is 20; the controls reduce them by different amounts.

## Why this works

The top residual risk is a workflow control, not a model control. That is the usual finding: model hardening is measurable and satisfying, while acknowledgement of AI output is the thing that actually prevents harm. A register that ranks model threats first is usually a register written by the model team.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L05/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Ranking ties — sort by `(-residual, id)` for a stable order.
- `KeyError: residual` — compute both scores in the same loop before sorting.
- Everything looks high risk — your likelihood scores are all 4 or 5; spread them.
- Assertion on T6 fails — you changed the scores; either justify the new ranking or restore the values.

## Marking rubric (100 marks)

- 40 marks — register is complete and internally consistent.
- 25 marks — ranking is explained rather than merely printed.
- 20 marks — budget argument follows from the numbers.
- 15 marks — counter-argument is specific and fair.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A threat without an asset cannot be mitigated, only feared.
- Residual risk is the number that gets funded.
- Human-factors threats are frequently the largest and the least owned.
