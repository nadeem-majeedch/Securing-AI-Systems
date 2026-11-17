---
title: MP03 · ML data poisoning detection prototype
description: Inject known poison into a dataset you control, then build and score a detector that has to find it.
---

# MP03 · ML data poisoning detection prototype

**After:** Module 07 · **Effort:** 11 h · **Stack:** Python, scikit-learn, Jupyter, SQLite or CSV artefacts
**Deliverable:** A detector, a labelled evaluation and a precision/recall table by poison rate

## Scenario

A retailer trains a demand-forecasting model on data assembled from a supplier portal. Suppliers can upload their
own historical sales. A competitor could, in principle, open an account and upload fabricated history for a
product category it wants under-forecast.

Nobody knows whether the current checks would notice. Your task is to find out: inject poison you control, build
the detector you would deploy, and report what it catches and what it misses.

## What you build

1. **A controlled attack.** At least two poisoning types: label flipping (or a label-noise variant) and one
   subtler pattern such as a target-category bias that leaves the marginal label distribution nearly unchanged.
   State the poison rate (start at 1 %, 3 % and 5 %).
2. **A detector suite.** At least three signals: per-source label statistics against history, a feature-space
   outlier score, and a slice-performance check that compares the poisoned model's error on the targeted slice
   with a clean baseline.
3. **A labelled evaluation.** Because you injected the poison, you know the ground truth. Report precision,
   recall and the false-positive count on clean rows at each poison rate.
4. **A triage output.** A ranked list of suspicious records with the signal that flagged each and a one-line
   reason, because a detector that says "1,240 records are suspicious" is unusable.
5. **A decision.** Which detector you would deploy at which threshold, given the measured precision, and what you
   would do when it fires.

## Suggested structure

```text
poisoning/
  inject.py     add_label_flip(df, rate, seed), add_target_bias(df, rate, seed)
  signals.py    label_shift(df), outlier_score(X), slice_gap(model, X, y)
  detect.py     combine(signals, weights) -> ranked list with reasons
  evaluate.py   score(predicted, injected_ids) -> precision/recall/fp
notebooks/
  investigation.ipynb
```

Keep the injected record ids in a separate file that the detector never reads. If the detector can see the answer
key, your precision is fiction.

## Checkpoints

| # | Checkpoint | Hours | Evidence |
|---|---|---|---|
| 1 | Threat model and injection design | 2 | Who can upload, what they gain, why the pattern is plausible |
| 2 | Clean baseline and injections | 3 | Three poison rates, each reproducible from a seed |
| 3 | Signals and combination | 3 | Each signal's standalone precision/recall |
| 4 | Evaluation by rate | 2 | Table of precision, recall, false positives at 1 %, 3 %, 5 % |
| 5 | Decision and limitation | 1 | Threshold chosen with a reason; the blind spot named |

## Deliverables

| Item | Format | Notes |
|---|---|---|
| Attack scripts | Python | Seeded, with the rate as a parameter |
| Detector | Python | Returns ranked records with reasons |
| Evaluation | Notebook + table | Precision, recall, FP count per rate |
| Decision note | 250 words | Deploy, tune, or reject — with the number that decided it |
| Limitation | 150 words | The attack your detector would not catch |

## Questions you must answer

1. Your detector's precision falls as the poison rate falls. Why, and what does that imply for a deployment where
   the base rate is unknown?
2. Which of your signals is evidence about the *data*, and which is evidence about the *model*? Why does the
   distinction matter for response?
3. If an attacker knows your detector, what is the cheapest way to evade it?

## Rubric

Apply the [shared mini-project rubric](../guidance/rubrics.md#mini-project-rubric), with these two indicators:

| Extra indicator | Proficient | Exemplary |
|---|---|---|
| **Evaluation honesty** | Precision and recall reported at one rate | Reported at three rates, with the ground-truth separation enforced and false positives counted on clean rows |
| **Response design** | Recommends blocking suspicious records | Distinguishes quarantine, retrain and accept, and states which records a human must review |

## Extension challenges

1. Add a clean-label attack (no label change) and report whether any of your signals survive it.
2. Measure the effect of poisoning on the targeted slice versus global accuracy, and use the gap as a detector.
3. Estimate the cost of the false positives in reviewer hours at the retailer's upload volume.

## Boundaries

Use synthetic or public data. Do not upload anything to a real supplier portal, and do not name a real supplier in
your report.
