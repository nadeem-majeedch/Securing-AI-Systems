---
title: NIST adversarial machine learning taxonomy
description: AI 100-2e2025 — the vocabulary for attacker goals, capabilities and mitigations, and the 2023 edition it replaced.
---

# NIST adversarial machine learning taxonomy

## What it is

**NIST AI 100-2e2025**, *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*,
published March 2025, is the current edition of NIST's AML taxonomy. It supersedes the 2023 edition
(AI 100-2e2023). It defines a conceptual hierarchy — machine-learning method, life-cycle stage, attacker goals,
objectives, capabilities and knowledge — and pairs attack classes with mitigation approaches. A glossary makes the
vocabulary consistent with the research literature.

The report covers both **predictive AI** (classifiers, regressors) and **generative AI** (LLMs and multimodal
models), which is why it is the single most useful citation when a report needs to be precise about what kind of
attack it means.

## Why it matters

Most confused security writing about ML comes from vocabulary, not ignorance. Three distinctions the taxonomy
forces:

1. **Goal versus technique.** Evasion, poisoning and privacy attacks are goals; a norm-bounded perturbation or a
   poisoned label set is a technique. A defence that addresses a technique may not address the goal.
2. **Attacker knowledge and capability.** White-box, grey-box and black-box are not flavours of the same result;
   they define which attacks are feasible and which measurements are meaningful.
3. **Stage.** Training-time and inference-time attacks have different controls. A pipeline control cannot stop an
   inference-time evasion; an input filter cannot undo a poisoned training set.

## When it is used

- Writing a threat model or an evaluation report where terms must be unambiguous.
- Choosing an attack for a robustness test, and justifying why that attack and budget.
- Reviewing a vendor claim: "robust" against which goal, at what capability, measured how?
- Teaching and assessment: the course's own question bank uses the taxonomy's distinctions.

It is **voluntary guidance**, not a standard you certify against.

## Structure, in the form you will use it

| Dimension | Values you will actually choose between |
|---|---|
| ML method | Supervised classification, regression, clustering, reinforcement learning, generative |
| Life-cycle stage | Training (data collection, training, fine-tuning) / deployment (inference) |
| Attacker goal | Availability, integrity, privacy — and for generative systems, abuse of capability |
| Attacker objective | Targeted misclassification, untargeted error, backdoor activation, data reconstruction, model theft |
| Attacker capability | Training-data control, model access, query access, code execution, label control |
| Attacker knowledge | White-box, grey-box, black-box |

A complete statement therefore looks like: *"targeted misclassification (objective), integrity (goal), at inference
(stage), black-box query access with 500 queries (capability and knowledge), against a supervised classifier."*
That sentence tells a reader exactly what was and was not shown.

## The four classical families, and what each needs

| Family | Goal | Typical capability | What a defence must do |
|---|---|---|---|
| **Evasion** | Integrity | Query or input control | Reduce sensitivity in the region the attacker can reach |
| **Poisoning** | Integrity (and availability) | Training-data or label influence | Detect or bound influence; validate provenance |
| **Privacy** (membership inference, inversion, attribute inference) | Privacy | Query access, sometimes confidence values | Bound what outputs reveal; regularise; coarsen |
| **Extraction** | Integrity of IP and of pricing | Query access at scale | Raise the cost per unit of information; watermark |

Generative systems add abuse categories — prompt injection, jailbreaks, harmful-content elicitation, agent
tool abuse — where the "model" boundary is the wrong unit and the *application* is the thing to secure. That is the
bridge to the [OWASP list](owasp.md) and to [ATLAS](mitre-atlas.md).

## How to apply it

**Step 1 — write the attacker statement.** One sentence using the dimensions above. If you cannot fill in
capability and knowledge, you are not ready to measure.

**Step 2 — pick the family and the test.** Each family suggests a measurement: accuracy under a budget for evasion;
attack success rate at a poison rate for poisoning; TPR at a fixed FPR for membership inference; fidelity versus
query budget for extraction.

**Step 3 — name the mitigation class, then the control.** The taxonomy gives mitigation categories (for example
adversarial training, input validation, output perturbation, differential privacy, rate limiting). Your report needs
the specific control and its enforcement point.

**Step 4 — scope the claim.** "Robust to PGD at ε = 0.1 on this dataset" is a claim the taxonomy lets you state
precisely. "Robust" is not.

## Version discipline

| Edition | Status | Note |
|---|---|---|
| AI 100-2e2023 | Historical | First edition; many courses and papers still cite it. Its categories remain useful, but check the 2025 text before quoting definitions |
| **AI 100-2e2025** | **Current** (final, March 2025) | Adds generative-AI coverage and revised terminology. A published errata note exists; check the CSRC record for updates |

Citing the 2023 edition in new work is a version error unless you are explicitly discussing its history.

## Worked example

A student evaluating a document-verification classifier wrote:

> Threat: targeted misclassification of tampered documents, integrity goal, inference stage, black-box access with
> the ability to re-photograph and re-compress (capability), no gradient access (knowledge). Test: PGD-20 at
> ε ∈ {0.05, 0.1, 0.2} in pixel space plus a print-and-photograph simulation, with random-noise control at the same
> budget. Claim: accuracy under attack at ε = 0.1 is 0.62 ± 0.03 over 1,000 images, three seeds.

Every dimension from the taxonomy appears, and the claim is bounded by the tests that produced it. That is what the
framework is for.

## Limitations to state

- A taxonomy is not a threat model: it does not know your assets, adversaries or consequences.
- It does not supply thresholds, severity or acceptance criteria.
- Generative-AI coverage is newer and less settled than the predictive material; treat its categories as a starting
  vocabulary, not a complete map.
- NIST guidance is voluntary; citing it does not create an obligation, and following it does not create compliance.

## Where it appears in this course

[Module 06](../modules/06-adversarial-ml.md), [Module 07](../modules/07-data-poisoning.md),
[Module 08](../modules/08-evasion-and-robustness.md), [Module 09](../modules/09-model-privacy.md),
[Module 10](../modules/10-model-extraction.md), and the [research reading list](../research/adversarial-ml.md).

## Sources

1. Vassilev, A., Oprea, A., Fordyce, A., Anderson, H., Davies, X. and Hamin, M., *Adversarial Machine Learning: A
   Taxonomy and Terminology of Attacks and Mitigations*, NIST AI 100-2e2025, March 2025.
   <https://doi.org/10.6028/NIST.AI.100-2e2025> · record and errata:
   <https://csrc.nist.gov/pubs/ai/100/2/e2025/final>
2. NIST, *AI 100-2e2025 potential updates* (errata note).
   <https://csrc.nist.gov/files/pubs/ai/100/2/e2025/final/docs/nist.ai.100-2e2025_potential_updates.pdf>
3. NIST, *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*, NIST AI 100-2e2023
   (superseded edition, cited here for version history).
