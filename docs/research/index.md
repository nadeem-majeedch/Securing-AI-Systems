---
title: Research
description: An annotated reading list across twelve research areas, with the papers that established each idea and the ones to read next.
hide:
  - toc
---

# Research reading list

This section is a reading list, not a literature review. Each area below has one page that names the papers worth
starting with, says what each established, and points to where the idea appears in the course.

Twelve areas, in four clusters:

| Area | Cluster page | Start with |
|---|---|---|
| Adversarial machine learning | [Adversarial ML](adversarial-ml.md#evasion) | Szegedy et al. 2014; Goodfellow et al. 2015 |
| Data poisoning | [Adversarial ML](adversarial-ml.md#poisoning) | Biggio et al. 2012; Carlini 2021 |
| Backdoor attacks | [Adversarial ML](adversarial-ml.md#backdoors) | Gu et al. 2017; Chen et al. 2017 |
| Model privacy | [Privacy and extraction](privacy.md#privacy) | Shokri et al. 2017; Abadi et al. 2016 |
| Membership inference | [Privacy and extraction](privacy.md#membership-inference) | Carlini et al. 2022 (LiRA) |
| Model inversion | [Privacy and extraction](privacy.md#model-inversion) | Fredrikson et al. 2015 |
| Model extraction | [Privacy and extraction](privacy.md#extraction) | Tramèr et al. 2016; Carlini et al. 2024 |
| Prompt injection | [LLMs and agents](llm-and-agents.md#prompt-injection) | Willison 2022; Greshake et al. 2023 |
| RAG security | [LLMs and agents](llm-and-agents.md#rag-security) | Zou et al., PoisonedRAG, USENIX Security 2025 |
| Agent security | [LLMs and agents](llm-and-agents.md#agent-security) | AgentDojo 2024; InjecAgent 2024 |
| AI supply chain security | [Operations](operations.md#supply-chain) | Ohm et al. 2020; Zhao et al. 2024 |
| Runtime monitoring | [Operations](operations.md#runtime-monitoring) | Llama Guard 2023; Attention Tracker 2025 |

## Reading a paper for this course

Five questions, in this order. If you cannot answer the third by the end, the paper is not yet useful to you.

1. **What is the adversary allowed to do?** Capability and knowledge, in the [NIST taxonomy](../frameworks/nist-aml.md)
   sense. Papers that omit this are not comparable with each other.
2. **What is measured, on what?** Dataset, sample size, metric, operating point. "Attack success rate" without a
   denominator is a headline.
3. **What would falsify the claim?** A defence paper that does not test an adaptive attacker is a hypothesis.
4. **What does the result cost?** Query budget, compute, data, latency. A defence nobody can afford is not deployed.
5. **What changed since?** A 2017 defence evaluated against 2017 attacks is a historical document.

## On evidence levels

Not everything cited in security writing is equal, and this course labels the difference:

| Level | What it is | How to treat it |
|---|---|---|
| **Peer-reviewed paper** | Conference or journal with review, e.g. IEEE S&P, USENIX Security, CCS, ICML, NeurIPS, ACL | Strongest available; still check the threat model and later work |
| **Preprint** | arXiv or similar, not peer-reviewed | Useful and often the only source for a new attack; cite as a preprint and say so |
| **Standard or official guidance** | NIST, ISO/IEC, OWASP, MITRE, regulators | Authoritative for definitions and expectations, not for empirical claims |
| **Vendor research / blog** | Company security teams, independent researchers | Often the only public source for a real incident; verify details and separate demonstration from exploitation |
| **Press reporting** | News outlets | Use for facts about an event, not for technical mechanism |

The [case studies](../case-studies/index.md) use the same labels, because the difference between "a researcher
demonstrated this" and "this was exploited in the wild" is the difference between a hypothesis and an incident.

## How to use this list in an assignment

A project report needs citations that do work, not decoration:

- **Cite the source of a definition** you rely on (for example the NIST taxonomy for "evasion").
- **Cite the source of a measurement method** (LiRA for membership inference at low FPR; PGD for a robustness
  baseline).
- **Cite the closest prior work** when you claim novelty, and say how yours differs.
- **Never cite a paper for a claim it does not make.** A common failure is citing a poisoning paper for a statistic
  about production systems; the paper measured a benchmark.

Each cluster page ends with "what this does not settle" — the open questions worth naming in a limitation section.
