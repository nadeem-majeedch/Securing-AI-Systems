---
title: References
description: Primary sources, frameworks, standards and tooling used throughout the course, with versions and access dates.
---

# References

Primary sources for the course. Every framework claim in a module traces back to an entry here, and every framework
has a full treatment in the [framework reference section](frameworks/index.md).

**Version discipline.** These materials change. Each framework entry records the edition and access date that the
course text was written against. When an entry moves, the affected modules are reviewed — see the framework watch
table at the end of this page.

**On standards.** ISO/IEC documents are copyrighted and must be purchased; the course describes their control areas
and never reproduces their text. NIST publications are US Government works and are quoted with attribution. EU legal
text is quoted minimally under EUR-Lex reuse terms.

**On obligation.** Only regulation creates legal obligation. Frameworks and standards in this list are voluntary
unless a law, regulator or contract adopts them; the
[guidance/standard/law table](frameworks/index.md#guidance-standard-law-know-which-you-are-holding) states which is
which.

## Frameworks and knowledge bases

**OWASP** — *Top 10 for LLM Applications*, 2026 edition.
:   Current edition, published August 2026. **This course's item-level tables use the 2025 list**, because the 2026
    ten items could not be verified against the published text at the time of writing; the 2026 edition is noted as
    current with revised ordering. Check the resource page before citing item numbers.
    <https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/> · accessed November 2026.
    Full treatment: [OWASP Top 10 for LLM Applications](frameworks/owasp.md).

**OWASP** — *Top 10 for LLM Applications*, 2025 edition.
:   The ten application risks used in modules 11–14, from prompt injection (`LLM01:2025`) to unbounded consumption
    (`LLM10:2025`). <https://genai.owasp.org/llm-top-10/> · accessed November 2026.

**OWASP** — *Top 10 for LLM Applications*, 2023–24 edition.
:   Historical. Retained because many papers and vendor documents still cite its numbering; superseded by the 2025
    list. <https://genai.owasp.org/llm-top-10-2023-24/> · accessed November 2026.

**OWASP** — *Machine Learning Security Top 10*, 2023.
:   Risk categories for classical ML systems: poisoning, supply chain, evasion, privacy and denial of service.
    <https://owasp.org/www-project-machine-learning-security-top-10/> · accessed November 2026.

**OWASP** — *API Security Top 10*, 2023.
:   Used in Module 12 for inference API hardening. <https://owasp.org/API-Security/> · accessed November 2026.

**OWASP** — *Top 10 CI/CD Security Risks*.
:   Used in Module 11 for pipeline hardening. <https://owasp.org/www-project-top-10-ci-cd-security-risks/> · accessed
    November 2026.

**OWASP** — *RAG Security Cheat Sheet*.
:   Per-chunk permissions, authorisation at retrieval, tenant isolation. Guidance, not research.
    <https://cheatsheetseries.owasp.org/cheatsheets/RAG_Security_Cheat_Sheet.html> · accessed November 2026.

**MITRE ATLAS** — *Adversarial Threat Landscape for Artificial-Intelligence Systems*.
:   Living knowledge base of adversary tactics and techniques against AI systems, structured like ATT&CK. At the
    November 2026 access date the site reported 16 tactics, 221 techniques, 44 mitigations, 77 case studies,
    44 entities and 37 software entries. <https://atlas.mitre.org/> · living, accessed November 2026.
    Full treatment: [MITRE ATLAS](frameworks/mitre-atlas.md).

**NIST** — *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023.
:   The Govern, Map, Measure, Manage structure used in Modules 04, 18 and 19. <https://doi.org/10.6028/NIST.AI.100-1>
    Full treatment: [NIST AI RMF](frameworks/nist-ai-rmf.md).

**NIST** — *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile*, NIST
AI 600-1, July 2024.
:   Generative-AI-specific risks, including prompt injection, confabulation and information integrity.
    <https://doi.org/10.6028/NIST.AI.600-1>

**NIST** — *AI RMF Playbook*.
:   Practical suggested actions per framework function. <https://www.nist.gov/itl/ai-risk-management-framework/ai-rmf-playbook>

**NIST** — *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*, NIST AI 100-2e2025,
March 2025.
:   **Current AML taxonomy**, superseding AI 100-2e2023. Covers predictive and generative AI; defines attacker goals,
    objectives, capabilities and knowledge. <https://doi.org/10.6028/NIST.AI.100-2e2025> · record and errata:
    <https://csrc.nist.gov/pubs/ai/100/2/e2025/final>
    Full treatment: [NIST adversarial machine learning taxonomy](frameworks/nist-aml.md).

**NIST** — *Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations*, NIST AI 100-2e2023.
:   **Superseded.** Cited only for version history; do not use its definitions in new work without checking the 2025
    text.

**NIST** — *The NIST Cybersecurity Framework (CSF) 2.0*, NIST CSWP 29, February 2024.
:   Six functions including Govern; profiles, tiers and informative references.
    <https://doi.org/10.6028/NIST.CSWP.29> · <https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final>
    Full treatment: [NIST Cybersecurity Framework 2.0](frameworks/nist-csf.md).

## Standards and secure development

**ISO/IEC 42001:2023** — *Information technology — Artificial intelligence — Management system*.
:   Requirements for an AI management system: governance, risk treatment, documented information, continual
    improvement. Certifiable as a management system; voluntary unless adopted. <https://www.iso.org/standard/42001>
    Full treatment: [ISO/IEC AI and security standards](frameworks/iso.md).

**ISO/IEC 23894:2023** — *Information technology — Artificial intelligence — Guidance on risk management*.
:   Risk-management guidance aligned with ISO 31000. <https://www.iso.org/standard/77304.html>

**ISO/IEC 27001:2022** — *Information security, cybersecurity and privacy protection — Information security
management systems — Requirements*.
:   The information-security management baseline that 42001 sits alongside. <https://www.iso.org/standard/54534.html>

**ISO/IEC 22989:2022** — *Artificial intelligence — Concepts and terminology*.
:   Shared vocabulary used to keep course terms consistent. <https://www.iso.org/standard/74296.html>

**ISO/IEC 5338:2023** — *Artificial intelligence — AI system life cycle processes*.
:   Life-cycle process model, used to check that a project has not skipped operation and retirement.
    <https://www.iso.org/standard/81118.html>

**NIST SP 800-218** — *Secure Software Development Framework (SSDF) Version 1.1*, February 2022.
:   Four practice groups: PO, PS, PW, RV. <https://csrc.nist.gov/pubs/sp/800/218/final>
    Full treatment: [Secure software development](frameworks/ssdlc.md).

**NIST SP 800-218A** — *Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: An
SSDF Community Profile*, July 2024.
:   Adds model and data provenance, training-data handling and model evaluation practices.
    <https://csrc.nist.gov/pubs/sp/800/218/a/final>

**NIST SP 800-218r1** — initial public draft, December 2025.
:   **Draft.** Not a requirement; cited only to note that a revision is in progress.
    <https://csrc.nist.gov/pubs/sp/800/218/r1/ipd>

**NIST AI 800-1** — *Managing Misuse Risk for Dual-Use Foundation Models*, initial public draft (second draft,
January 2025).
:   **Draft**, not final guidance. Cited in Module 20 for misuse-risk management practices, with draft status stated.
    <https://csrc.nist.gov/pubs/ai/800/1/ipd>

**NIST SP 800-30 Rev. 1** — *Guide for Conducting Risk Assessments*.
:   <https://doi.org/10.6028/NIST.SP.800-30r1>

**NIST SP 800-61 Rev. 3** — *Incident Response Recommendations and Considerations for Cybersecurity Risk Management*,
April 2025.
:   Current incident-response guidance, used in Module 18. <https://csrc.nist.gov/pubs/sp/800/61/r3/final>

**NIST SP 800-188** — *De-Identifying Government Datasets*, 2016.
:   De-identification practice and its limits, used in Module 10. <https://doi.org/10.6028/NIST.SP.800-188>

**NIST SP 800-53 Rev. 5** — *Security and Privacy Controls for Information Systems and Organizations*.
:   Control families referenced in Module 11. <https://doi.org/10.6028/NIST.SP.800-53r5>

## Regulation

**Regulation (EU) 2024/1689** — the Artificial Intelligence Act.
:   The only binding instrument in this collection. Risk tiers: prohibited, high-risk, transparency obligations,
    minimal risk, with a staged application timetable. **Check the consolidated text**: implementation dates for parts
    of the Act have been the subject of amendment proposals, and the course describes obligations at the level of
    structure, not as legal advice. <https://eur-lex.europa.eu/eli/reg/2024/1689>

**GDPR** — Regulation (EU) 2016/679.
:   Principles referenced in Module 10: lawfulness, data minimisation, storage limitation, and the rights of data
    subjects. The regulation is the authoritative text. <https://eur-lex.europa.eu/eli/reg/2016/679/oj>

**OECD** — *Recommendation of the Council on Artificial Intelligence*.
:   The AI principles that many national frameworks build on. <https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449>

## Case study sources

Primary records for the ten documented cases, listed by case. Full write-ups and evidence status:
[case studies](case-studies/index.md).

| Case | Primary source |
|---|---|
| C01 Bing prompt extraction | [Ars Technica report](https://arstechnica.com/information-technology/2023/02/ai-powered-bing-chat-spills-its-secrets-via-prompt-injection-attack/) |
| C02 ChatGPT cross-user exposure | [OpenAI postmortem](https://openai.com/index/march-20-chatgpt-outage/) |
| C03 torchtriton | [PyTorch advisory](https://pytorch.org/blog/compromised-nightly-dependency/) |
| C04 ShadowRay | [Oligo report](https://www.oligo.security/blog/shadowray-attack-ai-workloads-actively-exploited-in-the-wild) · [CVE-2023-48022](https://nvd.nist.gov/vuln/detail/CVE-2023-48022) |
| C05 Malicious hub models | [JFrog analysis](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/) · [HF pickle scanning](https://huggingface.co/docs/hub/security-pickle) |
| C06 EchoLeak | [MSRC advisory](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-32711) · [CVE-2025-32711](https://www.cve.org/CVERecord?id=CVE-2025-32711) |
| C07 CamoLeak | [Legit Security](https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code) |
| C08 DeepSeek database | [Wiz Research](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak) |
| C09 Amazon Q extension | [AWS bulletin AWS-2025-015](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/) · [CVE-2025-8217](https://www.cve.org/CVERecord?id=CVE-2025-8217) |
| C10 Air Canada | [2024 BCCRT 149 (CanLII)](https://www.canlii.org/en/bc/bc-crt/doc/2024/2024bccrt149/2024bccrt149.html) |

## Core papers

Full annotated entries, with venues and identifiers, are on the four
[research cluster pages](research/index.md). This list is the bibliography summary.

**Adversarial machine learning**
:   Szegedy, C. et al. "Intriguing properties of neural networks." ICLR 2014. arXiv:1312.6199.
:   Goodfellow, I., Shlens, J. and Szegedy, C. "Explaining and Harnessing Adversarial Examples." ICLR 2015. arXiv:1412.6572.
:   Kurakin, A., Goodfellow, I. and Bengio, S. "Adversarial examples in the physical world." ICLR Workshop 2017. arXiv:1607.02533.
:   Carlini, N. and Wagner, D. "Towards Evaluating the Robustness of Neural Networks." IEEE S&P 2017. doi:10.1109/SP.2017.49.
:   Madry, A. et al. "Towards Deep Learning Models Resistant to Adversarial Attacks." ICLR 2018. arXiv:1706.06083.
:   Athalye, A., Carlini, N. and Wagner, D. "Obfuscated Gradients Give a False Sense of Security." ICML 2018.
:   Croce, F. and Hein, M. "Reliable Evaluation of Adversarial Robustness with an Ensemble of Diverse Parameter-free Attacks." ICML 2020.

**Poisoning and backdoors**
:   Gu, T., Dolan-Gavitt, B. and Garg, S. "BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain." 2017. arXiv:1708.06733; journal version IEEE Access 7, 2019, doi:10.1109/ACCESS.2019.2909068.
:   Chen, X. et al. "Targeted Backdoor Attacks on Deep Learning Systems Using Data Poisoning." 2017. arXiv:1712.05526.
:   Biggio, B., Nelson, B. and Laskov, P. "Poisoning Attacks against Support Vector Machines." ICML 2012. arXiv:1206.6389.
:   Carlini, N. "Poisoning the Unlabeled Dataset of Semi-Supervised Learning." USENIX Security 2021.
:   Carlini, N. and Terzis, A. "Poisoning and Backdooring Contrastive Learning." ICLR 2022. arXiv:2106.09667.
:   Carlini, N. et al. "Poisoning Web-Scale Training Datasets is Practical." IEEE S&P 2024. doi:10.1109/SP54263.2024.00179.

**Privacy and extraction**
:   Shokri, R. et al. "Membership Inference Attacks Against Machine Learning Models." IEEE S&P 2017.
:   Fredrikson, M., Jha, S. and Ristenpart, T. "Model Inversion Attacks that Exploit Confidence Information and Basic Countermeasures." CCS 2015. doi:10.1145/2810103.2813677.
:   Tramèr, F. et al. "Stealing Machine Learning Models via Prediction APIs." USENIX Security 2016.
:   Abadi, M. et al. "Deep Learning with Differential Privacy." CCS 2016. doi:10.1145/2976749.2978318.
:   Carlini, N. et al. "Extracting Training Data from Large Language Models." USENIX Security 2021.
:   Carlini, N. et al. "Membership Inference Attacks From First Principles." IEEE S&P 2022. doi:10.1109/SP46214.2022.9833649.
:   Orekondy, T., Schiele, B. and Fritz, M. "Knockoff Nets: Stealing Functionality of Black-Box Models." CVPR 2019.
:   Carlini, N. et al. "Stealing Part of a Production Language Model." ICML 2024. PMLR 235.
:   Dwork, C. and Roth, A. *The Algorithmic Foundations of Differential Privacy.* 2014.

**Language models, RAG and agents**
:   Vaswani, A. et al. "Attention Is All You Need." NeurIPS 2017.
:   Lewis, P. et al. "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks." NeurIPS 2020.
:   Perez, F. and Ribeiro, I. "Ignore Previous Prompt: Attack Techniques For Language Models." 2022. arXiv:2211.09527.
:   Greshake, K. et al. "Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection." AISec '23. doi:10.1145/3605764.3623985.
:   Wei, A., Haghtalab, N. and Steinhardt, J. "Jailbroken: How Does LLM Safety Training Fail?" NeurIPS 2023.
:   Zou, A. et al. "Universal and Transferable Adversarial Attacks on Aligned Language Models." 2023. arXiv:2307.15043.
:   Zou, W. et al. "PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation." USENIX Security 2025.
:   Zhan, Q. et al. "InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents." Findings of ACL 2024.
:   Debenedetti, E. et al. "AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents." NeurIPS 2024 Datasets and Benchmarks.
:   Zhang, K. et al. "LLM Agents Should Employ Security Principles." 2025. arXiv:2505.24019.

**Supply chain and monitoring**
:   Ohm, M., Plate, H., Sykosch, A. and Meier, M. "Backstabber's Knife Collection: A Review of Open Source Software Supply Chain Attacks." DIMVA 2020. doi:10.1007/978-3-030-52683-2_2.
:   Zhao, J. et al. "Models Are Codes: Towards Measuring Malicious Code Poisoning Attacks on Pre-trained Model Hubs." ASE 2024. doi:10.1145/3691620.3695271.
:   Inan, H. et al. "Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations." 2023. arXiv:2312.06674.
:   Hung, K.-H. et al. "Attention Tracker: Detecting Prompt Injection Attacks in LLMs." Findings of NAACL 2025.
:   Sharma, M. et al. "Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming." 2025. arXiv:2501.18837.

**Data protection and engineering practice**
:   Sweeney, L. "k-anonymity: a model for protecting privacy." 2002.
:   Machanavajjhala, A. et al. "l-Diversity: Privacy Beyond k-Anonymity." 2006.
:   Sculley, D. et al. "Hidden Technical Debt in Machine Learning Systems." NeurIPS 2015.
:   Breck, E. et al. "The ML Test Score." IEEE Big Data 2017.
:   Mitchell, M. et al. "Model Cards for Model Reporting." FAT* 2019.
:   Shostack, A. *Threat Modeling: Designing for Security.* Wiley, 2014.

## Tooling

Tools change faster than papers. Versions are pinned in `requirements-labs.txt`; the catalogue below names what the
course uses and why, not a recommendation to install everything.

| Tool | Used in | Purpose |
|---|---|---|
| PyTorch | 04–10, 13 | Training and attack implementation |
| scikit-learn, NumPy, pandas, SciPy | measurement labs | Models, metrics and tabular handling |
| safetensors | 09, 13 | Safe model serialisation |
| FastAPI, pydantic, httpx | 14, 16 | The local prediction service and its client |
| A local vector store (in-memory) | 15 | Retrieval experiments |
| Ollama *(optional)* | 11 | One local-language-model demonstration |

## Framework watch

Revisions that would require a content review. Updated when any entry moves.

| Item | Edition in use | Next review trigger |
|---|---|---|
| OWASP Top 10 for LLM Applications | 2025 item list; 2026 edition noted as current | Item-level detail of the 2026 list |
| OWASP ML Security Top 10 | 2023 | New edition published |
| MITRE ATLAS | Living, accessed Nov 2026 | Annual review, or a new tactic family |
| NIST AI RMF | 1.0 (AI 100-1, 2023) | Revision published |
| NIST Generative AI Profile | AI 600-1 (2024) | Revision published |
| NIST AML taxonomy | **AI 100-2e2025** (2023 superseded) | Revision or errata beyond the published note |
| NIST CSF | **2.0 (CSWP 29, 2024)** | Revision published |
| NIST SSDF | **SP 800-218 v1.1** + 800-218A | SP 800-218r1 finalized |
| NIST AI 800-1 | Second public draft (Jan 2025) | Final publication |
| ISO/IEC 42001 | 2023 | Revision published |
| EU AI Act | Reg. (EU) 2024/1689 | Amendment, or new implementation guidance |

---

!!! note "Citing this course"

    Course content is intended for open educational use; the licence is pending final approval by the course owner.
    Until it is recorded, all rights are reserved. If you cite the course in academic work, cite the module and the
    date you accessed it, since modules are revised.

    [Credits and attribution](attribution.md) records what is original, what is third-party and under which terms, and
    gives the attribution required for the one dataset the course ships. The full legal position and the owner's
    decision record are in `LICENSING.md` in the repository; the complete register of libraries and frameworks is in
    `ATTRIBUTION.md`.
