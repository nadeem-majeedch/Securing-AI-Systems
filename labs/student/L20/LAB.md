# L20 — A jailbreak detector and the base-rate problem

| | |
|---|---|
| **Module** | M12 |
| **Difficulty** | Intermediate |
| **Estimated time** | 70 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

Trust and safety wants to block jailbreak attempts automatically. The vendor demo shows 96 % detection. The team's own traffic contains about one attack per thousand requests, and support is already understaffed.

## 2. Problem statement

Train a character-n-gram detector on a synthetic corpus, report TPR at 1 % FPR, compute precision at three prevalences, and decide what the detector may be allowed to do.

## 3. Learning objectives

- Build a text classifier that is robust to spacing and casing.
- Report an operating point instead of accuracy.
- Compute precision under class imbalance.
- Assign a detector a role inside a layered control.

## 4. Prerequisites

- L02 (evaluation), L19.

## 5. Required software

- Python 3.12+
- scikit-learn
- pandas
- NumPy

## 6. Dataset and input files

- No dataset: 300 synthetic prompts generated from templates in the script.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L20/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L20/starter.py
```

1. Generate 150 benign and 150 attack-shaped prompts from the given templates.
2. Split 60/40 with stratification.
3. Fit a TF-IDF character n-gram model and report holdout accuracy.
4. Pick the threshold at 1 % FPR and report TPR there, plus AUC.
5. Compute precision at prevalence 0.5, 0.05 and 0.001.
6. Assert TPR above 0.8 at 1 % FPR and precision below 0.2 at 0.1 % prevalence.
7. Fill the layering table and write the deployment recommendation.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L20/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The detector separates the templates almost perfectly: **AUC near 1.0** and **TPR 1.00 at 1 % FPR**. Precision is **0.990** at 50 % prevalence, **0.840** at 5 %, and **0.091** at 0.1 % — with about **10 false positives per 1,000 requests** at the last prevalence.

## 10. Interpretation of results

The detector's discrimination is excellent and its precision is still catastrophic at realistic prevalence. That is arithmetic, not a modelling failure: at 1 % FPR and 0.1 % prevalence, innocent traffic outnumbers attacks ten to one. A detector of this quality can triage; it cannot block.

## 11. Student tasks

1. Explain the precision collapse without using the word "overfit".
2. Report the review volume per 1,000 requests at 0.1 % prevalence.
3. State two attack families this detector would miss.
4. Write the deployment recommendation with the numbers.

## 12. Challenge exercises

1. Paraphrase five attack prompts and report the new TPR.
2. Add a rate-limit feature and report whether precision improves.
3. Design a two-stage control: cheap detector then expensive review, with a target queue length.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Character n-grams catch spacing and case changes that word tokens miss.
2. Precision = TP / (TP + FP) with TP = TPR × prevalence.
3. Use `np.searchsorted(fpr, 0.01)` to find the operating threshold.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L20/solution.py
labs/solutions/L20/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- AUC is 1.0 — the templates are too distinct; that is expected for synthetic data, and it is the point.
- Precision stays high at low prevalence — you used training prevalence in the formula.
- `trapz` missing — NumPy 2 removed it; use `np.trapezoid`.
- FPR index out of range — `searchsorted` returned len(fpr); clamp it.

## 16. Security lessons learned

- Accuracy and AUC do not decide deployment; precision at prevalence does.
- A detector is a triage component, not a gate.
- Layered controls must be designed together, not stacked after the fact.

## 17. Submission requirements

- The completed script and both tables.
- The deployment recommendation.
- Answers to the tasks.
- One paragraph on what you would monitor after launch.

## 18. Acceptable use

Evaluate the detector on the 300 template-generated prompts. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not collect or redistribute real jailbreak corpora, and do not deploy the detector as a filter without measuring its base rate first.

## 20. Data handling

Prompts are generated from templates and contain no user text. The prevalence figures are synthetic and must be labelled as such in any write-up.

## 21. Cleanup

Delete classifier artefacts and prompt exports you saved.

## 22. Restoring your environment

Core stack only; nothing else is installed.
