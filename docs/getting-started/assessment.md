---
title: Assessment
description: How the Securing AI Systems course is assessed — instruments, weighting, rubrics and the claim-discipline criterion.
---

# Assessment Overview

Every assessment instrument in this course is public. There are no hidden tests, and nothing is graded on attendance or participation.

That openness is deliberate: the course teaches that security claims are only worth their evidence, so the assessments measure evidence rather than recall.

## Instruments

| Instrument | Count | Purpose | Feedback |
|---|---|---|---|
| [Module quizzes](../quizzes/index.md) | 20 | Confirm recall and expose misconceptions | Instant on multiple choice; explanations for every option; written model answers |
| [End-of-level assessments](../quizzes/level-1.md) | 4 | Retention across five modules, closed-book | Marked after the attempt; model answers |
| [Final assessment](../quizzes/final.md) | 1 | Transfer across the whole course, timed | Marked after the attempt; pass mark 60 % |
| Tiered exercises | 20 × 9 | Apply and extend | Hints and expected outcomes |
| [Laboratories](../labs/index.md) | 20 | Build capability, with measurable results | Rubric, self-assessed |
| [Scenario assignments](../assignments/index.md) | 12 | Judgement under ambiguity, technical writing | Rubric with level descriptors |
| [Mini projects](../projects/mini/index.md) | 10 | Integrate two or three modules into a working artefact | Rubric |
| [Major projects](../projects/major/index.md) | 6 | End-to-end engineering and evaluation | Rubric and review checklist |
| [Capstone proposals](../capstone/proposals/index.md) | 5 | Assess a system and defend the assessment | Multi-criterion rubric and defence |
| [Capstone](../capstone/index.md) | 1 | Full-scope assessment and assurance pack | Multi-criterion rubric and defence |

## Default weighting

For a 4-credit adoption. Institutions may adjust; the instruments do not change.

| Component | Weight | Notes |
|---|---|---|
| Quizzes (best 16 of 20) | 10 % | Counted to encourage steady work, not cramming |
| End-of-level and final assessments | 0 % by default | Diagnostic; a level paper below 70 % triggers revision, not a penalty |
| Laboratories | 20 % | A must-pass subset gates progression |
| Scenario assignments | 15 % | Twelve briefs; technical writing is assessed explicitly |
| Mini projects | 15 % | Four submitted, ~3.75 % each; ten briefs available |
| Major projects | 15 % | Two submitted, 7.5 % each; six briefs available |
| Capstone and defence | 25 % | Decisive, but not so dominant that earlier work is irrelevant |

For the condensed track, drop the quizzes to 10 % of a 100 % scheme scaled to eight modules and weight the capstone-lite at 30 %.

## How laboratories are marked

A laboratory is marked on evidence, not effort. The rubric has four levels and five criteria.

| Criterion | Emerging (1) | Developing (2) | Proficient (3) | Exemplary (4) |
|---|---|---|---|---|
| **Correctness** | Result wrong or unreproducible | Result approximately right, method unclear | Correct, reproducible, parameters stated | Correct, reproducible, and verified by a second method |
| **Measurement** | No numbers, or numbers without denominators | Numbers reported for one run | Numbers with seed, sample size and variance | Numbers with confidence intervals and an attack-strength control |
| **Interpretation** | Restates the result | Explains what happened but not why | Connects the result to the threat model | Explains why the result would change under a different adversary |
| **Defence evaluation** | Defence asserted effective | Defence tested once | Defence tested with an adaptive attack | Defence tested adaptively, with residual risk quantified |
| **Reproducibility** | Notebook will not run | Runs with manual fixes | Runs from a fresh kernel | Runs from a fresh kernel on a clean environment, documented |

A laboratory scoring 1 on *Correctness* is returned unmarked. Everything else can be discussed.

## Claim discipline

One criterion appears in every technical instrument, because it does more pedagogical work than any other:

!!! quote "Claim discipline"

    **Exemplary:** every quantitative claim has a stated measurement method, sample size or seed, and a stated limitation.

    **Proficient:** claims are measured and reproducible, though limitations are implicit.

    **Developing:** results are reported without denominators, or a defence is declared effective without an adaptive test.

    **Emerging:** conclusions rest on one run, one seed, or an unstated assumption.

The reason is simple. The difference between an AI security engineer and an AI enthusiast is not knowledge of attacks — it is the habit of asking *how would I know this is true, and what would make it false?*

## Progression gates

Progression between parts is gated on evidence, not exposure. In self-study mode you assess yourself against the gate; the standard does not change.

| Gate | After | Requirement |
|---|---|---|
| G-0 | Orientation | Your environment check passes and a trivial model trains |
| G-1 | Module 03 | Quiz 3 ≥ 70 % and a threat register accepted against the rubric |
| G-2 | Module 06 | Lab 05 and Lab 06 reports accepted |
| G-3 | Module 08 | Lab 07 and Lab 08 reports accepted |
| G-4 | Module 12 | One major project accepted against the major-project rubric |
| G-5 | Module 19 | Red-team report and incident playbook accepted |

A failed gate means repeating the laboratory with feedback, not abandoning the course. Gates exist because Level 3 assumes capability, and a student without it will spend three times as long on Module 12 as on the revision they skipped.

## Academic integrity

The published course is a learning resource; graded work must be your own.

- **Quiz, level and final answers are published** under [answer keys](../quizzes/answers/index.md), because a self-study course with hidden keys is unusable. Reading a key before attempting the item defeats the only purpose the item has; the attempt is what is graded, and in a self-study setting only you can enforce that.
- **Laboratory results are traceable.** Every lab records a seed, an environment fingerprint and, in several cases, a per-student data split. A copied results table will not match the run.
- **Written work is checked for authorship** by your institution, not by this course.

If you are studying alone, integrity is simpler: the only person you can cheat is the one who needs the skill in eighteen months.

## Self-assessment without an instructor

If nobody is marking your work, mark it yourself — but do it properly:

1. **Write the rubric criteria down before you start.** Knowing that *Measurement* is worth a quarter of the mark changes how you work.
2. **Score yourself a day later**, not immediately. Immediate self-marking is generous.
3. **Find the weakest criterion and redo only that part.** This is faster than redoing the whole lab.
4. **Keep a portfolio.** Thirty-two laboratory reports and a capstone, honestly marked, are more convincing to an employer than a certificate.

## Next

<div class="sas-grid sas-grid--3" markdown>

<div class="sas-card" markdown>
<div class="sas-card__title">Learning roadmap</div>
The pathway, checkpoints and progress tracking in one place.

[Continue →](../roadmap.md)
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Quizzes</div>
Twenty module quizzes, four level papers and a final, all with public keys.

[Continue →](../quizzes/index.md)
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Capstone</div>
The final assessment: scope, milestones and public rubric.

[Continue →](../capstone/index.md)
</div>

</div>
