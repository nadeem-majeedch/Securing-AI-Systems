# L14 — Membership inference: measuring what a model remembers

| | |
|---|---|
| **Module** | M09 |
| **Difficulty** | Intermediate |
| **Estimated time** | 70 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

An admissions office publishes aggregate statistics and claims applicants cannot be linked to the model. A privacy researcher points out that the office also exposes a confidence score, and that a model trained on only a few hundred applications tends to memorise them.

## 2. Problem statement

Train a model that memorises, attack it with a threshold on confidence in the known label, report the advantage at 5 % false positives, and show that forcing the model to generalise reduces the leakage.

## 3. Learning objectives

- Build a membership-inference attack from model outputs alone.
- Report advantage at a fixed false-positive rate rather than accuracy.
- Connect memorisation to leakage with a measurable knob.
- State what an advantage does and does not prove.

## 4. Prerequisites

- L02 (evaluation), L15 recommended after this lab.

## 5. Required software

- Python 3.12+
- scikit-learn
- NumPy

## 6. Dataset and input files

- `labs/datasets/admissions.csv` — 900 applications; 200 are treated as members.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L14/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L14/starter.py
```

1. Split the table into 200 member rows and the rest as non-members.
2. Train a 1-nearest-neighbour model on the members; confirm training accuracy is 1.000.
3. Score every row by the probability it assigns to its true label.
4. Compute the ROC curve and report the advantage at 5 % FPR and `2*AUC-1`.
5. Repeat with k = 5 and k = 25 and tabulate accuracy, advantage and `2*AUC-1`.
6. Assert that k=1 leaks more than k=25 and that the leak is well above chance.
7. Write the sentence you would put in a privacy assessment.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L14/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

Training accuracy is **1.000**. At k=1 the attack reaches **2*AUC-1 = 0.426** and advantage at 5 % FPR **+0.037**. Increasing k to 5 gives **0.229**, and k=25 gives **0.054** while accuracy on non-members barely moves.

## 10. Interpretation of results

A 1-NN always returns probability 1.0, so the signal is not confidence magnitude but whether the model agrees with the known label — a subtle point that a naive implementation misses. The advantage at 5 % FPR is small because the operating point is severe; `2*AUC-1` shows the full ranking is informative.

## 11. Student tasks

1. Report advantage at 20 % FPR and explain why it is larger than at 5 %.
2. Explain why the attack needs some known labels and how an attacker might obtain them.
3. State what k=25 does to utility on non-members, using the table.
4. Write two sentences for the privacy assessment, one for each of k=1 and k=25.

## 12. Challenge exercises

1. Add a shadow-model attack: train a second 1-NN on a disjoint sample and fit the threshold on its members.
2. Try a random forest and report whether the leak is larger than for k=1.
3. Design the API change that would remove most of this signal without removing the decision.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. `predict_proba` rows are aligned with your input order.
2. Score a row by `proba[row, true_label]`, not by the maximum.
3. `np.interp(target_fpr, fpr, tpr)` gives TPR at a chosen FPR.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L14/solution.py
labs/solutions/L14/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- AUC is exactly 0.5 — you scored by maximum probability, which is always 1.0 for k=1.
- Advantage is negative — the threshold direction is inverted.
- Training accuracy is not 1.0 — k is greater than 1 or the model was fit on other rows.
- `trapz` missing — NumPy 2 removed it; use `np.trapezoid`.

## 16. Security lessons learned

- Memorisation is measurable, and capacity is the knob.
- Report an operating point, not a single accuracy.
- Membership leakage is about ranking, not identification.

## 17. Submission requirements

- The completed script and the leakage table.
- The privacy-assessment sentences from task 4.
- Answers to the remaining tasks.
- One paragraph on why the maximum-probability attack fails here.

## 18. Acceptable use

Measure the attack advantage on the synthetic admissions model with the member/non-member split the lab defines. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not run membership inference against a real service or a dataset of real people. This is a measurement exercise, and the ethical line is the population, not the code.

## 20. Data handling

All 900 applications are synthetic and the 200 members are a seeded subset. Report aggregate rates only, never a row-level guess about an individual.

## 21. Cleanup

Delete shadow-model checkpoints and any per-row score table you exported.

## 22. Restoring your environment

Core stack only.
