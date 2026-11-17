# L20 — Solution: A jailbreak detector and the base-rate problem

**Module:** M12  |  **Difficulty:** Intermediate  |  **Time:** 70 minutes

## Approach

The solution generates a templated corpus, fits a character n-gram classifier, picks the 1 % FPR operating point, and computes precision at three prevalences. The assertions require both good detection and the honest precision collapse.

## Reference results

The detector separates the templates almost perfectly: **AUC near 1.0** and **TPR 1.00 at 1 % FPR**. Precision is **0.990** at 50 % prevalence, **0.840** at 5 %, and **0.091** at 0.1 % — with about **10 false positives per 1,000 requests** at the last prevalence.

## Why this works

The detector's discrimination is excellent and its precision is still catastrophic at realistic prevalence. That is arithmetic, not a modelling failure: at 1 % FPR and 0.1 % prevalence, innocent traffic outnumbers attacks ten to one. A detector of this quality can triage; it cannot block.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L20/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- AUC is 1.0 — the templates are too distinct; that is expected for synthetic data, and it is the point.
- Precision stays high at low prevalence — you used training prevalence in the formula.
- `trapz` missing — NumPy 2 removed it; use `np.trapezoid`.
- FPR index out of range — `searchsorted` returned len(fpr); clamp it.

## Marking rubric (100 marks)

- 35 marks — detector and operating point correct.
- 30 marks — precision computed and interpreted at all three prevalences.
- 20 marks — layering table is coherent.
- 15 marks — recommendation is specific about role.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Accuracy and AUC do not decide deployment; precision at prevalence does.
- A detector is a triage component, not a gate.
- Layered controls must be designed together, not stacked after the fact.
