---
title: A2 · Securing a fraud detection pipeline
description: Assignment 2 — review a nightly-retrained fraud model and design its security controls.
---

# A2 · Securing a fraud detection pipeline

**After:** Module 07 · **Weight:** 10 % · **Length:** 1,100 words
**Deliverable:** A pipeline security review with a control plan and a rollback design

## Scenario

A mid-sized payments processor runs a gradient-boosted fraud model. It is retrained nightly on the last 90 days of
transactions, including labels reported by merchants through a partner portal. The model scores transactions in
under 40 ms and blocks about 1.2 % of traffic.

Two facts have emerged. First, a merchant account was compromised six weeks ago and its labels are unverified.
Second, a data scientist has been experimenting in the same repository with a `requirements.txt` that installs two
packages from a Git URL.

The head of risk wants a review that fits on four pages and answers one question: *what could let a fraudulent
transaction through without anyone noticing?*

## Problem statement

Assess the pipeline from label ingestion to served decision, identify the paths by which integrity can be lost,
and propose controls with their operational cost.

## Requirements

1. Map the pipeline in five stages: collection, labelling, feature construction, training, serving. Name the
   attacker access required at each stage.
2. Analyse **label poisoning** specifically: what access the compromised merchant had, the realistic poisoning
   rate, and the effect on a targeted pattern compared with overall accuracy.
3. Analyse **evasion**: what an attacker who can shape a transaction can do, and why aggregate accuracy will not
   show it.
4. Analyse **supply chain**: what the Git-installed dependency can do in a training job, and the control that
   would have prevented it.
5. Design a **rollback path**: what is versioned, what triggers a rollback, and who decides.
6. State the **monitoring signal** that would detect each failure within 24 hours.

## Tasks

1. Draw the five-stage map and annotate each stage with the access an attacker needs.
2. For label poisoning, state the poisoning rate you assume and justify it from the merchant portal's controls.
3. Describe a slice metric that would catch a targeted pattern that global accuracy hides.
4. Propose a dependency policy that permits internal packages without allowing unpinned Git installs.
5. Design the rollback: artefact versioning, trigger conditions, decision authority and verification after
   rollback.
6. Write a 150-word summary for the head of risk that names the two controls you would fund first.

## Deliverables

| Item | Format | Length |
|---|---|---|
| Pipeline map | diagram or table with access annotations | 1 page |
| Threat analysis | three sections (poisoning, evasion, supply chain) | 700 words |
| Control plan | table: control, stage, cost, residual | 1 page |
| Rollback design | procedure with triggers and authority | 300 words |
| Summary | prose | 150 words |

## Evaluation criteria

- **Access reasoning:** does each threat name the access it requires, and is that access realistic here?
- **Measurement:** are rates, slices and thresholds specified rather than implied?
- **Operational realism:** would the controls survive a 40 ms latency budget and a nightly retrain?
- **Recovery:** is the rollback specific enough to execute at 03:00 without the author present?

## Rubric

| Criterion | 1 — Emerging | 2 — Developing | 3 — Proficient | 4 — Exemplary |
|---|---|---|---|---|
| Access reasoning | Threats listed without access | Access named for some threats | Access named and justified for each | Access compared, and the cheapest path identified |
| Measurement | No numbers | Some rates, no denominators | Rates with stated denominators | Rates with the measurement method and its bias |
| Operational realism | Ignores latency and cadence | Mentions constraints | Controls fit the constraints | Controls fit, and the trade-off is quantified |
| Recovery | "Retrain the model" | Rollback mentioned | Versioned artefact and trigger | Executable procedure with authority and verification |

## Extension challenges

1. Estimate how many poisoned labels a 1 % poisoning rate implies at this volume, and whether the portal's
   controls make that feasible.
2. Design a canary pattern set that runs every hour against production scoring and alerts on a change.
3. Propose a compensation model for merchants whose labels are later found to be corrupt.

## Constraints

Use only the scenario. Do not attempt to access any payment system. Any numbers you introduce must be labelled as
assumptions with a stated basis.
