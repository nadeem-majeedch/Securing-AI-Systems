---
title: Assignments
description: Twelve scenario-based assignments that assess judgement and technical writing, with public rubrics.
hide:
  - toc
---

# Scenario Assignments

Twelve written assignments across the course. Each gives you a realistic, under-specified scenario and asks for a
decision you must defend in writing, usually with an artefact attached.

They exist because technical skill alone is not the job. The most common failure in AI security work is not a
missed attack — it is a correct finding that nobody acts on because it was not communicated in the language of the
person who owns the risk.

## What each assignment asks for

Every assignment has the same shape:

| Component | What it contains |
|---|---|
| **Scenario** | A system, an organisation, a constraint you cannot change |
| **Problem statement** | The decision the work must support |
| **Requirements** | What the deliverable must contain to be assessable |
| **Tasks** | The steps that produce it |
| **Deliverables** | Named artefacts with lengths or formats |
| **Evaluation criteria** | Four qualities the marker looks for |
| **Rubric** | Four criteria × four levels, published so you can mark your own work |
| **Extension challenges** | Three harder questions if you want to go further |

## The twelve assignments

| # | After | Assignment | Artefacts | Words |
|---|---|---|---|---|
| [A1](a01-threat-model-hospital.md) | Module 04 | **Threat model for a hospital AI application** — a register and a brief a clinical director can decide on | Register + brief | 1,200 |
| [A2](a02-fraud-pipeline.md) | Module 07 | **Securing a fraud detection pipeline** — poisoning, evasion and supply chain in a nightly retrain | Review + control plan + rollback | 1,100 |
| [A3](a03-poisoning-investigation.md) | Module 07 | **Identifying poisoning in a synthetic dataset** — decide what caused a 15-point accuracy fall | Report + reproducible analysis | 1,000 |
| [A4](a04-robustness-evaluation.md) | Module 08 | **Evaluating adversarial robustness** — protocol, results and a defensible claim | Protocol + results + claim | 1,000 |
| [A5](a05-privacy-assessment.md) | Module 09 | **Assessing model privacy risks** — measure membership leakage and write the residual a DPO can rely on | Assessment + notebook | 900 |
| [A6](a06-extraction-assessment.md) | Module 10 | **Evaluating model extraction risk** — cost curve against query budget and output granularity | Experiment + defence table | 900 |
| [A7](a07-chatbot-security.md) | Modules 11–12 | **Securing an LLM chatbot** — injection assessment and a conditional launch decision | Assessment + payload suite | 1,000 |
| [A8](a08-rag-security.md) | Module 13 | **Securing a RAG application** — tenant isolation, an ACL suite and deletion | Design + tests | 1,100 |
| [A9](a09-agent-authorisation.md) | Module 14 | **Designing an agent authorisation framework** — effective permissions, policy engine, confirmation points | Analysis + policy code | 1,000 |
| [A10](a10-supply-chain.md) | Module 15 | **AI supply chain security assessment** — inventory, substitution analysis and a release gate | Inventory + procedure | 900 |
| [A11](a11-security-audit.md) | Module 17 | **AI application security audit** — a five-day engagement with findings and a retest plan | Audit report + matrix | 1,200 |
| [A12](a12-monitoring-system.md) | Module 18 | **Designing a production AI security monitoring system** — six signals, thresholds and a playbook | Design + playbook | 1,200 |

## The shared rubric

Every assignment uses these four criteria. The indicators differ, but the levels do not.

| Criterion | Emerging (1) | Developing (2) | Proficient (3) | Exemplary (4) |
|---|---|---|---|---|
| **Decision quality** | No recommendation, or one that ignores the stated constraint | A defensible recommendation with thin justification | A clear recommendation that respects the constraint | A recommendation that names what it trades away, and why that trade is right here |
| **Technical accuracy** | Claims are wrong or unsupported | Mostly correct, with one significant error | Correct, current and correctly scoped | Correct, and distinguishes what is known from what is assumed |
| **Evidence** | Assertions without support | Some evidence, unevenly applied | Specific evidence cited for each material claim | Evidence quantified, with its limits stated |
| **Communication** | Reader cannot act on it | Understandable but unstructured | Structured for the stated reader, with a clear ask | A reader could act without asking a single question |

The fourth criterion is not about prose style. It is about whether the person reading your brief can make a
decision.

## Marking your own work

1. Read the rubric before you start writing, not after.
2. Draft, then leave it a day.
3. Score each criterion against the descriptors, choosing the *lower* level when you hesitate.
4. Rewrite only the weakest criterion.
5. Keep the marked version — twelve of these, honestly marked, are a portfolio.

## How the assignments relate to the quizzes

The [module quizzes](../quizzes/index.md) test whether you know the material. The assignments test whether you can
use it under a constraint, in writing, for a reader who is not you. A high quiz score with a weak assignment is
common and is exactly what the assignments are for.

## Submission if you are studying for credit

Assignments are submitted through your institution's normal channel. The published briefs are specifications;
submitting a brief instead of a deliverable, or reproducing an exemplar, is academic misconduct.

If you are studying alone, publish nothing that contains a real organisation's data, and replace any institutional
detail with a fictional equivalent before sharing your work.
