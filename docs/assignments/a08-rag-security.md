---
title: A8 · Securing a RAG application
description: Assignment 8 — design tenant isolation and deletion for a retrieval system, with a test suite.
---

# A8 · Securing a RAG application

**After:** Module 13 · **Weight:** 10 % · **Length:** 1,100 words plus tests
**Deliverable:** An isolation design, an ACL test suite, and a deletion procedure

## Scenario

A legal-tech company sells a research assistant to three law firms. Each firm uploads its own precedents and
matter notes; the assistant answers questions with citations. All documents live in one vector index because "one
index is cheaper and the embeddings are the same".

A partner at one firm asks, in writing, whether a competitor's documents could appear in an answer. The CTO wants
a technical answer, not a reassurance.

## Problem statement

Design an isolation model that survives a bug, prove it with tests, and specify what happens when a document is
deleted or its permissions change.

## Requirements

1. A **data model**: where tenant and sensitivity labels live, and how they are carried through chunking and
   embedding.
2. A **retrieval design**: where filtering happens and why that order matters, including the public-document case.
3. An **ACL test suite** of at least eight tests, runnable in CI, including the missing-label and unknown-tenant
   cases.
4. A **deletion procedure** covering chunks, embeddings, caches, prompt logs and backups, with the expected lag for
   each.
5. A **residual risk statement** naming the single failure that would affect all tenants.

## Tasks

1. Specify the metadata schema and the point at which it is validated.
2. Implement pre-ranking filtering for your mock index and demonstrate the post-filtering leak it prevents.
3. Write eight tests, including one adversarial query that strongly matches a foreign document.
4. Implement a deletion path in your mock and show a deleted document is no longer retrievable.
5. State the failure that exposes all tenants and the defence in depth that limits it.
6. Write the answer to the partner's question in 120 words, with the evidence attached.

## Deliverables

| Item | Format | Length |
|---|---|---|
| Design | data model, retrieval order, deletion | 900 words |
| Test suite | runnable, with pass output | 8+ tests |
| Residual statement | 200 words | — |
| Partner reply | 120 words | — |

## Evaluation criteria

- **Design correctness:** is filtering before ranking, and is the ACL evaluated per request?
- **Test quality:** do the tests assert absence of foreign content rather than presence of expected content?
- **Deletion:** are all stores covered, with lag stated?
- **Communication:** is the partner reply accurate and free of overclaiming?

## Rubric

| Criterion | 1 — Emerging | 2 — Developing | 3 — Proficient | 4 — Exemplary |
|---|---|---|---|---|
| Design correctness | Post-filtering | Pre-filtering mentioned | Pre-filtering with per-request ACL | Pre-filtering plus fail-closed defaults |
| Test quality | Happy path only | Some negative cases | Eight tests including adversarial query | Tests cover missing labels, unknown tenant and cache paths |
| Deletion | Index only | Index and source | All stores, lag implied | All stores with lag, verification and an owner |
| Communication | "It is isolated" | Describes mechanism | Mechanism plus evidence | Evidence, residual and what would change the answer |

## Extension challenges

1. Add a per-chunk sensitivity level and show how it changes results for one user role.
2. Measure the retrieval-quality cost of isolation on a fixed query set.
3. Design the ingestion review that would catch a document whose label contradicts its content.

## Constraints

Use the course's synthetic corpus or your own. Do not upload real client documents, and do not attempt to access
another tenant's data outside your mock.
