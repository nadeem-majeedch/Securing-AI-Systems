---
title: MITRE ATLAS
description: The adversary knowledge base for AI systems — how its tactics and techniques turn a threat model into tests.
---

# MITRE ATLAS

## What it is

**ATLAS** — *Adversarial Threat Landscape for Artificial-Intelligence Systems* — is a MITRE knowledge base of
adversary tactics and techniques involving AI. It is modelled on ATT&CK: tactics describe *why* an adversary acts
(their goal at a stage), techniques describe *how*, and each technique page links to real-world case studies,
mitigations and the software or entities involved.

Atlas is built from empirical evidence: observed attacks, red-team demonstrations and disclosures. It is a **living
knowledge base**, updated in numbered releases rather than editions.

**As published at access (November 2026):** 16 tactics, 221 techniques, 44 mitigations, 77 case studies,
44 entities and 37 software entries. <https://atlas.mitre.org/>

## Why it matters

A threat model tells you what you are worried about. ATLAS tells you what an adversary has actually done to systems
like yours, in a vocabulary your threat-intelligence team already consumes. That has three practical effects:

1. **Coverage becomes arguable.** "We tested prompt injection" is an assertion. "We tested the techniques under
   Initial Access, Execution and Exfiltration that apply to a RAG assistant, and these three were out of scope
   because…" is a coverage claim with edges.
2. **Detection engineers get identifiers.** A log rule can be annotated with a technique ID, which makes telemetry
   coverage measurable in the same way as ATT&CK coverage.
3. **Case studies anchor severity.** ATLAS entries link to documented incidents, which is how a hypothetical risk
   becomes a credible one in a risk register.

## When it is used

- Red-team planning and scoping (Modules 17 and the [P6 framework](../projects/major/p06-red-team-framework.md)).
- Detection engineering: mapping signals to techniques (Module 18).
- Threat intelligence: translating a vendor disclosure into the techniques it exercised.
- Architecture review: asking which tactics a proposed design makes cheap or expensive.

It is **not** a control framework and not a certification. It says nothing about your obligations; it describes
adversary behaviour.

## Structure you will actually use

The 16 tactics, as listed on the ATLAS matrix:

| | | | |
|---|---|---|---|
| Reconnaissance | Resource Development | AI Attack Adaptation | Initial Access |
| AI Model Access | Execution | Persistence | Privilege Escalation |
| Defense Evasion | Credential Access | Discovery | Lateral Movement |
| Collection | Command and Control | Exfiltration | Impact |

Four of these are AI-specific enough to be worth naming in a review: **AI Attack Adaptation** (an adversary adapting
to defences), **AI Model Access** (gaining access to a model or its artefacts), **AI Attack Adaptation** and the
model-artefact paths that sit under Resource Development.

Representative techniques, with the identifiers you can cite:

| Technique | ID | Where it lands in this course |
|---|---|---|
| LLM Prompt Injection | AML.T0051 | [Module 12](../modules/12-prompt-injection.md), [MP06](../projects/mini/mp06-injection-detection.md) |
| LLM Jailbreak | AML.T0054 | Module 12 |
| RAG Poisoning | AML.T0070 | [Module 13](../modules/13-rag-security.md), [MP07](../projects/mini/mp07-rag-access-control.md) |
| False RAG Entry Injection | AML.T0071 | Module 13 |
| Gather RAG-Indexed Targets | AML.T0064 | Module 13, reconnaissance stage |
| AI Agent Tool Invocation | AML.T0053 | [Module 14](../modules/14-agent-security.md), [MP08](../projects/mini/mp08-agent-authorisation.md) |
| Exfiltration via AI Agent Tool Invocation | AML.T0086 | Module 14, [P5](../projects/major/p05-agent-sandbox.md) |
| Training Data Poisoning | AML.T0020 | [Module 07](../modules/07-data-poisoning.md) |
| Publish Poisoned AI Artifacts | AML.T0115 | [Module 15](../modules/15-fine-tuning-supply-chain.md), [MP09](../projects/mini/mp09-supply-chain-checker.md) |
| AI Supply Chain Rug Pull | AML.T0109 | Module 15 |
| Cost Harvesting | AML.T0034 | [Module 16](../modules/16-secure-ai-apis.md) |
| Exfiltration via AI Inference API | AML.T0024 | Modules 10, 16 |
| Discover AI Model Outputs | AML.T0063 | Module 10, extraction reconnaissance |
| Recover AI Model Internals | AML.T0144 | Module 10 |
| Craft Adversarial Data | AML.T0043 | [Module 06](../modules/06-adversarial-ml.md) |
| Evade AI Model | AML.T0015 | [Module 08](../modules/08-evasion-and-robustness.md) |
| Erode Dataset Integrity | AML.T0059 | Module 07 |
| Denial of AI Service | AML.T0029 | Module 16 |
| Misconfigured or Publicly Exposed AI Services | AML.T0132 | Module 16, infrastructure |

Technique identifiers are stable enough to put in a report; names occasionally change between releases, so cite the
ID alongside the name.

## How to apply it

**Step 1 — pick the relevant tactics.** Not all 16 apply to every system. A batch classifier with no agent has no
tool-invocation path; a RAG assistant has several. Write down the ones you exclude and why.

**Step 2 — enumerate techniques per tactic and component.** Use the matrix filter, or the technique list, and record
(event, technique ID, whether the design makes it cheap or expensive).

**Step 3 — turn technique coverage into tests.** One technique may need several tests; one test may cover several
techniques. The coverage matrix in [P6](../projects/major/p06-red-team-framework.md) is exactly this, with
*tested / out of scope / not reached* per cell.

**Step 4 — annotate detections.** For each signal in your monitoring design, list the techniques it would reveal.
A signal that maps to no technique is either novel or unnecessary; both are worth knowing.

**Step 5 — read the case studies.** ATLAS's value is that its techniques are evidenced. The
[case studies section](../case-studies/index.md) in this course covers a subset in teaching depth.

## Worked example: a document assistant

| Stage | Tactic | Techniques worth testing | Test in the course |
|---|---|---|---|
| Recon | Discovery | Discover AI Model Outputs (AML.T0063) | Query the API with boundary inputs, record granularity |
| Initial access | Initial Access | LLM Prompt Injection (AML.T0051), Prompt Infiltration via Public-Facing Application (AML.T0093) | Twelve-payload suite |
| Collection | Collection | Data from Information Repositories (AML.T0036), Gather RAG-Indexed Targets (AML.T0064) | Cross-tenant query set |
| Exfiltration | Exfiltration | Exfiltration via AI Inference API (AML.T0024), via AI Agent Tool Invocation (AML.T0086) | Egress test, session-argument test |
| Impact | Impact | Cost Harvesting (AML.T0034), Erode Dataset Integrity (AML.T0059) | Quota test, poisoning injection |

That table is the bridge between a framework and a test plan. It takes an afternoon and it is the difference between
"we used ATLAS" and "we used ATLAS".

## Limitations to state

- ATLAS describes adversary behaviour, not your obligations, maturity or controls. Pair it with a risk framework.
- Coverage is evidence-weighted: techniques with no public observation may still be used against you.
- Technique granularity is uneven across tactics; a low count in one tactic is not reassurance.
- It is not a severity scheme. Impact and likelihood come from your own context.

## Sources

1. MITRE, *ATLAS — Adversarial Threat Landscape for Artificial-Intelligence Systems*, matrix and technique pages.
   <https://atlas.mitre.org/> (accessed November 2026; site reports 16 tactics, 221 techniques, 44 mitigations,
   77 case studies).
2. MITRE, *ATLAS data releases* (versioned technique and tactic data).
   <https://github.com/mitre-atlas/atlas-data/releases> (accessed November 2026).
3. Greshake, K. et al., "Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with
   Indirect Prompt Injection", *AISec '23*, 2023. <https://doi.org/10.1145/3605764.3623985> — the research basis for
   several injection techniques and case studies.
