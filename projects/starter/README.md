# Project starter kit

A small, local, dependency-light skeleton for the Securing AI Systems projects. It runs on a laptop CPU with
Python 3.10+, needs no API key, and exists so that setup does not consume the project.

```text
starter/
  app/            FastAPI service: API-key auth, per-cohort authorisation, quotas, audit
  eval/           Evaluation harness: attacks, budgets, a noise control, JSON results
  rag/            SQLite FTS5 retrieval with ACL filtering *before* ranking
  monitoring/     Three signals over the audit table
  notebooks/      Percent-format notebook for the analysis steps
  tests/          pytest suite covering the deny paths
```

## Run it

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
uvicorn app.main:app --port 8100
```

Demo keys (development only, hashed at startup): `demo-key-a` (cohort `alpha`), `demo-key-b` (cohort `beta`).

```bash
curl -s localhost:8100/health
curl -s -X POST localhost:8100/predict \
  -H 'X-API-Key: demo-key-a' -H 'Content-Type: application/json' \
  -d '{"cohort":"alpha","features":[0.4,-1.2,2.0,0.1]}'
```

## What is deliberately missing

This is a skeleton, not a solution. There is no threat model, no measurement of any defence, no isolation proof
(the tests that assert absence of foreign content are yours to write), and no severity or decision. The mock model
is deterministic and uninteresting: replacing it is step one of several projects.

If you submit this with cosmetic changes you will score *Developing* on method and *Emerging* on measurement.

## Configuration

| Variable | Default | Meaning |
|---|---|---|
| `SAS_DB` | `starter.db` | SQLite path for audit and quota state |
| `SAS_ENABLED` | `1` | `0` stops predictions while keeping `/health` alive |
| `SAS_RPM` | `10` | Requests per minute per key |
| `SAS_RPD` | `1000` | Requests per day per key |

## Use it

Copy it into your own repository rather than editing in place, so the reference stays runnable:

```bash
cp -r projects/starter ~/my-project
```

Keep the deny-path tests. They are the cheapest evidence you will have, and every project in the programme is marked
partly on whether the refusals hold.
