# L12 — Solution: PGD, projection and an honest robustness number

**Module:** M08  |  **Difficulty:** Advanced  |  **Time:** 90 minutes

## Approach

The solution implements PGD with a random start and projection, runs the comparison sweep with a budget assertion per row, then reproduces the unprojected mistake and asserts that it exceeds its declared epsilon.

## Reference results

Clean accuracy is **0.846**. FGSM/PGD-15 accuracy is **0.680/0.678** at epsilon 0.05, **0.479/0.486** at 0.10 and **0.058/0.063** at 0.20; the realised change equals epsilon in every row. The unprojected loop reports accuracy 0.000 with a realised change of **0.750** against a declared 0.200.

## Why this works

At this model size the iterative attack is not much stronger than one step — the model is nearly linear, so the sign step already captures most of the damage. That is a finding about the model, not a reason to skip PGD: on a deeper model the gap widens, and the unprojected number is not comparable to anything.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L12/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- `RuntimeError` about grad — the tensor is not a leaf; clone and call `requires_grad_(True)`.
- Budget exceeded — projection happens before the clamp or not at all.
- Accuracy identical to FGSM — alpha is equal to epsilon, so PGD takes one effective step.
- Unprojected accuracy better than projected — you are evaluating on a larger budget.

## Marking rubric (100 marks)

- 40 marks — PGD correct, including projection and random start.
- 25 marks — budget verified for every configuration.
- 20 marks — unprojected failure reproduced and explained.
- 15 marks — claim is specific and defensible.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A robustness number without its attack configuration is not a result.
- Projection is the difference between an attack and a bug.
- Iterative attacks cost compute; report that cost with the number.
