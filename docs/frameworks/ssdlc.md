---
title: Secure software development (SSDF)
description: NIST SP 800-218 and its generative-AI profile — the practices that make a pipeline produce evidence, not promises.
---

# Secure software development: the SSDF

## What it is

The **Secure Software Development Framework (SSDF)**, NIST SP 800-218 version 1.1 (February 2022), is a set of
secure-development practices organised into four groups. It is deliberately technology-neutral and outcome-oriented:
each practice says what a secure development programme does, not which tool to buy.

| Group | Concern | Examples of practices |
|---|---|---|
| **PO — Prepare the Organization** | Roles, policy, toolchains, training, secure development environments | Define security requirements; protect the build environment; provide role-based training |
| **PS — Protect the Software** | Protect code, releases and configuration from tampering | Protect all components from tampering; archive releases with integrity evidence |
| **PW — Produce Well-Secured Software** | Design, code, build and review securely | Review design against security requirements; configure compile-time protections; test executable code; review code for secure coding |
| **RV — Respond to Vulnerabilities** | Find, triage and fix vulnerabilities, and prevent recurrence | Identify residual vulnerabilities; assess, prioritise and remediate; root-cause analysis |

The **generative-AI community profile**, NIST SP 800-218A (July 2024), augments SSDF 1.1 for systems that train,
fine-tune or integrate generative models. It adds practices around model and data provenance, training-data
handling, model evaluation, and the AI-specific parts of the supply chain.

!!! note "Version status"

    SSDF 1.1 (SP 800-218, February 2022) is the current final version this course cites. NIST has published a draft
    revision (SP 800-218r1 initial public draft, December 2025); drafts are not final and should not be cited as
    current requirements. SP 800-218A is a final community profile that augments 1.1.

## Why it matters

Every AI security failure in the [case studies](../case-studies/index.md) has a development-process component: a
dependency installed by name, an artefact loaded by tag, a token with more scope than the build needed, a release
that shipped with a payload in it. The SSDF is the framework that turns those into practices with evidence.

It also solves a practical problem for this course: it tells you **what a release gate should require**. A gate is
only real if a practice produced an artefact the gate can check.

## When it is used

- Establishing or reviewing a development lifecycle, especially for pipelines that produce models.
- Responding to procurement questionnaires that ask about secure development (increasingly common for AI vendors).
- Designing CI/CD gates: each gate maps to a practice and checks its evidence.
- Post-incident: RV practices are where "the fix prevents recurrence" is decided rather than asserted.

## How to apply it to an AI pipeline

| Pipeline stage | SSDF practice area | Evidence the gate can check |
|---|---|---|
| Requirements | PO: define security requirements | A requirement list with test IDs |
| Dependencies | PS/PW: protect components, verify integrity | Lockfile with hashes; allowlisted sources; SBOM |
| Data ingestion | 800-218A: training-data provenance and handling | Dataset manifest with digests; supplier record |
| Model build | PW: build with integrity evidence | Reproducible build record; artefact digest |
| Evaluation | PW: test executable code; 800-218A: model evaluation | Attack suite results; canary-set results; thresholds |
| Release | PS: archive releases with integrity evidence | Signed manifest plus an independently held root |
| Deployment | PW/PS: configuration and environment protection | Serving loads by digest; secrets from environment; non-root |
| Operations | RV: identify, assess, remediate vulnerabilities | Monitoring signals; incident records; root-cause changes |

Read that table as a specification for [P1](../projects/major/p01-secure-ml-pipeline.md): it is exactly the evidence
its gates are supposed to require.

## The four practices most often missing in student work

1. **Protecting the build environment.** A CI job with a broad token can be turned into a supply-chain attack — see
   the [Amazon Q Developer case](../case-studies/c09-amazon-q-supply-chain.md). Scope the token to the repository and
   the branch it needs.
2. **Verifying components by digest, not by name.** Tags and package names are mutable. The
   [torchtriton case](../case-studies/c03-torchtriton-dependency-confusion.md) is a fifteen-minute read that makes
   this permanent.
3. **Archiving releases with integrity evidence.** If you cannot prove what you shipped, you cannot investigate an
   incident that starts six weeks later.
4. **Root-cause analysis that changes a control.** "Add the payload to the blocklist" is not a root-cause fix; the
   [capstone rubric](../capstone/index.md#public-rubric) marks remediation on whether the control changed.

## Worked example: a release gate

A student's gate for a fine-tuned model, written as SSDF-mapped checks:

| Check | SSDF hook | Failure mode it blocks |
|---|---|---|
| Lockfile hashes match the allowlisted set | PS | A dependency substituted at install time |
| Dataset manifest verifies against supplier root | 800-218A | A re-delivered dataset with altered rows |
| Evaluation suite passes thresholds on a pinned holdout | PW | A model that regressed on the canary slice |
| Artefact digest matches the signed manifest | PS | A substituted or corrupted weight file |
| Serving config has no plaintext credential | PO/PS | A secret in an image or repository |
| Rollback to the previous digest is tested | RV | An unrecoverable release |

Six checks, each with a named failure mode and an owner. That is a release gate; the rest is YAML.

## Limitations to state

- The SSDF is a practices framework, not a certification. It does not audit your code or your model.
- It is voluntary US guidance; contracts may require it, law does not (by itself).
- 800-218A is a community profile: useful and final, but not exhaustive for agentic systems, which are still moving
  faster than the guidance.
- It says little about *behavioural* security of a model (poisoning, backdoors) beyond provenance and evaluation
  practices; pair it with [AI 100-2](nist-aml.md).

## Where it appears in this course

[Module 15](../modules/15-fine-tuning-supply-chain.md) (supply chain and artefact integrity),
[Module 20](../modules/20-deployment-and-capstone.md) (release gates), the
[P1 pipeline project](../projects/major/p01-secure-ml-pipeline.md), and the
[MP09 integrity checker](../projects/mini/mp09-supply-chain-checker.md).

## Sources

1. NIST, *Secure Software Development Framework (SSDF) Version 1.1: Recommendations for Mitigating the Risk of
   Software Vulnerabilities*, NIST SP 800-218, February 2022.
   <https://csrc.nist.gov/pubs/sp/800/218/final>
2. NIST, *Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An SSDF Community
   Profile*, NIST SP 800-218A, July 2024. <https://csrc.nist.gov/pubs/sp/800/218/a/final>
3. NIST, *SP 800-218r1 initial public draft* (December 2025) — draft revision, not final.
   <https://csrc.nist.gov/pubs/sp/800/218/r1/ipd>
4. Ohm, M., Plate, H., Sykosch, A. and Meier, M., "Backstabber's Knife Collection: A Review of Open Source Software
   Supply Chain Attacks", *DIMVA 2020*. <https://doi.org/10.1007/978-3-030-52683-2_2>
