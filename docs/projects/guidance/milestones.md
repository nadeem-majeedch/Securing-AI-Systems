---
title: Milestones and checkpoints
description: The gates every project passes through, what each must produce, and how to tell you are actually at the next one.
hide:
  - toc
---

# Milestones and checkpoints

Projects fail in predictable places. These gates exist because each of them catches a failure that is cheap to fix
at the gate and expensive to fix at the end.

A **milestone** is a submission someone else could review. A **checkpoint** is a smaller self-check inside it. The
rule for both: if you cannot point at an artefact, you are not at the milestone.

## The five milestones

| # | Milestone | Question it answers | Artefact | Gate condition |
|---|---|---|---|---|
| **M1** | Scope and threat model | What are we protecting, from whom, and what is out of scope? | Scope note, asset table, threat table, acceptance criteria | Accepted **before** implementation begins |
| **M2** | Working skeleton | Does the system run end to end, without security claims? | Runnable code, baseline numbers, configuration record | Happy path reproducible from a clean checkout |
| **M3** | Controls and deny paths | Do the controls refuse what they should? | Policy code, negative tests, audit rows | Every control has a test that must fail without it |
| **M4** | Adversarial measurement | What does the control buy, and what does it cost? | Before/after table, control condition, adaptive attempt | Numbers with seeds and denominators |
| **M5** | Argument and handover | Would someone else trust and operate this? | Security argument, runbook, limitation | A reader can start, attack and roll back the system |

## Mini projects: five checkpoints in ten hours

| Checkpoint | Hours | Self-check |
|---|---|---|
| C1 Threat model | 1 | Can you name the adversary's access in one sentence? |
| C2 Core mechanism | 3 | Does the mechanism work on a clean input, and fail visibly on a bad one? |
| C3 Measurement | 3 | Is there a number with a denominator, and a benign comparison? |
| C4 Tests | 2 | Do your tests survive a fresh checkout, and does one of them fail if you remove the control? |
| C5 Decision and limitation | 1 | Does the decision name a trade-off, and the limitation name a test? |

If C2 takes more than four hours, the project is too large for its scope or the environment is fighting you. Cut the
scope, not the measurement.

## Major projects: the same five, with more evidence

| Milestone | Hours | Evidence that must exist at the gate |
|---|---|---|
| M1 | 4 | Asset table, at least eight threats, one exclusion with a stated cost |
| M2 | 7 | Baseline metrics, configuration record, one command to run |
| M3 | 8 | Deny-path tests (at least six), audit trail, policy engine tests |
| M4 | 4 | One attack run before and after a control, with a control condition |
| M5 | 2 | Claim-to-evidence table, runbook, rollback demonstrated, weakest assumption named |

M1 is a hard gate. Work submitted with a scope written after the implementation is marked on the scope criterion as
if it were absent, because the evidence it would have produced does not exist.

## Capstone: five milestones over sixty hours

The capstone adds authorisation and remediation to the same pattern. See the
[capstone page](../../capstone/index.md#milestones) for the hour allocation, and remember that M1 (proposal and
scope) must be accepted before testing starts.

## A twelve-week cadence

For a student working alongside the modules, one mini project per fortnight and one major project per level set is
realistic:

| Weeks | Project work | Module work |
|---|---|---|
| 1–2 | MP01 (integrity) | Modules 05, 15 |
| 3–4 | MP02 (robustness) | Modules 06, 08 |
| 5–6 | MP03 (poisoning) | Module 07 |
| 7–8 | MP04 (privacy) | Module 09 |
| 9–10 | MP05 (API) | Modules 03, 16 |
| 11–14 | **P1 (pipeline)** | Modules 15, 20 |
| 15–16 | MP06 (injection) | Modules 11, 12 |
| 17–18 | MP07 (RAG ACL) | Module 13 |
| 19–20 | MP08 (agent policy) | Module 14 |
| 21–24 | **P3 or P4** | Modules 12–14 |
| 25–26 | MP09 (supply chain) | Module 15 |
| 27–28 | MP10 (monitoring) | Module 18 |
| 29–36 | **Capstone** | Module 19, 20 |

Two major projects and the capstone is the recommended load. Three major projects is possible; six is not, and
attempting six produces six unfinished systems.

## Weekly rhythm

A project that only advances at weekends stalls at M2. Thirty minutes, four times a week, is enough:

- **Monday:** read the milestone's gate condition; write down the one artefact that would satisfy it.
- **Wednesday:** build; keep a running `NOTES.md` with decisions and their reasons.
- **Friday:** test; if a test cannot fail, it is not a test.
- **Sunday:** update the decision log and the limitation list. Ten minutes.

## What to do when stuck

Almost every stall is one of five things, and each has a specific move:

| Symptom | Likely cause | Move |
|---|---|---|
| Cannot start | The threat model is vague | Write the adversary's access in one sentence, then the asset they want |
| Code runs, nothing to measure | No baseline | Record the system's behaviour *without* the control, on the same inputs |
| Measurement looks wrong | Configuration not recorded | Fix the seed and the model version, rerun, compare |
| Controls seem to work everywhere | Tests cannot fail | Remove the control and confirm the test fails |
| Report will not come together | Decision never written | Write the decision in three sentences, then attach evidence to it |

## Review checklist before submitting

- [ ] Scope note names one exclusion and what it cost.
- [ ] Threat table has an enforcement point per row.
- [ ] Every control has a test that fails without it.
- [ ] At least one measurement has a benign comparison.
- [ ] Seeds, versions and commands are in the repository, not in your head.
- [ ] The report's first page contains the decision.
- [ ] The limitation names a test that would settle it.
- [ ] No secret, token or personal record appears anywhere in the submission.

That last item has failed more projects than any technical criterion. Check it by grepping, not by memory.
