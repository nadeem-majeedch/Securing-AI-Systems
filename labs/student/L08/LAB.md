# L08 — Adversarial perturbations against a digit classifier

| | |
|---|---|
| **Module** | M06 |
| **Difficulty** | Intermediate |
| **Estimated time** | 80 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A document-handling team uses a small image classifier to route scanned forms. A security review asks the standard question — what happens if someone deliberately alters a scan — and the team has no measurement, only an opinion that "a human wouldn't notice a small change".

## 2. Problem statement

Train a small classifier on 8×8 digits, implement the fast gradient sign method, verify that the perturbation respects its epsilon budget, and measure accuracy and attack success across an epsilon sweep.

## 3. Learning objectives

- Implement FGSM correctly, including the clamp to the valid input range.
- Verify the declared perturbation budget against the actual maximum change.
- Report attack success rate alongside clean accuracy.
- Explain why a small pixel change is a security problem, not a quality problem.

## 4. Prerequisites

- Module 06 lecture; L02 recommended.

## 5. Required software

- Python 3.12+
- PyTorch (CPU build)
- NumPy

## 6. Dataset and input files

- `labs/datasets/digits_subset.npz` — 1,797 8×8 digit images with labels, stored locally.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L08/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L08/starter.py
```

1. Load the `.npz`, scale pixels to [0, 1] and split 1,400 for training and the rest for testing.
2. Train a `Flatten → Linear(64, 10)` model for 12 epochs with Adam.
3. Implement `fgsm(x, y, eps)` using the sign of the input gradient.
4. Sweep epsilon over 0, 0.05, 0.10, 0.20 and 0.30.
5. For each epsilon, record accuracy, attack success and the maximum pixel change actually used.
6. Assert every perturbation stays within its epsilon.
7. Assert attack success increases with the budget, then write the defensive conclusion.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L08/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

Clean accuracy is **0.829**. Accuracy falls to **0.685** at epsilon 0.05, **0.496** at 0.10, **0.081** at 0.20 and **0.000** at 0.30. The `max_pixel_change` column equals epsilon in every row, which is the evidence that the budget was respected.

## 10. Interpretation of results

A 0.10 change is 10 % of the pixel range — visible only if you look for it, and it removes a third of the model's accuracy. The budget column matters as much as the accuracy column: without it, "90 % attack success" could mean an unbounded perturbation that no scanner would produce.

## 11. Student tasks

1. Report the pixel range and explain what epsilon 0.10 means in grey levels.
2. Rerun with 25 training epochs and report clean accuracy and success at epsilon 0.10.
3. Explain why the attack needs gradients and what a black-box attacker would do instead.
4. Write the two-sentence limitation for the model card.

## 12. Challenge exercises

1. Implement a one-step random-start variant and compare success at the same budget.
2. Add a simple input-smoothing defence and measure whether it reduces success.
3. Plot the adversarial example and its amplified perturbation for three digits.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. `torch.autograd.grad(loss, x)` returns the gradient only if `x.requires_grad_()` was set.
2. Clamp with `.clamp(0, 1)` after the step, or the attack exceeds the image range.
3. Measure the budget with `(x_adv - x).abs().max()`, not with a mean.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L08/solution.py
labs/solutions/L08/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- `RuntimeError: element 0 of tensors does not require grad` — the input tensor is not a leaf with `requires_grad`.
- Success rate is 0 — you attacked the wrong label direction (subtract instead of add the sign).
- Accuracy improves at higher epsilon — the perturbation is not clamped and leaves the valid range.
- Model stuck at 10 % accuracy — the labels were loaded as floats; keep them as `int64`.

## 16. Security lessons learned

- An attack result without a budget is not a result.
- Small, bounded changes are enough to break a linear classifier.
- The defender's metric is accuracy under attack at a stated epsilon.

## 17. Submission requirements

- The completed script and the epsilon sweep table.
- The two-sentence model-card limitation from task 4.
- Answers to the remaining tasks.
- One paragraph on whether input smoothing would satisfy the reviewer, with your measurement.

## 18. Acceptable use

Generate perturbations for the local classifier only. The point is to measure the model, not to attack a service. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not apply the perturbations to a deployed recogniser, a CAPTCHA, a document scanner or any system you do not own, and do not upload crafted images anywhere.

## 20. Data handling

`digits_subset.npz` is a third-party teaching extract (UCI, CC BY 4.0 — see `ATTRIBUTION.md`), not course-owned; keep its provenance note if you copy it.

## 21. Cleanup

Perturbed arrays live in memory. Delete any `.npz` or figure you saved, and remove the lab's `__pycache__` if you want a clean tree.

## 22. Restoring your environment

The pinned PyTorch wheel is all this lab needs. If you installed a CUDA build, no rollback is required.
