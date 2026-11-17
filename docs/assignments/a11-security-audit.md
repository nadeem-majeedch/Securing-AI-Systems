---
title: A11 · AI application security audit
description: Assignment 11 — audit a deployed assistant end to end and produce findings with evidence and owners.
---

# A11 · AI application security audit

**After:** Module 17 · **Weight:** 10 % · **Length:** 1,200 words plus an evidence pack
**Deliverable:** An audit report with findings, severity, evidence, and a retest plan

## Scenario

You have been engaged by a university to audit a student-facing assistant that answers questions about courses,
retrieves from a policy library, and can open a support ticket on the student's behalf. It has been live for six
months and has never been assessed.

The engagement is five days. The rules of engagement permit testing of a staging instance with two test accounts.
They forbid denial-of-service testing, any access to real student records, and any outbound email.

## Problem statement

Run a scoped audit that produces findings the university can fix, and a statement of what you did not cover.

## Requirements

1. A **scope and method** section: systems, accounts, threat families, techniques and limits.
2. A **coverage matrix** of threat family by component, with each cell marked tested, out of scope or not reached.
3. **Findings** in a fixed format: title, evidence, impact, reproduction, severity with justification, control,
   owner.
4. At least one finding must come from **indirect** content rather than a direct request.
5. A **retest plan** naming the exact tests that would close each finding.
6. A **limitations** section a reader can use to judge the assurance value of the audit.

## Tasks

1. Write the scope and method before testing, and record it unchanged in the report.
2. Build the coverage matrix; mark every cell, including the ones you did not reach.
3. Test the boundary: authentication, tenant scoping, error handling, and the ticket-creation capability.
4. Place an instruction in an authorised document in staging and observe whether the assistant follows it.
5. Assign severity from impact and exploitability, and record the assumption behind each rating.
6. Write the retest plan and the limitations section.

## Deliverables

| Item | Format | Length |
|---|---|---|
| Audit report | sections as specified | 1,000 words |
| Coverage matrix | threat × component | 1 page |
| Findings | fixed format, 4+ findings | 1 page each |
| Retest plan | test, expected result, owner | 1 page |

## Evaluation criteria

- **Method discipline:** was the scope written before testing, and is the matrix complete including gaps?
- **Evidence quality:** can each finding be reproduced from the report alone?
- **Severity reasoning:** is severity tied to impact and reachability in this deployment?
- **Honesty:** does the limitations section bound the assurance claim?

## Rubric

| Criterion | 1 — Emerging | 2 — Developing | 3 — Proficient | 4 — Exemplary |
|---|---|---|---|---|
| Method discipline | Ad hoc testing | Scope written after | Scope and matrix present | Matrix distinguishes untested from not-reached |
| Evidence quality | Screenshot only | Steps described | Reproducible steps with configuration | Reproducible, with the model and sampler recorded |
| Severity reasoning | All high | Impact only | Impact and exploitability | Plus the assumption that would change the rating |
| Honesty | "No other issues" | Brief caveat | Limitations listed | Limitations and their effect on the assurance claim |

## Extension challenges

1. Add a finding about the ticket tool's argument validation and propose the policy change.
2. Estimate the engineering effort for each remediation and reorder the findings by risk reduced per day.
3. Design a quarterly regression suite from your findings.

## Constraints

Test only the staging instance described, with the two accounts, and only within the stated rules of engagement.
Do not attempt to access real student data, and stop and notify if an action affects a real person.
