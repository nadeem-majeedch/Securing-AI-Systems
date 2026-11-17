---
title: Prompt injection, RAG and agent security
description: The research behind LLM application security — injection, jailbreaks, retrieval poisoning and tool-using agents.
---

# Prompt injection, RAG and agent security

This cluster is younger than the adversarial-ML literature and moves faster. The papers below are the ones that
established a concept, a benchmark or a measurement method; several are recent enough that the venue matters when
you cite them.

## Prompt injection

The core problem: an LLM cannot reliably distinguish instructions from data, so text that arrives as *content* can
act as *instruction*. Simon Willison named it in 2022; the systematic treatment for applications came in 2023.

| Source | What it established | Read it for |
|---|---|---|
| Willison, S., "Prompt injection attacks against GPT-3", blog, 12 September 2022. [Post](https://simonwillison.net/2022/Sep/12/prompt-injection/) | Named the class of attack | The origin of the term; a blog post, not a paper |
| Perez, F. and Ribeiro, I., "Ignore Previous Prompt: Attack Techniques For Language Models", 2022. [arXiv:2211.09527](https://arxiv.org/abs/2211.09527) | PromptInject: goal hijacking and prompt leaking in GPT-3 | Early systematisation; preprint |
| Greshake, K. et al., "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection", *AISec '23*. [DOI:10.1145/3605764.3623985](https://doi.org/10.1145/3605764.3623985) | Instructions in external content can hijack application behaviour and influence API calls | The paper that made *indirect* injection the central case |
| Wei, A., Haghtalab, N. and Steinhardt, J., "Jailbroken: How Does LLM Safety Training Fail?", *NeurIPS* 2023. [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2023/hash/fd6613131889a4b656206c50a8bd7790-Abstract-Conference.html) | Explains jailbreaks through competing objectives and mismatched generalisation | Why jailbreaks are a training-objective problem, not a filter problem |
| Zou, A. et al., "Universal and Transferable Adversarial Attacks on Aligned Language Models", 2023. [arXiv:2307.15043](https://arxiv.org/abs/2307.15043) | Greedy gradient-based search for adversarial suffixes (GCG) that transfer | Automated jailbreak search; preprint |

**Design consequence:** prompt-only defences are advisory. The controls that hold are outside the model — capability
removal, session-derived arguments, output handling — which is what [MP06](../projects/mini/mp06-injection-detection.md)
asks students to demonstrate.

**What this does not settle:** there is no general detector with a measured precision at realistic prevalence. Any
claim of "injection-proof" is a claim about a test suite, not about the class.

## RAG security

Retrieval adds two attack surfaces: the corpus (poisoning) and the boundary between documents (isolation). The
research on poisoning is now solid; the research on isolation is thinner, and much of the operational guidance comes
from OWASP rather than from papers.

| Source | What it established | Read it for |
|---|---|---|
| Zou, W., Geng, R., Wang, B. and Jia, J., "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models", *USENIX Security* 2025. [Paper](https://www.usenix.org/conference/usenixsecurity25/presentation/zou-poisonedrag) | Injected corpus texts can steer answers to attacker-chosen targets | The measured basis for corpus-integrity controls |
| OWASP, *RAG Security Cheat Sheet*. [Cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html) | Operational guidance: per-chunk permissions, authorisation at retrieval, tenant isolation | The control patterns this course teaches; guidance, not research |
| SafeRAG benchmark, *ACL* 2025. [ACL Anthology](https://aclanthology.org/2025.acl-long.230) | A benchmark of attack scenarios across retrieval and generation components | Comparing attack families |

**Honest note:** I did not find a canonical peer-reviewed paper that establishes tenant isolation in RAG as a
research result. The practice is well-founded engineering (authorise before ranking, fail closed, verify before
generation) and is documented by OWASP; treat claims about it as engineering guidance, not experimental findings.

## Agent security

An agent composes a model with tools, which turns a text-level problem into an action-level one. Research here is
mostly benchmark-driven: build an environment, measure injection success against real tools.

| Paper | What it established | Read it for |
|---|---|---|
| Debenedetti, E. et al., "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents", *NeurIPS 2024 Datasets and Benchmarks*. [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html) | An extensible environment for testing injection and defences on tool-using tasks | The evaluation design to copy |
| Zhan, Q., Liang, Z., Ying, Z. and Kang, D., "InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents", *Findings of ACL 2024*. [ACL Anthology](https://aclanthology.org/2024.findings-acl.624) | A benchmark of indirect injection causing harmful actions and exfiltration | Attack taxonomy for tool use |
| Zhang, K. et al., "LLM Agents Should Employ Security Principles", 2025. [arXiv:2505.24019](https://arxiv.org/abs/2505.24019) | Argues for least privilege and complete mediation; proposes an agent sandbox framing | The design-principles argument; preprint |

**What the course takes from this cluster:** a successful injection is only a finding if it reaches a capability.
Measure per capability, and fix by removing or gating the capability, as in
[MP08](../projects/mini/mp08-agent-authorisation.md) and [P5](../projects/major/p05-agent-sandbox.md).

**What this does not settle:** benchmarks measure success against their own tasks and models; a suite result does not
transfer to your prompts, your tools or your users. And the strongest published defences are still capability
restriction, not clever prompting.

## Reading order if you have one evening

1. Greshake et al. 2023 — indirect injection, the application view.
2. PoisonedRAG (USENIX Security 2025) — why corpus integrity is a security property.
3. AgentDojo 2024 — how to measure an agent defence.
4. Wei et al. 2023 — why safety training does not close the class.

## Open questions

1. What would a defence look like that is not capability removal, and how would we know it works?
2. How should a RAG system prove isolation to an auditor — what test, what evidence?
3. Which agent design patterns make injection harmless rather than merely unlikely?
4. How do you measure a detector's precision when the prevalence of successful injection in production is unknown?
