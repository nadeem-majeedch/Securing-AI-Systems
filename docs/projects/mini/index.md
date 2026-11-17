---
title: Mini projects
description: Ten ten-hour projects that turn one security control into a working, measured artefact.
hide:
  - toc
---

# Mini projects

Ten projects, each about ten to twelve hours. Every one produces a **tool or a measurement**, not an essay: a
script that decides, a harness that measures, or a service that enforces something.

Mini projects exist because the gap between "I know what an ACL is" and "I built a retrieval filter that fails
closed and proved it with a test" is where most of the learning in this course happens.

## The ten

| # | Project | After | Stack | Evidence it must produce |
|---|---|---|---|---|
| [MP01](mp01-dataset-integrity.md) | Dataset integrity verification tool | 05, 15 | Python, SQLite, hashlib | Manifest verification on a tampered copy, with the exact failing file |
| [MP02](mp02-robustness-evaluation.md) | Adversarial robustness evaluation tool | 06, 08 | Python, scikit-learn or PyTorch | Accuracy under two attacks at three budgets, with a same-budget control |
| [MP03](mp03-poisoning-detection.md) | Poisoning detection prototype | 07 | Python, scikit-learn, Jupyter | Precision and recall of the detector against a known poison rate |
| [MP04](mp04-privacy-risk.md) | Model privacy risk assessment | 09 | Python, scikit-learn, Jupyter | Membership-inference advantage at a stated false-positive rate |
| [MP05](mp05-secure-inference-api.md) | Secure ML inference API | 03, 16 | FastAPI, SQLite, Docker | A passing authorisation and quota test suite, plus an audit trail |
| [MP06](mp06-injection-detection.md) | Prompt injection detection demonstration | 11, 12 | Python, Ollama or a mock | Per-capability success rates for a layered defence and its bypass |
| [MP07](mp07-rag-access-control.md) | RAG access-control validator | 13 | Python, SQLite FTS, FastAPI | A test that proves no foreign chunk reaches the prompt |
| [MP08](mp08-agent-authorisation.md) | AI agent tool authorisation prototype | 14 | Python, SQLite, FastAPI | Deny-by-default policy with ten decisions and an audit row each |
| [MP09](mp09-supply-chain-checker.md) | Model supply chain integrity checker | 15 | Python, hashlib, zipfile | A clean and a tampered bundle, separated by a signed manifest |
| [MP10](mp10-monitoring-dashboard.md) | AI security logging and monitoring dashboard | 18 | Python, SQLite, FastAPI, HTML | Three signals, thresholds with base rates, and one alert exercised end to end |

## How a mini project is marked

All ten use the [shared mini-project rubric](../guidance/rubrics.md#mini-project-rubric): threat model, method,
measurement, decision, and honest limitation. Each brief adds two project-specific indicators that the marker
applies alongside it.

The **decision** is the part most submissions get wrong. "It works" is not a decision. A decision reads: *for this
deployment, I would ship the manifest check and not the drift detector, because the detector's precision at our
volume is 0.3 and the check catches the failure we actually saw.*

## Choosing an order

If you are following the modules in order, the mini projects fall naturally:

<div class="sas-grid sas-grid--3" markdown>

<div class="sas-card" markdown>
<div class="sas-card__title">Levels 1–2</div>
MP01, MP02, MP03, MP04 — data, evasion, poisoning, privacy. Each produces a measurement you can put in a results
table.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Level 3</div>
MP06, MP07, MP08 — models as systems. Each produces an enforcement point with tests.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Level 4</div>
MP05, MP09, MP10 — serving, provenance, detection. These are the ones an employer recognises as engineering.
</div>

</div>

## What you need before starting

- A working Python environment from the [learning environment](../../getting-started/environment.md) page.
- A repository of your own. Nothing in these projects requires a network service.
- The willingness to write the threat model **before** the code. Every brief assumes you did.

If a project needs a model you do not have, use [Ollama](https://ollama.com) with a small local model or the mock
service in the [starter kit](../guidance/starter-templates.md). No commercial API key is required anywhere in this
programme.
