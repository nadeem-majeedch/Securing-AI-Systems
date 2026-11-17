---
title: "Level 1 assessment — Foundation — answer key"
description: "Answer key for level 1 assessment — foundation."
hide:
  - toc
---

# Level 1 assessment — Foundation — answer key

## Section A key

| # | Item | Answer | Type | Outcome |
|---|---|---|---|---|
| 1 | L1-Q01 | A | Recall | M01.1 |
| 2 | L1-Q02 | A | Application | M02.2 |
| 3 | L1-Q03 | A | Judgement | M03.1 |
| 4 | L1-Q04 | A | Application | M04.2 |
| 5 | L1-Q05 | A | Recall | M05.3 |
| 6 | L1-Q06 | A | Judgement | M04.3 |
| 7 | L1-Q07 | A | Application | M03.3 |
| 8 | L1-Q08 | A | Judgement | M05.5 |

## Section A explanations

**1. L1-Q01** — **A: The presence of an adversary choosing inputs**

Safety assumes expected use and accidents; security assumes someone adapting inputs to cause failure, which changes both the analysis and the evidence required.

- **B** — Dataset size matters to both reviews and does not distinguish them.
- **C** — Serving framework is an engineering detail.
- **D** — Hardware cost is unrelated to either analysis.

**2. L1-Q02** — **A: Leakage must be measured, because memorisation is likely**

Near-perfect fit on few records is the condition under which memorisation occurs, so a membership test is required rather than assumed unnecessary.

- **B** — Small datasets increase, not decrease, the risk per record.
- **C** — Differential privacy is a training guarantee, not a by-product of size.
- **D** — Extraction needs only query access.

**3. L1-Q03** — **A: The tenant must be derived from the token, not the body**

A caller-supplied tenant is an authorisation decision delegated to the attacker; the authenticated claim is the only trustworthy source.

- **B** — Signing is the correct primitive for integrity and identity.
- **C** — Compression is irrelevant to the flaw.
- **D** — Accepting unsigned tokens removes authentication entirely.

**4. L1-Q04** — **A: Elevation of privilege; remove the external send capability**

Following data-borne instructions grants content the operator's authority, and the durable fix is to remove or constrain the capability rather than to log it.

- **B** — Repudiation is about denying an action, not acquiring authority.
- **C** — Availability is not the threat here.
- **D** — No identity is being impersonated.

**5. L1-Q05** — **A: A bound on any single record's influence on outputs**

Differential privacy bounds per-record influence and composes across queries; k-anonymity hides a record within a group but fails on homogeneous groups.

- **B** — That is the definition of k-anonymity, not of DP.
- **C** — Removing quasi-identifiers is a preprocessing step in some methods.
- **D** — DP does not remove publication duties.

**6. L1-Q06** — **A: It gives the reader no basis for choosing what to fix first**

Prioritisation is the register's product; a uniform rating removes the analysis the reader needs to act.

- **B** — Critical is a common top level in many schemes.
- **C** — Sensitivity increases the need for modeling.
- **D** — Row count is not a rule.

**7. L1-Q07** — **A: The SHA-256 digest of the file, sent by a separate channel**

Integrity needs a digest compared against a value the receiver trusts independently; a key or password travelling with the data proves nothing.

- **B** — A key sent alongside the ciphertext provides no independent evidence.
- **C** — Encoding is reversible formatting.
- **D** — A password in the filename is disclosed with the archive.

**8. L1-Q08** — **A: Delete source rows, snapshots and derived artefacts, and assess the model's influence**

Erasure covers copies and derivatives, so the work is deletion plus an influence assessment, with retraining or unlearning where the residual is material.

- **B** — A source deletion does not remove snapshots or learned influence.
- **C** — Refusal is a legal position that is often wrong.
- **D** — Deleting the model is disproportionate and may not be required.

## Section B model answers

<div class="sas-answer"><p class="sas-item__head"><strong>L1-W1</strong> <span class="sas-meta">8 marks</span></p><p class="sas-answer__q">A hospital wants a triage assistant that reads referrals and can page a clinician. Identify four trust boundaries, one control for each, and the single control you would insist on before launch.</p><p class="sas-answer__label">Model answer</p><p>Boundaries: referral text into the model (control: treat as data, validate extracted fields against structured records); retrieval index to assistant (tenant and role filtering before ranking); assistant to paging system (allowlist of roles and on-call schedules, no free-text destinations); operator to index (provenance and review before ingestion). The control to insist on is that paging is constrained to the authenticated clinician's on-call group and requires confirmation, because an unauthorised page is an immediate clinical harm.</p></div>

<div class="sas-answer"><p class="sas-item__head"><strong>L1-W2</strong> <span class="sas-meta">8 marks</span></p><p class="sas-answer__q">A dataset drops names but keeps postcode, birth date and admission date. Explain the re-identification path and two controls, and state what residual risk remains.</p><p class="sas-answer__label">Model answer</p><p>The three fields are quasi-identifiers: joined against a voter roll or public directory they can single out individuals, and the join needs no name at all. Controls: generalise or suppress (postcode district, birth year, month of admission) with a measured k, and release aggregates or a differentially private summary instead of row-level data. Residual risk remains because generalisation reduces but does not eliminate linkage, and rare combinations persist; the release should therefore be treated as personal data with a documented assessment rather than as anonymised.</p></div>

<div class="sas-answer"><p class="sas-item__head"><strong>L1-W3</strong> <span class="sas-meta">9 marks</span></p><p class="sas-answer__q">Write the risk section of a review for a fraud model retrained nightly on merchant-reported labels. Name three risks, their evidence, and one measurable indicator for each.</p><p class="sas-answer__label">Model answer</p><p>Label poisoning: evidence is that the label source is external and unverified; indicator is the per-merchant label-flip rate against adjudication. Adversarial evasion: evidence is that decisions affect money and inputs are user-controlled; indicator is the detection rate on a held-out structuring probe set. Privacy leakage: evidence is high-capacity training on cardholder records; indicator is membership-inference advantage at a stated false-positive rate. Each indicator is measurable on a schedule, which is what makes the risk section operational rather than descriptive.</p></div>

