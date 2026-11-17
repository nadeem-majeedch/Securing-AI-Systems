---
title: Frameworks
description: What each AI security framework is for, when to reach for it, and how to use it without mistaking guidance for law.
hide:
  - toc
---

# Security frameworks

A framework is a shared vocabulary plus a structure for decisions. It is not a checklist that makes a system
secure, and — with one exception noted below — it is not law. What a framework buys you is the ability to say
"we assessed this the way our sector assesses it" and to be understood by someone who was not in the room.

This section covers seven bodies of guidance. Each page answers the same four questions: **what it is**, **why it
matters**, **when it is used**, and **how to apply it to a system you are building**.

| Page | Framework | Current edition | What it is best at |
|---|---|---|---|
| [OWASP Top 10 for LLM Applications](owasp.md) | OWASP GenAI Security Project | 2026 (2025 widely cited) | Naming application-level LLM risks and their mitigations |
| [MITRE ATLAS](mitre-atlas.md) | MITRE | Living knowledge base | Adversary tactics and techniques, threat-informed testing |
| [NIST AI RMF](nist-ai-rmf.md) | NIST | AI 100-1 (2023) + GenAI Profile AI 600-1 (2024) | Organisational risk governance across the lifecycle |
| [NIST CSF 2.0](nist-csf.md) | NIST | CSWP 29 (2024) | Mapping AI risk into an existing cyber programme |
| [NIST adversarial ML taxonomy](nist-aml.md) | NIST | AI 100-2e2025 (2025) | Precise language for attacks, goals and mitigations |
| [ISO/IEC standards](iso.md) | ISO/IEC | 42001:2023, 23894:2023, 27001:2022, 22989:2022, 5338:2023 | Management systems, certification and audit |
| [Secure development (SSDF)](ssdlc.md) | NIST | SP 800-218v1.1 + SP 800-218A (2024) | Practices that produce evidence in a build pipeline |

## Guidance, standard, law: know which you are holding

The distinction matters more in AI than in most fields, because vendors cite frameworks as though they were
obligations.

| Instrument | Status | What that means for you |
|---|---|---|
| OWASP Top 10, MITRE ATLAS | Community guidance | Voluntary. Useful for prioritisation and testing; not auditable as a control set |
| NIST AI RMF, CSF 2.0, AI 100-2, SSDF | Voluntary consensus guidance (US) | Voluntary unless a contract, regulator or internal policy adopts them. Widely used as a de facto expectation |
| ISO/IEC 42001, 27001 | Voluntary, certifiable management-system standards | Voluntary; certification is a commercial and assurance choice. Binding only when a contract or regulation requires it |
| EU AI Act — Regulation (EU) 2024/1689 | **Binding law** in the EU, with staged application dates | In force since 1 August 2024. Obligations apply on a published timetable, not all at once. Check the consolidated text for the current dates |

!!! warning "Do not treat guidance as a legal mandate"

    NIST publications, OWASP projects, MITRE ATLAS and ISO/IEC standards are not, by themselves, legal
    requirements. The EU AI Act is a regulation and does create obligations — but for organisations in scope, in
    stages, and alongside national implementation. This course teaches the frameworks as professional practice.
    For any compliance decision, the governing law and your regulator's guidance decide, not this page.

## Which framework, when

<div class="sas-grid sas-grid--2" markdown>

<div class="sas-card" markdown>
<div class="sas-card__title">You are designing a system</div>
Start with the **AI RMF** to structure the risk work (Govern, Map, Measure, Manage), use **ATLAS** to enumerate
what an adversary would try, and use the **OWASP Top 10** as the application-risk checklist for the LLM surface.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">You are testing a system</div>
Use **AI 100-2e2025** for precise attack vocabulary, **ATLAS** for technique coverage, and your own threat model to
decide what is in scope. Report in the language of the receiving team.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">You are building a pipeline</div>
Use the **SSDF** (with SP 800-218A for generative-AI components) so that each practice produces an artefact — a
review, a test, a signed build — that a release gate can require.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">You are answering a board or a client</div>
Use **CSF 2.0** if the organisation already reports cyber risk that way, **ISO/IEC 42001** if it wants a certifiable
AI management system, and a **crosswalk** so one piece of evidence serves several frameworks.
</div>

</div>

## A crosswalk you can reuse

The same control satisfies several frameworks; the value of a crosswalk is that you write the evidence once.

| Control you actually built | ATLAS technique it addresses | AI 100-2 category | OWASP LLM risk | AI RMF function |
|---|---|---|---|---|
| Pre-ranking tenant filter in retrieval | Gather RAG-Indexed Targets (AML.T0064); RAG Poisoning (AML.T0070) | Privacy / integrity | Vector and Embedding Weaknesses (LLM08:2025) | Measure, Manage |
| Session-derived tool arguments | AI Agent Tool Invocation (AML.T0053) | Integrity / abuse | Excessive Agency (LLM06:2025) | Map, Manage |
| Artefact digest verified against an independent root | AI Supply Chain Rug Pull (AML.T0109) | Integrity | Supply Chain (LLM03:2025) | Govern, Measure |
| Output filter before a sink | LLM Response Rendering (AML.T0077) | Integrity | Improper Output Handling (LLM05:2025) | Protect-equivalent in CSF |
| Per-principal query quotas | Cost Harvesting (AML.T0034) | Availability | Unbounded Consumption (LLM10:2025) | Manage |

Technique identifiers are ATLAS's; the OWASP identifiers are the 2025 edition's (`LLM01:2025` … `LLM10:2025`).
Most organisations will hold a crosswalk like this in a spreadsheet and update it when an edition changes. Doing so
once is worth more than citing five frameworks in a report.

## Version discipline

Frameworks move. Every page here records the edition and the access date, and says what has been superseded.
Two rules keep a course honest:

1. **Cite the edition, not just the name.** "OWASP Top 10 for LLM Applications" without a year is ambiguous
   between three editions with different items.
2. **Mark historical material as historical.** The 2023 OWASP list and the 2023 NIST AML taxonomy are still
   useful for understanding how the field's language developed; they are not current guidance.

The [references page](../references.md#framework-watch) carries the change log for this course, and
`python scripts/check_links.py` verifies that the links on these pages still resolve.

## How to apply a framework in one page

A framework earns its place only if it changes a decision. The pattern that works, in any of the seven:

1. **Choose the scope.** One system, one release, one data flow. A framework applied to "the organisation" produces
   a document nobody uses.
2. **Map its items to your components.** For each item: does this component exist, and who owns it? Items with no
   owner are the finding.
3. **Record the gap, not the aspiration.** "No artefact verification at serving" is a gap; "we plan to adopt zero
   trust" is a slogan.
4. **Attach evidence to each claim.** A test, a configuration, a signed artefact, a measurement.
5. **State the residual.** What the framework does not cover for your system, and who accepted it.

The [capstone proposals](../capstone/proposals/index.md) and [major projects](../projects/major/index.md) are
structured so that this mapping is part of the deliverable rather than an appendix.
