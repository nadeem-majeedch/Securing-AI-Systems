---
title: Supply chain and runtime monitoring
description: The research and primary sources behind artefact integrity, model-hub risk and detecting attacks while a model is serving.
---

# Operations: supply chain and monitoring

Two areas that are usually taught as engineering rather than research, and are better for having sources: the
integrity of what you deploy, and the detection of what happens after you deploy it.

## Supply chain

The threat is not new — software supply chains have been attacked for a decade — but models add artefact types that
no package manager was designed to protect: weights, tokenisers, adapters, and hubs that execute code on load.

| Source | What it established | Read it for |
|---|---|---|
| Ohm, M., Plate, H., Sykosch, A. and Meier, M., "Backstabber's Knife Collection: A Review of Open Source Software Supply Chain Attacks", *DIMVA* 2020. [DOI:10.1007/978-3-030-52683-2_2](https://doi.org/10.1007/978-3-030-52683-2_2) | A systematic review of open-source supply-chain attack mechanisms | The general taxonomy you can reuse for models |
| Zhao, J. et al., "Models Are Codes: Towards Measuring Malicious Code Poisoning Attacks on Pre-trained Model Hubs", *ASE* 2024. [DOI:10.1145/3691620.3695271](https://doi.org/10.1145/3691620.3695271) | A pipeline (MalHug) for detecting malicious code in model-hub artefacts, deployed on a mirror | The academic treatment of model-hub risk |
| Carlini, N. et al., "Poisoning Web-Scale Training Datasets is Practical", *IEEE S&P* 2024. [DOI:10.1109/SP54263.2024.00179](https://doi.org/10.1109/SP54263.2024.00179) | Split-view and frontrunning attacks against public datasets | Why a dataset snapshot and a provenance record are controls |
| Hugging Face, *Pickle scanning* documentation. [Docs](https://huggingface.co/docs/hub/security-pickle) | What the hub scans for, and the limits of that scanning | The mitigation's own limitation statement |

**What the course takes from this cluster:** identity and behaviour are separate checks. A digest proves what you
loaded; a probe set proves how it behaves. [MP09](../projects/mini/mp09-supply-chain-checker.md) requires both, and
[P1](../projects/major/p01-secure-ml-pipeline.md) makes them release gates.

**What this does not settle:** no scanning technology reliably identifies a backdoored model. Prevention is
provenance; detection is behavioural testing with its own false-positive rate.

## Runtime monitoring

Detection after deployment is the least mature area in the course, and the honest statement is that there is more
engineering practice than validated science. The research that exists clusters into classifiers for unsafe content,
detectors for injection, and benchmark environments.

| Source | What it established | Read it for |
|---|---|---|
| Inan, H. et al., "Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations", 2023. [arXiv:2312.06674](https://arxiv.org/abs/2312.06674) | An LLM-based classifier screening inputs and outputs against a safety taxonomy | The pattern behind most commercial guardrails; preprint |
| Hung, K.-H. et al., "Attention Tracker: Detecting Prompt Injection Attacks in LLMs", *Findings of NAACL* 2025. [ACL Anthology](https://aclanthology.org/2025.findings-naacl.123) | A training-free detector using attention patterns associated with injection | A research detector, with a benchmark result rather than a deployment result |
| Sharma, M. et al. (Anthropic), "Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming", 2025. [arXiv:2501.18837](https://arxiv.org/abs/2501.18837) | Input/output classifiers trained from natural-language rules against universal jailbreaks | The red-teaming scale needed to evaluate a classifier defence; preprint |
| Debenedetti et al., AgentDojo, *NeurIPS 2024*. [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html) | An environment for measuring attack and defence in tool-using agents | The benchmark to reuse for agent monitoring tests |

**The arithmetic that governs every alert:** precision depends on prevalence. A detector with 95 % TPR and 1 % FPR,
in a stream where 0.1 % of requests are attacks, produces roughly nine false alerts per true one. That calculation —
not the TPR — decides whether an alert is usable. It is the reason
[MP10](../projects/mini/mp10-monitoring-dashboard.md) requires a base rate alongside every threshold.

**What this does not settle:** no public study establishes detection rates for AI-specific attacks in production
traffic, because the prevalence is unknown and incidents are rarely disclosed with telemetry. Treat detector claims
as benchmark results under stated conditions.

## The primary sources you should read before citing a vendor

1. **NIST AI 100-2e2025** for the attack taxonomy — it is the shared vocabulary that makes a detection claim
   comparable. <https://csrc.nist.gov/pubs/ai/100/2/e2025/final>
2. **MITRE ATLAS** for technique identifiers you can attach to a detection rule. <https://atlas.mitre.org/>
3. **The vendor's own advisory** for an incident: postmortems and CVE records, not press coverage, carry the
   mechanism. See the [case studies](../case-studies/index.md) for worked examples of the difference.

## A monitoring design checklist drawn from the sources

| Question | Where the answer comes from |
|---|---|
| What failures am I trying to detect? | Your threat model + ATLAS techniques |
| What signal observes each failure? | Logs, canary sets, retrieval traces, artefact digests |
| What is the expected rate of that signal in normal traffic? | Measured baseline, not intuition |
| What is the alert volume at my threshold? | Arithmetic from the baseline |
| What happens when it fires? | Runbook with evidence preservation |
| What does this design not detect? | A written blindness statement |

## Open questions

1. How should an organisation measure the prevalence of AI-specific attacks in its own traffic?
2. Which signals remain useful when the attacker knows the detector?
3. What does a canary set need to contain to detect silent quality regressions in a RAG system?
4. Can artefact-level and behaviour-level integrity checks be made cheap enough to run per request?
