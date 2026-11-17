---
title: "Level 4 assessment — Professional practice — answer key"
description: "Answer key for level 4 assessment — professional practice."
hide:
  - toc
---

# Level 4 assessment — Professional practice — answer key

## Section A key

| # | Item | Answer | Type | Outcome |
|---|---|---|---|---|
| 1 | L4-Q01 | A | Recall | M16.1 |
| 2 | L4-Q02 | A | Application | M17.2 |
| 3 | L4-Q03 | A | Judgement | M18.2 |
| 4 | L4-Q04 | A | Recall | M18.4 |
| 5 | L4-Q05 | A | Application | M20.2 |
| 6 | L4-Q06 | A | Judgement | M19.4 |
| 7 | L4-Q07 | A | Application | M20.1 |
| 8 | L4-Q08 | A | Judgement | M17.4 |

## Section A explanations

**1. L4-Q01** — **A: Authorisation depends on a value the caller controls**

The tenant must come from the authenticated principal; a body field lets any caller cross a boundary by editing one value.

- **B** — Transport encryption covers the body.
- **C** — Length is irrelevant.
- **D** — Caching is unrelated.

**2. L4-Q02** — **A: Threat family and system component**

Threat by component shows which combinations were exercised, which makes untested cells visible to a reader.

- **B** — Those are payload properties.
- **C** — Those are logistics.
- **D** — Those are performance metrics.

**3. L4-Q03** — **A: Alert fatigue, because ordinary clients mistype credentials**

Single-event alerts on common events produce untriageable volume; the signal must be a rate or pattern relative to a baseline.

- **B** — It catches noise more reliably than attacks.
- **C** — Authentication remains necessary.
- **D** — Monitoring does not change accuracy.

**4. L4-Q04** — **A: Hash verification plus behavioural parity on a probe set**

Identity and behaviour are separate checks, and availability establishes neither.

- **B** — Availability is not integrity.
- **C** — A container can start with the wrong artefact.
- **D** — Confirmation is not evidence.

**5. L4-Q05** — **A: Compare a new model's outputs with the live model without affecting users**

Shadow mode mirrors traffic and discards decisions, which measures behavioural difference safely before exposure.

- **B** — That describes a canary.
- **C** — Rollback is a separate mechanism.
- **D** — Caching is unrelated.

**6. L4-Q06** — **A: Has the information, time and authority to reverse the decision**

Oversight is the ability to disagree effectively, not the presence of a person in the loop.

- **B** — Click-through approval becomes rubber-stamping.
- **C** — A log entry proves presence only.
- **D** — Annual review is not per-decision oversight.

**7. L4-Q07** — **A: A recorded waiver naming the risk, approver, compensating control and expiry**

A waiver is legitimate only when it is explicit, owned and time-bounded; otherwise the risk disappears from the record rather than from the system.

- **B** — Verbal agreement leaves no accountable record.
- **C** — Removing the gate hides the risk from future releases.
- **D** — Re-running until a flaky result passes is not a decision.

**8. L4-Q08** — **A: Impact and exploitability in this deployment, with assumptions stated**

Decision-makers need consequence and reachability; sophistication and payload counts describe the test rather than the risk.

- **B** — Sophistication is not consequence.
- **C** — Payload counts measure the test.
- **D** — Age is unrelated.

## Section B model answers

<div class="sas-answer"><p class="sas-item__head"><strong>L4-W1</strong> <span class="sas-meta">8 marks</span></p><p class="sas-answer__q">Write the incident timeline and first four actions for a suspected extraction campaign detected at 02:00, and state what you would preserve before blocking.</p><p class="sas-answer__label">Model answer</p><p>Timeline: detection at 02:00 from a per-principal similarity rule, containment at 02:10, scope assessment by 03:00, notification of the model owner at 03:15. Actions: snapshot logs and a query sample; throttle or revoke the principal's credential; determine which model and data the queries reached and whether full-precision outputs were returned; notify the on-call lead and open the incident record. Preserve logs and the query sample before blocking, because blocking first can lose the only record of what was extracted and from where.</p></div>

<div class="sas-answer"><p class="sas-item__head"><strong>L4-W2</strong> <span class="sas-meta">9 marks</span></p><p class="sas-answer__q">Produce a six-gate release checklist for a customer-facing assistant with a payment tool. For each gate, name the evidence and the failure it blocks.</p><p class="sas-answer__label">Model answer</p><p>Utility: task accuracy above threshold on a held-out set, blocking a model that cannot do the job. Injection: zero tool-call success on a 20-payload suite, blocking text-driven payments. Authorisation: cross-tenant denial suite passing, blocking data exposure. Privacy: membership leakage below threshold, blocking a model that memorises customers. Integrity: manifest hash match through an independent channel, blocking a substituted artefact. Recoverability: rollback tested within the target window, blocking an unrecoverable release. Each gate names its producing test, its threshold and its owner, so the decision is mechanical and the reason legible.</p></div>

<div class="sas-answer"><p class="sas-item__head"><strong>L4-W3</strong> <span class="sas-meta">9 marks</span></p><p class="sas-answer__q">Write the residual-risk paragraph a regulator would read for a triage assistant, including the assumption that would defeat your argument.</p><p class="sas-answer__label">Model answer</p><p>State what was tested and what was not: injection success at zero for tool calls on the eight-payload suite, but no adversarial clinical phrasing beyond that set; retrieval isolation passing its suite, but a residual risk from misconfigured ACLs at ingestion; oversight designed with clinician overrule, but untested at real volume. State the residual in operational terms: novel phrasing may still alter summaries, and clinicians remain the control that catches it. Name the assumption that would defeat the argument: that clinicians read the cited evidence and have time to disagree. If that assumption is false, the oversight control is nominal and the residual is unacceptable.</p></div>

