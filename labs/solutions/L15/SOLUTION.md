# L15 — Solution: Attribute inference and model inversion on applicant data

**Module:** M09  |  **Difficulty:** Advanced  |  **Time:** 80 minutes

## Approach

The solution standardises the features, trains the admission model, then fits a score-to-group classifier and reports precision against the base rate. Inversion uses greedy coordinate ascent in standardised space and is scored by cosine similarity to the admitted prototype.

## Reference results

The model reaches **0.799** accuracy and group B's base rate is **0.427**. Inferring group from the score gives precision **0.515** at threshold 0.4, **0.533** at 0.5 and **0.638** at 0.6 — above the base rate at every threshold. The reconstruction reaches cosine **0.953** to the admitted prototype against **0.182** for the global mean.

## Why this works

The attribute is inferable because group correlates with the features, not because the model uses it. That is why removing a column is not a fairness control. Inversion recovers the *direction* of the admitted profile — high grades and test scores — while overshooting the magnitude, which is exactly what an optimisation without a data prior does.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L15/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Precision below the base rate — the score is not carrying the attribute; check the correlation first.
- Reconstruction error worse than the baseline — you are comparing magnitudes in raw units.
- Every trial is rejected — the model predicts probability, so compare `predict_proba`, not `predict`.
- Attribute attack perfect — you accidentally trained on the group column.

## Marking rubric (100 marks)

- 35 marks — attribute inference measured against a base rate.
- 30 marks — inversion implemented and scored correctly.
- 20 marks — overshoot explained.
- 15 marks — finding is precise and free of overclaiming.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A model can leak an attribute it never uses.
- Inversion recovers prototypes and directions, not individuals.
- Output granularity is a privacy control with a measurable effect.
