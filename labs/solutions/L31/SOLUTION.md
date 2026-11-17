# L31 — Solution: Fairness evaluation and a mitigation that only half-works

**Module:** M19  |  **Difficulty:** Intermediate  |  **Time:** 75 minutes

## Approach

The solution trains a baseline, measures three fairness metrics per group, reweights the training rows, and reports the before/after table. The assertions require movement toward parity without claiming that the problem is solved.

## Reference results

Baseline selection rates are **0.531 for group B** against a higher rate for group A, giving a **disparate impact ratio of 0.728** and an opportunity gap of **0.041**; group B's calibration gap is **0.154**. After reweighting the ratio is **0.730**, the gap **0.052**, and calibration **0.151** — a small move in the intended direction and no collapse of the other metrics.

## Why this works

The mitigation nudges selection rates without changing the within-group ranking, so the AUCs barely move and the opportunity gap can widen slightly. That is the honest result: reweighting is a threshold and loss intervention, not a feature intervention, and fairness metrics trade against each other.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L31/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- `roc_auc_score` fails for a group — that group has only one class in the split; seed the split.
- Ratio above 1 — the reference group is the one in the denominator; state it explicitly.
- Reweighting changes nothing — weights were computed from the test split.
- All metrics improve — you evaluated on training data.

## Marking rubric (100 marks)

- 35 marks — metrics computed correctly per group.
- 30 marks — mitigation applied and measured.
- 20 marks — trade-off explained.
- 15 marks — committee sentence is accurate.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Not using an attribute does not make outcomes equal.
- Fairness metrics move independently; report the set.
- A mitigation that helps one metric can leave another unchanged.
