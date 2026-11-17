# L09 — Transfer attacks and the price of a black-box query

| | |
|---|---|
| **Module** | M06 |
| **Difficulty** | Advanced |
| **Estimated time** | 90 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A document-routing vendor publishes an API and keeps the model secret. The security team has two models of their own: one is visibly similar to the vendor's, one is not. They want to know whether an attacker who never sees the vendor's weights can still break it — and what a purely black-box attacker has to spend.

## 2. Problem statement

Craft a perturbation on your own model, test whether it transfers to a second architecture you did not attack, compare it with random noise at the same budget, and price a black-box random-search attack in queries.

## 3. Learning objectives

- Measure transfer success between two architectures.
- Compare transfer with a random-noise control at the same budget.
- Quantify the query cost of black-box search.
- Explain why an unpublished model is not a security control.

## 4. Prerequisites

- L08 (FGSM on digits).

## 5. Required software

- Python 3.12+
- PyTorch (CPU)
- NumPy

## 6. Dataset and input files

- `labs/datasets/digits_subset.npz` — same split as Lab 08.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L09/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L09/starter.py
```

1. Load the digits and build a linear model A and a one-hidden-layer model B on the same training rows.
2. Confirm both are accurate on clean test data.
3. Craft a single FGSM perturbation on A at epsilon 0.2 and check the budget.
4. Score the same adversarial images against B, and against random noise at the same epsilon.
5. Run a 200-try single-pixel random search against B and report the query count and accuracy.
6. Assert that the white-box attack works on A and that transfer beats random noise.
7. State what an attacker needs to reproduce your white-box result against a third-party model.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L09/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

Clean accuracy is **A 0.831** and **B 0.821**. The white-box attack drops A to **0.063**. The same images drop B to **0.272** — a transfer effect of **0.549** — while random noise at the same budget drops B only to 0.806. The black-box single-pixel search spends **79,400 queries** and leaves B at 0.819.

## 10. Interpretation of results

Transfer works because both models learned similar features from the same data; it costs one gradient and no knowledge of B's weights. The black-box result is the counterweight: naive random search over a single pixel is almost useless, which is why real query attacks use scores and many iterations — and why query volume is a detection signal.

## 11. Student tasks

1. Report how many of B's predictions changed relative to its clean predictions.
2. Repeat the transfer at epsilon 0.1 and state whether the effect survives a smaller budget.
3. Explain in three sentences why transfer is stronger between models trained on the same data.
4. Write the sentence you would put in a threat model about API-only access.

## 12. Challenge exercises

1. Try a targeted transfer: craft the perturbation so images are misclassified as a specific class.
2. Add a third model with a different activation and report whether transfer still holds.
3. Estimate the queries needed for the random search to beat transfer, and extrapolate from your measurements.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Reuse the FGSM function from Lab 08; the only change is which model computes the gradient.
2. For transfer, do not recompute gradients on B — just evaluate B on A's adversarial images.
3. Random noise must use the same epsilon; otherwise the comparison is meaningless.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L09/solution.py
labs/solutions/L09/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Transfer accuracy equals clean accuracy — you accidentally attacked B instead of A.
- Perturbation exceeds 0.2 — clamp after the step.
- The random search improves nothing — you are replacing pixels with values outside the valid range.
- Different clean accuracies — the models were trained on different splits; use one split.

## 16. Security lessons learned

- A hidden architecture raises the attacker's cost but does not stop transfer.
- Always include a same-budget random control; it is the cheapest sanity check in adversarial ML.
- Query count is both an attack cost and a defender's signal.

## 17. Submission requirements

- The completed script and the transfer table.
- The black-box measurement with its query count.
- Threat-model sentence from task 4.
- Answers to the remaining tasks.

## 18. Acceptable use

Measure transfer between two models you train here, and count queries in the simulation. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not send queries to a commercial prediction API or a hosted model. The black box in this lab is a local model with its gradients hidden, and the query budget is simulated.

## 20. Data handling

Same synthetic digits extract as L08. No query log from a real service is used or created.

## 21. Cleanup

Delete saved query logs and substitute-model checkpoints; the script otherwise keeps both in memory.

## 22. Restoring your environment

Nothing beyond the pinned stack; no service is started.
