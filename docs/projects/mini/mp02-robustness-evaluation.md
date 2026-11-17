---
title: MP02 · Adversarial robustness evaluation tool
description: Build a harness that measures accuracy under attack at three budgets, with a control that makes the number interpretable.
---

# MP02 · Adversarial robustness evaluation tool

**After:** Modules 06 and 08 · **Effort:** 11 h · **Stack:** Python, scikit-learn or PyTorch, NumPy, Jupyter
**Deliverable:** A reusable evaluation harness, a results table and a claim statement

## Scenario

A document-scanning team ships a classifier that decides whether a photographed form is complete. A customer asks
whether the model is "robust". The team has one number: 96 % accuracy on a held-out set. They have no idea what
that number means under an adversary, and no way to find out before the next release.

You will build the harness they should have: a script that takes a model, a dataset and a threat model, and
returns a table that a security reviewer can read without trusting the author.

## What you build

1. **Baseline evaluation.** Clean accuracy on a held-out split, with the split described (size, class balance,
   seed).
2. **Two attacks.** A single-step attack (FGSM-style) and an iterative one (PGD-style with a random start and
   projection). If you use scikit-learn, implement the gradient for a linear or logistic model yourself; do not
   call a library that hides the budget.
3. **Budget enforcement.** Assert that the realised perturbation respects the stated L∞ budget, and report the
   realised mean and maximum change. A harness that claims ε = 0.1 while producing 0.13 is not measuring what it
   says.
4. **A same-budget control.** Random noise of the same magnitude, so the drop can be attributed to the attack
   rather than to perturbation size. This is the step most student harnesses omit and most reviewers look for.
5. **Report.** A JSON result file plus a Markdown table: clean accuracy, attack accuracy at 0.05 / 0.1 / 0.2,
   control accuracy at the same budgets, and the delta between attack and control.

## Suggested structure

```text
robustness/
  data.py        load_digits_split(seed) -> X_train, y_train, X_test, y_test
  attacks.py     fgsm(model, X, y, eps), pgd(model, X, y, eps, steps, restarts)
  evaluate.py    evaluate(model, X, y, budgets) -> list[Result]
  report.py      to_markdown(results) -> str
tests/
  test_attacks.py   budget assertion, monotonicity, determinism under seed
```

`evaluate` must be callable with any object exposing `predict` and `grad`, which is what makes the harness reusable
across the course's later projects.

## Checkpoints

| # | Checkpoint | Hours | Evidence |
|---|---|---|---|
| 1 | Threat model and budget justification | 1 | What an attacker can change about a photographed form, in pixels and compression |
| 2 | Baseline and single-step attack | 3 | Clean and FGSM accuracy, with the realised ε printed |
| 3 | Iterative attack and control | 3 | PGD at three budgets plus random-noise control at the same budgets |
| 4 | Determinism and tests | 2 | Same seed gives the same numbers; budget assertion fails on an oversized step |
| 5 | Report and claim | 2 | One table, one 40-word claim, one limitation |

## Deliverables

| Item | Format | Notes |
|---|---|---|
| Harness | Python package | One command reproduces every number |
| Results | JSON + Markdown | Three budgets, two attacks, control |
| Tests | `pytest` | Budget, determinism, monotonicity |
| Claim statement | ≤ 40 words | Names the attack, budget and result |
| Limitation | 150 words | The reason your conclusion might be wrong |

## Questions you must answer

1. Why is the random-noise control necessary, and what would you conclude if attack and control accuracy were
   equal at every budget?
2. Your iterative attack is stronger than your single-step attack. What does the size of the gap tell a reviewer
   about the model, and about your harness?
3. What does your result *not* say about an attacker who can re-photograph the form instead of editing pixels?

## Rubric

Apply the [shared mini-project rubric](../guidance/rubrics.md#mini-project-rubric), with these two indicators:

| Extra indicator | Proficient | Exemplary |
|---|---|---|
| **Attack validity** | Attacks run and produce plausible drops | Budget assertion, restarts and a control that isolates attack from noise |
| **Claim discipline** | Claim summarises the table | Claim matches the table exactly and excludes what was not tested, in the same sentence |

## Extension challenges

1. Add a third attack with a different norm (L2) and report whether the ranking of budgets changes.
2. Train on adversarial examples and re-run the harness adaptively against the defended model; report what the
   defence bought in accuracy, latency and residual attack success.
3. Make the harness fail the build when accuracy under attack drops by more than five points against a stored
   baseline.

## Boundaries

Use the course dataset or one you generate. Do not attack a deployed service, and do not include material that
would help forge or alter a real document.
