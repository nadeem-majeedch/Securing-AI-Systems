# Third-Party Attribution Register

**Document ID:** `SAS-ATTR-001`
**Maintained with:** `requirements-docs.txt`, `requirements-dev.txt`, `requirements-labs.txt`
**Last reviewed:** 17 November 2026

Everything in the course that was not written for the course is recorded here, with its licence and the obligation that licence places on the course. If a file in this repository uses third-party material that is not in this register, that is a defect — see §11.

**What this register is for.** Two things that are easy to get wrong and expensive to fix later:

1. **The course must not claim to license what it does not own.** `LICENSING.md` recommends CC BY 4.0 and CC0 for original material; those licences stop at the boundary of everything below.
2. **Attribution must be findable.** A student writing an essay, a department adopting the course, or a publisher checking reuse can see here what came from where.

**Two registers exist, deliberately.** This file is the technical register: versions, licences, paths and obligations. The student-facing summary is [Credits and attribution](docs/attribution.md) — shorter, no version churn, and part of the website. Sources cited in the teaching text live in [References](docs/references.md) and the four research cluster pages; this register does not duplicate the bibliography.

---

## 1. Frameworks, standards and guidance

All of these are **cited and described, never reproduced**. No text, table, figure or checklist from any of them is copied into the course.

| Material | Owner | Terms | Used in | Obligation met by |
|---|---|---|---|---|
| OWASP Top 10 for LLM Applications (2023–24, 2025, 2026 editions) | OWASP Foundation | OWASP content is published under CC BY-SA 4.0; item names and identifiers are cited | Modules 11–14, framework page, quizzes | Citation with edition and link; no item text reproduced |
| OWASP Machine Learning Security Top 10 (2023) | OWASP Foundation | CC BY-SA 4.0 (project content) | Modules 05–10 | Citation and link |
| OWASP API Security Top 10 (2023) | OWASP Foundation | CC BY-SA 4.0 | Module 12, 16 | Citation and link |
| OWASP Top 10 CI/CD Security Risks | OWASP Foundation | CC BY-SA 4.0 | Module 15 | Citation and link |
| OWASP RAG Security Cheat Sheet | OWASP Foundation | CC BY-SA 4.0 | Module 13 | Citation and link |
| MITRE ATLAS | The MITRE Corporation | MITRE terms of use; trademark of MITRE | Modules 04, 06–20; framework page | Technique and tactic identifiers cited by ID; ATLAS is not presented as course-authored; no MITRE logo or branding used |
| NIST AI RMF 1.0 (AI 100-1, 2023) and Generative AI Profile (AI 600-1) | NIST (US Government) | US Government work, not subject to copyright in the US | Modules 04, 18, 19, 20 | Quoted with attribution; no implication of NIST endorsement |
| NIST AI 100-2e2025 adversarial ML taxonomy (and superseded 100-2e2023) | NIST | US Government work | Modules 06–10 | Definitions paraphrased with citation; superseded edition labelled as such |
| NIST CSF 2.0 (CSWP 29, 2024) | NIST | US Government work | Module 03, framework page | Citation and link |
| NIST SP 800-218 and SP 800-218A (SSDF) | NIST | US Government work | Modules 11, 15, 20 | Practice identifiers cited (PO, PS, PW, RV) |
| NIST SP 800-30r1, 800-53r5, 800-61r3, 800-188, AI 800-1 (draft) | NIST | US Government work | Modules 04, 05, 10, 18 | Citation; draft status stated where applicable |
| ISO/IEC 42001:2023, 23894:2023, 27001:2022, 22989:2022, 5338:2023 | ISO and IEC | **Copyrighted; must be purchased.** No reproduction permitted | Modules 03, 19, 20; framework page | Control areas described in the course's own words, clause titles cited, links to the ISO catalogue. **No text or table reproduced** |
| Regulation (EU) 2024/1689 (AI Act) | European Union | EUR-Lex reuse terms; attribution required | Modules 19, 20 | Quoted minimally, with the ELI link; described at the level of structure, not as legal advice |
| Regulation (EU) 2016/679 (GDPR) | European Union | EUR-Lex reuse terms | Module 10, 19 | Principles paraphrased with citation |
| OECD Recommendation on AI | OECD | OECD terms of use | Module 19 | Citation and link |
| CVE records (CVE-2023-48022, CVE-2025-32711, CVE-2025-8217) | MITRE / CNA of record | CVE terms of use | Case studies C04, C06, C09 | Identifier and link only |

## 2. Research papers

The course cites 43 core papers in its bibliography, plus the annotated entries on the four research cluster pages, the standards and frameworks in §1, and the primary sources for the ten case studies. Reproducing all of them here would duplicate the bibliography without adding a licence fact, so the policy is stated once and the bibliography does the attribution.

| | |
|---|---|
| **Where cited** | `docs/references.md` (summary bibliography), `docs/research/*.md` (annotated entries with venue and identifier), every module's "further reading" section |
| **What is used** | Bibliographic details, and short paraphrase or quotation of findings |
| **What is not used** | PDFs, figures, tables, abstracts reproduced in full, or substantial verbatim text |
| **Terms** | Each paper keeps its own licence — arXiv's non-exclusive licence, CC BY, or a publisher agreement. The course makes no claim over any of them and grants none |
| **Obligation** | Author, title, venue, year and identifier (arXiv ID, DOI or proceedings link) at every citation. Where a claim is contested, the course names the competing result instead of picking a winner silently |

**Case studies.** The ten documented cases cite primary sources in `docs/references.md` §"Case study sources" — vendor advisories, CVE records, regulator decisions and one court decision. News reports and vendor blogs are linked, not reproduced, and each case page states its evidence status (confirmed breach, mitigated vulnerability, researcher demonstration, or hypothetical) because the difference matters to a student's risk judgement.

## 3. Quotation and fair-use posture

| Material | How it is used | Why it is defensible |
|---|---|---|
| One-sentence quotations from papers | Inline, with quotation marks and a citation | Short quotation for criticism and teaching, attributed |
| NIST definitions | Quoted with attribution | US Government works carry no copyright in the US |
| EU legal text | Short phrases quoted, with the ELI link | EUR-Lex reuse decision permits reuse with attribution |
| ISO/IEC clause titles | Referenced, never quoted | Titles and identifiers are facts; the text is licensed |
| Court decision (2024 BCCRT 149) | Facts and outcome summarised, with a CanLII link | Judicial decisions are published; the summary is the course's own |

No material is included on the assumption that "educational use" makes copyright irrelevant. Where a quotation was not clearly permitted, the course paraphrases instead.

## 4. Code libraries

### 4.1 Documentation build (`requirements-docs.txt`)

| Package | Pinned version | Licence | Obligation |
|---|---|---|---|
| MkDocs | 1.6.1 | BSD-2-Clause | Retain copyright and licence notice in redistributed source; no endorsement claim |
| MkDocs Material | 9.8.0 | MIT | Retain notice if the theme is redistributed |
| pymdown-extensions | 12.3 | MIT | Retain notice |

### 4.2 Development and quality assurance (`requirements-dev.txt`)

| Package | Pinned version | Licence | Obligation |
|---|---|---|---|
| pytest | 9.1.1 | MIT | None beyond notice retention |
| pytest-cov | 7.1.0 | MIT | None beyond notice retention |
| nbformat | 5.10.4 | BSD-3-Clause | Notice retention |
| PyYAML | 6.0.2 | MIT | Notice retention |
| ruff | 0.14.3 | MIT | Notice retention |

These are never installed in a student's environment and none of their code is shipped in the built site.

### 4.3 Laboratory stack (`requirements-labs.txt`)

Installed by the student, in the student's own virtual environment. The course distributes no part of them.

| Package | Pinned version | Licence | Notes |
|---|---|---|---|
| NumPy | 2.5.3 | BSD-3-Clause (with bundled components under 0BSD, MIT, Zlib, CC0) | — |
| pandas | 3.0.6 | BSD-3-Clause | — |
| scikit-learn | 1.9.1 | BSD-3-Clause | Also the source of the digits dataset — see §6 |
| matplotlib | 3.11.2 | PSF-based matplotlib licence (BSD-compatible) | — |
| SciPy | 1.18.1 | BSD-3-Clause | — |
| PyTorch | 2.14.1 | BSD-3-Clause | Wheels bundle third-party components under their own notices |
| safetensors | 0.8.0 | Apache-2.0 | Safe serialisation, Modules 09, 15 |
| JupyterLab | 4.6.6 | BSD-3-Clause | The student's own environment |
| ipykernel | 7.4.0 | BSD-3-Clause | Notebook kernel |
| pydantic | 2.13.5 | MIT | Request models in the Module 16 service exercise |
| FastAPI | 0.162.0 | MIT | The local inference service the Module 16 laboratory hardens |
| httpx | 0.28.1 | BSD-3-Clause | Client used to exercise that service |

`nbformat` and `nbclient` moved to `requirements-dev.txt` in Phase 14: they are validation tooling, not part of a
student's runtime. `torchvision`, `adversarial-robustness-toolbox`, `opacus`, `transformers` and `datasets` were
removed because no laboratory or notebook imports them; the techniques they would supply are implemented in the
course's own code.

**Apache-2.0 obligations.** If a student redistributes a derivative of safetensors, they must retain notices and state changes. The course's own code does not copy from these projects; it imports them, which places no notice obligation on the course's MIT-licensed code.

**What the course does not do:** it does not vendor, patch, fork or redistribute any laboratory dependency, and it does not ship a model or checkpoint from any of them.

## 5. Vendored JavaScript

One third-party runtime library is stored in the repository rather than fetched from a CDN, because a CDN request made every diagram disappear when the network was unavailable or blocked (see `CHANGELOG.md`, 0.9.0).

| Item | Version | Licence | Path | Modification |
|---|---|---|---|---|
| Mermaid | 11.17.2 | MIT | `docs/assets/javascript/vendor/mermaid.min.js` | Vendored unmodified from the published minified distribution. No local edits, no stripped notices |
| ↳ DOMPurify (bundled inside Mermaid) | 3.4.12 | Apache-2.0 OR MPL-2.0 | same bundle | Unmodified; its notice is retained inside the file |
| ↳ d3, KaTeX, marked, cytoscape, rough.js, lodash, dayjs (bundled inside Mermaid) | as shipped by Mermaid 11.17.2 | ISC (d3), MIT (others) | same bundle | Unmodified |

**Obligation.** The MIT and Apache-2.0 notices of these components are retained in the vendored file, and this row is the attribution. The bundle is loaded only on pages that contain a diagram (`docs/assets/javascript/diagrams.js` checks for a diagram before loading it). No other third-party JavaScript is executed by the site.

**Not used:** Google Fonts, Google Analytics, any tag manager, any advertising or session-recording script, any CDN, any icon webfont.

## 6. Datasets

| Dataset | Origin | Licence | Distributed in this repository | Obligation |
|---|---|---|---|---|
| Admissions, patients, transactions, referrals, API logs, RAG documents, tool requests | Written for this course. Deterministic generator: `labs/scripts/make_datasets.py`, seed 2026 | Recommended CC0 1.0 (pending owner approval — `LICENSING.md`) | **Yes** — `labs/datasets/*.csv`, `*.json` | Attribution is requested by the course as a courtesy, not required by CC0 |
| Clean and tampered model bundles (`model_bundle/`, `model_bundle_tampered/`) | Generated for this course by the same script | Recommended CC0 1.0 (pending approval) | **Yes** — `labs/datasets/model_bundle*/` | As above |
| `digits_subset.npz` — 1,797 8×8 handwritten-digit images | **Third-party.** Test set of the UCI *Optical Recognition of Handwritten Digits* database, donated by E. Alpaydin and C. Kaynak (Bogaziçi University, 1998), shipped inside scikit-learn and re-exported by `make_datasets.py` | **CC BY 4.0** (UCI Machine Learning Repository, dataset 80) | **Yes** — `labs/datasets/digits_subset.npz` | Attribution to Alpaydin and Kaynak, the dataset title, the UCI link and the CC BY 4.0 notice; changes indicated (re-exported to a compressed NumPy archive, images only, targets retained) |
| Any other dataset | — | — | **No** | The course downloads no dataset. `make_datasets.py` states "Nothing is downloaded", and the notebooks load no remote data |

**This is the one place where the recommended open licences stop.** `digits_subset.npz` is not the course's to license. It may be redistributed because CC BY 4.0 allows it, provided the attribution above travels with it — which is why the notice is repeated in `docs/attribution.md`, in Module 08's laboratory page, and here.

**Attribution text to reuse verbatim:**

> Optical Recognition of Handwritten Digits, E. Alpaydin and C. Kaynak (1998), UCI Machine Learning Repository, <https://archive.ics.uci.edu/dataset/80/optical+recognition+of+handwritten+digits>, licensed CC BY 4.0. Re-exported as an 8×8 image array with targets in this course's laboratory data.

**No personal data.** The synthetic tables contain no real people, no real organisations and no records derived from a real dataset. The digits images are of anonymous handwriting samples collected for research in 1998; they carry no identifiers.

## 7. Images, diagrams and icons

| Item | Status |
|---|---|
| Photographs, screenshots of third-party products, stock images | **None in the repository.** The site contains no raster images at all |
| Diagrams | All authored for this course as Mermaid source in the page that displays them. Original; covered by the recommended content licence (CC BY 4.0) |
| Icons in the header, navigation, admonitions and footer | Supplied by MkDocs Material (MIT). The icon artwork is Material Design Icons, Apache-2.0. Not redistributed as separate files; delivered by the theme |
| Favicon | Material's default, or none; no third-party logo is used |
| University, framework and vendor logos | **Not used.** Frameworks are named in text. Naming a framework is nominative use, not a trademark licence |
| Fonts | System font stack (`Segoe UI`, `SF Pro`, `Inter`, `Arial`). No webfont is downloaded and no font is redistributed |

If a diagram, screenshot or photograph is added later, it gets a row here before it is published, with its source and licence. A screenshot of a third-party product is not automatically reusable — the vendor's terms decide.

## 8. Code samples attributed to their sources

| Sample | Position |
|---|---|
| Attack and defence implementations (FGSM, PGD, poisoning, membership inference, extraction, injection) | Written for this course from the published algorithms; each module cites the originating paper (§2). No verbatim third-party implementation is recorded in this register |
| Instrumented examples adapted from a library's documentation | None recorded. If one is added, it goes in this table with the project, version, licence and a note on what changed |
| Student-contributed code | Recorded in the pull request that adds it, credited in the module's "further reading" or acknowledgements, and added here if it carries a licence obligation |

A negative entry is a claim, so it is checkable: `grep -rn -e SPDX -e Copyright -e "adapted from" labs scripts docs/assets --include=*.py --include=*.js` returns nothing today. If it stops returning nothing, this section is out of date.

## 9. Names, marks and affiliation

- **University of the Punjab**, **PUCIT** and **Department of Data Science** are named to state the instructor's affiliation. No licence to these marks is granted by the course, and no derivative may imply that the University endorses it.
- **OWASP**, **MITRE**, **ATLAS**, **NIST**, **ISO**, **IEC**, **Hugging Face**, **PyTorch** and product names appear as nominative references. They are the property of their owners.
- The course name **Securing AI Systems** and the instructor's name identify the official edition. A modified or translated edition must say that it is modified and must not imply endorsement (CC BY 4.0 §3(a)(1)(B)).

## 10. Verification

Run when a dependency is added or upgraded, and before every publication:

```bash
# What is actually installed, and under what licence
python - <<'PY'
import importlib.metadata as m
for name in ["mkdocs", "mkdocs-material", "pymdown-extensions", "numpy", "pandas",
             "scikit-learn", "torch", "safetensors", "fastapi", "httpx"]:
    try:
        md = m.metadata(name)
        print(f"{name:32s}", md.get("License-Expression") or (md.get("License") or "")[:40])
    except Exception:
        print(f"{name:32s} not installed in this environment")
PY

# Every pinned package must appear in this register
grep -hE "^[a-zA-Z]" requirements-docs.txt requirements-dev.txt requirements-labs.txt | grep -v "^#"

# Confirm the vendored bundle still has its notices
grep -c "DOMPurify" docs/assets/javascript/vendor/mermaid.min.js
```

**Release check.** `DEPLOYMENT.md` §4 requires this register to be current before a site is published. A dependency that is not in this file blocks the release, not the other way round.

## 11. Adding material

From `CONTRIBUTING.md` §6: any pull request that adds a library, a dataset, an image, a diagram from elsewhere, or a code sample adapted from another project must add a row to the appropriate table here **in the same change**, with the licence and the obligation. If the licence is unclear, the material does not go in.

---

*Related: `LICENSING.md` (what the course itself is licensed under), [Credits and attribution](docs/attribution.md) (student-facing), [References](docs/references.md) (the bibliography), `SECURITY.md`.*
