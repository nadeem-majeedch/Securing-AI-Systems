---
title: OWASP Top 10 for LLM Applications
description: The application-level risk list for LLM systems — the 2025 items, the 2026 edition, and how to use it without treating it as a checklist.
---

# OWASP Top 10 for LLM Applications

## What it is

A community-maintained list of the most significant security risks in applications built on large language
models, published by the OWASP GenAI Security Project. Each entry gives a description, common attack scenarios
and mitigations, and the project cross-references other frameworks including NIST publications, MITRE ATLAS,
CWE and the OWASP Top 10 for Agentic Applications.

It is **application** guidance, not model guidance: the unit of analysis is the deployed system — prompt assembly,
retrieval, tools, output handling — which is why it fits this course better than a model-centric list.

**Editions and status (accessed November 2026):**

| Edition | Status | Link |
|---|---|---|
| 2023–24 | Historical; different item set (for example *Training Data Poisoning*, *Model Denial of Service*, *Overreliance*) | [Archive](https://genai.owasp.org/llm-top-10-2023-24/) |
| 2025 | Superseded but still the edition most vendor documentation cites | [Project page](https://genai.owasp.org/llm-top-10/) |
| 2026 | **Current.** Published August 2026; revised rankings and expanded coverage | [2026 release](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) |

!!! note "Why this page lists 2025 items"

    The 2025 item identifiers (`LLM01:2025` … `LLM10:2025`) are stable, widely cited and verifiable, so they are
    listed in full below. The 2026 edition is current and changes the ranking and some framing; where this course
    cites an item by identifier, it names the year. Read the 2026 document itself for its ordering rather than
    trusting a secondary summary — including this one.

## The 2025 items

| ID | Risk | What it means in practice |
|---|---|---|
| LLM01:2025 | **Prompt Injection** | Text in the request or in retrieved content changes what the application does, including tool calls |
| LLM02:2025 | **Sensitive Information Disclosure** | Training data, system prompt content, other users' data or secrets appear in output |
| LLM03:2025 | **Supply Chain** | Model artefacts, tokenisers, adapters, plugins and dependencies are substituted or malicious |
| LLM04:2025 | **Data and Model Poisoning** | Pre-training, fine-tuning or embedding data is manipulated to change behaviour |
| LLM05:2025 | **Improper Output Handling** | Model output is passed to a sink — HTML, SQL, shell, another model — without validation |
| LLM06:2025 | **Excessive Agency** | The system can act beyond what the task needs, through tools, permissions or autonomy |
| LLM07:2025 | **System Prompt Leakage** | Instructions are recoverable and contain information that matters when disclosed |
| LLM08:2025 | **Vector and Embedding Weaknesses** | Retrieval and embedding layers leak across tenants, are poisoned, or are manipulated |
| LLM09:2025 | **Misinformation** | Confident, plausible, wrong output is acted on without verification |
| LLM10:2025 | **Unbounded Consumption** | Cost, quota or latency is driven without limit: resource exhaustion, model theft by query, denial of wallet |

## Why it matters

Three reasons, in order of practical weight:

1. **It is the language risk owners already use.** A finding written as "LLM06:2025 Excessive Agency, because the
   refund tool takes the amount from the conversation" is actionable by a product team that has never read a paper.
2. **It forces the application view.** Prompt injection only becomes a *system* problem when you see retrieval and
   tools in the same picture; the list is organised that way.
3. **It maps outward.** The entries cross-reference CWE and ATLAS, so the same issue can be reported to an
   application-security team and a threat-intelligence team without translation.

## When it is used

- Design review of an LLM feature, before launch.
- Threat modelling: as a prompt for "have we considered…", not as the model itself.
- Vendor questionnaires: asking which items a supplier has tested, and with what evidence.
- Red-team scoping: choosing test families that cover the list, then deciding what is out of scope.

It is *not* used to decide whether a system is compliant with anything. It carries no legal weight and no
certification.

## How to apply it

**Step 1 — map items to components.** Build a table with one row per item and one column per component (prompt
assembly, retrieval, tools, output handling, model, infrastructure). Mark *present*, *not applicable* or *not
assessed*. The gaps are the finding.

**Step 2 — convert the top items into tests.** An item is a category; your test is specific. For LLM01, "ten
payloads across direct, indirect and obfuscated families, measured per capability" is a test; "we reviewed prompt
injection" is not.

**Step 3 — write the mitigation at the enforcement point.** OWASP's mitigations are generic by design. "Restrict
model permissions" becomes "the tool executor derives arguments from the session and the policy engine denies by
default" — a control with a location.

**Step 4 — record what the list does not cover.** It says little about classical ML attacks (evasion, extraction),
about model weights as artefacts, or about fairness. Those belong to the [AML taxonomy](nist-aml.md) and
[ISO/IEC guidance](iso.md).

## A worked mapping for a support assistant

| Component | LLM01 | LLM05 | LLM06 | LLM08 | Test that provides evidence |
|---|---|---|---|---|---|
| Prompt assembly | app | — | — | app | Untrusted text labelled; injection suite run per capability |
| Retrieval | app | — | — | app | Foreign-chunk absence test across tenants |
| Tool layer | app | app | app | — | Ten requests, five denials, audit row each |
| Output renderer | — | app | — | — | Sink escaping test; output filter precision measured |

`app` means applicable. Filling this in takes twenty minutes and exposes immediately which components have no
evidence behind them.

## Common misuses

- **Treating the list as a test plan.** The items are categories; the tests are yours.
- **Ranking by the numbering.** The order reflects community voting, not your system's risk. A low-numbered item may
  be irrelevant to a batch classifier; a high-numbered one may be your main exposure.
- **Citing an edition without a year.** Three editions exist with different items.
- **Using it to claim compliance.** It is guidance. If you need an auditable management system, that is
  [ISO/IEC 42001](iso.md); if you need law, that is your regulator.

## Where it appears in this course

- [Module 11](../modules/11-llm-security.md) and [Module 12](../modules/12-prompt-injection.md) — LLM01, LLM07.
- [Module 13](../modules/13-rag-security.md) and [Module 14](../modules/14-agent-security.md) — LLM06, LLM08.
- [Module 15](../modules/15-fine-tuning-supply-chain.md) — LLM03, LLM04.
- [Module 16](../modules/16-secure-ai-apis.md) — LLM05, LLM10.
- Mini projects [MP06](../projects/mini/mp06-injection-detection.md), [MP07](../projects/mini/mp07-rag-access-control.md),
  [MP08](../projects/mini/mp08-agent-authorisation.md).

## Sources

1. OWASP GenAI Security Project, *OWASP Top 10 for LLM Applications 2026*, August 2026.
   <https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/> (accessed November 2026).
2. OWASP GenAI Security Project, *Top 10 for LLM Applications 2025*, project page listing `LLM01:2025`–`LLM10:2025`.
   <https://genai.owasp.org/llm-top-10/> (accessed November 2026).
3. OWASP GenAI Security Project, *Top 10 for LLM Applications 2023–24* (archive).
   <https://genai.owasp.org/llm-top-10-2023-24/> (accessed November 2026).
4. OWASP Cheat Sheet Series, *RAG Security Cheat Sheet* — operational guidance on per-chunk permissions and
   retrieval-time authorisation. <https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html>
   (accessed November 2026).
