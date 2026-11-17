---
title: A10 · AI supply chain security assessment
description: Assignment 10 — audit a fine-tuning pipeline's dependencies, artefacts and provenance.
---

# A10 · AI supply chain security assessment

**After:** Module 15 · **Weight:** 10 % · **Length:** 900 words plus audit output
**Deliverable:** A supply-chain assessment with an artefact verification procedure and a release gate

## Scenario

A media company fine-tunes an open-weight model on its archive to auto-tag footage. The pipeline pulls a base
model by name from a public hub, installs dependencies from a `requirements.txt` that includes two Git URLs, and
publishes the tuned weights to an internal registry with a tag.

A partner will consume the tuned model through an API. The partner's security team has sent a questionnaire that
asks, among other things, "how do you verify the integrity of the model you deploy?"

## Problem statement

Assess the pipeline as a supply chain, identify the points where an artefact could be substituted, and design the
verification and gates that would let you answer the partner's question with evidence.

## Requirements

1. A **component inventory** with, for each component: source, version or digest, trust decision and owner.
2. A **substitution analysis**: for each component, what an attacker would need and what they would gain.
3. A **verification procedure** covering artefact hashing, manifest trust, format restrictions and behavioural
   checks.
4. A **release gate** with at least four checks, each with a failure mode.
5. An answer to the partner's question in 200 words, citing the procedure rather than asserting confidence.

## Tasks

1. Build the inventory from the scenario and mark which entries are unpinned or unverified.
2. Analyse the two Git dependencies: what executes at install time, and in which identity.
3. Demonstrate artefact verification on the course's clean and tampered bundles, and report the difference.
4. Show what a manifest that travels inside the bundle cannot prove, and what replaces it.
5. Design the gate and state what it blocks, including the missing-evidence case.
6. Answer the partner, and list the two residual risks you would disclose.

## Deliverables

| Item | Format | Length |
|---|---|---|
| Component inventory | table with source, version, trust, owner | 1 page |
| Substitution analysis | per component: access, gain, control | 700 words |
| Verification procedure | steps with expected output | 1 page |
| Release gate | checks and failure modes | 1 page |
| Partner answer | 200 words | — |

## Evaluation criteria

- **Inventory completeness:** are base model, code, data, tokeniser and output artefact all present?
- **Access reasoning:** is the attacker's required access stated for each path?
- **Verification depth:** does the procedure distinguish identity from behaviour?
- **Disclosure:** are residual risks stated rather than implied?

## Rubric

| Criterion | 1 — Emerging | 2 — Developing | 3 — Proficient | 4 — Exemplary |
|---|---|---|---|---|
| Inventory | Lists packages only | Adds the model | Adds data and artefact | Adds owner and trust anchor for each |
| Access reasoning | "Could be malicious" | Access named for some | Named for each path | Ranked by ease and impact |
| Verification depth | Hash only | Hashes and format | Hashes, manifest trust, behaviour | Plus a probe set and a signature chain |
| Disclosure | None | One risk | Two risks with mitigation | Risks, mitigation and a review date |

## Extension challenges

1. Design the signing and key-distribution scheme for the internal registry, including rotation.
2. Add a dependency policy that permits an internal mirror without allowing direct Git installs.
3. Write the incident procedure for discovering that a deployed artefact's digest does not match.

## Constraints

Use the course's synthetic bundles. Do not download real model weights, and do not run untrusted code outside a
sandbox with no credentials.
