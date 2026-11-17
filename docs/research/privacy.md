---
title: Privacy, membership inference, inversion and extraction
description: The four inference attacks on models — what each reveals, the papers that established them, and how to measure them honestly.
---

# Privacy and extraction

Four attack families are often conflated: model privacy (a broad goal), membership inference, model inversion and
attribute inference (specific inferences), and model extraction (stealing functionality or parameters). They share
query access and differ in what the attacker wants.

## Privacy

"Privacy" in ML security usually means *inference about training data from model behaviour*. The goal is not to
break the model but to learn something about the people in it. Differential privacy is the main formal mitigation.

| Paper | What it established | Read it for |
|---|---|---|
| Shokri, Stronati, Song and Shmatikov, "Membership Inference Attacks Against Machine Learning Models", *IEEE S&P* 2017. [IEEE](https://ieeexplore.ieee.org/document/7958568) | Predictions can reveal whether a record was in training data, including in ML-as-a-service | The shadow-model framing that still defines the field |
| Abadi et al., "Deep Learning with Differential Privacy", *ACM CCS* 2016. [DOI:10.1145/2976749.2978318](https://doi.org/10.1145/2976749.2978318) | DP-SGD: per-example gradient clipping plus noise, with privacy accounting | The mechanism behind most formal privacy claims |
| Carlini et al., "Extracting Training Data from Large Language Models", *USENIX Security* 2021. [Paper](https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting) | Verbatim training examples, including personal information, can be elicited from GPT-2 | Why memorisation is a privacy property, not just a quality one |

**What the course takes from this cluster:** measure leakage at a stated operating point, and report the attack you
used. A privacy claim without an attack and an FPR is not a measurement. See
[MP04](../projects/mini/mp04-privacy-risk.md) and [Module 09](../modules/09-model-privacy.md).

## Membership inference

The question: was this specific record in the training set? The field's methodological turning point was evaluating
at low false-positive rates rather than average accuracy.

| Paper | What it established | Read it for |
|---|---|---|
| Carlini, Chien, Nasr, Song, Terzis and Tramèr, "Membership Inference Attacks From First Principles", *IEEE S&P* 2022. [DOI:10.1109/SP46214.2022.9833649](https://doi.org/10.1109/SP46214.2022.9833649) | The likelihood-ratio attack (LiRA); argue for TPR at low FPR as the metric | The standard your result should be comparable to |
| Shokri et al. 2017 (above) | Feasibility in black-box settings | The attack most students implement first |

**Metric discipline:** report TPR at 1 % and 5 % FPR, and 2·AUC − 1, with the population, split and model described.
A single "accuracy" number for a membership attack is uninterpretable because the base rate is 50 % by construction.

**What this does not settle:** a negative result bounds one attack at one operating point on one population. It is
not evidence of privacy, and the honest phrasing is "no leakage was detected by this attack at this operating
point".

## Model inversion

The question: what does the model's representation of a class look like, and can it reconstruct features of
training inputs? In the original work, confidence values were enough to produce recognisable images.

| Paper | What it established | Read it for |
|---|---|---|
| Fredrikson, Jha and Ristenpart, "Model Inversion Attacks that Exploit Confidence Information and Basic Countermeasures", *ACM CCS* 2015. [DOI:10.1145/2810103.2813677](https://doi.org/10.1145/2810103.2813677) | Confidence outputs enable inference of sensitive features, including recognisable face images | The argument for coarsening output granularity |

**Design implication:** output granularity is a privacy control. A probability with four decimal places carries more
information than a band. Decide which tier gets which, and say why.

## Extraction

The question: can the attacker reproduce the model's functionality — or recover parts of its parameters — through
queries? Extraction is an IP and a competitive-risk problem, and for a pricing model it is a security problem.

| Paper | What it established | Read it for |
|---|---|---|
| Tramèr, Zhang, Juels, Reiter and Ristenpart, "Stealing Machine Learning Models via Prediction APIs", *USENIX Security* 2016. [Paper](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/tramer) | Practical extraction through prediction APIs; API design changes the risk | Equation-solving and decision-boundary attacks |
| Orekondy, Schiele and Fritz, "Knockoff Nets: Stealing Functionality of Black-Box Models", *CVPR* 2019. [CVPR](https://openaccess.thecvf.com/content_CVPR_2019/html/Orekondy_Knockoff_Nets_Stealing_Functionality_of_Black-Box_Models_CVPR_2019_paper.html) | Substitute models trained on queried inputs reproduce functionality | Why "the weights are secret" is not a control |
| Carlini et al., "Stealing Part of a Production Language Model", *ICML* 2024. [PMLR](https://proceedings.mlr.press/v235/carlini24a.html) | Black-box API access recovered embedding-projection layers of production models and hidden dimensions of GPT-3.5 variants | The current state of the art, and its limits |

**What the course takes from this cluster:** extraction is measured as fidelity against query budget, with the
target's own accuracy reported alongside so fidelity is not mistaken for quality. See
[MP04](../projects/mini/mp04-privacy-risk.md) for privacy and [Module 10](../modules/10-model-extraction.md) for
extraction's economics.

**What this does not settle:** the 2024 work demonstrates recovery of specific components, not a full clone of a
production model. Reports that say "a model was stolen" usually mean functionality was approximated; say which.

## A measurement template you can reuse

For any of these four, a defensible result states:

1. **Attack:** name and reference (for example LiRA; or a threshold attack on true-label confidence).
2. **Access:** black-box queries, confidence values or labels; query budget.
3. **Population:** how members and non-members were drawn, and why they are comparable.
4. **Metric and operating point:** TPR at stated FPR; fidelity at stated budget.
5. **Control:** a regularised or output-coarsened variant, measured on the same split.
6. **Scope:** the sentence that says what the number does not cover.

## Open questions

1. How should leakage be reported for models that are fine-tuned per tenant, where the population is tiny?
2. What is the right operating point for a privacy claim in a regulated sector — and who decides?
3. How do extraction defences interact with legitimate integrations that also need high query volume?
4. Can memorisation be measured before deployment, or only after enough queries accumulate?
