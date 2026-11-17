---
title: "Level 2 assessment — Intermediate — answer key"
description: "Answer key for level 2 assessment — intermediate."
hide:
  - toc
---

# Level 2 assessment — Intermediate — answer key

## Section A key

| # | Item | Answer | Type | Outcome |
|---|---|---|---|---|
| 1 | L2-Q01 | A | Recall | M06.1 |
| 2 | L2-Q02 | A | Application | M07.3 |
| 3 | L2-Q03 | A | Judgement | M08.3 |
| 4 | L2-Q04 | A | Recall | M09.1 |
| 5 | L2-Q05 | A | Application | M10.2 |
| 6 | L2-Q06 | A | Judgement | M08.2 |
| 7 | L2-Q07 | A | Application | M09.4 |
| 8 | L2-Q08 | A | Judgement | M07.5 |

## Section A explanations

**1. L2-Q01** — **A: Flips the model's decision while the original is classified correctly**

Validity is the pair of constraint and effect; perceptibility, data access and transfer are properties some attacks have and others do not.

- **B** — Visibility is a design goal, not the definition.
- **C** — Training data is one attack setting.
- **D** — Transfer is common but not guaranteed.

**2. L2-Q02** — **A: The poisoning rate and the clean model's trigger rate**

Without the attacker's access constraint and a baseline, the success rate cannot be attributed to the backdoor rather than to a common target class.

- **B** — Epochs do not establish the attack's cost.
- **C** — Capacity is not the constraint.
- **D** — Test size affects precision, not attribution.

**3. L2-Q03** — **A: Gradient masking made the PGD evaluation misleading**

When a different attack family succeeds where the tuned one fails, the original evaluation measured the attack's weakness rather than the model's robustness.

- **B** — Model size is not the mechanism.
- **C** — PGD is a standard evaluation method.
- **D** — A defence that falls to a simple attack is not sound.

**4. L2-Q04** — **A: True-positive rate at a stated false-positive rate**

The attack is a ranking problem under an error constraint, so the operating point must be stated for the number to be comparable.

- **B** — A fixed threshold mixes both error types.
- **C** — Shadow-model count is method detail.
- **D** — Target AUC measures the model, not the leak.

**5. L2-Q05** — **A: It rises, because each query now carries one bit**

Confidence across classes is the signal that makes extraction cheap; removing it raises the number of queries needed for the same fidelity.

- **B** — Labels are noisier targets than probabilities.
- **C** — The decision is unchanged but the information returned is not.
- **D** — Labels still carry signal, just far less per query.

**6. L2-Q06** — **A: The smoothed prediction is unchanged within that L2 ball**

The certificate bounds change in the smoothed prediction under L2 perturbation and says nothing about correctness or other norms.

- **B** — The guarantee is about the smoothed classifier.
- **C** — Other attack families are outside the certificate.
- **D** — Accuracy and radius are different quantities.

**7. L2-Q07** — **A: Coarsening the output, because it removes fine-grained signal**

Inference attacks consume fine-grained output; a coarse band carries a fraction of the information and can be applied at the interface.

- **B** — Consent changes the legal basis, not the leak.
- **C** — More capacity usually increases memorisation.
- **D** — Logging supports response, not prevention.

**8. L2-Q08** — **A: Treat it as partial, because pruning may weaken rather than remove the trigger**

Sanitisation methods can reduce the trigger's effect without removing the mechanism, so retraining on reviewed data remains the reliable repair.

- **B** — A trigger can survive pruning.
- **C** — Accuracy improvement is not the security criterion.
- **D** — Pruning typically costs accuracy.

## Section B model answers

<div class="sas-answer"><p class="sas-item__head"><strong>L2-W1</strong> <span class="sas-meta">8 marks</span></p><p class="sas-answer__q">Design a robustness evaluation for an image classifier used in document verification. State the attack suite, the budgets, the control and the claim the results would support.</p><p class="sas-answer__label">Model answer</p><p>Suite: PGD with restarts at two budgets, a transfer attack from a substitute trained on similar documents, and an acquisition-realistic transform such as print-and-scan or JPEG compression, all at a stated L-infinity budget justified by sensor and compression effects. Control: random noise at the same budget, to separate attack effect from general degradation. Report clean accuracy, attacked accuracy and the flip count with seeds and variance on held-out data. The claim supported is narrow: resistance to those attacks at those budgets on that data, with no statement about other norms or physical conditions.</p></div>

<div class="sas-answer"><p class="sas-item__head"><strong>L2-W2</strong> <span class="sas-meta">8 marks</span></p><p class="sas-answer__q">A model trained on 300 patient records will be offered as a queryable service to researchers. Write the privacy assessment plan with two measurements and two controls.</p><p class="sas-answer__label">Model answer</p><p>Measure membership inference on members and non-members from the same population at a stated false-positive rate, and attribute inference on a sensitive field using the score alone. Controls: train with differential privacy at a stated epsilon and publish the utility cost, and restrict the interface to coarse bands with per-researcher query budgets and logging. Include the residual: DP bounds per-record influence rather than eliminating inference, and repeated queries compose, so the assessment needs a review date and a query-monitoring trigger.</p></div>

<div class="sas-answer"><p class="sas-item__head"><strong>L2-W3</strong> <span class="sas-meta">9 marks</span></p><p class="sas-answer__q">Explain how you would distinguish a poisoned training set from a genuinely drifting population when accuracy falls by 15 points in a week, naming the evidence for each hypothesis.</p><p class="sas-answer__label">Model answer</p><p>Poisoning evidence: a change in the ingestion log with a timestamp, rows from one source with anomalous label or feature statistics, a detectable patch or cluster, and an accuracy drop concentrated on a specific slice or trigger rather than spread evenly. Drift evidence: a shift in feature distributions that coincides with an upstream schema or vendor change, degradation across all slices proportional to their exposure to the new distribution, and recovery when recent data is used for retraining. The decisive step is to retrain on a versioned snapshot from before the change and compare slice-level results, which separates data corruption from population movement.</p></div>

