---
title: ISO/IEC AI and security standards
description: Which ISO/IEC standards matter for AI security, what they actually contain, and why none of them is law.
---

# ISO/IEC AI and security standards

## What they are

ISO/IEC publishes international standards. Five matter most for this course, and they do different jobs:

| Standard | Title | Published | Job |
|---|---|---|---|
| **ISO/IEC 42001:2023** | Information technology — Artificial intelligence — Management system | December 2023 | Requirements for an AI management system (AIMS). **Certifiable** |
| **ISO/IEC 23894:2023** | Information technology — Artificial intelligence — Guidance on risk management | February 2023 | Guidance on integrating AI risk management into organisational risk processes |
| **ISO/IEC 27001:2022** | Information security, cybersecurity and privacy protection — Information security management systems — Requirements | October 2022 | Requirements for an ISMS. **Certifiable** (and one amendment published) |
| **ISO/IEC 22989:2022** | Information technology — Artificial intelligence — Artificial intelligence concepts and terminology | July 2022 | Shared vocabulary for AI systems |
| **ISO/IEC 5338:2023** | Information technology — Artificial intelligence — AI system life cycle processes | December 2023 | Life-cycle process model for AI systems |

Two things follow from that table and are worth stating plainly:

- **42001 and 27001 are management-system standards.** They specify how an organisation governs a domain —
  policy, roles, risk assessment, objectives, internal audit, continual improvement — not which technical control to
  implement for prompt injection. Certification audits the management system, not your model.
- **The standards are copyrighted.** You can read the scope and structure from ISO's catalogue, but the text must be
  purchased. This course describes control areas and never reproduces clause text.

## Why they matter

1. **Procurement.** Enterprise and public-sector buyers increasingly ask for ISO/IEC 42001 or 27001 as evidence of a
   managed approach, and contracts may require them.
2. **Structure for the boring half of security.** Policy, competence, documented decisions and internal audit are
   what make a control survive staff turnover. The management-system standards are good at that.
3. **Vocabulary stability.** 22989 makes terms mean the same thing across an organisation's documents; 5338 gives a
   life-cycle model that maps cleanly onto the [major projects](../projects/major/index.md).

## When they are used

- Certification or readiness for it (42001, 27001).
- Building an AI governance function: who approves a model, how risk is assessed, how incidents feed improvement.
- Mapping an existing ISMS to AI activities (27001 plus 42001's AI-specific expectations).
- Contractual assurance: "supplier shall maintain an AI management system meeting ISO/IEC 42001".

## Not law

ISO/IEC standards are **voluntary**. They become binding only when:

- legislation or a regulator adopts or references them,
- a contract requires them, or
- an organisation adopts them in its own policy.

Certification is a business decision. It evidences a management system at a point in time, not the security of a
particular model. Do not let a slide say "ISO 42001 compliant, therefore the assistant is secure" — that is the same
category error as "we have a firewall, therefore we are secure".

!!! note "The one binding instrument in this collection"

    The [EU AI Act](../frameworks/index.md#guidance-standard-law-know-which-you-are-holding) is a regulation, not a
    standard. It creates legal obligations for in-scope providers and deployers on a staged timetable. ISO/IEC
    standards may be used to demonstrate conformity, but the obligation comes from the regulation.

## How to apply 42001 without drowning in it

A student or small team does not implement a full AIMS. The useful subset:

1. **Scope statement.** Which AI systems, which parts of the organisation. One page.
2. **Roles and accountability.** Who owns the model, who owns the data, who accepts residual risk, who can stop
   deployment. Names, not functions.
3. **Risk assessment method.** Reuse [AI RMF Map/Measure](nist-ai-rmf.md) or the course's threat-model template;
   the standard requires a method, not a specific one.
4. **Life-cycle controls.** Requirements, design, data, build, test, deploy, monitor, retire — with the evidence each
   stage produces. [SSDF](ssdlc.md) supplies the build-stage practices.
5. **Supplier management.** Model providers, data suppliers, hosting. What you require, how you verify it.
6. **Incident and improvement.** The incident record changes a control, not just a narrative.
7. **Internal audit and management review.** One honest review a year beats a binder.

That subset is also the skeleton of the course's [assurance pack](../capstone/index.md#deliverables), which is
deliberate: a capstone that produces these artefacts is most of the way to a small AIMS.

## How 23894 and 5338 help in practice

- **23894** gives risk-management guidance that aligns with ISO 31000. Use it when an organisation already runs
  enterprise risk and needs to place AI risk inside it rather than in a separate register.
- **5338** gives a life-cycle process model. Use it to check that a project has not skipped a stage — most student
  projects skip *operation and retirement*, and the monitoring and deletion work in
  [P4](../projects/major/p04-rag-assistant.md) exists to fill that hole.

## Worked crosswalk on the course

| Course artefact | ISO/IEC hook |
|---|---|
| Threat model and risk register with owners | 23894 guidance; 42001 risk assessment |
| Model card and data provenance | 42001 life-cycle and supplier expectations; 22989 vocabulary |
| Release gate with evidence | 5338 verification processes; [SSDF](ssdlc.md) practices |
| Incident record that changes a control | 42001 improvement; 27001 incident management |
| DPIA-style assessment | 42001 impact assessment expectations; GDPR where applicable |

## Limitations to state

- Management-system certification does not test your model's robustness, injection resistance or privacy leakage.
- Standards lag the research: agent security and RAG isolation are thinly covered, so supplement with
  [ATLAS](mitre-atlas.md), [OWASP](owasp.md) and current papers ([research](../research/index.md)).
- The text is paywalled, which makes it hard for students to verify secondary summaries; cite clause areas
  carefully and say when you are relying on a summary.
- Voluntary status means "we follow ISO" is a claim about intent unless certified, and certification is a claim
  about a management system, not a deployment.

## Where it appears in this course

[Module 19](../modules/19-governance-and-ethics.md) (governance and assurance),
[Module 20](../modules/20-deployment-and-capstone.md) (release gates and traceability), and the
[capstone](../capstone/index.md).

## Sources

1. ISO/IEC, *ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system*.
   <https://www.iso.org/standard/42001> (catalogue record, accessed November 2026).
2. ISO/IEC, *ISO/IEC 23894:2023 — Information technology — Artificial intelligence — Guidance on risk management*.
   <https://www.iso.org/standard/77304.html> (accessed November 2026).
3. ISO/IEC, *ISO/IEC 27001:2022 — Information security, cybersecurity and privacy protection — Information security
   management systems — Requirements*. <https://www.iso.org/standard/54534.html> (accessed November 2026).
4. ISO/IEC, *ISO/IEC 22989:2022 — Artificial intelligence — Concepts and terminology*.
   <https://www.iso.org/standard/74296.html> (accessed November 2026).
5. ISO/IEC, *ISO/IEC 5338:2023 — Artificial intelligence — AI system life cycle processes*.
   <https://www.iso.org/standard/81118.html> (accessed November 2026).
6. European Parliament and Council, *Regulation (EU) 2024/1689 (Artificial Intelligence Act)*, in force
   1 August 2024. <https://eur-lex.europa.eu/eli/reg/2024/1689> (consolidated text; check application dates).
