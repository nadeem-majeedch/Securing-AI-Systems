# L31 — Fairness evaluation and a mitigation that only half-works

| | |
|---|---|
| **Module** | M19 |
| **Difficulty** | Intermediate |
| **Estimated time** | 75 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

An admissions model is accused of disadvantageing one applicant group. The vendor reports that the model does not use the group column at all, and considers the matter closed. The committee asks for selection rates, error rates and calibration by group.

## 2. Problem statement

Measure selection rate, equal opportunity and calibration by group, apply a reweighting mitigation, and report which of the three metrics moved and which did not.

## 3. Learning objectives

- Compute disparate impact, equal opportunity and calibration gap.
- Distinguish a ranking problem from a threshold problem.
- Apply sample reweighting and measure its effect.
- Report several fairness metrics without collapsing them into one.

## 4. Prerequisites

- L02 (metrics), L15 (attribute inference).

## 5. Required software

- Python 3.12+
- scikit-learn
- pandas

## 6. Dataset and input files

- `labs/datasets/admissions.csv` — 900 applications with a `group` column.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L31/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L31/starter.py
```

1. Split 60/40 with stratification on the label and keep the group column.
2. Train logistic regression and produce scores and thresholded predictions.
3. Compute selection rate, TPR, calibration gap and AUC per group.
4. Report the disparate impact ratio and the opportunity gap.
5. Reweight training rows so each group contributes equally and repeat the measurements.
6. Table before and after for all three metrics.
7. Assert the impact ratio moves toward parity and report the opportunity gap honestly.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L31/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

Baseline selection rates are **0.531 for group B** against a higher rate for group A, giving a **disparate impact ratio of 0.728** and an opportunity gap of **0.041**; group B's calibration gap is **0.154**. After reweighting the ratio is **0.730**, the gap **0.052**, and calibration **0.151** — a small move in the intended direction and no collapse of the other metrics.

## 10. Interpretation of results

The mitigation nudges selection rates without changing the within-group ranking, so the AUCs barely move and the opportunity gap can widen slightly. That is the honest result: reweighting is a threshold and loss intervention, not a feature intervention, and fairness metrics trade against each other.

## 11. Student tasks

1. Explain why the ratio moved so little.
2. Report what an equal-opportunity constraint would require instead.
3. State whether the model's AUC by group supports the vendor's claim, and why that is not enough.
4. Write the committee sentence with three numbers.

## 12. Challenge exercises

1. Try a group-specific threshold and report the fairness and utility cost.
2. Remove the features most correlated with group and report the utility loss.
3. Design a monitoring dashboard that would catch a drift in the ratio.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Disparate impact is the ratio of selection rates, not their difference.
2. Sample weights of `1/group_frequency` equalise each group's contribution.
3. Calibration gap is `|mean score - base rate|` within a group.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L31/solution.py
labs/solutions/L31/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- `roc_auc_score` fails for a group — that group has only one class in the split; seed the split.
- Ratio above 1 — the reference group is the one in the denominator; state it explicitly.
- Reweighting changes nothing — weights were computed from the test split.
- All metrics improve — you evaluated on training data.

## 16. Security lessons learned

- Not using an attribute does not make outcomes equal.
- Fairness metrics move independently; report the set.
- A mitigation that helps one metric can leave another unchanged.

## 17. Submission requirements

- The completed script and both tables.
- The committee sentence with three numbers.
- Answers to the tasks.
- One paragraph on which metric you would put in a release gate, and why.

## 18. Acceptable use

Evaluate the three fairness metrics on the synthetic admissions model and the `group` column. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not infer protected attributes of real people, and do not present the synthetic mitigation as evidence about a real admissions process.

## 20. Data handling

Group labels are synthetic and the model never sees them. Report aggregate metrics only.

## 21. Cleanup

Delete fairness tables or figures you saved.

## 22. Restoring your environment

Core stack only.
