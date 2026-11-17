---
title: Capstone proposals
description: Five comprehensive capstone proposals, each with a full brief, threat model, methodology and rubric.
hide:
  - toc
---

# Capstone proposals

Five proposals, one per sector. Each is a complete brief: eighteen sections from industry background to assessment
rubric. Choose one, adapt it, or use the structure to write your own.

The proposals are deliberately large. A capstone is sixty hours of assessed work, and a proposal that could be
finished in twenty would teach you nothing about scoping. Part of the assessment is deciding what to cut: your
proposal submission must name what you are **not** doing and why.

| # | Proposal | Sector | Core security problem | Modules |
|---|---|---|---|---|
| [C1](c01-clinical-triage.md) | TriageAssist — secure clinical referral triage | Healthcare | Retrieval isolation and meaningful oversight under time pressure | 05, 09, 13, 19 |
| [C2](c02-credit-poisoning.md) | CreditGuard — poisoning-resilient credit decisioning | Financial services | Data integrity and model risk when labels come from a partner | 07, 08, 10, 19 |
| [C3](c03-campus-assistant.md) | Campus Assistant — multi-tenant knowledge and actions | Higher education | Tenancy boundaries and tool authority in one assistant | 13, 14, 16 |
| [C4](c04-benefits-assistant.md) | Benefits Guide — eligibility support with contestable decisions | Public sector | Fairness, privacy and a decision a citizen can challenge | 09, 17, 19 |
| [C5](c05-offline-ops-copilot.md) | OfflineOps — air-gapped operations copilot | Manufacturing and utilities | Prompt injection and supply-chain integrity with no cloud | 11, 12, 14, 15, 18 |

## How to choose

1. **By access.** Which system could you actually build and test in sixty hours, alone? Every proposal is designed to
   run on a laptop CPU with synthetic data.
2. **By gap.** Which of the [capstone rubric](../../capstone/index.md#public-rubric) criteria is your weakest? The
   proposals stress different ones: C1 and C4 stress oversight and assurance; C2 stresses measurement; C5 stresses
   containment.
3. **By interest.** You will spend sixty hours with this system. Pick the sector you would read about voluntarily.

## What you submit

Your proposal submission is **M1** of the capstone: this brief adapted to your chosen system, with your scope
decision, your threat model, your rules of engagement and your acceptance criteria. The eighteen headings below are
the required structure; the content must be yours.

<div class="sas-grid sas-grid--2" markdown>

<div class="sas-card" markdown>
<div class="sas-card__title">Proposal versus solution</div>
These pages are **briefs**. They describe what must be built and how it will be judged; they do not contain the
architecture decisions, controls or measurements that earn marks. Sample-solution guidance is kept separate, in the
repository's `projects/solutions/` directory, and is deliberately partial.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Before you start</div>
Read the [project workflow](../../projects/guidance/workflow.md), the [milestone guide](../../projects/guidance/milestones.md) and the
[capstone rules](../../capstone/index.md). M1 must be accepted before any testing begins.
</div>

</div>
