# Module coverage report

**20 modules, all present, all complete.** Each module page was parsed for front matter, section headings, prose volume, diagrams, inline mathematics, tables and Python. All measurements are from the files as they stand, not from any earlier report.

## 1. The section contract

Every one of the 20 pages carries the same 16 `##` sections, in the same order:

`Introduction · Learning objectives · Prerequisites · Detailed explanations · Key terminology · Mathematical foundations · Step-by-step: … · Real-world scenarios · Python walkthrough · Security implications · Detection and mitigation · Practical exercises · Knowledge check · Frameworks, research and cases · Summary · References`

There is no exception and no missing section. The "Step-by-step" heading is module-specific (e.g. "Step-by-step: your first security assessment") while keeping the prefix, which is what a navigation-oriented reader expects.

## 2. Per-module measurements

| # | Module | Words | Mermaid | Inline maths | Python blocks | Tables |
|---|---|---|---|---|---|---|
| 01 | introduction | 3488 | 1 | 17 | 1 | 4 |
| 02 | ml-security-fundamentals | 3018 | 1 | 15 | 1 | 4 |
| 03 | cybersecurity-fundamentals | 3284 | 1 | 18 | 1 | 5 |
| 04 | threat-modeling | 3026 | 2 | 12 | 1 | 6 |
| 05 | secure-data-management | 2913 | 1 | 32 | 1 | 6 |
| 06 | adversarial-ml | 2961 | 1 | 48 | 1 | 5 |
| 07 | data-poisoning | 3322 | 1 | 29 | 1 | 4 |
| 08 | evasion-and-robustness | 2900 | 1 | 48 | 1 | 3 |
| 09 | model-privacy | 2996 | 1 | 46 | 1 | 4 |
| 10 | model-extraction | 2901 | 1 | 18 | 1 | 5 |
| 11 | llm-security | 2938 | 1 | 14 | 1 | 4 |
| 12 | prompt-injection | 2897 | 1 | 15 | 1 | 6 |
| 13 | rag-security | 2900 | 1 | 10 | 2 | 4 |
| 14 | agent-security | 3002 | 1 | 21 | 2 | 4 |
| 15 | fine-tuning-supply-chain | 2905 | 1 | 12 | 1 | 4 |
| 16 | secure-ai-apis | 2863 | 1 | 20 | 1 | 5 |
| 17 | red-teaming | 3012 | 1 | 27 | 1 | 6 |
| 18 | monitoring-and-response | 3104 | 1 | 31 | 1 | 5 |
| 19 | governance-and-ethics | 3100 | 1 | 10 | 1 | 6 |
| 20 | deployment-and-capstone | 3171 | 1 | 19 | 1 | 7 |

Range: 2,863–3,488 words; 1–2 diagrams; 10–48 inline maths expressions; 1–2 Python blocks; 3–7 tables. Front matter is present on all 20 with six keys each (`title`, `description`, `sas_module`, `sas_level`, `sas_status`, `sas_hours`), and every module declares a level consistent with the four-level structure.

## 3. Substantiveness tests

**Duplication.** All 190 module pairs were compared with 8-token shingles. **No pair exceeds 0.10 similarity**; the highest pairs are adjacent modules that legitimately share vocabulary (06/08 on evasion, 12/13 on LLM trust boundaries). No module is a copy of another with the nouns changed.

**Superficiality.** Every module's `Detailed explanations` section carries several named subsections with prose paragraphs rather than bullet stubs; the mathematics sections use displayed equations, not just symbols in text; the "Frameworks, research and cases" section names specific documents (NIST AI RMF, OWASP LLM/ML Top 10, ISO/IEC 42001 and 23894, MITRE ATLAS, EU AI Act, GDPR, plus named papers) instead of gesturing at "industry frameworks".

**Levels.** Level 1 (M01–M05) is conceptual and control-oriented; Level 2 (M06–M10) is measurement-heavy (evasion, poisoning, privacy, extraction); Level 3 (M11–M15) covers LLM, RAG, agents, fine-tuning supply chain; Level 4 (M16–M20) covers interface hardening, red teaming, monitoring, governance and release. The progression is real: the same loan/clinical/referral case study recurs and is re-analysed with the tools of the current level, which is what gives the course coherence.

## 4. Findings

| Severity | Finding |
|---|---|
| Medium | Module cards on 12 pages said "1 lab" while the module has two. **Fixed**: cards now say "2 labs" for M03, M05, M06, M07, M08, M09, M11, M12, M13, M16, M17, M19. |
| Low | Each module page carries only one Python block (two in M13, M14). The runnable depth is in the notebooks, and each page links to its notebook and lab, so this is a deliberate split — but a reader who stays inside the module pages sees very little code. |
| Low | 56 search-index entries (mostly index pages) have no body text and are findable only by title. |

No module is missing, none is a stub, none fails its own stated contract. The coverage claim "20 modules in four levels" is accurate as written.
