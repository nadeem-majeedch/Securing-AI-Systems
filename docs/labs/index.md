---
title: Practical Labs
description: The thirty-two laboratories of Securing AI Systems — what each builds, which module it belongs to, and how long it takes.
hide:
  - toc
---

# Practical Labs

Thirty-two laboratories across the twenty modules, one or two per module. Each builds one capability, states numeric success criteria you can check yourself, and ends with a results table you fill in. Every laboratory ships with a starter script and a separate reference solution under `labs/`.

A laboratory you cannot report is a laboratory you did not do. That is why every one of them asks for evidence rather than a feeling.

## What a lab contains

Every laboratory follows the same structure, so you spend your attention on the problem rather than on finding your place:

| Section | What it gives you |
|---|---|
| **Scenario** | The situation and why it matters |
| **Problem statement** | What you build, in one paragraph |
| **Learning objectives** | The capability you gain here |
| **Prerequisites** | The module reading and earlier labs you need |
| **Required software** | Exact packages and versions, standard library where possible |
| **Dataset and input files** | What the files are and how to regenerate them |
| **Detailed instructions** | Ordered tasks with checkpoints |
| **Python implementation** | The walkthrough that produces the evidence |
| **Expected results** | Numbers you can verify, not adjectives |
| **Interpretation** | What the numbers mean and what they do not |
| **Student tasks** | What you extend or repeat yourself |
| **Challenge exercises** | Harder variants for a stronger portfolio |
| **Hints** | Progressive nudges before the solution |
| **Solution** | A separate reference implementation and write-up |
| **Troubleshooting** | The two or three failures students actually hit |
| **Security lessons** | The defensive principle the lab demonstrates |
| **Submission** | What to hand in and how it is marked |
| **Acceptable use** | What this lab may be run against, and what it may never touch |
| **Scope restrictions** | The specific targets and techniques that are out of bounds here |
| **Data handling** | What the data is, why it is synthetic, and how to keep it |
| **Cleanup** | The files and processes this lab creates, and how to remove them |
| **Restoring your environment** | What was installed or started, and how to get back to clean |

## The catalogue

Every laboratory listed here is released and runnable: `labs/student/Lxx/` holds the brief and starter script, `labs/solutions/Lxx/` the reference solution. Budgets are for a four-core laptop CPU with no GPU.

| # | Laboratory | Module | Difficulty | Budget |
|---|---|---|---|---|
| 01 | Auditing the security properties of a clinical triage assistant | [01](../modules/01-introduction.md) | Beginner | 45 minutes |
| 02 | Baseline fraud model: metrics, calibration and confident errors | [02](../modules/02-ml-security-fundamentals.md) | Beginner | 60 minutes |
| 03 | Dataset integrity: hash manifests, tamper detection and MACs | [03](../modules/03-cybersecurity-fundamentals.md) | Beginner | 45 minutes |
| 04 | Least privilege for an analytics platform | [03](../modules/03-cybersecurity-fundamentals.md) | Intermediate | 60 minutes |
| 05 | Threat modelling and risk ranking for a hospital summariser | [04](../modules/04-threat-modeling.md) | Beginner | 50 minutes |
| 06 | Intake validation and quarantine for a dirty referral feed | [05](../modules/05-secure-data-management.md) | Beginner | 50 minutes |
| 07 | De-identification and linkage risk in a patient extract | [05](../modules/05-secure-data-management.md) | Intermediate | 70 minutes |
| 08 | Adversarial perturbations against a digit classifier | [06](../modules/06-adversarial-ml.md) | Intermediate | 80 minutes |
| 09 | Transfer attacks and the price of a black-box query | [06](../modules/06-adversarial-ml.md) | Advanced | 90 minutes |
| 10 | Poisoning a fraud model with flipped labels | [07](../modules/07-data-poisoning.md) | Intermediate | 75 minutes |
| 11 | Finding a backdoor: data scan and ablation audit | [07](../modules/07-data-poisoning.md) | Advanced | 80 minutes |
| 12 | PGD, projection and an honest robustness number | [08](../modules/08-evasion-and-robustness.md) | Advanced | 90 minutes |
| 13 | Two defences, two promises: adversarial training and a certificate | [08](../modules/08-evasion-and-robustness.md) | Challenge | 120 minutes |
| 14 | Membership inference: measuring what a model remembers | [09](../modules/09-model-privacy.md) | Intermediate | 70 minutes |
| 15 | Attribute inference and model inversion on applicant data | [09](../modules/09-model-privacy.md) | Advanced | 80 minutes |
| 16 | Extraction from a mock admissions API | [10](../modules/10-model-extraction.md) | Intermediate | 80 minutes |
| 17 | Tokens, context budget and the flat prompt | [11](../modules/11-llm-security.md) | Beginner | 50 minutes |
| 18 | Decoding determinism and the replayable incident | [11](../modules/11-llm-security.md) | Intermediate | 60 minutes |
| 19 | Direct prompt injection against a mock assistant | [12](../modules/12-prompt-injection.md) | Beginner | 55 minutes |
| 20 | A jailbreak detector and the base-rate problem | [12](../modules/12-prompt-injection.md) | Intermediate | 70 minutes |
| 21 | RAG retrieval that leaks one document | [13](../modules/13-rag-security.md) | Intermediate | 70 minutes |
| 22 | An ACL test suite for a RAG index | [13](../modules/13-rag-security.md) | Advanced | 80 minutes |
| 23 | Authorising an AI agent's tool calls | [14](../modules/14-agent-security.md) | Intermediate | 75 minutes |
| 24 | A malicious dependency and a tampered model bundle | [15](../modules/15-fine-tuning-supply-chain.md) | Beginner | 60 minutes |
| 25 | A poisoned fine-tuning run and the pattern scan | [16](../modules/16-secure-ai-apis.md) | Advanced | 85 minutes |
| 26 | An insecure prediction API and its hardened twin | [16](../modules/16-secure-ai-apis.md) | Beginner | 55 minutes |
| 27 | Rate limits and abuse controls on a prediction API | [17](../modules/17-red-teaming.md) | Intermediate | 70 minutes |
| 28 | A red-team matrix and a coverage statement | [18](../modules/18-monitoring-and-response.md) | Advanced | 90 minutes |
| 29 | Triaging suspicious usage in an AI service | [17](../modules/17-red-teaming.md) | Intermediate | 65 minutes |
| 30 | Recovering from a compromised model | [19](../modules/19-governance-and-ethics.md) | Challenge | 100 minutes |
| 31 | Fairness evaluation and a mitigation that only half-works | [19](../modules/19-governance-and-ethics.md) | Intermediate | 75 minutes |
| 32 | A release gate that reads evidence | [20](../modules/20-deployment-and-capstone.md) | Challenge | 110 minutes |

## Notebooks

Every laboratory ships as a Jupyter notebook. These are the versions the course was written against: download the ones for the module you are working on, open them in Jupyter, and run from a fresh kernel.

The notebooks ship with the outputs produced when the course was built, all regenerated on a CPU-only machine for this audit; they make no network calls and use no API keys. If a number differs from the text, check the seed and the library versions before assuming the notebook is wrong.

| Module | Notebook files |
|---|---|
| 01 | [01-security-concepts.ipynb](../notebooks/M01/01-security-concepts.ipynb) |
| 02 | [01-training-and-evaluation.ipynb](../notebooks/M02/01-training-and-evaluation.ipynb) · [02-failure-modes.ipynb](../notebooks/M02/02-failure-modes.ipynb) |
| 03 | [01-hashing-and-integrity.ipynb](../notebooks/M03/01-hashing-and-integrity.ipynb) · [02-access-control-and-secrets.ipynb](../notebooks/M03/02-access-control-and-secrets.ipynb) |
| 04 | [01-threat-model-and-risk.ipynb](../notebooks/M04/01-threat-model-and-risk.ipynb) |
| 05 | [01-secure-dataset-handling.ipynb](../notebooks/M05/01-secure-dataset-handling.ipynb) · [02-validation-and-anomalies.ipynb](../notebooks/M05/02-validation-and-anomalies.ipynb) · [03-deidentification-and-linkage.ipynb](../notebooks/M05/03-deidentification-and-linkage.ipynb) |
| 06 | [01-adversarial-examples.ipynb](../notebooks/M06/01-adversarial-examples.ipynb) · [02-adversary-models-and-budgets.ipynb](../notebooks/M06/02-adversary-models-and-budgets.ipynb) |
| 07 | [01-data-poisoning.ipynb](../notebooks/M07/01-data-poisoning.ipynb) · [02-backdoor-toy-model.ipynb](../notebooks/M07/02-backdoor-toy-model.ipynb) |
| 08 | [01-pgd-and-robust-evaluation.ipynb](../notebooks/M08/01-pgd-and-robust-evaluation.ipynb) · [02-adversarial-training-and-certification.ipynb](../notebooks/M08/02-adversarial-training-and-certification.ipynb) |
| 09 | [01-membership-inference.ipynb](../notebooks/M09/01-membership-inference.ipynb) · [02-inversion-and-attribute-inference.ipynb](../notebooks/M09/02-inversion-and-attribute-inference.ipynb) |
| 10 | [01-model-extraction.ipynb](../notebooks/M10/01-model-extraction.ipynb) |
| 11 | [01-tokens-and-context.ipynb](../notebooks/M11/01-tokens-and-context.ipynb) · [02-decoding-and-reproducibility.ipynb](../notebooks/M11/02-decoding-and-reproducibility.ipynb) |
| 12 | [01-prompt-injection.ipynb](../notebooks/M12/01-prompt-injection.ipynb) · [02-jailbreak-detection-and-mitigation.ipynb](../notebooks/M12/02-jailbreak-detection-and-mitigation.ipynb) |
| 13 | [01-secure-rag.ipynb](../notebooks/M13/01-secure-rag.ipynb) · [02-retrieval-access-control-tests.ipynb](../notebooks/M13/02-retrieval-access-control-tests.ipynb) |
| 14 | [01-agent-tool-authorisation.ipynb](../notebooks/M14/01-agent-tool-authorisation.ipynb) |
| 15 | [01-artefact-integrity.ipynb](../notebooks/M15/01-artefact-integrity.ipynb) · [02-finetuning-poisoning.ipynb](../notebooks/M15/02-finetuning-poisoning.ipynb) |
| 16 | [01-input-validation.ipynb](../notebooks/M16/01-input-validation.ipynb) · [02-secure-fastapi-service.ipynb](../notebooks/M16/02-secure-fastapi-service.ipynb) |
| 17 | [01-red-team-matrix.ipynb](../notebooks/M17/01-red-team-matrix.ipynb) |
| 18 | [01-security-logging.ipynb](../notebooks/M18/01-security-logging.ipynb) · [02-incident-detection-and-recovery.ipynb](../notebooks/M18/02-incident-detection-and-recovery.ipynb) |
| 19 | [01-fairness-and-impact.ipynb](../notebooks/M19/01-fairness-and-impact.ipynb) |
| 20 | [01-release-gate.ipynb](../notebooks/M20/01-release-gate.ipynb) |

Notebooks are also linked from each module's overview card, next to its lab.

## The runtime rule

Every laboratory must complete inside its stated budget on a laptop CPU. That constraint shaped the labs: small datasets, small models, fixed seeds, no downloads for the core path, and no network access at all — the datasets are generated locally by `labs/scripts/make_datasets.py`.

If a lab exceeds its budget on your machine, the lab's troubleshooting note lists the two usual causes — an accidental GPU fallback to CPU with an oversized batch, or a stale notebook kernel holding an old model in memory.

## The lab log

Keep one log across the course. It is the raw material for your portfolio, and it is what makes a result reproducible six months later.

```text
Lab:            05 — Four-attack benchmark
Date:           2026-11-20
Environment:    Python 3.12.7, torch 2.5.1 (CPU), ART 1.19.0
Seed:           42
Dataset:        supplied subset, 5,000 images, checksum verified

Attack      | ASR   | mean L-inf | queries | seconds
FGSM        | 0.41  | 0.031      | 1       | 2.1
PGD-20      | 0.93  | 0.031      | 20      | 41.0
C&W L2      | 0.97  | 0.019 (L2) | 500     | 96.4
Decision    | 0.78  | n/a        | 1,842   | 210.0

Surprise:   PGD needed 40 iterations, not 20, to pass 0.90 ASR.
Question:   does the pattern hold at 16/255? (next: MP1)
```

## Marking

Laboratories are marked against the [five-criterion rubric](../getting-started/assessment.md#how-laboratories-are-marked), with claim discipline applied throughout. A lab scoring *Emerging* on correctness is returned unmarked — not to punish, but because a result that cannot be reproduced cannot be discussed.

## Safety

Every offensive laboratory states its acceptable-use boundary at the top. All targets are synthetic or supplied inside the sandbox. Nothing here authorises testing a system you do not own or have written permission to test.

If you are unsure whether something is in scope, it is not in scope.
