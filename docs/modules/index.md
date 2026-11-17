---
title: Course Modules
description: All twenty modules of Securing AI Systems, organised into four levels from foundation to professional practice.
hide:
  - toc
---

# Course Modules

Twenty modules in four levels: **Foundation**, **Intermediate**, **Advanced** and **Professional Practice**. Each module is a complete lesson of 8–24 hours on a single page, so you can read it, work the examples and check yourself without hunting for a separate lab, exercise set or quiz page.

Read the level you are in from the start. The order is a dependency order, not a difficulty ranking: Module 07 assumes Module 06's adversary models, and Module 12 assumes Module 11's account of the context window.

## How a module works

Every module contains the same sixteen components, in the same order:

| # | Component | What it gives you |
|---|---|---|
| 1 | Introduction | Why the topic exists, framed by a realistic failure |
| 2 | Learning objectives | Seven things you can do afterwards, stated as capabilities |
| 3 | Prerequisites | Exactly which earlier material is assumed |
| 4 | Detailed explanations | The theory, developed rather than summarised |
| 5 | Important terminology | A table of the terms the module uses precisely |
| 6 | Mathematical foundations | Every equation defined variable by variable |
| 7 | Step-by-step technical explanations | The procedure, in the order a practitioner does it |
| 8 | Real-world examples | Healthcare, finance, universities, cities, vision, language, autonomy, generative AI |
| 9 | Diagrams and architecture illustrations | Mermaid diagrams, each with a text description |
| 10 | Python examples | Runnable code, no GPU, no API key, no network |
| 11 | Security implications | The consequences that follow from the theory |
| 12 | Detection and mitigation | Controls in a table, with what each one misses |
| 13 | Practical exercises | Recall, apply and extend, in that order |
| 14 | Knowledge-check questions | Collapsible questions with answers and reasoning |
| 15 | Module summary | The argument of the module in a few paragraphs |
| 16 | References | Attributed sources, with a route to the next module |

While modules are being released, each page shows its **status**: `planned`, `draft` (written, not yet reviewed), `in review`, or `complete`. Everything in this curriculum is currently `draft`.

!!! info "Progress tracking"

    Mark a module complete with the button at the top of its page. Progress is stored in your browser only — no account, no tracking. Totals appear on the [learning roadmap](../roadmap.md).

## Level 1 — Foundation

*52 hours · modules 01–05*

Builds the vocabulary and the systems view. No security background is assumed; nothing later works without it.

| # | Module | Hours | What it establishes |
|---|---|---|---|
| 01 | [Introduction to Securing AI Systems](01-introduction.md) | 8 | What is being protected, from whom, and the four-level map of the course |
| 02 | [Fundamentals of AI, ML and Deep Learning Security](02-ml-security-fundamentals.md) | 10 | What training optimises, what artefacts exist, and why learned systems fail differently |
| 03 | [Cybersecurity Fundamentals for AI Systems](03-cybersecurity-fundamentals.md) | 10 | Identity, access control, cryptography, trust boundaries and defence in depth |
| 04 | [AI Threat Modeling and Risk Assessment](04-threat-modeling.md) | 12 | STRIDE for ML, MITRE ATLAS, attack trees, severity scoring |
| 05 | [Secure Data Management and Dataset Protection](05-secure-data-management.md) | 12 | Classification, minimisation, de-identification and its limits, lineage, labelling |

## Level 2 — Intermediate

*72 hours · modules 06–10*

The technical heart of the course: attacks implemented and measured, defences evaluated against an adversary who knows they exist.

| # | Module | Hours | What it establishes |
|---|---|---|---|
| 06 | [Adversarial Machine Learning](06-adversarial-ml.md) | 14 | The four attack families, three adversary models, evasion as constrained optimisation |
| 07 | [Data Poisoning and Backdoor Attacks](07-data-poisoning.md) | 16 | Availability, targeted and clean-label poisoning; triggers, detection, removal |
| 08 | [Model Evasion and Robustness](08-evasion-and-robustness.md) | 16 | PGD, margin attacks, adversarial training, randomised smoothing, adaptive evaluation |
| 09 | [Model Privacy: Membership Inference and Model Inversion](09-model-privacy.md) | 14 | Advantage, shadow models, inversion, DP-SGD and privacy accounting |
| 10 | [Model Extraction and Intellectual Property Protection](10-model-extraction.md) | 12 | Query-based extraction, fidelity, quotas, output rounding, watermarks |

## Level 3 — Advanced

*72 hours · modules 11–15*

The part that dates fastest and the part you will meet most often in practice: language models, retrieval and agents.

| # | Module | Hours | What it establishes |
|---|---|---|---|
| 11 | [Fundamentals of LLM Security](11-llm-security.md) | 12 | Tokens, attention, the shared context window, roles, decoding, training supply chain |
| 12 | [Prompt Injection and Jailbreak Attacks](12-prompt-injection.md) | 16 | Direct and indirect injection, jailbreak families, layered defence and measurement |
| 13 | [RAG Security and Knowledge Base Protection](13-rag-security.md) | 14 | Ingestion poisoning, tenant isolation, embedding leakage, grounding controls |
| 14 | [AI Agent Security and Tool Abuse](14-agent-security.md) | 16 | Excessive agency, confused deputies, policy gates, sandboxing, egress control |
| 15 | [Secure Fine-Tuning and Model Supply Chain](15-fine-tuning-supply-chain.md) | 14 | Unsafe serialisation, adapters, provenance, signing, ML bill of materials |

## Level 4 — Professional Practice

*88 hours · modules 16–20*

What happens when the system is real: hardened interfaces, authorised testing, operations, governance, and deployment.

| # | Module | Hours | What it establishes |
|---|---|---|---|
| 16 | [Secure AI APIs and Application Development](16-secure-ai-apis.md) | 16 | Authentication, quotas, input validation, output handling, multi-tenancy, cost bounds |
| 17 | [AI Red Teaming and Security Testing](17-red-teaming.md) | 16 | Scoping, test matrices, corpora, confidence intervals, reporting that changes decisions |
| 18 | [AI System Monitoring, Incident Response and Recovery](18-monitoring-and-response.md) | 16 | Drift and attack detection, alert design, the incident lifecycle, recovery with evidence |
| 19 | [AI Governance, Privacy, Ethics and Compliance](19-governance-and-ethics.md) | 16 | NIST AI RMF, risk tiers, DPIA, fairness metrics, model cards, vendor risk |
| 20 | [Secure AI Deployment and Capstone Projects](20-deployment-and-capstone.md) | 24 | Release gates, shadow and canary deployment, rollback, traceability, capstone briefs |

## Where the projects sit

Modules teach capability; projects test integration.

| After | Project | Integrates |
|---|---|---|
| Modules 05, 15 | [MP01 — Dataset integrity verification tool](../projects/mini/mp01-dataset-integrity.md) | Provenance, manifest verification |
| Modules 06, 08 | [MP02 — Adversarial robustness evaluation tool](../projects/mini/mp02-robustness-evaluation.md) | Evasion, measurement discipline |
| Module 07 | [MP03 — Poisoning detection prototype](../projects/mini/mp03-poisoning-detection.md) | Poisoning, detection, triage |
| Module 09 | [MP04 — Model privacy risk assessment](../projects/mini/mp04-privacy-risk.md) | Membership inference, residual risk |
| Modules 03, 16 | [MP05 — Secure ML inference API](../projects/mini/mp05-secure-inference-api.md) | Auth, quotas, audit |
| Modules 11, 12 | [MP06 — Prompt injection detection demonstration](../projects/mini/mp06-injection-detection.md) | Injection, layered defence |
| Module 13 | [MP07 — RAG access-control validator](../projects/mini/mp07-rag-access-control.md) | Retrieval isolation, deletion |
| Module 14 | [MP08 — Agent tool authorisation prototype](../projects/mini/mp08-agent-authorisation.md) | Authority, confused deputy, audit |
| Module 15 | [MP09 — Supply chain integrity checker](../projects/mini/mp09-supply-chain-checker.md) | Artefact verification, release gates |
| Module 18 | [MP10 — Monitoring dashboard](../projects/mini/mp10-monitoring-dashboard.md) | Signals, thresholds, triage |
| Modules 05–20 | [P1–P6 — Major projects](../projects/major/index.md) | End-to-end systems and assessment frameworks |
| Module 20 | [Capstone proposals](../capstone/proposals/index.md) | Everything |

## Reading order if you are not following the pathway

Some modules stand alone better than others.

- **Only care about generative AI?** Read 03, then 11–14, then 16. You will miss the measurement discipline from Level 2, which is what separates a claim from a finding.
- **Preparing for a security engineering role?** Read 01–05, then 15, 16, 18, 19. The adversarial modules are useful context but less of the day job.
- **Doing research in adversarial ML?** Read 02, 04, 06–10 in full, and treat 17 as the evaluation standard you will be held to.
