---
title: Getting Started
description: Orientation for the Securing AI Systems course — how it works, what you need, and how to begin.
---

# Getting Started

Welcome. This page tells you how the course works before you spend an hour inside it.

If you only read one thing here, read this: **the course is built around doing, not reading.** Every module hands you a laboratory with numeric success criteria. A student who reads all twenty modules and runs none of the laboratories has learned vocabulary, not capability — and will not be able to answer the first question in an interview.

## Before your first hour

<div class="sas-grid sas-grid--3" markdown>

<div class="sas-card sas-card--step" markdown>
<div class="sas-card__step">1</div>
<div class="sas-card__title">Check the prerequisites</div>
Ten minutes. Confirm that Python, NumPy and the idea of a training loop are familiar, and find the refresher if not.

[Prerequisites →](prerequisites.md)
</div>

<div class="sas-card sas-card--step" markdown>
<div class="sas-card__step">2</div>
<div class="sas-card__title">Set up one environment</div>
Twenty minutes. One virtual environment, one install command, one check script. Doing this properly now prevents a week of confusing errors later.

[Learning environment →](environment.md)
</div>

<div class="sas-card sas-card--step" markdown>
<div class="sas-card__step">3</div>
<div class="sas-card__title">Choose a study plan</div>
Five minutes. Full pathway, condensed semester track, or a specialisation. They use the same content.

[Study plans →](study-plans.md)
</div>

</div>

## How the course is structured

Five parts, twenty modules. Each module is a self-contained unit of roughly ten to eighteen hours, and each ends with something you can check yourself against.

| Part | Modules | What it establishes | Approx. hours |
|---|---|---|---|
| [Level 1 — Foundation](../modules/index.md#level-1-foundation) | 01–05 | Security vocabulary, ML fundamentals, classical controls, threat modelling, data protection | 52 |
| [Level 2 — Intermediate](../modules/index.md#level-2-intermediate) | 06–10 | Attacks and defences, measured: evasion, poisoning, robustness, privacy, extraction | 72 |
| [Level 3 — Advanced](../modules/index.md#level-3-advanced) | 11–15 | LLMs, injection, retrieval, agents, and the model supply chain | 72 |
| [Level 4 — Professional Practice](../modules/index.md#level-4-professional-practice) | 16–20 | APIs, red teaming, operations, governance, deployment | 88 |

Around the modules sit thirty-two [laboratories](../labs/index.md), twelve [scenario assignments](../assignments/index.md), twenty [self-check quizzes](../quizzes/index.md), [projects and a capstone](../projects/index.md).

## What a module contains

Every module uses the same structure inside one page, so you always know where you are:

<div class="sas-grid sas-grid--2" markdown>

<div class="sas-card sas-card--plain" markdown>
**Overview** — why the topic matters, what you will be able to do, the theory, and a worked demonstration with expected output.
</div>

<div class="sas-card sas-card--plain" markdown>
**Laboratory** — a practical exercise with setup, steps, numeric success criteria and a results table to fill in, with its notebook linked from the module card.
</div>

<div class="sas-card sas-card--plain" markdown>
**Exercises** — recall, apply and extend, so you can go as deep as you need, plus a previous/next module link at the foot of the page.
</div>

<div class="sas-card sas-card--plain" markdown>
**Knowledge check and quiz** — collapsible questions in the page, then a separate self-marking quiz with written items.
</div>

</div>

While modules are being released, a module page shows its **status**. A `planned` module has its scope defined but no teaching content yet; `draft` has content in review; `complete` has been through the full quality contract.

## The five-session rhythm

Each module is designed for the same rhythm. Following it matters more than it looks — it is what turns reading into recall.

| Session | What you do | Time |
|---|---|---|
| 1. Read | Conceptual core, noting the threat and control table as you go | ~90 min |
| 2. Reproduce | Run the demonstration and match the numbers in the text | ~45 min |
| 3. Do the lab | Complete the laboratory and record results in the lab log | 3–5 h |
| 4. Self-check | Quiz and exercises, then revisit the sections you missed | ~45 min |
| 5. Reflect | One page: what would you check first in a real system, and why? | ~20 min |

Session 5 is the one students skip and the one that matters most. Writing a page in your own words is the only reliable test of whether the material became yours.

## How you are assessed

There are no hidden assessments in self-study mode. Every instrument is public, and the [assessment overview](assessment.md) explains how each is marked, including the rubric used across the course and the gates between parts.

If you are studying for credit, your institution may adjust the weighting. The instruments do not change.

## Safety and ethics

!!! warning "Read this before any offensive module"

    The course teaches attack techniques because you cannot defend what you cannot attack. All laboratories target synthetic data, models you trained yourself, or applications supplied inside the course sandbox.

    **You must never apply these techniques to a system you do not own or have explicit written permission to test.** Unauthorised testing of another person's AI system is a criminal offence in many jurisdictions, a breach of contract in most, and always a breach of professional ethics. "It was only a prompt" is not a defence: indirect prompt injection against a production assistant is unauthorised access.

Beyond the law, three professional expectations run through the course:

- **Minimise impact.** A proof of concept that demonstrates access is enough; never exfiltrate real user data, never cause a denial of service, never persist access.
- **Report responsibly.** If you find a real vulnerability, follow coordinated disclosure: report privately to the owner, agree a timeline, and publish nothing until it is fixed.
- **Write down your authorisation.** Scope, dates, targets, stop conditions, and who approved it. Module 18 makes this a deliverable because professionals are judged on their paperwork as much as their technique.

The full rules — responsible tool use, authorised testing, academic honesty, citation, sensitive data, and vulnerability disclosure — are on [Academic integrity and responsible use](academic-integrity.md). Read it before your first offensive laboratory. [Privacy](privacy.md) explains what the course stores, which is one completion date in your own browser and nothing else.

## Getting help when you are stuck

| Situation | What to do |
|---|---|
| An install or environment error | Read the troubleshooting table in [Learning Environment](environment.md#troubleshooting) first — it covers the five most common failures |
| A lab produces different numbers than the text | Check the seed, the library versions, and whether you are on CPU or GPU; then read the lab's "expected variance" note |
| A concept will not land | Do the worked demonstration before re-reading the theory; concrete before abstract is faster here |
| You disagree with something | Good. The exercises include "find the flaw in this claim" items deliberately. Write your objection down and test it |

## Next steps

<div class="sas-grid sas-grid--3" markdown>

<div class="sas-card" markdown>
<div class="sas-card__title">How to use this course</div>
Reading modes, icons, progress tracking, and how to work with the notebooks.

[Continue →](how-to-use.md)
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Learning roadmap</div>
The full pathway, checkpoint gates, and three study plans with honest hour counts.

[Continue →](../roadmap.md)
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Module 01</div>
Security foundations for AI systems — assets, actors, trust boundaries, and your first threat model.

[Begin →](../modules/01-introduction.md)
</div>

</div>
