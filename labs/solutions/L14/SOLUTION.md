# L14 — Solution: Membership inference: measuring what a model remembers

**Module:** M09  |  **Difficulty:** Intermediate  |  **Time:** 70 minutes

## Approach

The solution trains a 1-NN on 200 members, scores rows by the probability assigned to the true label, and measures the leak with `2*AUC-1` and the advantage at 5 % FPR. A k-sweep then shows the leak falling from 0.426 to 0.054.

## Reference results

Training accuracy is **1.000**. At k=1 the attack reaches **2*AUC-1 = 0.426** and advantage at 5 % FPR **+0.037**. Increasing k to 5 gives **0.229**, and k=25 gives **0.054** while accuracy on non-members barely moves.

## Why this works

A 1-NN always returns probability 1.0, so the signal is not confidence magnitude but whether the model agrees with the known label — a subtle point that a naive implementation misses. The advantage at 5 % FPR is small because the operating point is severe; `2*AUC-1` shows the full ranking is informative.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L14/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- AUC is exactly 0.5 — you scored by maximum probability, which is always 1.0 for k=1.
- Advantage is negative — the threshold direction is inverted.
- Training accuracy is not 1.0 — k is greater than 1 or the model was fit on other rows.
- `trapz` missing — NumPy 2 removed it; use `np.trapezoid`.

## Marking rubric (100 marks)

- 35 marks — attack implemented with the correct score.
- 25 marks — advantage and AUC reported and interpreted.
- 25 marks — k-sweep connects capacity to leakage.
- 15 marks — privacy statement is accurate and non-alarmist.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Memorisation is measurable, and capacity is the knob.
- Report an operating point, not a single accuracy.
- Membership leakage is about ranking, not identification.
