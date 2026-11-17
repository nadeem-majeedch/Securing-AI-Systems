# L12 — PGD, projection and an honest robustness number

| | |
|---|---|
| **Module** | M08 |
| **Difficulty** | Advanced |
| **Estimated time** | 90 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A model card claims "robust to adversarial perturbations". The reviewer asks for the attack, the budget and the measured accuracy. The team sends a single number with no epsilon, and a script that does not clamp its perturbation — the number is therefore meaningless and the claim unsupportable.

## 2. Problem statement

Implement projected gradient descent with a random start and correct projection, compare it with FGSM, reproduce the unprojected mistake, and write the claim the evidence actually supports.

## 3. Learning objectives

- Implement PGD with projection and a random start.
- Verify the realised perturbation against the declared budget.
- Show how omitting the projection inflates the result.
- Write a robustness claim with its attack configuration attached.

## 4. Prerequisites

- L08 (FGSM), L09 recommended.

## 5. Required software

- Python 3.12+
- PyTorch (CPU)
- NumPy

## 6. Dataset and input files

- `labs/datasets/digits_subset.npz`.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L12/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L12/starter.py
```

1. Load digits, train the linear model and confirm clean accuracy.
2. Implement `pgd(x, y, eps, alpha, steps)` with a random start and element-wise projection.
3. For epsilon 0.05, 0.10 and 0.20 compare FGSM and PGD-15, recording the realised maximum change.
4. Assert every realised change is within its epsilon.
5. Run the same loop without projection and report the realised change against the declared budget.
6. Assert the unprojected loop exceeds its budget.
7. Write the defensible claim and the indefensible one.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L12/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

Clean accuracy is **0.846**. FGSM/PGD-15 accuracy is **0.680/0.678** at epsilon 0.05, **0.479/0.486** at 0.10 and **0.058/0.063** at 0.20; the realised change equals epsilon in every row. The unprojected loop reports accuracy 0.000 with a realised change of **0.750** against a declared 0.200.

## 10. Interpretation of results

At this model size the iterative attack is not much stronger than one step — the model is nearly linear, so the sign step already captures most of the damage. That is a finding about the model, not a reason to skip PGD: on a deeper model the gap widens, and the unprojected number is not comparable to anything.

## 11. Student tasks

1. Report the realised perturbation for FGSM and PGD at epsilon 0.10 and explain any difference.
2. Increase PGD to 30 steps and report whether accuracy changes materially.
3. Explain why a random start matters on a piecewise-linear model.
4. Rewrite the vendor's claim as a sentence you could defend in a review.

## 12. Challenge exercises

1. Add restarts (three random starts, keep the worst case) and report the change.
2. Implement an L2 projection instead of L-inf and report robust accuracy.
3. Design the evaluation record you would require from a vendor: list every field.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Project with `torch.max(torch.min(x_adv, x + eps), x - eps)` and then clamp to [0, 1].
2. Detach the tensor between steps, then re-enable gradients on the new tensor.
3. Measure the budget on the final tensor, not on an intermediate one.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L12/solution.py
labs/solutions/L12/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- `RuntimeError` about grad — the tensor is not a leaf; clone and call `requires_grad_(True)`.
- Budget exceeded — projection happens before the clamp or not at all.
- Accuracy identical to FGSM — alpha is equal to epsilon, so PGD takes one effective step.
- Unprojected accuracy better than projected — you are evaluating on a larger budget.

## 16. Security lessons learned

- A robustness number without its attack configuration is not a result.
- Projection is the difference between an attack and a bug.
- Iterative attacks cost compute; report that cost with the number.

## 17. Submission requirements

- The completed script and both tables.
- The two claims from instruction 7.
- The evaluation-record fields from challenge 3.
- Answers to the tasks.

## 18. Acceptable use

Run the attack loop against your own small classifier with the budget the lab declares. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not lift the epsilon bound, and do not turn the loop into a denial-of-service test against a real endpoint. The unbounded-loop demonstration is capped by the script on purpose.

## 20. Data handling

The digits extract is third-party teaching data, and perturbed examples stay local.

## 21. Cleanup

Nothing is written. Delete figures or `.pt` files you saved and clear `__pycache__` if you want a clean `git status`.

## 22. Restoring your environment

Nothing beyond the pinned PyTorch; no service is started.
