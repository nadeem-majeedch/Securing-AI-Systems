---
title: Project rubrics
description: The shared rubrics for mini projects, major projects and capstone proposals, with the indicators markers apply.
hide:
  - toc
---

# Project rubrics

Three rubrics cover the whole programme: one for mini projects, one for major projects, one for the capstone
proposal and its defence. Each brief adds two project-specific indicators on top; the criteria and weights below
never change.

Marking is on **evidence**, not effort. A project that runs but cannot be repeated scores lower than one that runs
slowly and states its conditions.

## Mini-project rubric

Ten hours, one artefact, one decision. Weights are percentages of the mini-project mark.

| Criterion | Weight | Emerging (1) | Developing (2) | Proficient (3) | Exemplary (4) |
|---|---|---|---|---|---|
| **Threat model** | 15 % | Absent, or a list of generic AI risks | Names an adversary but not their access | Adversary, access and goal stated, and used to choose the tests | Threat model drives a stated exclusion you would defend |
| **Method** | 25 % | Tool run with defaults; steps not reproducible | Steps described, one parameter unstated | Reproducible from the brief plus your notes: seeds, versions, commands | Reproducible, and a second method or control confirms the result |
| **Measurement** | 25 % | A number without a denominator | Numbers for one run | Numbers with sample size, seed and variance | Numbers with a control condition and an operating point |
| **Decision** | 20 % | "It works" | A recommendation without a trade-off | A recommendation that names what it gives up | A recommendation with the threshold or condition that would reverse it |
| **Honest limitation** | 15 % | None, or "results may vary" | One generic caveat | The specific reason the conclusion might be wrong | The limitation, plus the test that would settle it |

A mini project scoring 1 on **Measurement** is returned for rework. Everything else can be discussed.

## Major-project rubric

Twenty-five hours, an end-to-end system or study. Weights differ from the mini rubric because integration and
engineering quality now matter as much as the measurement.

| Criterion | Weight | Emerging (1) | Developing (2) | Proficient (3) | Exemplary (4) |
|---|---|---|---|---|---|
| **Scope and threat model** | 15 % | Scope retrofitted or unbounded | Scope stated, threats partly enumerated | Scope bounded, threats tied to components, exclusions justified | Scope used to make a real exclusion decision, with the cost of that decision stated |
| **Technical execution** | 30 % | Does not run, or runs only on the author's machine | Runs with manual fixes | Runs from a clean checkout with documented commands | Runs cleanly, and an adaptive attempt against your own control is included |
| **Measurement** | 20 % | Claims without numbers | Numbers for the happy path | Numbers with seeds, denominators and variance | Numbers with a control, an operating point and a stated base rate |
| **Engineering quality** | 15 % | Secrets in the repo, no tests | Some tests, configuration unclear | Tests for deny paths, configuration without secrets, a rollback path | Plus a working kill switch and a runbook someone else could follow |
| **Communication** | 15 % | Report unreadable by the intended reader | Structured but buries the decision | Decision up front, evidence behind it | A busy engineer could act after reading the first page |
| **Honest limitation** | 5 % | Claims completeness | Notes a caveat | Names the weakest part of the argument | Names it and says what evidence would change the conclusion |

## Capstone rubric

The capstone proposal and the capstone itself are marked on the same six criteria used on the
[capstone page](../../capstone/index.md#public-rubric): scope and authorisation, technical depth, evidence quality,
severity judgement, remediation, and the assurance argument. Weighting is 15 / 25 / 20 / 10 / 15 / 15.

The five proposals differ in domain, not in standard. Choosing a proposal does not change what counts as exemplary.

## How the two project-specific indicators work

Each brief lists two extra indicators with *Proficient* and *Exemplary* descriptors only. They are applied inside
the criterion they belong to — usually **Method** or **Measurement** — and they cannot raise a score above 4 or
lower it below 1. Their purpose is to stop a project from passing on general competence while missing the one
thing that project was designed to teach.

For example, MP01's **Failure taxonomy** indicator sits inside **Method**: a checker that reports "verification
failed" for both a modified file and a malformed manifest has not built the taxonomy the project is about.

## Claim discipline

One rule runs through every rubric, and it is the rule this course exists to teach:

!!! quote "The claim-discipline rule"

    Every quantitative claim states how it was measured, on what sample, and what it does not cover. A claim that
    cannot be checked is not a result.

In practice, a submission loses marks when it writes "the detector is 94 % accurate" without saying 94 % of what,
on how many records, at what prevalence, against which attack.

## Self-marking

1. Score each criterion before reading the project-specific indicators — they are refinements, not a rescue.
2. Choose the lower level when you hesitate. Self-marking inflates; that is why the descriptors are behavioural.
3. Rewrite only the weakest criterion, then re-score. Keeping both versions shows you what changed.
4. Record the score and the date. Twelve mini projects, honestly marked, are a portfolio with a trail.
