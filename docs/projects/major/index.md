---
title: Major projects
description: Six end-to-end projects of about twenty-five hours, each a working system with a security argument attached.
hide:
  - toc
---

# Major projects

Six projects, each about twenty-five hours. Where a mini project proves one control, a major project has to make
several controls coexist: the pipeline that trains the model, the service that serves it, the data that flows
through both, and the evidence that any of it works.

Do two. A student who completes P1 and P4 has measured a system and secured one; a student who completes P3 and P5
has secured a conversational surface and contained an agent. Do not attempt all six.

## The six

| # | Project | After | Core stack | The hard part |
|---|---|---|---|---|
| [P1](p01-secure-ml-pipeline.md) | End-to-end secure machine learning pipeline | 05, 07, 15, 20 | Python, scikit-learn or PyTorch, SQLite, Docker | Making every stage's evidence a gate rather than a document |
| [P2](p02-healthcare-ai.md) | Secure healthcare AI application | 05, 09, 19 | FastAPI, scikit-learn, SQLite, Jupyter | Privacy and oversight that survive a clinician's real workload |
| [P3](p03-llm-chatbot.md) | Secure LLM-based chatbot | 11, 12, 16 | FastAPI, Ollama or mock, SQLite | Keeping the capability useful after removing the dangerous paths |
| [P4](p04-rag-assistant.md) | Secure RAG institutional knowledge assistant | 13, 14 | FastAPI, SQLite FTS, local embeddings | Multi-tenant isolation that fails closed, plus deletion that means it |
| [P5](p05-agent-sandbox.md) | AI agent with sandboxing and permission controls | 14, 16, 18 | Python, Docker, SQLite | Containment you can demonstrate, not merely configure |
| [P6](p06-red-team-framework.md) | AI red teaming and vulnerability assessment framework | 17, 18 | Python, FastAPI, SQLite | Coverage and severity that a reader can audit |

## What every major project must contain

1. **A bounded scope.** What is in, what is out, and the sentence that justifies the exclusion.
2. **A threat model** with trust boundaries, at least eight threats, and a control mapped to each.
3. **A working system.** From a clean checkout, one documented command brings it up.
4. **A security argument.** Claims mapped to evidence: test, measurement or configuration.
5. **A measurement.** At least one attack or failure scenario run against your own system, before and after the
   control.
6. **An operational story.** Logs, an alert, a rollback and a kill switch — or a stated reason why one is out of
   scope.
7. **A named weakest assumption.** The one thing that, if false, makes the whole argument collapse.

## Milestones

Every major project uses the same five milestones. The briefs give project-specific evidence for each.

| # | Milestone | Hours | Gate |
|---|---|---|---|
| M1 | Scope, threat model and acceptance criteria | 4 | Accepted before code is written |
| M2 | Skeleton that runs end to end, without security claims | 7 | A working happy path and a recorded baseline |
| M3 | Controls implemented, deny paths tested | 8 | Test suite passing, including negative cases |
| M4 | Adversarial measurement and hardening | 4 | Before/after numbers for at least one attack |
| M5 | Security argument, runbook and defence | 2 | A reader could operate and challenge the system |

M1 is a gate in the literal sense: a submission that starts at M2 and back-fills a scope is marked down on
**Scope and threat model** regardless of the quality of the code.

## How major projects are marked

The [major-project rubric](../guidance/rubrics.md#major-project-rubric) applies: scope 15 %, technical execution
30 %, measurement 20 %, engineering quality 15 %, communication 15 %, honest limitation 5 %. Each brief adds two
project-specific indicators.

## Working alone, working with a partner

All six are sized for one person. If you work in a pair, split by component (pipeline and service, retrieval and
agent) rather than by phase, and keep a decision log: who chose what, and on what evidence. Pairs are marked on
the same rubric, with the individual contribution visible in the decision log.

## What "done" means

A major project is done when someone else can start it, attack it, read the result and find the limitation — without
you in the room.

<div class="sas-grid sas-grid--2" markdown>

<div class="sas-card" markdown>
<div class="sas-card__title">Before you start</div>
Read the [project workflow](../guidance/workflow.md) and the [milestone and checkpoint
guide](../guidance/milestones.md). They describe the seven steps and the gates that apply to all three tiers.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Starter code</div>
The [starter kit](../guidance/starter-templates.md) provides a runnable FastAPI service, an evaluation harness, a
retrieval skeleton and a monitoring query set. Use it or replace it, but do not let setup consume the project.
</div>

</div>
