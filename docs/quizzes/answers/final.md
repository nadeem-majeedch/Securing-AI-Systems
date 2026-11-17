---
title: "Final assessment — answer key"
description: "Answer key for final assessment."
hide:
  - toc
---

# Final assessment — answer key

## Section A key

| # | Item | Answer | Type | Outcome |
|---|---|---|---|---|
| 1 | F-Q01 | A | Recall | M01.3 |
| 2 | F-Q02 | A | Application | M03.2 |
| 3 | F-Q03 | A | Judgement | M04.4 |
| 4 | F-Q04 | A | Application | M06.5 |
| 5 | F-Q05 | A | Judgement | M07.1 |
| 6 | F-Q06 | A | Recall | M09.5 |
| 7 | F-Q07 | A | Application | M10.4 |
| 8 | F-Q08 | A | Judgement | M12.5 |
| 9 | F-Q09 | A | Application | M14.4 |
| 10 | F-Q10 | A | Recall | M16.5 |
| 11 | F-Q11 | A | Judgement | M18.5 |
| 12 | F-Q12 | A | Application | M20.3 |

## Section A explanations

**1. F-Q01** — **A: It averages over a distribution the attacker does not sample from**

The adversary chooses a region of input space, so an average over test data says nothing about the inputs that will be used against the system.

- **B** — The value is irrelevant to the argument.
- **C** — Accuracy is computable for classifiers.
- **D** — Accuracy and latency are distinct.

**2. F-Q02** — **A: A scoped service identity limited to those two paths**

Blast radius follows from what the workload can reach; a scoped identity keeps a compromised job from becoming an account-wide incident.

- **B** — Shared accounts remove attribution and over-grant.
- **C** — Administrator rights convert code execution into cluster compromise.
- **D** — Personal tokens cannot be rotated cleanly.

**3. F-Q03** — **A: Residual and unverified, with a test date required**

An untested control is a hypothesis; a register that claims reduction without evidence is a wish list.

- **B** — Deployment is not evidence of effect.
- **C** — Design intent does not establish effectiveness.
- **D** — Deferral leaves the risk unmanaged.

**4. F-Q04** — **A: The attack configuration and a same-budget random control**

The number means nothing without the attack, its budget and a control showing the drop is caused by the attack rather than by the perturbation size.

- **B** — Capacity does not describe the attack.
- **C** — Training time is unrelated.
- **D** — Class count is task detail.

**5. F-Q05** — **A: Clean-label poisoning**

Clean-label attacks keep correct labels and modify features, so the signal exists only in the feature distribution.

- **B** — Availability attacks usually show label noise at scale.
- **C** — Label flipping is visible by definition.
- **D** — Relabelled triggers appear in label statistics.

**6. F-Q06** — **A: No leakage was detected by this attack at this operating point on this population**

A negative result is scoped by method, operating point and population; generalising it converts absence of evidence into evidence of absence.

- **B** — Privacy is a system property, not a test outcome.
- **C** — A stronger attack may succeed.
- **D** — The test says nothing about the data's content.

**7. F-Q07** — **A: Per-account query quotas with coarser output**

Extraction consumes information per query and across queries, so both levers act on the channel rather than on the weights.

- **B** — That changes the model.
- **C** — Retraining changes the target without limiting queries.
- **D** — Class count is set by the task.

**8. F-Q08** — **A: Refuse roughly ten legitimate requests per real attack**

With that prevalence the false positives outnumber true positives by about ten to one, so blocking converts the detector into a source of refusals.

- **B** — TPR is not precision.
- **C** — The arithmetic shows a large effect.
- **D** — Layered controls remain necessary.

**9. F-Q09** — **A: Validating the amount against the order record and a policy cap**

Arguments must be checked against authoritative data, because the model can be persuaded to supply any value.

- **B** — A prompt rule is advisory.
- **C** — Rounding changes presentation.
- **D** — Logging records the loss.

**10. F-Q10** — **A: Authorisation denials with principal, action and reason**

Denials record refused attempts, which is where probing and escalation appear first, and they avoid storing sensitive payloads.

- **B** — Full payloads create exposure with little detection value.
- **C** — Image size is inventory metadata.
- **D** — Accuracy is not an event stream.

**11. F-Q11** — **A: The causal mechanism, the failed control and the change that prevents recurrence**

A review earns its cost by changing a control and naming the mechanism; otherwise the same incident returns by another path.

- **B** — Timeline is context, not a corrective action.
- **C** — Individual blame does not prevent recurrence.
- **D** — Capacity is not the mechanism.

**12. F-Q12** — **A: That the digest matches and behaviour matches the reference**

Tags are mutable labels; identity and behaviour are the two checks that establish what is actually running.

- **B** — Existence is an inventory fact.
- **C** — A URL proves reachability.
- **D** — Logging is observability.

## Section B model answers

<div class="sas-answer"><p class="sas-item__head"><strong>F-W1</strong> <span class="sas-meta">15 marks</span></p><p class="sas-answer__q">Threat model a hospital assistant that summarises referrals, retrieves from a clinical index and can page the on-call clinician. Produce four threat rows with likelihood, impact, control and residual risk, and name the assumption a reviewer should challenge.</p><p class="sas-answer__label">Model answer</p><p>Expected rows: manipulated referral instructing omission (likely, severe; control: treat text as data and cross-check structured allergy fields; residual: novel phrasing), cross-ward retrieval (possible, severe; control: scope by ward and role before ranking; residual: misconfigured ACL), clinician paged for a non-urgent case (likely, moderate; control: page only the authenticated on-call group with confirmation; residual: fatigue), hallucinated finding (likely, severe; control: extractive summary with citations and sign-off; residual: citation drift). The assumption to challenge is that clinicians read the cited evidence under time pressure; if they do not, oversight is nominal.</p></div>

<div class="sas-answer"><p class="sas-item__head"><strong>F-W2</strong> <span class="sas-meta">15 marks</span></p><p class="sas-answer__q">A vendor offers a fraud model with a 0.91 AUC and a 'robust and private' claim. Write the technical due-diligence list you would issue, with the evidence required for each item.</p><p class="sas-answer__label">Model answer</p><p>Utility: AUC with the evaluation population and time window, not a single number. Robustness: the attack family, norm, budget, measured accuracy under attack and a same-budget control, plus whether the evaluation was adaptive to their defence. Privacy: a membership-inference result at a stated false-positive rate on members and non-members, and the training-time privacy mechanism with epsilon if claimed. Data: provenance and labelling process, retention and deletion commitments. Supply chain: artefact digest, format, and change-notification terms. Each item names the artefact or number that would satisfy it, so the vendor cannot answer with adjectives.</p></div>

<div class="sas-answer"><p class="sas-item__head"><strong>F-W3</strong> <span class="sas-meta">15 marks</span></p><p class="sas-answer__q">Design the monitoring and response plan for a deployed RAG assistant, including three signals, two thresholds with their base-rate justification, and the recovery verification you would require.</p><p class="sas-answer__label">Model answer</p><p>Signals: per-principal query similarity with boundary concentration (extraction); retrieval isolation failures and foreign-document attempts (confidentiality); canary-set output quality covering refusals, omissions and citations (integrity). Thresholds: similarity above a stated percentile sustained for ten minutes, justified by the observed distribution of legitimate batch traffic; isolation failures above zero in any window, because the expected rate is zero and any occurrence is a defect. Recovery verification: hash match against the signed manifest plus behavioural parity on the canary set, with credentials rotated and a named owner for the root cause. The plan should state what was not detected, so the residual is visible.</p></div>

<div class="sas-answer"><p class="sas-item__head"><strong>F-W4</strong> <span class="sas-meta">15 marks</span></p><p class="sas-answer__q">Write the assurance argument for releasing an AI feature next week with one known failing control, and state what you would refuse to sign.</p><p class="sas-answer__label">Model answer</p><p>The argument should state each claim with its evidence, mark the failing control explicitly, and describe the compensating measure: for example retrieval isolation failing one test, with a temporary restriction that the assistant serves a single tenant until the fix lands. Residual risk is stated in operational terms with a monitoring trigger and an expiry date, and an owner is named. Refuse to sign if the failing control concerns data exposure with no compensating restriction, if the residual is unquantified, if no post-launch owner exists, or if the waiver has no expiry. The distinction is between accepting a bounded risk and accepting an unbounded one.</p></div>

