# L10 — Poisoning a fraud model with flipped labels

| | |
|---|---|
| **Module** | M07 |
| **Difficulty** | Intermediate |
| **Estimated time** | 75 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A payments team retrains its fraud model every night on data that includes merchant-reported labels. A compromised merchant account starts reporting legitimate transactions as fraudulent, and the labels flow straight into training. Nobody notices because the model still looks accurate.

## 2. Problem statement

Flip a fraction of the training labels, retrain a tree model, and measure the accuracy and fraud-recall cost at several poisoning rates. Then poison one specific pattern and show that the aggregate metric misses it entirely.

## 3. Learning objectives

- Measure model degradation as a function of the poisoning rate.
- Explain why a high-capacity model is the vulnerable one.
- Distinguish availability poisoning from targeted poisoning.
- Design a slice metric that would catch the targeted case.

## 4. Prerequisites

- L02 (baseline fraud model).

## 5. Required software

- Python 3.12+
- scikit-learn
- NumPy

## 6. Dataset and input files

- `labs/datasets/transactions.csv` — 1,800 transactions with a rule-generated label.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L10/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L10/starter.py
```

1. Load the transactions and split 70/30 once, with a fixed seed.
2. Train a fully grown decision tree and record clean accuracy.
3. For each poisoning rate in 0, 0.05, 0.10 and 0.20, flip that share of training labels and retrain.
4. Record test accuracy and fraud recall for each rate.
5. Append 40 rows describing a structured small payment labelled legitimate, retrain, and probe that pattern.
6. Assert that 20 % flipping reduces accuracy and that most structuring probes are now missed.
7. Write the slice metric that would have exposed the targeted attack.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L10/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

Clean accuracy is **0.839**. Flipping 5 % of labels drops it to **0.763**, 10 % to **0.735** and 20 % to **0.683**. The targeted poison makes **20 of 20** structuring probes look legitimate, while global accuracy falls by only 0.156.

## 10. Interpretation of results

Label noise is not random damage: a tree memorises the flipped rows and then generalises the wrong rule into the region around them. The targeted case is worse than the aggregate suggests — the model is wrong exactly where the attacker wants it to be, and the accuracy number still looks publishable.

## 11. Student tasks

1. Report fraud recall at each rate and explain why it moves differently from accuracy.
2. Replace the tree with logistic regression and report whether poisoning is still effective.
3. Explain why 40 poisoned rows out of 1,300 are enough for the targeted effect.
4. Write the one-paragraph incident note you would send the merchant team.

## 12. Challenge exercises

1. Design a label-provenance check that would quarantine the compromised merchant's labels.
2. Measure how many poisoned rows are needed to flip the structuring pattern at 50 %.
3. Try a defence: train on a trimmed subset (drop the noisiest 5 % by loss) and report the recovery.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Choose flipped indices once per rate with `rng.choice(..., replace=False)`.
2. Keep the test set clean; poisoning the evaluation would hide the effect.
3. A probe is just a feature row; use `np.tile` to repeat it.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L10/solution.py
labs/solutions/L10/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Accuracy improves with poisoning — you flipped labels in the test set too.
- No effect at 5 % — a shallow tree or a linear model averages the noise away; keep the tree deep.
- Probes all classified legitimate even before poisoning — the pattern is unlike the training data; compare with the clean model.
- Recall computed as a count — divide by the number of true frauds.

## 16. Security lessons learned

- A model that can memorise can be taught a lie with very few rows.
- Global accuracy is the wrong gate for targeted poisoning.
- Label provenance is a data-control problem, not a modelling problem.

## 17. Submission requirements

- The completed script and the poisoning sweep.
- The targeted result with the probe count.
- The slice metric from task 7 of the instructions.
- Answers to the remaining tasks.

## 18. Acceptable use

Corrupt a copy of the synthetic transactions table inside the script and retrain the local model. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not poison a shared dataset, a colleague's training run or a production pipeline. The lesson is defensive: how little poison moves a metric.

## 20. Data handling

`transactions.csv` is synthetic. Keep flipped-label copies in memory or in a scratch file you delete, so nobody mistakes them for data.

## 21. Cleanup

Delete the poisoned CSV or checkpoint if you wrote one, and regenerate the dataset if the original changed.

## 22. Restoring your environment

Core stack only.
