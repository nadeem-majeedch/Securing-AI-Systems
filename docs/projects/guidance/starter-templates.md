---
title: Starter templates
description: A runnable local starter kit for the projects, and how to adapt it without letting setup consume the work.
hide:
  - toc
---

# Starter templates

The projects assume you can serve a model, evaluate a dataset and query a log. Rather than have every student
rebuild that scaffolding, this programme ships a small starter kit in the repository at:

```text
projects/starter/
  README.md            how to run it
  requirements.txt     FastAPI, uvicorn, numpy, pytest, httpx
  app/                 a secure-by-default inference service
  eval/                an evaluation harness with seeds and a JSON report
  rag/                 FTS5 retrieval with pre-ranking ACL filtering
  monitoring/          three signals over an audit table
  notebooks/           a percent-format notebook for the analysis steps
  Dockerfile
  tests/               pytest suite covering the deny paths
```

Everything in it runs locally with Python and SQLite. It needs no API key, no cloud account and no GPU. A small
local model through [Ollama](https://ollama.com) is optional; the service ships with a deterministic mock model so
that the tests do not depend on one.

## What each part is for

| Part | Use it when | Projects it serves |
|---|---|---|
| `app/` | You need an authenticated, quota-limited endpoint to attack and to test | MP05, P3, P4, P5 |
| `eval/` | You need a measurement loop with seeds, budgets and a JSON result file | MP02, MP04, MP06, P1 |
| `rag/` | You need retrieval where the ACL is applied before ranking | MP07, P4 |
| `monitoring/` | You need signals and thresholds over a request log | MP06, MP10, P5 |
| `notebooks/` | You want the analysis in cells with outputs kept | MP03, MP04, P1, P2 |

## Running it

```bash
cd projects/starter
python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --port 8100
```

The test suite is the point. It contains the deny paths — missing key, wrong cohort, exhausted quota, oversized
body — and it should pass before you change anything, so that when you break it you know it was you.

## What the starter deliberately does not do

It is a **skeleton**, not a solution. The following are missing on purpose, because each is a project's actual work:

- **No threat model.** The service has controls; it has no argument about why those controls and not others.
- **No measurement.** `eval/` runs an evaluation, but it does not know what attack you are defending against or how
  to report a control condition.
- **No isolation proof.** `rag/` filters before ranking, but the tests that assert absence of foreign content are
  yours to write.
- **No severity or decision.** Nothing in the kit tells you whether a finding matters.
- **A mock model.** Its outputs are deterministic and uninteresting; substituting a real local model is step one of
  several projects.

If you submit the starter with cosmetic changes, you will score at *Developing* on method and *Emerging* on
measurement. That is what the rubric is for.

## Adapting it

1. **Copy, do not fork in place.** `cp -r projects/starter my-project` and work in your own repository, so the
   original stays runnable as a reference.
2. **Keep the deny paths.** They are the cheapest evidence you will ever have. Add to them; do not delete them
   because your design changed the shape of the refusal.
3. **Replace the model behind one interface.** `app/model.py` exposes `predict(features) -> dict`. A scikit-learn
   model, a small PyTorch model and an Ollama call can all sit behind it; the service should not care.
4. **Record configuration next to results.** The evaluation harness writes `config.json` beside `results.json` for a
   reason: a number without its configuration cannot be compared with anything.

## When you need something the kit does not have

| Need | Suggestion | Cost |
|---|---|---|
| Local LLM for injection work | Ollama with a 3–8 B parameter model, temperature 0 | one download, CPU only |
| Embeddings for retrieval | Skip them: FTS5 is reproducible and fast enough at 4,000 documents | none |
| Vector database | Only if a project explicitly asks; SQLite FTS5 plus cosine over stored vectors is enough for the scale here | none |
| Container isolation | Docker with a non-root user, read-only root, `--memory`, `--cpus`, `--network none` | one Docker install |
| Notebook outputs | Percent-format `.py` in `notebooks/`, executed with `jupytext`/`papermill` if you want a rendered copy | small |

## Honest note on scope

The kit is about 900 lines. It is enough to run, test and attack. It is not enough to score well, and that gap is
intentional: the marks are for the threat model, the measurement and the decision, none of which can be shipped in a
template.
