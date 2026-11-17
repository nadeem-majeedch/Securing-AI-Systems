# L09 — Solution: Transfer attacks and the price of a black-box query

**Module:** M06  |  **Difficulty:** Advanced  |  **Time:** 90 minutes

## Approach

The solution trains two models on one split, attacks only the first, evaluates the same tensor on the second, and compares with noise. A single-pixel search then prices the black-box route, and three assertions pin the relationships the lab teaches.

## Reference results

Clean accuracy is **A 0.831** and **B 0.821**. The white-box attack drops A to **0.063**. The same images drop B to **0.272** — a transfer effect of **0.549** — while random noise at the same budget drops B only to 0.806. The black-box single-pixel search spends **79,400 queries** and leaves B at 0.819.

## Why this works

Transfer works because both models learned similar features from the same data; it costs one gradient and no knowledge of B's weights. The black-box result is the counterweight: naive random search over a single pixel is almost useless, which is why real query attacks use scores and many iterations — and why query volume is a detection signal.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L09/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Transfer accuracy equals clean accuracy — you accidentally attacked B instead of A.
- Perturbation exceeds 0.2 — clamp after the step.
- The random search improves nothing — you are replacing pixels with values outside the valid range.
- Different clean accuracies — the models were trained on different splits; use one split.

## Marking rubric (100 marks)

- 35 marks — transfer measured correctly with a valid control.
- 25 marks — black-box cost reported honestly.
- 25 marks — explanation of why transfer works is correct.
- 15 marks — threat-model sentence is specific and defensible.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A hidden architecture raises the attacker's cost but does not stop transfer.
- Always include a same-budget random control; it is the cheapest sanity check in adversarial ML.
- Query count is both an attack cost and a defender's signal.
