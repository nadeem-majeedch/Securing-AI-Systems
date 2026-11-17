# L02 — Solution: Baseline fraud model: metrics, calibration and confident errors

**Module:** M02  |  **Difficulty:** Beginner  |  **Time:** 60 minutes

## Approach

The solution fits the baseline, reports the three metrics side by side, bins the probabilities, and then isolates the confident errors. Two assertions pin the baseline: AUC above 0.75 and at least one confident error, so the lab cannot pass on a broken model.

## Reference results

The fraud rate is about 0.218. The baseline reaches **accuracy 0.857, ROC AUC 0.875 and Brier 0.104**. The calibration table is close to the diagonal in the populated bins (for example 0.700 predicted against 0.780 observed in the 0.6–0.8 bin). There are 77 errors, of which **2** have probability above 0.8.

## Why this works

Accuracy alone would hide the class imbalance, AUC hides the probability scale, and Brier alone hides where the errors are. The two confident errors are the reviewable unit: the model is wrong and sure, which is exactly the state that produces a bad automated decision with no human hesitation.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L02/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- `ConvergenceWarning` — raise `max_iter`; the features are unscaled, which slows lbfgs.
- All probabilities near 0.2 — you may be using `predict` instead of `predict_proba`.
- Empty calibration bins — coarse bins are fine here; the extremes genuinely have few rows.
- AUC close to 0.5 — the label column was read as a string; cast with `.astype(int)`.

## Marking rubric (100 marks)

- 40 marks — correct metrics and a reproducible split.
- 25 marks — calibration table interpreted, not just printed.
- 20 marks — confident errors identified and explained.
- 15 marks — task answers refer to measured numbers.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A single metric is a policy choice disguised as a measurement.
- Confident errors, not average accuracy, decide whether a human will catch a mistake.
- Every later attack needs this baseline, so pin the seed and the split.
