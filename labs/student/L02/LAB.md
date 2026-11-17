# L02 — Baseline fraud model: metrics, calibration and confident errors

| | |
|---|---|
| **Module** | M02 |
| **Difficulty** | Beginner |
| **Estimated time** | 60 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A payments team has a rule-based fraud engine and wants a machine-learning challenger. Before anyone attacks the new model, the risk committee asks for the baseline numbers the model will be judged against — and for the errors the model is most certain about.

## 2. Problem statement

Train a logistic-regression baseline on the transaction extract, report accuracy, ROC AUC and Brier score, check calibration in coarse bins, and list the confident errors that a reviewer would have to defend.

## 3. Learning objectives

- Report three metrics that answer three different questions.
- Read a calibration table and explain what a Brier score adds.
- Identify confident errors and explain why they matter more than average accuracy.
- Produce the reproducible baseline that later labs attack.

## 4. Prerequisites

- Module 02 lecture; L01 recommended.

## 5. Required software

- Python 3.12+
- pandas
- scikit-learn
- NumPy

## 6. Dataset and input files

- `labs/datasets/transactions.csv` — 1,800 synthetic card transactions with a rule-generated label.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L02/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L02/starter.py
```

1. Load the transactions and separate the five features from `is_fraud`.
2. Split 70/30 with stratification and a fixed `random_state`.
3. Fit `LogisticRegression(max_iter=1000)` and take the positive-class probability.
4. Compute accuracy, ROC AUC and Brier score; print them as a three-row table.
5. Bin the probabilities into five ranges and print mean score versus observed fraud rate per bin.
6. Count the errors and the subset with predicted probability above 0.8.
7. Assert AUC is above 0.75 and that at least one confident error exists.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L02/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The fraud rate is about 0.218. The baseline reaches **accuracy 0.857, ROC AUC 0.875 and Brier 0.104**. The calibration table is close to the diagonal in the populated bins (for example 0.700 predicted against 0.780 observed in the 0.6–0.8 bin). There are 77 errors, of which **2** have probability above 0.8.

## 10. Interpretation of results

Accuracy alone would hide the class imbalance, AUC hides the probability scale, and Brier alone hides where the errors are. The two confident errors are the reviewable unit: the model is wrong and sure, which is exactly the state that produces a bad automated decision with no human hesitation.

## 11. Student tasks

1. Refit without `stratify` and report how the fraud rate in the test set changes.
2. Replace the threshold 0.5 with 0.3 and report precision, recall and the number of false positives.
3. Add `amount * merchant_risk` as a feature and report whether AUC moves.
4. Explain in three sentences why a Brier score of 0.104 can coexist with 85.7 % accuracy.

## 12. Challenge exercises

1. Add a second model (random forest) and compare the same three metrics.
2. Design a review queue that surfaces the 20 highest-risk transactions per day and measure its precision.
3. Write the one-paragraph model card section on known limitations for this baseline.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. `predict_proba(X)[:, 1]` is the fraud probability; `predict` already applies 0.5.
2. `np.digitize(proba, bins)` gives bin indices for the calibration table.
3. Brier is the mean squared error of the probabilities: `mean((p - y) ** 2)`.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L02/solution.py
labs/solutions/L02/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- `ConvergenceWarning` — raise `max_iter`; the features are unscaled, which slows lbfgs.
- All probabilities near 0.2 — you may be using `predict` instead of `predict_proba`.
- Empty calibration bins — coarse bins are fine here; the extremes genuinely have few rows.
- AUC close to 0.5 — the label column was read as a string; cast with `.astype(int)`.

## 16. Security lessons learned

- A single metric is a policy choice disguised as a measurement.
- Confident errors, not average accuracy, decide whether a human will catch a mistake.
- Every later attack needs this baseline, so pin the seed and the split.

## 17. Submission requirements

- The completed script and its console output.
- The three-metric table and the calibration table.
- A short paragraph on the two confident errors and what you would do about them.
- Answers to the four student tasks.

## 18. Acceptable use

Train and evaluate only against `labs/datasets/transactions.csv`, a synthetic card-transaction table whose labels come from a rule in the generator. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not connect to an issuer, a payment processor or a production fraud model, and do not tune thresholds against real chargebacks. The calibration numbers describe this synthetic table.

## 20. Data handling

Card numbers are format-only synthetic strings and no cardholder exists. Treat merchant and amount columns as if they were sensitive, so the habit carries into real work, and never commit an augmented copy.

## 21. Cleanup

This lab keeps everything in memory. Delete any model or metrics file you saved yourself, and run `python labs/scripts/make_datasets.py` if you altered the CSV.

## 22. Restoring your environment

The pinned environment is sufficient; nothing else is installed.
