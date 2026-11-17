---
title: A1 · Threat model for a hospital AI application
description: Assignment 1 — produce a threat register and an executive brief for a clinical summarisation assistant.
---

# A1 · Threat model for a hospital AI application

**After:** Module 04 · **Weight:** 10 % of the assignment component · **Length:** 1,200 words plus a register
**Deliverable:** A threat register (CSV or table) and a 400-word brief for a non-technical clinical director

## Scenario

St Mary's NHS-style trust is piloting an assistant that reads electronic referrals and drafts a summary for the
receiving clinician. It retrieves relevant past letters from a shared index, can request a translation, and can
page the on-call registrar. The pilot covers two wards; the index holds letters from six.

The clinical director will approve or reject the pilot in ten working days. She has no security background and has
been told by the vendor that the system "uses a large language model with safety guardrails". She has one
question: *what could go wrong for a patient, and what are you doing about it?*

## Problem statement

Produce a threat model that a clinician can act on. The register must be technically defensible; the brief must
be decidable by someone who will not read the register.

## Requirements

1. A data-flow description with **explicit trust boundaries**, including the index, the paging system and the
   referral source. A diagram is welcome but a numbered boundary list is acceptable.
2. **At least twelve threats**, each mapped to a STRIDE or LINDDUN category, with likelihood (1–5), impact (1–5)
   and a one-paragraph justification for both numbers.
3. Each threat must name a **control that exists or is proposed**, and the **residual risk** after that control.
4. Separate **patient-safety consequences** from organisational consequences (data protection, reputational,
   financial). A reader must be able to see which rows could harm a patient.
5. The executive brief must contain: the three risks that matter, the decision you want, the residual you are
   asking her to accept, and the monitoring that would tell you if you were wrong.
6. Every quantitative claim must state its basis. "High likelihood" without a reason is not acceptable.

## Tasks

1. List the assets and the trust boundaries. Justify why the index is a boundary rather than an internal store.
2. Enumerate threats from the boundaries outward, not from the controls inward.
3. Score likelihood and impact, and record the assumption behind each score in one sentence.
4. Identify which threats are **not** mitigated by the vendor's guardrail claim, and say why in one line each.
5. Write the 400-word brief, then cut it by 20 %. The cut is part of the exercise.
6. Add a one-page appendix listing what you did **not** assess, and why.

## Deliverables

| Item | Format | Length |
|---|---|---|
| Threat register | table/CSV with columns: id, asset, boundary, category, threat, likelihood, impact, justification, control, residual | 12+ rows |
| Data-flow description | numbered boundary list or diagram | 1 page |
| Executive brief | prose for a clinical director | 400 words |
| Limitations appendix | bullet list | 1 page |

## Evaluation criteria

- **Boundary analysis:** are the boundaries the right ones, and is the index treated as untrusted?
- **Threat quality:** are threats specific to this system, or generic AI risks copied from a list?
- **Evidence discipline:** does each score have a stated basis, and is the residual honest?
- **Decision usefulness:** could the clinical director decide after reading only the brief?

## Rubric

| Criterion | 1 — Emerging | 2 — Developing | 3 — Proficient | 4 — Exemplary |
|---|---|---|---|---|
| Boundary analysis | Components listed, no boundaries | Boundaries drawn but the index treated as internal | Boundaries justified, including retrieval and tools | Boundaries justified, and the assumption that would move one is stated |
| Threat specificity | Generic AI risks | Some system-specific threats | Threats tied to this workflow and these assets | Threats include the clinical failure path, not only the data path |
| Scoring | Numbers without basis | Basis for some scores | Basis for every score | Scores attached to assumptions that could be tested |
| Brief | Technical summary | Understandable but unstructured | Decideable, with the ask stated | A reader could approve or reject without asking a question |

## Extension challenges

1. Add an attack tree for "wrong patient receives a summary" and identify a single cut that breaks three paths.
2. Model the paging tool's failure modes as a separate mini-model, including the human process around it.
3. Re-score the register for a deployment that serves one ward and no paging capability, and explain which rows
   change and by how much.

## Constraints

Work only from the described scenario. Do not contact the trust, do not test any real system, and replace any
real organisation or patient detail with a fictional equivalent before sharing your work.
