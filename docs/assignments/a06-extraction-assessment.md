---
title: A6 · Evaluating model extraction risk
description: Assignment 6 — measure how cheaply a proprietary scoring model can be copied, and design the defence.
---

# A6 · Evaluating model extraction risk

**After:** Module 10 · **Weight:** 10 % · **Length:** 900 words plus an experiment
**Deliverable:** An extraction-risk assessment, a cost curve and a defence recommendation with its product cost

## Scenario

A pricing startup sells access to a model that estimates willingness-to-pay for insurance products. The API
returns a probability and has a free tier of 1,000 calls per day. The founder believes the model is safe because
"nobody can copy 40 million parameters from an API".

You have the model's public documentation, a mock API you build yourself, and the course dataset. The board wants
to know whether a competitor could reproduce the pricing function closely enough to compete.

## Problem statement

Quantify the relationship between query budget, output granularity and extraction fidelity, then recommend a
defence whose cost the board can weigh against the risk.

## Requirements

1. A **mock API** with three output modes: probability, rounded probability, and label.
2. A **cost curve**: fidelity against budget at three budgets, plus a paired comparison of the three modes at one
   budget.
3. An **attacker model**: what an adversary with ten accounts and patience could achieve, and the assumption behind
   it.
4. A **defence package**: at least three measures, each with its product cost and its measured or expected effect.
5. A **recommendation** that states what the defence buys in months of delay, if anything.

## Tasks

1. Build the target model and the mock API with a query counter.
2. Sample queries around the observed feature ranges and fit substitutes at 50, 150 and 500 queries.
3. Measure fidelity against the target's predictions on held-out rows, and report the target's own accuracy.
4. Repeat at one budget with rounded and label-only output.
5. Estimate the total queries and accounts needed to reach 0.9 fidelity, and the time that takes at the free-tier
   rate.
6. Recommend the package and state the assumption that would make your recommendation wrong.

## Deliverables

| Item | Format | Length |
|---|---|---|
| Experiment | code and results table | — |
| Assessment | prose, 700 words | — |
| Defence table | measure, cost, effect, residual | 1 page |
| Recommendation | 150 words for the board | — |

## Evaluation criteria

- **Experimental design:** is the sampling distribution stated, and is fidelity measured on held-out rows?
- **Quantification:** does the report give a cost in queries, accounts and time rather than an adjective?
- **Defence analysis:** are product costs stated, and is the plateau explained rather than assumed?
- **Decision:** is the recommendation specific enough to approve or reject?

## Rubric

| Criterion | 1 — Emerging | 2 — Developing | 3 — Proficient | 4 — Exemplary |
|---|---|---|---|---|
| Experimental design | Fidelity on training queries | Held-out fidelity | Held-out, sampling stated | Held-out with a sampling-choice ablation |
| Quantification | No numbers | Budget only | Budget, accounts, time | Cost curve with the plateau explained |
| Defence analysis | Generic list | Costs missing | Costs stated | Costs and measured effect, with residual |
| Decision | "Add rate limits" | Specific measure named | Package with trade-off | Package, expected delay, and the assumption that flips it |

## Extension challenges

1. Implement active learning and compare the queries needed to reach 0.9 fidelity.
2. Add a watermark trigger set and describe the verification procedure a third party would run.
3. Model the attacker's economics: cost per query against the value of the copied model.

## Constraints

Test only your own mock service. Do not query a real commercial API, and do not reproduce a real vendor's model in
your report.
