---
title: A12 · Designing a production AI security monitoring system
description: Assignment 12 — design detection, triage and response for a deployed AI service.
---

# A12 · Designing a production AI security monitoring system

**After:** Module 18 · **Weight:** 10 % · **Length:** 1,200 words plus a design diagram
**Deliverable:** A monitoring design with signals, thresholds, triage rules and an incident playbook

## Scenario

A bank has deployed an assistant for its contact-centre staff. It summarises customer records, retrieves policy
documents and can draft replies. It has been live for three months, generates 40,000 requests per day, and has no
AI-specific monitoring: the operations team watches uptime, latency and error rate.

The head of security has budget for one engineer for a quarter and wants "detection that would have caught the
things in your course".

## Problem statement

Design a monitoring and response capability that fits one engineer and one quarter, is explicit about what it will
not detect, and can be operated by the existing on-call team.

## Requirements

1. **Six signals**, each with: what it measures, the failure it indicates, the data needed, and the cost to build.
2. **Thresholds** for each signal, with the base-rate reasoning and the expected alert volume per week.
3. A **triage rule set**: how an alert becomes a case, who decides, and what evidence is collected first.
4. An **incident playbook** for one scenario, with containment, evidence preservation, recovery verification and
   notification.
5. A **quarter plan**: what ships in weeks 1–4, 5–8 and 9–12, and what is deliberately deferred.
6. A **statement of blindness**: what this design will not detect.

## Tasks

1. Choose signals that map to AI-specific failures: extraction, injection, retrieval isolation, artefact
   integrity, output quality, credential misuse.
2. For each, estimate the alert volume at the bank's traffic, and justify the threshold.
3. Write the triage rule for two signals, including the combination that escalates.
4. Write the playbook for a suspected extraction campaign.
5. Sequence the build so that week 4 delivers something usable, not a platform.
6. Write the blindness statement and the metric you would use to justify next quarter's budget.

## Deliverables

| Item | Format | Length |
|---|---|---|
| Signal table | six rows: measure, failure, data, cost, threshold, volume | 1 page |
| Triage rules | two worked rules plus escalation | 400 words |
| Playbook | phases with actions and owners | 1 page |
| Quarter plan | three phases with deliverables | 300 words |
| Blindness statement | 150 words | — |

## Evaluation criteria

- **Signal relevance:** do the signals detect the failures the course describes, rather than generic anomalies?
- **Alert realism:** are volumes and thresholds justified against a base rate?
- **Operability:** could the existing on-call team run this without the author?
- **Honesty:** is the blindness statement specific?

## Rubric

| Criterion | 1 — Emerging | 2 — Developing | 3 — Proficient | 4 — Exemplary |
|---|---|---|---|---|
| Signal relevance | Uptime and latency only | One AI-specific signal | Four or more mapped to failures | Six, each tied to a named failure mode |
| Alert realism | No volumes | Volumes guessed | Thresholds with base-rate reasoning | Volumes, thresholds and a tuning plan |
| Operability | Requires the author | Documented | Playbook with owners | Playbook, evidence steps and a drill |
| Honesty | "Covers all risks" | Brief caveat | Blindness listed | Blindness with the metric that would justify more |

## Extension challenges

1. Add a canary set of documents and questions that runs hourly and reports behavioural drift.
2. Design the retention policy for the evidence the playbook collects.
3. Write the one-page proposal for the second engineer, using your alert-volume data.

## Constraints

Design only. Do not instrument a real service, and use synthetic traffic if you prototype a detector.
