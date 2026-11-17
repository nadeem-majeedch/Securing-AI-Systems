# Licensing

**Status: no licence has been applied. All rights are reserved until the owner records a decision here and the licence files are added.**

**Document ID:** `SAS-LIC-001`
**Phase:** TASK 11 — licensing, attribution and repository documentation
**Prepared:** 17 November 2026
**Prepared for:** the course owner — Engr. Dr. Muhammad Nadeem Majeed, Professor, Department of Data Science (PUCIT), University of the Punjab, Lahore
**Decision required before:** the first public release, any DOI or institutional repository deposit, or any reuse by a third party

This file is a recommendation and a decision record. It does not grant anything. It audits what the repository currently says about licensing, inventories every category of material in the repository, recommends a licence for each, states the consequences of that recommendation honestly, and lists what must be true before the licence files are created.

---

## 1. What the repository currently declares

The audit below is the result of reading the files, not of assuming a default. Nothing was added or changed in this step.

| Source | What it currently says | Consistent? |
|---|---|---|
| `LICENSE`, `LICENSE-CODE`, `COPYING*` | **Absent.** No licence file exists anywhere in the repository | — |
| `README.md` §23 "Copyright and licensing" | "Licence undecided": the README records that no licence has been approved, that all rights are reserved until one is, and that §3 of this file recommends CC BY 4.0 + MIT + CC0 for the owner's decision | Internally consistent: the README now points at the recommendation instead of proposing a conflicting licence, and the owner's decision is still the open item |
| `mkdocs.yml` → `copyright` | "Course content © Muhammad Nadeem Majeed · Department of Data Science (PUCIT), University of the Punjab, Lahore" | Consistent with "all rights reserved"; a copyright notice is not a licence |
| `overrides/partials/copyright.html` | Footer line: "Course materials are under review; see the repository for licence status." | Consistent |
| `docs/references.md` closing note | "the licence is pending final approval by the course owner … Until it is recorded, all rights are reserved." | Consistent |
| `docs/attribution.md` | Student-facing summary of the same status | Consistent (added in this task) |
| `REPOSITORY_AUDIT.md` F-06 | Records that the repository has no licence and treats it as a High-severity gap | Consistent |
| `DEVELOPMENT_ROADMAP.md` D-01 | "Content licence" is an open blocking decision for the owner | Consistent — still open |
| `README.md` badge | `licence-pending approval` | Consistent |
| Third-party material | No third-party licence text, dataset copy, paper, or image is redistributed in the repository | Consistent — see §5 |

**Conclusion of the audit.** There is **no existing licence decision to honour, revoke or relicense**. There is one recorded *proposal* (CC BY-NC-SA 4.0 + MIT) in the README, and the course owner is the only rights holder on record. Nothing has been released, so no downstream user holds rights that a decision here could take away.

**One thing the audit cannot settle from inside the repository:** the instructor is a university employee. Many institutions claim ownership of, or a licence over, teaching material created in the course of employment, and some require approval before a public licence is applied. This must be checked against the University of the Punjab's intellectual-property policy (or a written confirmation from the department) before a licence is recorded. Until then the safe position is the current one: all rights reserved.

---

## 2. Inventory of material in the repository

Every category below was located in the file tree. The inventory is exhaustive at directory level; it is the basis for the recommendations in §3.

| # | Category | Where it lives | Volume | Rights position |
|---|---|---|---|---|
| 1 | **Original source code** — laboratory starters and solutions, dataset generators, environment and link checkers, assessment builder, progress/quiz/diagram scripts, stylesheets | `labs/student/*/starter.py`, `labs/solutions/*/solution.py`, `labs/scripts/`, `scripts/`, `assessments/build.py`, `docs/assets/javascript/`, `docs/assets/stylesheets/` | 83 Python files, 4 JavaScript files, 2 stylesheets | Created for this course; owner-held |
| 2 | **Original educational content** — module prose, exercises, quizzes and answer keys, assignments, projects, capstone briefs, case-study write-ups, framework and research pages, glossary, rubrics, Mermaid diagrams, navigation and site copy | `docs/**` except `docs/assets/` and `docs/notebooks/`, `COURSE_ARCHITECTURE.md`, root documentation | 157 Markdown pages, plus 31 repository documents | Created for this course; owner-held |
| 3 | **Original synthetic datasets** — admissions, patients, transactions, referrals, API logs, RAG documents, tool requests, and two model bundles (clean and tampered) | `labs/datasets/` | 5 CSVs, 2 JSON files, 1 NumPy archive and 2 model bundles | Generated deterministically by `labs/scripts/make_datasets.py` (seed 2026); no real people, no scraped rows |
| 4 | **Third-party dataset (derived)** — `digits_subset.npz`, a compressed extract of the optical-recognition handwritten-digits set shipped with scikit-learn (`sklearn.datasets.load_digits`) | `labs/datasets/digits_subset.npz` | 1,797 images | **Not owner-held.** Comes from the UCI ML Repository via scikit-learn's bundled copy; see `ATTRIBUTION.md` |
| 5 | **Research papers and referenced materials** — citations, identifiers, short quotations | `docs/references.md`, `docs/research/`, module "further reading" | No PDFs, no abstracts reproduced wholesale | Third-party; cited, never relicensed |
| 6 | **Images, diagrams and external resources** — no third-party images; all diagrams authored as Mermaid source; theme icons vendored by MkDocs Material | `docs/**` (Mermaid fences), `docs/assets/javascript/vendor/mermaid.min.js` | 0 images, 38 diagrams | Diagrams are owner-held; Mermaid is MIT; icons MIT/Apache-2.0 |
| 7 | **Third-party libraries** — documentation build and laboratory stack | `requirements-docs.txt`, `requirements-dev.txt`, `requirements-labs.txt` | See `ATTRIBUTION.md` §4 | Permissive; each keeps its own terms |

Two facts follow from the inventory and shape the recommendation:

- **There is essentially no third-party material to relicense.** Everything a student reads is original, except the citations and the one derived digits dataset. A permissive course licence is therefore unusually clean here.
- **The code and the prose are interleaved in the same pages.** A notebook cell, a code block inside a module, and a `starter.py` file can contain the same snippet. The licence model must say which layer wins, or readers will be unsure whether they may reuse a code sample they found in a lesson.

---

## 3. Recommended licensing model

The proposal under consideration — MIT for code, CC BY 4.0 for content, CC0 1.0 for synthetic data — is coherent, widely used for open courseware, and legally compatible across the three layers. **The recommendation is to adopt it, subject to the four conditions in §4.**

| Material | Recommended licence | Why this one | What a reader may then do |
|---|---|---|---|
| **Original source code** | **MIT** | Shortest permissive licence that is understood by every toolchain and procurement office; compatible with every dependency in `requirements-labs.txt` (MIT, BSD, Apache-2.0); no copyleft obligation on a student's own project | Use, modify, distribute and sell the code, including inside proprietary work, provided the copyright notice and permission notice travel with it. No warranty |
| **Original educational content** | **CC BY 4.0** | The standard licence for open educational resources: reuse, translation, remixing and commercial use allowed, with attribution. It is the licence most university repositories and OER catalogues expect | Copy, adapt, translate and teach from the material, including commercially, with credit, a licence link, and an indication of changes |
| **Original synthetic datasets** | **CC0 1.0** | Data needs the least friction possible: a student or researcher must be able to merge, relabel and redistribute a synthetic table without a compliance review. CC0 waives copyright and neighbouring rights and needs no attribution | Anything, with no conditions. Attribution is requested by the course as a courtesy, not as a legal term |
| **Third-party datasets** | **Unchanged — their own terms** | The course cannot relicense what it does not own. The single derived dataset is documented and its origin retained | Whatever the upstream terms allow. The course states the origin so a reader can check |
| **Research papers and referenced materials** | **Cited, never redistributed** | Papers carry their own licences (often arXiv's non-exclusive licence, sometimes CC BY, sometimes publisher-exclusive). Reproduction would require a per-paper review | Read the source at the publisher's or arXiv's site; cite it. Short quotations remain quotations |
| **Images, diagrams and external resources** | **CC BY 4.0 for original diagrams; third-party assets stay with their owners** | Diagrams were authored for the course in Mermaid source, so the content licence can cover them. No third-party image is bundled, so nothing needs clearing | Reuse a diagram with attribution under CC BY 4.0; icons and Mermaid remain under MIT/Apache-2.0 |

### 3.1 The content licence: CC BY 4.0 versus the earlier CC BY-NC-SA 4.0 proposal

An earlier README draft proposed **CC BY-NC-SA 4.0**. The README now records the licence as undecided and points here; the alternative stays available and is set out below, because it is a defensible policy and not a wrong one. The owner should choose deliberately, because the two options produce materially different courses.

| Question | CC BY 4.0 (recommended) | CC BY-NC-SA 4.0 (current proposal) |
|---|---|---|
| Can another university teach from it? | Yes, with attribution | Yes, if the use is non-commercial. Whether a publicly funded degree is "non-commercial" is genuinely contested, which is why many institutions refuse NC material |
| Can a student reuse a paragraph in a thesis or a paid internship report? | Yes, with attribution | Probably, but the student has to reason about it. NC creates hesitation where none should exist |
| Can a publisher sell a printed edition? | Yes, with attribution | No |
| Can a company train staff on it internally? | Yes, with attribution | Arguably no — commercial use is excluded |
| Can a translator post an adaptation under a different licence? | Yes, if changes are indicated | Only under the same NC-SA terms (ShareAlike) |
| Counts as "open" under the common OER definitions (and the UNESCO recommendation) | Yes | No — NC and SA are excluded by several definitions, including the one most OER catalogues apply |
| Protects against a commercial competitor packaging the course | No | Partly |
| Attribution and no-endorsement still apply | Yes (§3 of the licence) | Yes |

**Recommendation: CC BY 4.0.** The course exists to be studied by students who may work in industry, and to be adopted by departments that have no budget. NC makes both audiences pause, and in practice NC licences are frequently ignored rather than respected, which produces worse attribution than a permissive licence does. The commercial-resale worry is real but smaller than it looks: attribution is required in every case, the instructor and the University keep their names on the official edition, and the repository remains the canonical, maintained version. A reseller competes with a free download and must credit the author while doing so.

If the owner prefers the protective option, CC BY-NC-SA 4.0 remains available and consistent with the existing README text. Nothing else in this document changes: the code and data recommendations are independent.

### 3.2 The code/content boundary

A single rule, stated here so that pages do not need to repeat it:

> **Code is MIT; prose is CC BY 4.0. Where they are mixed on one page, the code is MIT and the text around it is CC BY 4.0.**

Concretely:

| Artefact | Licence |
|---|---|
| `*.py`, `*.js`, `*.css`, shell snippets, `mkdocs.yml`, `requirements*.txt`, the assessment builder | MIT |
| Code blocks and runnable cells inside a lesson or notebook | MIT — a reader may lift a snippet into their own project |
| The prose, exercises, quiz items, rubrics and explanations *around* that code | CC BY 4.0 |
| A Jupyter notebook as a whole (prose cells plus code cells) | Mixed: prose CC BY 4.0, code MIT. The notebook file itself may be redistributed under either, because both licences permit redistribution |
| Synthetic CSVs, JSON fixtures and generated model bundles | CC0 1.0 |
| `digits_subset.npz` | Third-party; see `ATTRIBUTION.md` |

This is the arrangement used by several large open courseware projects, and it is why the recommendation keeps MIT for code rather than putting everything under CC BY: a student who copies an attack implementation into a commercial security tool should not have to attribute a licence notice in their product's about box for a 15-line function, and a company's legal review should not have to read a Creative Commons deed to approve one.

### 3.3 What the recommended licences do not grant

Stated plainly, because licensing documents that only list permissions mislead:

- **No trademark or endorsement right.** CC BY 4.0 §3(a)(1)(B) and the MIT notice give no permission to use the instructor's name, the course name, or the University's name and marks to imply endorsement of a derivative, a training product or a consultancy. A translated or modified edition must say so.
- **No warranty.** The material teaches offensive security techniques and will be used on real systems by someone. Neither licence offers any warranty of fitness, accuracy or safety; the disclaimers in both licences do the work, and `SECURITY.md` and the academic-integrity page carry the expectations.
- **No patent licence beyond what each licence states.** MIT is silent on patents; CC BY 4.0 §2(b)(2) expressly does not license patent or trademark rights. The synthetic data contains no patented method, and the code implements published techniques whose patents, if any, belong to their authors.
- **No rights in third-party material.** A citation is not a sublicence. Frameworks, standards, papers, libraries and the derived digits dataset remain under their own terms.
- **No rights over a student's own work.** Lab reports, projects and capstones written by students belong to their authors (and possibly their institution), not to the course. The course cannot license them and does not claim to.

---

## 4. Conditions that must hold before the licence is recorded

The recommendation is not an instruction to write `LICENSE` files today. Four conditions come first.

1. **Owner sign-off.** Recorded in §6 below. The content licence is the one decision that cannot be delegated to a tooling session; the code and data recommendations should still be confirmed in the same record so that all three layers move together.
2. **Institutional position confirmed.** The department or university IP office confirms that the instructor may license the material, or names the approval that is required. If the institution claims ownership, the licence needs its consent; if it claims a non-exclusive licence, the CC BY grant should be checked against it.
3. **The third-party register is complete.** `ATTRIBUTION.md` must list every library, dataset and referenced framework before a licence claims to cover "the course". It does, as of this task; it must stay that way (see `CONTRIBUTING.md` §6).
4. **The derived dataset is decided.** Either keep `digits_subset.npz` and rely on the attribution entry, or regenerate the laboratory data from the synthetic generator alone. Keeping it is defensible — the digits set is publicly distributed and widely reused in teaching — but the repository must not imply that CC0 covers it. The register says so explicitly.

---

## 5. Third-party material: what is never relicensed

This is a hard constraint, not a preference.

| Material | Owner | What the course may do | What it must never do |
|---|---|---|---|
| ISO/IEC standards (42001, 23894, 27001, 22989, 5338) | ISO / IEC | Describe control areas, cite clause numbers and titles, link to the catalogue | Reproduce text, tables or figures; redistribute a purchased copy |
| NIST publications (AI 100-1, AI 600-1, AI 100-2e2025, CSWP 29, SP 800-218, SP 800-61r3 …) | US Government | Quote with attribution; NIST works are not copyrighted in the US | Imply NIST endorsement of the course |
| OWASP, MITRE ATLAS | OWASP Foundation, MITRE | Cite item and technique identifiers; link | Redistribute their lists as if course-authored; use their marks as branding |
| EU AI Act, GDPR | European Union | Quote minimally under EUR-Lex reuse terms with attribution | Present the course text as legal advice |
| Research papers | Their authors and publishers | Cite, link, quote briefly with attribution | Host PDFs, reproduce figures, paraphrase closely without citation |
| `digits_subset.npz` | UCI ML Repository / scikit-learn distribution | Use in the laboratory, record origin and the upstream terms | Claim it under CC0 or CC BY; remove the provenance note |
| Libraries in `requirements*.txt` | Their maintainers | Depend on them, vendor where necessary (Mermaid) | Strip their notices; relicense the vendored file |
| University and department names | University of the Punjab | State the affiliation factually | Licence the marks; imply institutional endorsement of a derivative |

---

## 6. Owner decision record

To be completed by the course owner. One line per decision; nothing is applied until every line is recorded.

| ID | Decision | Recommendation | Owner's decision | Date |
|---|---|---|---|---|
| D-01a | Licence for original educational content | **CC BY 4.0** (alternative: CC BY-NC-SA 4.0, §3.1) | ☐ approve CC BY 4.0 ☐ keep CC BY-NC-SA 4.0 ☐ defer | |
| D-01b | Licence for original source code | **MIT** | ☐ approve ☐ defer | |
| D-01c | Licence for original synthetic datasets | **CC0 1.0** | ☐ approve ☐ defer | |
| D-01d | Derived digits dataset: keep with attribution, or regenerate | **Keep, documented** | ☐ keep ☐ regenerate ☐ defer | |
| D-01e | Institutional IP confirmation obtained | **Required before publication** | ☐ confirmed ☐ outstanding | |
| D-01f | Attribution wording for derivatives ("not endorsed by …") | **Required in the licence notice** | ☐ approve ☐ defer | |

Signed: ______________________  (course owner)   Date: ____________

---

## 7. What happens after approval

The steps are listed here so the owner can see the cost of approval — it is about an hour of work, not a project.

1. Add `LICENSE` (MIT, code), `LICENSE-CONTENT` (CC BY 4.0, prose) and `LICENSE-DATA` (CC0 1.0, synthetic data), each with the full licence text, a scope line naming which paths it covers, and the copyright line.
2. Add SPDX identifiers where files support them — `# SPDX-License-Identifier: MIT` at the top of Python and JavaScript sources — and a short "Licensing" section in `README.md` replacing §23's pending text.
3. Add a "Licensing" block to `docs/attribution.md`: the three licences, the scope table from §3.2, and a link to the licence files. Keep the student page short and link to this document for the reasoning.
4. Update the footer line in `overrides/partials/copyright.html` and the `licence-pending approval` badge in `README.md`.
5. Record the change in `CHANGELOG.md` and close D-01 in `DEVELOPMENT_ROADMAP.md`.
6. Re-run `python -m mkdocs build --strict` and `python scripts/check_links.py`, then confirm the published site shows the licence on the home page and in the footer.

**Deliberately not done in this task:** no `LICENSE` file was created, no `copyright` field was changed, no badge was altered, and no page claims a licence. The repository still says "all rights reserved", which is the correct statement while D-01a–D-01f are open.

---

## 8. If the owner decides not to publish under an open licence

A valid outcome, and worth stating so the decision is a real one. The course would then be published as an all-rights-reserved website with an explicit permission for classroom and personal study, something like: *"You may read, study and teach from this material. You may not redistribute or republish it without written permission."* In that case:

- `LICENSE` files are not created; `README.md` §23 becomes the permission statement.
- The attribution and academic-integrity obligations in this task still apply unchanged.
- The course remains citable, but not reusable — which is the difference that most affects translation, archiving and adoption by other departments.

---

*Related: `ATTRIBUTION.md` (third-party register), `docs/attribution.md` (student-facing summary), `SECURITY.md`, `CODE_OF_CONDUCT.md`, `docs/getting-started/academic-integrity.md`.*
