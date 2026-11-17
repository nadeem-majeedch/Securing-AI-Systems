---
title: A5 · Assessing model privacy risks
description: Assignment 5 — measure privacy leakage in a small model and write the assessment a DPO can sign.
---

# A5 · Assessing model privacy risks

**After:** Module 09 · **Weight:** 10 % · **Length:** 900 words plus a measurement notebook
**Deliverable:** A privacy assessment with measured leakage, two controls and a residual statement

## Scenario

A fertility clinic has trained a model that predicts treatment response from 900 historical patient records. It
wants to offer the model to two partner clinics as a queryable service, returning a probability. The data
protection officer has to approve the arrangement and has asked a direct question: *can a partner learn whether a
named patient was in the training set?*

The clinic cannot share records. It can share the model and aggregated results.

## Problem statement

Measure the leakage that a partner with query access could exploit, and write an assessment that answers the DPO's
question with evidence rather than assurance.

## Requirements

1. A **membership-inference measurement** on members and non-members from the same population, reporting the
   true-positive rate at a stated false-positive rate and 2·AUC−1.
2. An **attribute-inference measurement** on one sensitive field, with the base rate stated.
3. Two **controls**, each with its measured or expected effect and its cost.
4. A **residual statement** in plain language that the DPO can rely on.
5. A **retention and deletion** position: what happens to a record that is erased after training.

## Tasks

1. Split the population, train on the member half, and score both halves by the probability assigned to the true
   label.
2. Compute the ROC curve and report the two metrics with the operating point.
3. Fit a simple attribute-inference model from score to a sensitive field and report precision against the base
   rate.
4. Choose two controls: one interface change and one training change. Predict the effect of each, then measure
   one.
5. Write the residual statement: what the clinic can tell a partner, and what it cannot.
6. State the deletion position, including what would be required before a claim of erasure is made.

## Deliverables

| Item | Format | Length |
|---|---|---|
| Assessment | prose with tables | 800 words |
| Measurement notebook | runnable, seeded | — |
| Residual statement | plain language, 150 words | — |
| Deletion position | bullets with obligations | 200 words |

## Evaluation criteria

- **Measurement:** is the attack correctly specified, and is the operating point stated?
- **Interpretation:** does the report distinguish ranking leakage from identification?
- **Control realism:** are the controls implementable by this clinic, and are their costs stated?
- **Honesty:** does the residual statement avoid claiming privacy that was not demonstrated?

## Rubric

| Criterion | 1 — Emerging | 2 — Developing | 3 — Proficient | 4 — Exemplary |
|---|---|---|---|---|
| Measurement | AUC only, no operating point | TPR or FPR reported separately | Both, with 2·AUC−1 | Both, with the population and split described |
| Interpretation | "The model is private/anonymous" | Recognises leakage exists | Distinguishes ranking from identification | Explains what a negative result would and would not mean |
| Control realism | Generic advice | One feasible control | Two feasible controls with costs | Controls measured or bounded, with residual stated |
| Honesty | Overclaims | Hedged inconsistently | Accurate within scope | Names the untested attack and the review date |

## Extension challenges

1. Add a shadow-model attack and compare its advantage with the simple threshold attack.
2. Evaluate a differentially private variant at two epsilon values and report the utility cost.
3. Draft the partner-facing data-use terms that match your residual statement.

## Constraints

Use synthetic or fully de-identified data. Do not attempt to re-identify any individual. If you use the course
dataset, cite the generator and the seed.
