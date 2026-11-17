---
title: A3 · Identifying poisoning in a synthetic dataset
description: Assignment 3 — investigate a suspicious accuracy drop and decide whether the data was poisoned.
---

# A3 · Identifying poisoning in a synthetic dataset

**After:** Module 07 · **Weight:** 10 % · **Length:** 1,000 words plus a notebook or script
**Deliverable:** An investigation report with reproducible analysis and a recommendation

## Scenario

A university's admissions office uses a model to prioritise applications for manual review. Accuracy on the
annual holdout set fell from 0.84 to 0.69 after a routine retrain. The data science team suspects a distribution
shift; the registrar suspects the model is "broken"; a local journalist has asked whether applications were
manipulated.

You have: the training data from both runs, the labels, the model artefacts, and the ingestion logs with a
timestamp and source field per batch. You do not have the applicants.

The synthetic dataset supplied with the Module 07 laboratory is a suitable stand-in; you may also construct your
own with a documented generation script. If you build your own, publish the generator: the marker needs to be able
to regenerate your data, not just read your conclusions.

## Problem statement

Decide whether the fall is explained by population change, label corruption or deliberate poisoning, and defend the
decision with evidence that another analyst could reproduce.

## Requirements

1. A **hypothesis set** with at least three explanations and the evidence that would distinguish them.
2. An **analysis** that reports: accuracy by slice, label statistics by source and batch, duplicate rates, and a
   feature-space outlier scan.
3. A **reproduction package**: script or notebook, seed, environment note and the exact commands.
4. A **decision** with a confidence statement, and the evidence that would change your mind.
5. A **recommendation** to the registrar in plain language that does not overstate what you found.

## Tasks

1. Write the three hypotheses before you look at the data, and record what you expect to see under each.
2. Compute the slice-level accuracy drop. Identify whether it is concentrated or uniform.
3. Examine label statistics per source and batch; look for a batch whose label distribution differs from its
   history.
4. Run an outlier scan appropriate to the data, and state its assumption and its failure mode.
5. Compare a retrain on the pre-incident snapshot with the current model on the same holdout.
6. Write the decision, the confidence and the falsifier.
7. Write the registrar's paragraph: what happened, what it means for applicants, what you are doing next.

## Deliverables

| Item | Format | Length |
|---|---|---|
| Investigation report | prose with tables | 900 words |
| Analysis package | script/notebook, seed, commands | runnable |
| Decision record | one page: decision, confidence, falsifier | 1 page |
| Registrar paragraph | plain language | 150 words |

## Evaluation criteria

- **Method:** are the tests appropriate, and are their assumptions stated?
- **Discrimination:** does the evidence actually separate the hypotheses, or is it consistent with all of them?
- **Reproducibility:** can another analyst rerun your analysis from the package alone?
- **Communication:** is the registrar's paragraph accurate about uncertainty?

## Rubric

| Criterion | 1 — Emerging | 2 — Developing | 3 — Proficient | 4 — Exemplary |
|---|---|---|---|---|
| Method | One test, no assumption | Several tests, assumptions implicit | Appropriate tests with stated assumptions | Tests chosen to discriminate between hypotheses |
| Discrimination | Evidence fits every hypothesis | Some separation | Clear separation with a stated basis | A falsifier is named and would be observable |
| Reproducibility | Will not run | Runs with manual fixes | Runs from a fresh environment | Runs, with seed, versions and expected output |
| Communication | Overclaims or vague | Understandable, hedged unevenly | Accurate and measured | States what is unknown and what it means for applicants |

## Extension challenges

1. Add a second, subtler poisoning pattern that your scan would miss, and describe the test that would catch it.
2. Estimate the cost of the wrong decision in each direction (false alarm versus missed poisoning) and use it to
   justify your confidence threshold.
3. Design the ingestion control that would have made this investigation unnecessary.

## Constraints

Use synthetic or fully de-identified data only. Do not attempt to obtain real applicant records. If you construct
your own dataset, publish the generator with the report.
