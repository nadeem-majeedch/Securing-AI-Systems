---
title: Projects
description: Ten mini projects, six major projects and five capstone proposals that turn modules into working systems.
hide:
  - toc
---

# Projects

Modules teach one capability at a time. Projects test whether you can hold several at once, under a constraint you
did not choose, and then explain what your evidence does and does not support.

This programme has three tiers, and they are not interchangeable. A mini project proves one control. A major project
makes several coexist. A capstone assesses a system and defends the assessment.

## The three tiers

| Tier | Count | Effort each | What it produces | Marked on |
|---|---|---|---|---|
| [Mini projects](mini/index.md) | 10 | 10–12 h | A tool, a measurement, or an enforcement point | [Mini rubric](guidance/rubrics.md#mini-project-rubric) |
| [Major projects](major/index.md) | 6 | ~25 h | A working system with a security argument | [Major rubric](guidance/rubrics.md#major-project-rubric) |
| [Capstone proposals](../capstone/proposals/index.md) | 5 | 60 h | An assessed system and an assurance pack | [Capstone rubric](../capstone/index.md#public-rubric) |

**Recommended load:** six to eight mini projects, two major projects, one capstone. The full pathway in the
[study plans](../getting-started/study-plans.md) assumes four mini and two major for the 460-hour route; the
programme offers more so that you can choose by interest and by sector rather than by timetable.

## Mini projects

Ten, each about ten to twelve hours. Every one produces an artefact that decides something: a verifier that fails, a
detector that scores, a policy that denies, a dashboard that alerts.

| # | Project | After |
|---|---|---|
| MP01 | Dataset integrity verification tool | 05, 15 |
| MP02 | Adversarial robustness evaluation tool | 06, 08 |
| MP03 | Poisoning detection prototype | 07 |
| MP04 | Model privacy risk assessment | 09 |
| MP05 | Secure ML inference API | 03, 16 |
| MP06 | Prompt injection detection demonstration | 11, 12 |
| MP07 | RAG access-control validator | 13 |
| MP08 | Agent tool authorisation prototype | 14 |
| MP09 | Supply chain integrity checker | 15 |
| MP10 | Security logging and monitoring dashboard | 18 |

[All ten briefs →](mini/index.md)

## Major projects

Six, each about twenty-five hours. These are end-to-end: a pipeline, a service, an agent, an assessment framework.

| # | Project | After |
|---|---|---|
| P1 | End-to-end secure machine learning pipeline | 05, 07, 15, 20 |
| P2 | Secure healthcare AI application | 05, 09, 19 |
| P3 | Secure LLM-based chatbot | 11, 12, 16 |
| P4 | Secure RAG institutional knowledge assistant | 13, 14 |
| P5 | AI agent with sandboxing and permission controls | 14, 16, 18 |
| P6 | AI red teaming and vulnerability assessment framework | 17, 18 |

[All six briefs →](major/index.md)

## Capstone proposals

Five sector-based proposals, each with the full eighteen-section brief: architecture, threat model, requirements,
methodology, metrics, deliverables and rubric.

| # | Proposal | Sector |
|---|---|---|
| C1 | TriageAssist — secure clinical referral triage | Healthcare |
| C2 | CreditGuard — poisoning-resilient credit decisioning | Financial services |
| C3 | Campus Assistant — tenancy and tool authority | Higher education |
| C4 | Benefits Guide — contestable eligibility support | Public sector |
| C5 | OfflineOps — air-gapped operations copilot | Manufacturing and utilities |

[All five proposals →](../capstone/proposals/index.md)

## How the tiers differ

| | Mini | Major | Capstone |
|---|---|---|---|
| Scope given to you | Fixed, with success criteria | Bounded, with objectives | Broad, with a proposal you must cut down |
| Code expected | 200–500 lines | 800–2,000 lines | A working system plus an assessment |
| Measurement | One controlled comparison | Several, including an adaptive attempt | An assessment of someone else's or your own system, with severity |
| Written output | 1–2 pages | 3–5 pages | An assurance pack and a defence |
| Failure mode | "It works" | Controls that exist but are not tested | Findings without severity or remediation |

## The seven steps

Every project follows the same order, and the order is assessed:

1. Define the problem and the decision it supports.
2. Identify assets, boundaries and threats.
3. Design a control and an enforcement point per threat.
4. Implement, deny paths first.
5. Test effectiveness with a benign comparison.
6. Evaluate the limitations.
7. Document decision-first.

[Project workflow →](guidance/workflow.md) · [Milestones and checkpoints →](guidance/milestones.md)

## Getting started

<div class="sas-grid sas-grid--3" markdown>

<div class="sas-card" markdown>
<div class="sas-card__title">Starter kit</div>
A runnable FastAPI service, evaluation harness, retrieval skeleton and monitoring queries — local, no API key.

[Starter templates →](guidance/starter-templates.md)
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Rubrics</div>
Three rubrics, published in full: mini, major and capstone, with claim discipline applied throughout.

[Project rubrics →](guidance/rubrics.md)
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Capstone rules</div>
Authorisation routes, milestones, the defence and the academic-integrity boundary.

[Capstone →](../capstone/index.md)
</div>

</div>

## Technology

Every project runs locally with Python. The stack across the programme is deliberately boring:

`Python` · `scikit-learn` · `PyTorch` (where gradients are needed) · `FastAPI` · `SQLite` (including FTS5) ·
`Jupyter` · `NumPy` · `Docker` (for containment work) · `Hugging Face` (for a tokeniser or a small model) ·
`Ollama` (for a local LLM) · a vector store only where a project genuinely needs one.

No commercial API is required for any project, and no project is marked on using one.

## Integrity and separation

Briefs are public. **Sample solutions are not in the briefs**: the repository keeps deliberately partial
solution guidance in `projects/solutions/`, separated so that you meet the problem before the answer. Nothing there
is a complete submission, and a submission that reproduces it scores at *Developing* at best.

If you are studying for credit, submit your own work through your institution's channel and cite any external code
you adapted, including the starter kit.
