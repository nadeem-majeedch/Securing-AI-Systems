---
title: NIST AI Risk Management Framework
description: The AI RMF's four functions, its generative-AI profile, and how a student uses it without turning it into paperwork.
---

# NIST AI Risk Management Framework

## What it is

The **AI Risk Management Framework (AI RMF 1.0)**, NIST AI 100-1, published January 2023, is voluntary US guidance
for managing risk from AI systems across their lifecycle. It is organised into four functions — **Govern, Map,
Measure, Manage** — each with categories and subcategories describing outcomes rather than specific controls.

Two companions matter for this course:

| Document | Date | What it adds |
|---|---|---|
| **AI RMF 1.0** — NIST AI 100-1 | January 2023 | The framework itself: four functions, trustworthiness characteristics, profiles |
| **Generative AI Profile** — NIST AI 600-1 | July 2024 | Generative-AI-specific risk categories and suggested actions, cross-referenced to the four functions |
| **Managing Misuse Risk for Dual-Use Foundation Models** — NIST AI 800-1 | Second public draft, January 2025 | Misuse risk management for foundation models; check NIST for final status before citing as final |

The AI RMF is also one of the documents that establishes the vocabulary — *trustworthiness characteristics* such as
valid and reliable, safe, secure and resilient, accountable and transparent, explainable and interpretable,
privacy-enhanced, and fair with harmful bias managed.

## Why it matters

The AI RMF is the frame most organisations use to answer "who owns this risk, and how would we know we handled it?"
It does three things a technical checklist cannot:

1. **It puts governance first.** *Govern* is a function, not a preamble: accountability, culture, policies and
   oversight are treated as engineering prerequisites.
2. **It separates mapping from measuring.** Deciding what the risks are is a different activity from quantifying
   them, and conflating the two is how teams end up measuring what is easy.
3. **It is profile-based.** You tailor the framework to a use case instead of implementing everything.

## When it is used

- Establishing or auditing an AI risk programme.
- Producing a risk register with owners and accepted residuals.
- A DPIA-adjacent assessment for a generative-AI feature (with the GenAI Profile).
- Answering a board question: "what is our AI risk posture, and what changed this quarter?"

It is **voluntary guidance**. It becomes binding only through contract, regulator expectation or an organisation's
own policy. It does not certify anything.

## The four functions, in the form a student can use

| Function | Question it answers | Artefact you can hand in |
|---|---|---|
| **Govern** | Who is accountable, under what policy, with what oversight? | Risk register with named owners; an approval record; a policy mapping |
| **Map** | What is the context, and which risks matter here? | System description, threat model, affected parties, risk tiers |
| **Measure** | How would we know, and how much? | Test results, measurement plan, thresholds, residual estimates |
| **Manage** | What do we do about it, and who accepts the rest? | Treatment decisions, compensating controls, monitoring, review dates |

A common student failure is to produce a Map and call it a framework. A risk register with no measurement and no
named acceptance is a list of worries.

## How to apply it: a six-step pattern

1. **Write the system boundary** (Map). One paragraph, plus a data-flow sketch with trust boundaries. If two people
   disagree where the boundary is, stop and resolve that first.
2. **Enumerate risks with a framework's vocabulary.** Use [AI 100-2](nist-aml.md) for attack classes and
   [ATLAS](mitre-atlas.md) for techniques; the AI RMF deliberately does not supply a threat catalogue.
3. **Assign owners and tiers** (Govern). Every risk gets a person, not a team name. Tier the system by consequence:
   what happens if it is wrong, to whom, at what scale.
4. **Choose measurements** (Measure). For each material risk, one measurement with a denominator and a threshold,
   plus the test that produces it. "Prompt injection" is not a measurement; "tool-call success rate on a
   twelve-payload suite, per capability" is.
5. **Decide and record** (Manage). Treat, transfer, avoid or accept — with the residual stated and a review date.
6. **Instrument the residual** (Manage + Measure). What signal tells you the accepted risk has grown? That signal
   belongs in the monitoring plan, not in a promise.

## What the generative-AI profile changes

AI 600-1 (July 2024) adds risk categories that classical ML frameworks do not cover well. The ones this course
treats as first-class:

- **Information integrity** — confabulated or manipulated content presented as fact.
- **Information security** — prompt injection, data exposure, model and data supply chain.
- **Data privacy** — memorisation, inference, and the effect of fine-tuning on both.
- **Harmful bias and homogenisation** — including the loss of minority views in generated content.
- **Human-AI configuration** — automation bias and over-reliance in oversight.
- **Value chain and component integration** — third-party models, adapters and tooling.

Use the profile as a checklist of *kinds of harm*, then map each to a test in this course. The
[C4 benefits proposal](../capstone/proposals/c04-benefits-assistant.md) is built around exactly this mapping.

## Worked example: mapping one feature

A student building a clinical triage assistant produced this table. It is reproduced because it is the shape the
assessment rewards.

| AI RMF function | What they wrote | Evidence |
|---|---|---|
| Govern | "Clinical safety lead owns triage risk; DPIA approved 12 March; review quarterly" | Signed approval; register row |
| Map | "Four boundaries: referral input, patient index, reviewer, audit store" | Data-flow diagram; threat table |
| Measure | "Urgent-class recall 0.81 (n=200); cross-patient retrieval 0/200 prompts" | Test output, seeds, split digest |
| Manage | "Ship with citation requirement; accept residual of model-written prose changing after injection; monitor canary omissions weekly" | Decision note; monitoring query |

Note that the measurement column contains numbers with denominators and the Manage column contains an accepted
residual, not a promise to fix everything.

## Limitations to state in your report

- The AI RMF is outcome-based: it tells you what to achieve, not which control to implement. You still need
  engineering guidance — [SSDF](ssdlc.md) for the pipeline, [OWASP](owasp.md) for the application surface.
- It is not a threat catalogue. Without [AI 100-2](nist-aml.md) or ATLAS, Map degenerates into brainstorming.
- Voluntary does not mean optional in practice: contracts and regulators increasingly reference it.
- A profile is only as good as its exclusions; state what you left out.

## Where it appears in this course

[Module 04](../modules/04-threat-modeling.md) (Map), [Module 18](../modules/18-monitoring-and-response.md) (Measure,
Manage), [Module 19](../modules/19-governance-and-ethics.md) (Govern), and the
[capstone assurance pack](../capstone/index.md#deliverables).

## Sources

1. NIST, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023.
   <https://doi.org/10.6028/NIST.AI.100-1> · publication record:
   <https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10>
2. NIST, *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*,
   NIST AI 600-1, July 2024. <https://doi.org/10.6028/NIST.AI.600-1> · publication record:
   <https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence>
3. NIST, *Managing Misuse Risk for Dual-Use Foundation Models*, NIST AI 800-1, second public draft, January 2025.
   <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.800-1.ipd2.pdf> — draft; verify final status before relying on it.
4. NIST, *Trustworthy and Responsible AI Resource Center* (crosswalks and profiles).
   <https://airc.nist.gov/home> (accessed November 2026).
