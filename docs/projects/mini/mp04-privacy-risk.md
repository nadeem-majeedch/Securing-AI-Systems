---
title: MP04 · Model privacy risk assessment
description: Measure membership leakage in a model you trained, then write the assessment a data protection officer can sign.
---

# MP04 · Model privacy risk assessment

**After:** Module 09 · **Effort:** 10 h · **Stack:** Python, scikit-learn, NumPy, Jupyter
**Deliverable:** A measured leakage assessment with two controls and a residual statement

## Scenario

A clinic trains a model that predicts whether a patient will respond to a treatment, using 1,200 historical
records. It wants to expose the model to two partner clinics as a probability-returning endpoint. The data
protection officer has one question: *can a partner learn whether a named patient was in the training set?*

You cannot share records, but you can share measurements. Build the assessment.

## What you build

1. **A membership-inference attack.** Split a population into members (trained on) and non-members (held out) from
   the same distribution. Score both by the probability the model assigns to the true label. Report the ROC curve,
   TPR at a stated false-positive rate (5 % and 1 %), and 2·AUC − 1.
2. **A second attack.** Either an attribute-inference attempt on one sensitive field or a shadow-model variant.
   Report precision against the base rate, not accuracy.
3. **Two controls, measured.** One interface control (rounding, coarser output, or a query cap) and one training
   control (regularisation, fewer features, or a differentially private variant). Measure at least one; bound the
   other and say why you could not measure it.
4. **A residual statement.** Plain language, 150 words, that the DPO could paste into a risk register — including
   what your measurement does *not* establish.
5. **A deletion position.** What happens to a record erased after training, and what you would need before claiming
   erasure.

## Suggested structure

```text
privacy/
  split.py       members_and_nonmembers(df, seed)
  attack.py      score_membership(model, X, y) -> scores; roc_metrics(scores, labels)
  controls.py    round_output(p, digits), regularised_model(alpha)
  report.py      assessment_table(results) -> str
notebooks/
  assessment.ipynb
```

## Checkpoints

| # | Checkpoint | Hours | Evidence |
|---|---|---|---|
| 1 | Population, split and threat model | 2 | Who queries, what they already know, what success means |
| 2 | Membership attack and metrics | 3 | ROC curve, TPR at 5 % and 1 % FPR, 2·AUC − 1 |
| 3 | Second attack | 2 | Precision against base rate, with the base rate stated |
| 4 | Controls | 2 | Measured effect of at least one control |
| 5 | Residual and deletion position | 1 | 150-word residual; erasure obligations listed |

## Deliverables

| Item | Format | Notes |
|---|---|---|
| Notebook | Runnable, seeded | Produces every number in the report |
| Assessment | 800 words | Method, results, controls, residual |
| Residual statement | 150 words | No jargon the DPO cannot verify |
| Deletion position | 200 words | Cover artefacts, caches and backups |

## Questions you must answer

1. Why can a model with high accuracy have low membership leakage, and why does that not make it private?
2. Your attack's TPR at 1 % FPR is 8 %. What can the clinic say to a partner, and what must it not say?
3. Rounding output to two decimals reduces leakage. What does it cost the partner, and how would you decide whether
   the trade is acceptable?

## Rubric

Apply the [shared mini-project rubric](../guidance/rubrics.md#mini-project-rubric), with these two indicators:

| Extra indicator | Proficient | Exemplary |
|---|---|---|
| **Attack specification** | Membership advantage reported | Advantage at two operating points, with population and split described |
| **Residual honesty** | States that leakage was found or not found | States the attack, operating point and population the result applies to, and names an untested attack |

## Extension challenges

1. Add a shadow-model attack and compare its advantage with the threshold attack.
2. Train a differentially private variant at two ε values and report the utility cost on the same split.
3. Draft the partner-facing data-use terms that match your residual statement.

## Boundaries

Synthetic or fully de-identified data only. Do not attempt re-identification, and do not publish a dataset that
could be linked to individuals.
