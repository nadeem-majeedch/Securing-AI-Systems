---
title: A9 · Designing an AI agent authorisation framework
description: Assignment 9 — compute an agent's effective permissions, reduce them, and specify confirmation points.
---

# A9 · Designing an AI agent authorisation framework

**After:** Module 14 · **Weight:** 10 % · **Length:** 1,000 words plus a policy implementation
**Deliverable:** A permission analysis, a policy engine with tests, and a confirmation design

## Scenario

An operations team wants an agent that can read tickets, search a knowledge base, send email to customers, issue
refunds up to £200, and create calendar events for on-call staff. It will run as a service account with broad
access "so it can recover from unusual situations".

The finance director has approved a pilot. The security team has to specify the authorisation model before it is
connected to the production ticketing system.

## Problem statement

Compute the agent's effective permissions as proposed, reduce them to the minimum that supports the workflow, and
show that the reductions do not break the legitimate path.

## Requirements

1. An **effective-permission analysis**: the union of what the service account can reach, expressed as
   (principal, action, resource) triples.
2. A **policy design** with deny-by-default, role and tenant checks, amount limits and recipient constraints.
3. An **implementation** of the policy with at least ten test requests, including five that must be denied.
4. A **confirmation design**: which actions require human confirmation, what the confirmation shows, and who can
   approve.
5. An **audit record** specification: the fields required to explain a decision without rerunning the agent.

## Tasks

1. Write the proposed permission set and compute its union. Show the triples, not a description.
2. Identify the confused-deputy path in the current design and the request that would exploit it.
3. Implement the policy engine and run the ten requests; report decision and rule for each.
4. Demonstrate that the legitimate workflow still completes under the reduced policy.
5. Specify the confirmation boundary and justify it by reversibility and external effect.
6. Specify the audit fields and a retention period with a reason.

## Deliverables

| Item | Format | Length |
|---|---|---|
| Permission analysis | triple table, before and after | 1 page |
| Policy implementation | code plus test output | 10+ cases |
| Confirmation design | table: action, confirmation, approver | 1 page |
| Audit specification | fields and retention | 300 words |

## Evaluation criteria

- **Permission reasoning:** is the union computed rather than described?
- **Policy correctness:** does it deny by default and derive the tenant from the principal?
- **Workflow preservation:** does the legitimate path still work after reduction?
- **Auditability:** can a reviewer reconstruct any decision from the record?

## Rubric

| Criterion | 1 — Emerging | 2 — Developing | 3 — Proficient | 4 — Exemplary |
|---|---|---|---|---|
| Permission reasoning | Describes access in prose | Lists tools | Computes triples | Computes triples and ranks by consequence |
| Policy correctness | Allowlist of tools only | Some checks | Deny by default, tenant from principal | Plus argument validation against source data |
| Workflow preservation | Not tested | Asserted | Tested for the main path | Tested, with the cost of each reduction stated |
| Auditability | Logs the answer | Logs the tool | Logs decision and rule | Logs rule, reason and effective principal |

## Extension challenges

1. Add a per-session budget so repeated small refunds cannot exceed the cap.
2. Design the escalation path for an action above the cap, including the approval artefact.
3. Model a second agent that delegates to this one, and show where authority must be re-checked.

## Constraints

Run everything against a mock ticketing and payment service. Do not connect to a production system, and do not
issue real refunds or emails.
