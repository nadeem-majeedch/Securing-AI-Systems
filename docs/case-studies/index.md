---
title: Case studies
description: Documented AI security incidents and disclosures, each with background, architecture, root cause and lessons — plus clearly labelled hypothetical scenarios.
hide:
  - toc
---

# Case studies

Ten documented cases, each written to the same nine-section structure: background, architecture, security weakness,
threat scenario, impact, root cause, detection, mitigation, lessons.

These are teaching documents, not accusations. Each page states **what the public record actually supports** — a
researcher's demonstration is not an exploited breach, and a mitigated vulnerability is not a customer data loss.
Where the evidence is thin, the page says so.

!!! warning "Real versus hypothetical"

    Every case in this section is based on a documented disclosure, advisory, CVE, court decision or peer-reviewed
    paper, with the source linked. Cases that are **constructed for teaching** are kept separately in
    [Hypothetical scenarios](hypothetical.md) and carry a banner saying so. No incident, statistic or research
    finding in this section has been invented; where a number is a researcher's estimate, it is attributed.

## The ten

| # | Case | Year | Class | Evidence status |
|---|---|---|---|---|
| [C01](c01-bing-prompt-extraction.md) | Bing Chat system-prompt extraction | 2023 | Prompt injection, instruction disclosure | Demonstrated publicly; Microsoft acknowledged the technique |
| [C02](c02-chatgpt-redis.md) | ChatGPT cross-user data exposure | 2023 | Implementation defect, data isolation | Vendor postmortem |
| [C03](c03-torchtriton-dependency-confusion.md) | PyTorch `torchtriton` dependency confusion | 2022 | Software supply chain | Vendor security advisory |
| [C04](c04-shadowray-ray.md) | ShadowRay: exposed Ray Jobs API | 2023–24 | Unauthenticated infrastructure, AI compute | CVE + researcher report; vendor dispute recorded |
| [C05](c05-huggingface-pickle.md) | Malicious models on a public hub | 2024 | Model artefact supply chain, deserialisation | Researcher analysis + hub documentation |
| [C06](c06-echoleak-copilot.md) | EchoLeak: zero-click injection in M365 Copilot | 2025 | Indirect prompt injection, exfiltration | CVE-2025-32711; vendor mitigated; no known exploitation |
| [C07](c07-camoleak-copilot-chat.md) | CamoLeak: exfiltration via Copilot Chat | 2025 | Injection, proxy abuse, data exfiltration | Researcher disclosure; vendor mitigated; no CVE found |
| [C08](c08-deepseek-database.md) | Exposed DeepSeek database | 2025 | Unauthenticated data store, AI infrastructure | Researcher report; vendor secured |
| [C09](c09-amazon-q-supply-chain.md) | Amazon Q Developer extension compromise | 2025 | Software supply chain, over-scoped token | Vendor bulletin + CVE-2025-8217 |
| [C10](c10-air-canada-chatbot.md) | Air Canada chatbot liability | 2024 | Accuracy, accountability, governance | Tribunal decision |

## Additional documented incidents

These are referenced in the course but not written up as full case studies. Each has a primary source you can read.

| Incident | Year | What it illustrates | Source |
|---|---|---|---|
| Microsoft Tay | 2016 | Coordinated abuse of a learning chatbot; the first widely reported case of user-driven behaviour corruption | [Microsoft statement](https://blogs.microsoft.com/blog/2016/03/25/learning-tays-introduction/) |
| Hugging Face Spaces secrets access | 2024 | Platform secrets exposure and the limits of an initial disclosure | [Hugging Face update](https://huggingface.co/blog/space-secrets-disclosure) |
| MCP Inspector unauthenticated command execution | 2025 | Tooling in the agent ecosystem inheriting classic RCE risk; CVE-2025-49596 | [Advisory](https://github.com/modelcontextprotocol/inspector/security/advisories/GHSA-7f8r-222p-6f5g) · [Tenable](https://www.tenable.com/security/research/tra-2025-20) |
| Meta LLaMA weights distributed beyond the approved group | 2023 | Model-weight leakage after controlled release; initial path not established publicly | [CyberScoop](https://cyberscoop.com/meta-large-language-model-available-online) |

## What the collection does not contain, and why

- **A confirmed production model-poisoning incident.** No public record establishes one with verifiable provenance
  and observed behavioural change. Claims otherwise are treated as unverified; teaching that case is done with a
  [hypothetical scenario](hypothetical.md) instead.
- **A confirmed model-extraction theft from a production API.** The research demonstrates extraction (Carlini et
  al., ICML 2024, with the provider's approval); no publicly documented hostile theft with measured fidelity exists.
- **A confirmed agentic breach caused by injected instructions in a customer deployment.** The 2025 Copilot
  disclosures are mitigated vulnerabilities without reported exploitation.

That absence is itself a lesson: the field's evidence base is weighted toward demonstrations and mitigations, so a
risk register that only accepts "proven in the wild" evidence will systematically under-count AI risk.

## How to use a case study

1. **Read the source before the summary.** Each page links the primary record; the page is a teaching frame, not a
   substitute.
2. **Fill in the architecture yourself.** The architecture section describes the components the disclosure
   implicates, not a vendor diagram.
3. **Separate weakness from impact.** A design weakness that was mitigated before exploitation still teaches the
   control; it does not support a claim that data was stolen.
4. **Write the lesson as a test.** "Validate untrusted context" is a slogan; "a payload suite of twelve items, per
   capability, with the tool log as the success criterion" is a lesson you can assess.

## Mapping cases to the course

| Module | Case to read alongside |
|---|---|
| [03](../modules/03-cybersecurity-fundamentals.md), [16](../modules/16-secure-ai-apis.md) | C02, C04, C08 |
| [11](../modules/11-llm-security.md), [12](../modules/12-prompt-injection.md) | C01, C06 |
| [13](../modules/13-rag-security.md) | C06 (retrieval context), C05 |
| [14](../modules/14-agent-security.md) | C07, C09 |
| [15](../modules/15-fine-tuning-supply-chain.md) | C03, C05, C09 |
| [17](../modules/17-red-teaming.md), [18](../modules/18-monitoring-and-response.md) | C04, C06, C08 |
| [19](../modules/19-governance-and-ethics.md) | C10 |
