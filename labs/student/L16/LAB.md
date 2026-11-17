# L16 — Extraction from a mock admissions API

| | |
|---|---|
| **Module** | M10 |
| **Difficulty** | Intermediate |
| **Estimated time** | 80 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A consultancy sells access to its admissions scoring model through an API that returns a probability. A competitor with a modest budget starts querying it. The vendor insists the model is safe because the weights are secret and the API is rate-limited only by courtesy.

## 2. Problem statement

Rebuild the target model from API answers at three query budgets, compare probability outputs with label-only outputs, and measure what rounding to one decimal does to the copy.

## 3. Learning objectives

- Measure extraction fidelity against query budget.
- Compare information per query across output formats.
- Quantify the effect of a small product-level control.
- Explain why quotas are a security control.

## 4. Prerequisites

- L02 (evaluation), L10 recommended.

## 5. Required software

- Python 3.12+
- scikit-learn
- NumPy

## 6. Dataset and input files

- `labs/datasets/admissions.csv` — 600 rows train the target, the rest evaluate fidelity.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L16/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L16/starter.py
```

1. Train the target logistic model on the first 600 rows and record held-out accuracy.
2. Wrap it in a mock API that counts queries and can return probability, rounded probability or a label.
3. For budgets 50, 150 and 500, query, fit a substitute and measure fidelity on held-out rows.
4. Repeat at 150 queries with label-only output and compare.
5. Repeat at 150 queries with probabilities rounded to one decimal.
6. Assert fidelity does not fall as the budget grows and that 500 queries recovers most of the model.
7. Write the interface recommendation, with the numbers that support it.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L16/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The target scores about **0.83** on held-out rows. Extraction fidelity is **0.813** at 50 queries, **0.833** at 150 and **0.823** at 500 — a plateau, because the substitute is already as good as its query distribution allows. At 150 queries, probabilities give **0.833** and labels **0.800**; rounding gives **0.823**.

## 10. Interpretation of results

Fidelity saturates rather than climbing forever: after the substitute captures the boundary, extra queries buy little. That plateau is the defender's lever — a quota below it makes extraction expensive. The output-format gap is real but modest here because the model is simple; it widens on harder targets.

## 11. Student tasks

1. Explain why the 500-query copy is not better than the 150-query copy.
2. Report the fidelity cost of returning labels only.
3. State the quota you would set and the assumption it depends on.
4. Write the sentence you would say to the team that needs probabilities.

## 12. Challenge exercises

1. Use active learning: query where the substitute is least certain, and compare fidelity at 150 queries.
2. Make the target a random forest and report whether extraction gets harder.
3. Add a watermark trigger and describe how you would test a suspect copy.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Sample queries around the observed feature ranges, not uniformly over the whole space.
2. Distil continuous outputs with ridge regression; labels with a classifier.
3. Measure fidelity against the target's own predictions on held-out rows.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L16/solution.py
labs/solutions/L16/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Fidelity near 0.5 — the query distribution misses the region where the boundary lives.
- `Unknown label type: continuous` — you passed probabilities to a classifier; use ridge.
- Counter never increments — you call the model directly instead of the API wrapper.
- Budget comparison uses different test rows — fix the evaluation set once.

## 16. Security lessons learned

- Extraction cost is measured in queries, not in effort.
- Output granularity and quotas are cheaper than detection.
- A fidelity plateau is the number a quota should be set against.

## 17. Submission requirements

- The completed script and the budget table.
- The interface recommendation with numbers.
- Answers to the tasks.
- One paragraph on how you would detect this behaviour in production.

## 18. Acceptable use

Query the in-process mock admissions API that the starter constructs. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not run the extraction loop against a commercial API, and do not exceed a vendor's terms even in testing. The mock has no network listener.

## 20. Data handling

Synthetic admissions data trains the target; the fidelity set is held out locally.

## 21. Cleanup

Delete substitute models and query logs you saved.

## 22. Restoring your environment

Nothing is installed beyond the pinned stack, and no listener is left open.
