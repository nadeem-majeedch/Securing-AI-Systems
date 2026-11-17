# L15 — Attribute inference and model inversion on applicant data

| | |
|---|---|
| **Module** | M09 |
| **Difficulty** | Advanced |
| **Estimated time** | 80 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

The admissions model was audited for direct use of protected group membership and passed: the group column is not an input. A journalist asks a sharper question — can the score be used to infer group membership anyway, and can the model be made to describe a typical successful applicant?

## 2. Problem statement

Infer the protected attribute from the model's score, then invert the model by greedy coordinate ascent to reconstruct a representative admitted profile, comparing both against honest baselines.

## 3. Learning objectives

- Distinguish direct use of an attribute from inference of it.
- Measure attribute inference against the base rate.
- Implement model inversion without gradients.
- Report inversion as a direction recovered, not a person recovered.

## 4. Prerequisites

- L14 (membership inference).

## 5. Required software

- Python 3.12+
- scikit-learn
- NumPy

## 6. Dataset and input files

- `labs/datasets/admissions.csv` — 900 applications with a `group` column the model never sees.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L15/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L15/starter.py
```

1. Standardise the three academic features and train a logistic model on admission only.
2. Take the score for every applicant and fit a small model that predicts group from the score alone.
3. Report precision, recall and flagged counts at three thresholds, against the base rate.
4. Implement greedy coordinate ascent that maximises the admitted probability.
5. Compare the reconstruction with the admitted prototype using cosine similarity, and with the global mean.
6. Assert the reconstruction beats the global-mean baseline and scores above 0.8.
7. State the difference between the two attacks in one paragraph.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L15/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The model reaches **0.799** accuracy and group B's base rate is **0.427**. Inferring group from the score gives precision **0.515** at threshold 0.4, **0.533** at 0.5 and **0.638** at 0.6 — above the base rate at every threshold. The reconstruction reaches cosine **0.953** to the admitted prototype against **0.182** for the global mean.

## 10. Interpretation of results

The attribute is inferable because group correlates with the features, not because the model uses it. That is why removing a column is not a fairness control. Inversion recovers the *direction* of the admitted profile — high grades and test scores — while overshooting the magnitude, which is exactly what an optimisation without a data prior does.

## 11. Student tasks

1. Report the precision at the threshold that flags the fewest applicants and say who would use it.
2. Explain why the reconstruction overshoots the prototype on every feature.
3. Design a change to the API that reduces attribute inference without changing the decision.
4. Write the two-sentence finding for the journalist, with numbers.

## 12. Challenge exercises

1. Add a prior penalty toward the global mean and report how the reconstruction changes.
2. Repeat the attribute attack using only a binary decision instead of a score.
3. Design an audit that would detect this inference path before publication.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Standardise features before comparing profiles; raw units are dominated by test scores.
2. Cosine similarity compares direction; that is the fair metric for inversion.
3. Greedy ascent: for each feature, try a grid of quantiles and keep the best score.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L15/solution.py
labs/solutions/L15/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Precision below the base rate — the score is not carrying the attribute; check the correlation first.
- Reconstruction error worse than the baseline — you are comparing magnitudes in raw units.
- Every trial is rejected — the model predicts probability, so compare `predict_proba`, not `predict`.
- Attribute attack perfect — you accidentally trained on the group column.

## 16. Security lessons learned

- A model can leak an attribute it never uses.
- Inversion recovers prototypes and directions, not individuals.
- Output granularity is a privacy control with a measurable effect.

## 17. Submission requirements

- The completed script and both tables.
- The journalist finding from task 4.
- The API change from task 3, with its expected effect.
- Answers to the remaining tasks.

## 18. Acceptable use

Reconstruct prototypes and infer the hidden `group` column from the synthetic admissions model. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not apply inversion to real applicants, real faces or any model trained on people, and do not publish reconstructed records even from this data without labelling them as artefacts.

## 20. Data handling

Synthetic applications only. Reconstructed prototypes are optimiser output, not recovered records, and must be described that way in any report.

## 21. Cleanup

Delete saved prototypes, figures and inferred-attribute tables.

## 22. Restoring your environment

Core stack only; nothing else is installed.
