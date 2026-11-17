---
title: Adversarial ML, poisoning and backdoors
description: The papers that established evasion, poisoning and backdoor attacks, what each showed, and the open questions.
---

# Adversarial ML, poisoning and backdoors

Three areas share a page because they share a threat model: an adversary who can influence either the input at
inference time or the data at training time. The distinction between them is *when* the influence happens and *what
persists*.

## Evasion

An evasion attack changes an input at inference time so the model misclassifies it. Nothing about the model changes.

| Paper | What it established | Read it for |
|---|---|---|
| Szegedy et al., "Intriguing Properties of Neural Networks", *ICLR* 2014. [arXiv:1312.6199](https://arxiv.org/abs/1312.6199) | Small, deliberately chosen perturbations cause confident misclassification; examples transfer between models | The original observation, including transferability |
| Goodfellow, Shlens and Szegedy, "Explaining and Harnessing Adversarial Examples", *ICLR* 2015. [arXiv:1412.6572](https://arxiv.org/abs/1412.6572) | Linearity as an explanation; the fast gradient sign method (FGSM) | Why one backward pass is enough to be dangerous |
| Kurakin, Goodfellow and Bengio, "Adversarial Examples in the Physical World", *ICLR Workshop* 2017. [arXiv:1607.02533](https://arxiv.org/abs/1607.02533) | Perturbations survive being photographed | Why the digital/physical distinction matters for a threat model |
| Carlini and Wagner, "Towards Evaluating the Robustness of Neural Networks", *IEEE S&P* 2017. [DOI:10.1109/SP.2017.49](https://doi.org/10.1109/SP.2017.49) | Strong optimisation-based attacks; defensive distillation did not provide the claimed robustness | The template for "attack the defence, not the model" |
| Madry et al., "Towards Deep Learning Models Resistant to Adversarial Attacks", *ICLR* 2018. [arXiv:1706.06083](https://arxiv.org/abs/1706.06083) | Robustness as min-max optimisation; PGD as both attack and training method | Why PGD is the default evaluation baseline |
| Athalye, Carlini and Wagner, "Obfuscated Gradients Give a False Sense of Security", *ICML* 2018 | Many defences that reported robustness failed under adaptive attacks because they masked gradients | The evaluation standard this course enforces in [Module 08](../modules/08-evasion-and-robustness.md) |

**What the course takes from this cluster:** a robustness number is meaningless without an attack, a budget and a
control condition. The [MP02 harness](../projects/mini/mp02-robustness-evaluation.md) exists to make students
produce all three.

**What this does not settle:** robustness to a norm-bounded attack says little about a different norm, a physical
transformation, or an adaptive attacker who targets your defence specifically.

## Poisoning

A poisoning attack changes training data so that the learned model behaves differently at test time.

| Paper | What it established | Read it for |
|---|---|---|
| Biggio, Nelson and Laskov, "Poisoning Attacks against Support Vector Machines", *ICML* 2012. [arXiv:1206.6389](https://arxiv.org/abs/1206.6389) | Crafted training points can increase test error by shifting the decision boundary | The original optimisation view of poisoning |
| Carlini, "Poisoning the Unlabeled Dataset of Semi-Supervised Learning", *USENIX Security* 2021. [Paper](https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-poisoning) | A small fraction of malicious examples in the *unlabelled* set can cause targeted misclassification | Why "we only poison labels" is too narrow a threat model |
| Carlini and Terzis, "Poisoning and Backdooring Contrastive Learning", *ICLR* 2022. [arXiv:2106.09667](https://arxiv.org/abs/2106.09667) | Very small poisoning fractions in noisy web-scale data can enable targeted poisoning or patch backdoors | The economics of poisoning at scale |
| Carlini et al., "Poisoning Web-Scale Training Datasets is Practical", *IEEE S&P* 2024. [DOI:10.1109/SP54263.2024.00179](https://doi.org/10.1109/SP54263.2024.00179) | Split-view and frontrunning attacks against datasets such as LAION-400M and COYO-700M | Why dataset snapshots and provenance are security controls |
| Zou et al., "PoisonedRAG", *USENIX Security* 2025. [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag) | Injected texts in a retrieval corpus can steer answers to attacker-chosen targets | The RAG case: poisoning without touching weights |

**What the course takes from this cluster:** detection is a measurement problem with a base rate. The
[MP03 prototype](../projects/mini/mp03-poisoning-detection.md) asks students to report precision and recall at three
poison rates, because that is what a deployment decision needs.

**What this does not settle:** there is no public, independently verified case of a production model being poisoned
and shown to behave differently because of it. Treat claims otherwise as unverified; the
[hypothetical scenarios](../case-studies/hypothetical.md) page exists precisely for teaching that case without
inventing an incident.

## Backdoors

A backdoor is a poisoning attack with a trigger: the model behaves normally on clean inputs and attacker-chosen on
triggered ones. It is the clearest example of a failure that aggregate accuracy cannot reveal.

| Paper | What it established | Read it for |
|---|---|---|
| Gu, Dolan-Gavitt and Garg, "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain", 2017. [arXiv:1708.06733](https://arxiv.org/abs/1708.06733) | A model can pass clean evaluation while misclassifying triggered inputs | The canonical demonstration, and the supply-chain framing |
| Gu, Liu, Dolan-Gavitt and Garg, "BadNets: Evaluating Backdooring Attacks on Deep Neural Networks", *IEEE Access* 7, 2019. [DOI:10.1109/ACCESS.2019.2909068](https://doi.org/10.1109/ACCESS.2019.2909068) | Journal version with broader evaluation including a traffic-sign case | A citable peer-reviewed version |
| Chen et al., "Targeted Backdoor Attacks on Deep Learning Systems Using Data Poisoning", 2017. [arXiv:1712.05526](https://arxiv.org/abs/1712.05526) | Targeted backdoors under a comparatively weak attacker-knowledge model | What an attacker needs to know to succeed |

**Why it matters for artefacts:** a backdoored model is indistinguishable from a clean one without behavioural
testing. That is the argument for the [supply-chain checker](../projects/mini/mp09-supply-chain-checker.md) and for
loading artefacts by digest rather than by name.

## Where the course uses these papers

- [Module 06](../modules/06-adversarial-ml.md) — evasion mechanics and the four-family map.
- [Module 07](../modules/07-data-poisoning.md) — poisoning, backdoors, detection.
- [Module 08](../modules/08-evasion-and-robustness.md) — evaluation and adaptive attacks.
- [Module 13](../modules/13-rag-security.md) — corpus poisoning.
- [P1](../projects/major/p01-secure-ml-pipeline.md) and [P4](../projects/major/p04-rag-assistant.md) — pipeline and
  corpus integrity controls.

## Open questions worth naming in a limitation

1. How do you evaluate robustness to an attacker you have not modelled, without claiming universal robustness?
2. Which poisoning defences survive an adversary who knows the detector and can choose the poison rate?
3. Can provenance controls (manifests, signed datasets, snapshot pins) be deployed at the speed of data acquisition?
4. What does a backdoor detection method's false-positive rate have to be before a team will act on it?
