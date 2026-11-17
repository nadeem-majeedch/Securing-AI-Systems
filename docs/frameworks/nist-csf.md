---
title: NIST Cybersecurity Framework 2.0
description: How CSF 2.0's six functions carry AI risk, and how to reuse an existing cyber programme instead of starting another.
---

# NIST Cybersecurity Framework 2.0

## What it is

The **NIST Cybersecurity Framework (CSF) 2.0**, NIST CSWP 29, published 26 February 2024, is voluntary guidance for
managing cybersecurity risk. It is not AI-specific, and that is its main value: most organisations already report
cyber risk this way, and AI systems sit inside that estate rather than beside it.

Version 2.0 restructured the framework around **six functions**:

| Function | What it covers |
|---|---|
| **Govern (GV)** | Risk strategy, roles, policy, supply-chain risk management, oversight — new in 2.0 |
| **Identify (ID)** | Asset management, risk assessment, improvement |
| **Protect (PR)** | Identity and access, awareness, data security, platform security, technology resilience |
| **Detect (DE)** | Continuous monitoring, adverse event analysis |
| **Respond (RS)** | Incident management, analysis, reporting, communication, mitigation |
| **Recover (RC)** | Recovery planning, execution, communication |

Each function contains categories and subcategories, and the framework adds **profiles** (current and target state)
and **tiers** (rigour of governance). CSF 2.0 also includes informative references to other standards — a crosswalk
mechanism rather than a fresh control catalogue.

## Why it matters

AI security programmes fail in a predictable way: they are built as a parallel universe with their own register,
their own incident process and their own exceptions. CSF 2.0 gives you the opposite move — place AI risk inside the
existing functions, and reference the AI-specific material where it is needed.

Concretely:

- **Govern** is where "the model owner accepted the residual" becomes a real decision with a name.
- **Detect** is where prompt-injection signals join the SIEM instead of living in a notebook.
- **Respond** is where a poisoned artefact triggers the same incident process as a compromised build server.
- **Recover** is where "roll back to the previous digest and verify behaviour" is a rehearsed step.

## When it is used

- Organisations with an existing CSF-based cyber programme extending it to AI.
- Reporting cyber risk to a board or regulator in a familiar structure.
- Gap analysis: which function has no AI-relevant activity at all?
- Vendor conversations: "which CSF subcategories does your service support, and with what evidence?"

CSF 2.0 is **voluntary**. It is not a law and it does not certify. Where a regulator references it, that reference
creates the obligation, not the framework.

## How to apply it

**Step 1 — inventory the AI systems as assets.** CSF assumes asset management. A model, its training data, its
index, its prompt template and its tools are all assets; list them with owners.

**Step 2 — write a current profile for AI.** For each function, one or two sentences on what the organisation
actually does today for AI systems. Not what the policy says — what happens.

**Step 3 — choose a target profile for the next 12 months.** Three to six changes, each with an owner and an
evidence artefact. A target profile with thirty items will not be implemented.

**Step 4 — borrow AI-specific content for the gaps.** CSF deliberately does not describe AI attacks. Use
[AI 100-2](nist-aml.md) and [ATLAS](mitre-atlas.md) for threat content, [OWASP](owasp.md) for application risks, and
[SSDF](ssdlc.md) for the build pipeline.

**Step 5 — record the crosswalk.** One control, several frameworks. The crosswalk on the
[frameworks index](index.md#a-crosswalk-you-can-reuse) is a starting point.

## A CSF-shaped table for an AI feature

| Function | AI-specific activity | Evidence a reviewer would accept |
|---|---|---|
| Govern | Model owner named; residual accepted in writing; vendor terms reviewed | Register row, signed decision, contract clause |
| Identify | Model, data, index, prompt and tools registered as assets | Asset list with owners and data classes |
| Protect | Keys per environment; artefacts loaded by digest; retrieval filtered by principal | Configuration, test output, deny-path suite |
| Detect | Per-principal query rates; canary-set quality; denial-rate alert | Dashboard, query, alert history |
| Respond | Playbook for suspected extraction; evidence preservation before blocking | Runbook, drill record |
| Recover | Rollback to previous digest; behavioural probe after restore | Rollback log, probe output |

If a row has no evidence, that is the finding — and it is a finding a cyber audience already knows how to act on.

## Where CSF fits with the AI RMF

They overlap, and that is fine. A workable division:

- **AI RMF** for the risk lifecycle and the trustworthiness characteristics of the AI system itself.
- **CSF 2.0** for the security operations that surround it: identity, detection, response, recovery, supply chain.
- **Crosswalk** the two so that *Govern* in each is the same conversation.

A student writing an assurance pack should say which they used for what. "Both, interchangeably" is a sign that
neither was used.

## Limitations to state

- CSF is not AI-specific: it will not tell you what a prompt injection is, or how to measure robustness.
- Its subcategories are outcomes; turning them into tests is your work.
- Tiers describe governance rigour, not technical strength; a Tier 4 organisation can still ship a vulnerable model.
- Voluntary status means a CSF profile is not evidence of compliance with anything except your own target.

## Where it appears in this course

[Module 03](../modules/03-cybersecurity-fundamentals.md) (the classical controls AI inherits),
[Module 16](../modules/16-secure-ai-apis.md) (Protect and Detect for inference services),
[Module 18](../modules/18-monitoring-and-response.md) (Detect, Respond, Recover), and the
[P1 pipeline](../projects/major/p01-secure-ml-pipeline.md) (Govern and Protect across stages).

## Sources

1. NIST, *The NIST Cybersecurity Framework (CSF) 2.0*, NIST CSWP 29, February 2024.
   <https://doi.org/10.6028/NIST.CSWP.29> · publication record:
   <https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final>
2. NIST, *CSF 2.0 informative references and profiles* (crosswalk material).
   <https://www.nist.gov/cyberframework> (accessed November 2026).
