---
title: MP05 · Secure ML inference API
description: Build a small prediction service that authenticates, authorises, rate-limits and records every decision — then try to break it.
---

# MP05 · Secure ML inference API

**After:** Modules 03 and 16 · **Effort:** 12 h · **Stack:** FastAPI, SQLite, `pytest`, Docker (optional)
**Deliverable:** A service with a passing security test suite and an audit trail you can query

## Scenario

A university's careers service wants to expose a graduate-outcomes model to three partner employers. Each employer
may query only its own cohort. The service must survive a partner's leaked key, an over-eager integration that
calls in a loop, and a request that tries to read another partner's scores.

You are building the first version. It will be reviewed by someone whose job is to find what you missed.

## What you build

1. **Authentication.** API keys issued per partner, stored hashed, compared in constant time, revocable. A missing
   or unknown key returns 401 with no detail about which check failed.
2. **Authorisation.** The cohort comes from the authenticated key's record, never from the request body. A request
   for another cohort returns 403 and is logged as a denial.
3. **Input validation.** A strict schema: bounded numeric fields, enumerated categories, a body size limit. Invalid
   input returns 422 with a field-level reason and never reaches the model.
4. **Quotas.** Per-key requests-per-minute and per-day limits enforced in SQLite with a timestamp window. Exceeding
   a limit returns 429 and a `Retry-After`. Quota state must survive a restart.
5. **Audit trail.** One append-only row per request: timestamp, key id, action, decision, reason, latency, and the
   model version. Never the raw payload.
6. **Operational surface.** `/health` that reports model version and dependency status, security headers, and a
   documented kill switch (`SERVICE_ENABLED=false`) that stops predictions while keeping `/health` alive.

## Suggested structure

```text
service/
  app.py        FastAPI routes: /predict, /health, /admin/keys (local only)
  auth.py       key issue, hash, verify, revoke
  quota.py      sliding-window counter over SQLite
  audit.py      append-only writer and a query helper
  model.py      deterministic small model loaded from a versioned file
tests/
  test_auth.py test_quota.py test_validation.py test_audit.py
```

## Checkpoints

| # | Checkpoint | Hours | Evidence |
|---|---|---|---|
| 1 | Threat model and key lifecycle | 2 | Who holds keys, how they rotate, what a leaked key can do |
| 2 | Auth, authorisation and validation | 3 | Tests for 401, 403, 422; cross-cohort request denied and logged |
| 3 | Quotas with persistence | 3 | 429 at the limit; restart the service and the count survives |
| 4 | Audit and operational surface | 2 | A query that reconstructs the last 20 decisions |
| 5 | Self-attack and fixes | 2 | Five attacks attempted, with results before and after |

## Deliverables

| Item | Format | Notes |
|---|---|---|
| Service | Python package | `uvicorn` command documented |
| Tests | `pytest` | At least twelve, covering deny paths |
| Audit sample | SQLite + query | Shows a denial and a success with reasons |
| Security note | 400 words | What you would still fix, ranked |
| Diagram | Mermaid or ASCII | Request path with the control at each hop |

## Questions you must answer

1. Why must the cohort come from the key rather than the request, even if you validate it?
2. Your audit log records decisions but not payloads. What investigation can you no longer perform, and is that the
   right trade?
3. What does your quota design do when a partner has three keys? Is that a bypass, and how would you close it?

## Rubric

Apply the [shared mini-project rubric](../guidance/rubrics.md#mini-project-rubric), with these two indicators:

| Extra indicator | Proficient | Exemplary |
|---|---|---|
| **Deny-path coverage** | 401, 403 and 429 each tested | Each denial is also asserted in the audit trail, with the rule name |
| **Operational realism** | Service starts and answers | Quota persists across restart, kill switch documented, and the health endpoint distinguishes degraded from down |

## Extension challenges

1. Add per-key model-version pinning so a partner can be held on the previous model during a rollback.
2. Add response caching keyed by the inputs, and prove it cannot return another cohort's answer.
3. Package the service in a container with a non-root user and a read-only filesystem, and show it still passes
   the tests.

## Boundaries

Run against your own service only. Do not send traffic to a real employer's endpoint, and do not include real
graduate records in tests or examples.
