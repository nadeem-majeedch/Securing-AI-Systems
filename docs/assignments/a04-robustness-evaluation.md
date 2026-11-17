---
title: A4 · Evaluating adversarial robustness
description: Assignment 4 — design and run a robustness evaluation, then write the claim it supports.
---

# A4 · Evaluating adversarial robustness

**After:** Module 08 · **Weight:** 10 % · **Length:** 1,000 words plus code and results
**Deliverable:** An evaluation protocol, a results table and a claim statement for the model card

## Scenario

A document-verification product uses a small image classifier to check whether a photographed identity document
has been tampered with. The vendor's model card says "robust to adversarial manipulation". A prospective bank
client has asked for evidence before signing.

You have the model, a synthetic document dataset, and two weeks. The bank's security team has one condition: the
claim must be one their auditor can reproduce.

## Problem statement

Design and execute a robustness evaluation that produces a defensible claim, and rewrite the vendor's claim so
that it matches the evidence.

## Requirements

1. A **threat model** for this product: what an attacker can change (print, photograph, compress, edit), and the
   norm and budget that represent those changes.
2. An **attack suite** with at least three attacks, including one adaptive to the defence if a defence exists.
3. A **control** at the same budget, so the effect of the attack is separable from general degradation.
4. **Results** on held-out data with seeds, restarts and variance; clean accuracy reported alongside.
5. A **claim statement** of at most 40 words, naming the attack, norm, budget, result and what is not claimed.
6. A **limitations section** listing what the evaluation cannot support.

## Tasks

1. Justify the budget in physical terms (pixels, print resolution, compression), not by convenience.
2. Implement or run the attacks and the control; report accuracy with the number of inputs.
3. Test the defence adaptively: if the pipeline includes preprocessing, attack the composed system.
4. Compute the gap between the strongest and weakest attack, and explain what a large gap implies.
5. Write the 40-word claim, then have someone check that every number in it is in your table.
6. Write the two sentences you would say to the bank if the results are weaker than the vendor claimed.

## Deliverables

| Item | Format | Length |
|---|---|---|
| Protocol | threat model, attacks, budgets, control | 1 page |
| Results | table with seeds, restarts, variance | 1 page |
| Code | runnable script/notebook | — |
| Claim statement | ≤ 40 words | — |
| Limitations | bullet list with reasons | 300 words |

## Evaluation criteria

- **Threat fidelity:** does the budget correspond to what the attacker can do to a photographed document?
- **Evaluation strength:** are the attacks strong enough to falsify the defence, and is a control present?
- **Reporting:** are the numbers complete enough to compare with other work?
- **Claim discipline:** is the claim exactly what the evidence supports, no more?

## Rubric

| Criterion | 1 — Emerging | 2 — Developing | 3 — Proficient | 4 — Exemplary |
|---|---|---|---|---|
| Threat fidelity | Budget chosen arbitrarily | Budget reasoned but not physical | Budget tied to acquisition effects | Budget tied to effects and its assumption tested |
| Evaluation strength | One attack, defaults | Two attacks, no control | Three attacks plus control | Adaptive attack, restarts, and a gap analysis |
| Reporting | Accuracy only | Accuracy and budget | Accuracy, budget, seeds, variance | Full table including flip counts and control |
| Claim discipline | Restates the vendor | Narrows the claim partially | Claim matches the table | Claim matches and names what is excluded |

## Extension challenges

1. Add a physical simulation (print, photograph, JPEG) and report whether digital robustness survives it.
2. Estimate the cost per evaluation run and recommend a cadence for re-running it.
3. Design a regression test that would fail the build if robustness drops by more than five points.

## Constraints

Use the synthetic dataset and your own model. Do not test any real identity document, do not attempt to defeat a
real verification system, and do not publish material that could be used to forge a document.
