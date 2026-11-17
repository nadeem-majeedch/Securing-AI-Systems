# L08 — Solution: Adversarial perturbations against a digit classifier

**Module:** M06  |  **Difficulty:** Intermediate  |  **Time:** 80 minutes

## Approach

The solution trains the linear baseline, implements FGSM with an explicit clamp, and sweeps epsilon while recording both accuracy and the realised perturbation. The assertions check the budget and the monotonicity of attack success.

## Reference results

Clean accuracy is **0.829**. Accuracy falls to **0.685** at epsilon 0.05, **0.496** at 0.10, **0.081** at 0.20 and **0.000** at 0.30. The `max_pixel_change` column equals epsilon in every row, which is the evidence that the budget was respected.

## Why this works

A 0.10 change is 10 % of the pixel range — visible only if you look for it, and it removes a third of the model's accuracy. The budget column matters as much as the accuracy column: without it, "90 % attack success" could mean an unbounded perturbation that no scanner would produce.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L08/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- `RuntimeError: element 0 of tensors does not require grad` — the input tensor is not a leaf with `requires_grad`.
- Success rate is 0 — you attacked the wrong label direction (subtract instead of add the sign).
- Accuracy improves at higher epsilon — the perturbation is not clamped and leaves the valid range.
- Model stuck at 10 % accuracy — the labels were loaded as floats; keep them as `int64`.

## Marking rubric (100 marks)

- 40 marks — FGSM implemented correctly and budget verified.
- 25 marks — sweep table complete and interpreted.
- 20 marks — gradient-access requirement explained.
- 15 marks — limitation statement is accurate and non-promotional.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- An attack result without a budget is not a result.
- Small, bounded changes are enough to break a linear classifier.
- The defender's metric is accuracy under attack at a stated epsilon.
