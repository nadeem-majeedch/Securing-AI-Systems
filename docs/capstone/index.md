---
title: Capstone
description: The capstone brief — scope, milestones, deliverables and the public rubric for the final assessment.
---

# Capstone

The capstone is where the course stops being a set of modules and becomes a professional deliverable.

You will assess one AI system end to end: threat-model it, test it under a written scope, report findings with severity and evidence, remediate, and produce an assurance pack that states what you can and cannot claim about the result.

Estimated effort: **60 hours**, spread across five milestones.

## Choose your system

You need a system you are authorised to test. Three routes, in order of preference:

| Route | System | Notes |
|---|---|---|
| **A — Course exercises** | The deliberately vulnerable assistant you build in the Module 12 and 14 exercises (a summariser with one tool, and a RAG assistant) | Safest; no authorisation needed; scoped and reproducible |
| **B — Your own build** | Something you built for another course, a project, or work | Authorisation is yours to give; document it |
| **C — Written permission** | A real system whose owner has authorised you in writing | Highest realism; requires the authorisation document as an appendix |

Anything else is out of scope. "It was publicly accessible" is not authorisation, and "I only used the interface as intended" is not a defence when the intent was to find a way to misuse it.

## Five proposals

If you would rather adapt a complete brief than design your own, choose one of five sector proposals. Each carries the
full eighteen-section structure: industry background, problem statement, objectives, scope, architecture, threat
model, functional and security requirements, dataset requirements, implementation and testing methodology, expected
results, evaluation metrics, deliverables, extensions and rubric.

| # | Proposal | Sector | Core problem |
|---|---|---|---|
| [C1](proposals/c01-clinical-triage.md) | TriageAssist — clinical referral triage | Healthcare | Retrieval isolation and real oversight |
| [C2](proposals/c02-credit-poisoning.md) | CreditGuard — credit decisioning | Financial services | Label poisoning and model risk |
| [C3](proposals/c03-campus-assistant.md) | Campus Assistant — tenancy and tools | Higher education | Isolation composed with authority |
| [C4](proposals/c04-benefits-assistant.md) | Benefits Guide — eligibility support | Public sector | Faithful explanation and contestability |
| [C5](proposals/c05-offline-ops-copilot.md) | OfflineOps — air-gapped copilot | Manufacturing, utilities | Injection and supply chain with no cloud |

Adapting a proposal does not lower the standard: the rubric below is unchanged, and your M1 submission must show the
scope decisions you made — including what you cut and why. [Compare the proposals →](proposals/index.md)

## Milestones

| # | Milestone | What you submit | Hours |
|---|---|---|---|
| **M1** | Proposal and scope | System description, threat model, rules of engagement, planned techniques, stop conditions | 8 |
| **M2** | Testing report | Evidence collected under the scope, with reproducible steps and minimal-impact proofs | 20 |
| **M3** | Findings and severity | Findings register with severity, impact, affected assets, and remediation options with costs | 10 |
| **M4** | Remediation | The fixes, or a reviewed design for them, plus a retest showing the finding is closed | 12 |
| **M5** | Assurance pack and defence | System card, risk register with owners, control-to-evidence table, assurance argument, and a 15-minute defence | 10 |

M1 must be accepted before testing begins. A capstone that starts with testing and writes the scope afterwards is failed on scope, regardless of what it finds.

## Deliverables

<div class="sas-grid sas-grid--2" markdown>

<div class="sas-card sas-card--plain" markdown>
**System and threat model.** What the system does, who uses it, what it holds, where the trust boundaries are, and what an attacker would want.
</div>

<div class="sas-card sas-card--plain" markdown>
**Rules of engagement.** Targets, dates, techniques permitted and excluded, data handling, stop conditions, and the approver.
</div>

<div class="sas-card sas-card--plain" markdown>
**Findings register.** Each finding with an identifier, severity, evidence, impact, and remediation option.
</div>

<div class="sas-card sas-card--plain" markdown>
**Evidence.** Reproducible steps, commands, and minimal proofs. No exfiltrated data, no persistence, no availability damage.
</div>

<div class="sas-card sas-card--plain" markdown>
**Remediation and retest.** What you changed, why, and the evidence that the finding is closed.
</div>

<div class="sas-card sas-card--plain" markdown>
**Assurance pack.** System card, RMF-shaped risk register, control-to-evidence table, and a two-page assurance argument.
</div>

</div>

## Public rubric

| Criterion | Weight | Emerging | Proficient | Exemplary |
|---|---|---|---|---|
| **Scope and authorisation** | 15 % | Missing or retrofitted | Written, respected | Written, respected, and used to make a real exclusion decision |
| **Technical depth** | 25 % | Surface checks only | At least two significant findings with sound method | Findings that required understanding the system, not just running tools |
| **Evidence quality** | 20 % | Screenshots without context | Reproducible steps with outputs | Reproducible, minimal, and independently repeatable by a reviewer |
| **Severity judgement** | 10 % | Severity asserted | Justified with a stated scheme | Justified, and calibrated against what the business actually loses |
| **Remediation** | 15 % | Recommended only | Implemented and retested | Implemented, retested, and shown not to break the product |
| **Assurance argument** | 15 % | Claims without evidence | Claims mapped to artefacts | Claims with evidence and a named weakest assumption |

## The defence

Fifteen minutes, plus questions. You present the system, the two findings you consider most important, the remediation, and the residual risk. Then you are asked three questions:

1. **What would you test next, with another week?**
2. **Which of your conclusions is most likely to be wrong, and why?**
3. **If the product owner refused your top remediation, what would you do?**

There are no trick questions. The third is the one most candidates answer badly, by insisting rather than by finding the next-best control.

## Academic integrity

Your capstone must be your own work. Testing someone else's system without authorisation is misconduct and, depending on jurisdiction, a criminal offence. Using a published report as a template is fine; presenting one as your assessment is not.

If you are studying for credit, the capstone is normally worth 25 % of the final mark. See the [assessment overview](../getting-started/assessment.md) for weighting and the claim-discipline criterion applied throughout.
