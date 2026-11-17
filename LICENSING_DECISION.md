# Licensing decision — for owner approval

**Prepared:** 17 November 2026 · **Status:** awaiting the owner's decision · **Not yet applied**

This is the decision paper, not the decision. **No `LICENSE` file has been created**, `mkdocs.yml` still says
© all rights reserved, and the site footer still says the licence is under review. Nothing below takes effect until
you sign §6 and ask for the files to be added.

Background, inventory and the full legal reasoning are in `LICENSING.md`; this page is the one to read if you have
ten minutes.

---

## 1. What you are deciding

Three licences, one per layer of the course, plus one position on material you do not own.

| Layer | Recommendation | Why |
|---|---|---|
| **Original source code** — lab starters and solutions, dataset generator, site scripts, assessment builder, JavaScript and CSS | **MIT** | Shortest permissive licence every toolchain, procurement office and student understands. Compatible with every dependency in the stack (BSD, MIT, Apache-2.0). A student can lift an attack implementation into their own project, including a commercial one, if they keep the notice. |
| **Original educational material** — module prose, exercises, quizzes, keys, assignments, projects, rubrics, diagrams, site copy | **CC BY 4.0** | The standard open-courseware licence. Another department can teach from it, a student can quote it in a thesis, a translator can adapt it, all with attribution. It is what OER catalogues and university repositories expect. |
| **Original synthetic datasets** — the CSVs, JSON fixtures and generated model bundles in `labs/datasets/` | **CC0 1.0** | Data needs the least friction. A student must be able to merge, relabel and redistribute a synthetic table without a compliance review, and a waiver is the only licence that delivers that. Attribution is requested as a courtesy, not imposed as a term. |
| **Third-party material** | **Unchanged — their terms** | You cannot license what you do not own. This is a constraint, not a choice: see §4. |

A reader can always tell which applies, because the rule is stated once and repeated nowhere: **code is MIT, prose is
CC BY 4.0, synthetic data is CC0, and third-party material stays with its owner.** Where code and prose share a page —
a notebook, or a code block inside a lesson — the code is MIT and the surrounding text is CC BY 4.0.

---

## 2. Why these three and not something simpler

**Why not one licence for everything?** CC BY on source code creates attribution obligations in every downstream
product's about box for a fifteen-line function, and MIT on prose gives no attribution requirement for a course you
may spend years maintaining. Splitting them is what open courseware projects converged on, and it is what a
company's legal review expects to see.

**Why not CC BY-NC-SA 4.0?** It is a defensible choice and the README proposed it in an earlier draft. It is not
recommended because "non-commercial" is genuinely ambiguous for a publicly funded university (the NC clause may
exclude exactly the audience the course is for), because it makes students hesitate to quote the course in paid work,
and because NC-SA material is excluded from several OER definitions. If you prefer it, nothing else in this document
changes — only the text licence.

**Why CC0 for the data?** The datasets are synthetic, contain no personal data, and exist to be manipulated. Any
licence with conditions on them slows a student down for no benefit to you.

---

## 3. What each licence permits and requires

| | MIT (code) | CC BY 4.0 (content) | CC0 1.0 (data) |
|---|---|---|---|
| Copy and redistribute | Yes | Yes | Yes |
| Modify and adapt | Yes | Yes, with changes indicated | Yes |
| Commercial use | Yes | Yes | Yes |
| Attribution required | Copyright and permission notice must travel | Credit, licence link, changes indicated | Not required |
| Share-alike | No | No | No |
| Warranty | None | None | None |
| Trademark / endorsement rights | Not granted | Not granted (§3) | Not applicable |

Two consequences worth stating plainly, because licensing pages that only list permissions mislead:

- **No endorsement.** Neither licence lets anyone use your name, the course name, or the University's name to imply
  that a derivative, a training product or a consultancy is endorsed. A modified edition must say it is modified.
- **No warranty, and no safety claim.** The course teaches offensive technique. The licences disclaim fitness and
  accuracy; `SECURITY.md` and the academic-integrity page carry the expectations instead.

---

## 4. Third-party material — never relicensed

| Material | Position |
|---|---|
| `labs/datasets/digits_subset.npz` | A derived extract of the UCI handwritten-digits set distributed with scikit-learn, **CC BY 4.0**, credited in `ATTRIBUTION.md`. It must never be described as CC0 or course-owned. Kept, or regenerated from the synthetic generator if you prefer a single-provenance repository. |
| Python libraries | Their own licences (BSD-3-Clause, MIT, Apache-2.0). Imported, not redistributed; `ATTRIBUTION.md` §4 lists each with its obligation. |
| Mermaid (vendored) | MIT, kept with its notices; it bundles DOMPurify and d3 under their own terms. |
| ISO/IEC standards | Cited by clause and title only. Never quoted, never redistributed. |
| NIST, OWASP, MITRE ATLAS, EU AI Act, GDPR | Cited and linked; short quotations only, with attribution. |
| Research papers | Cited with venue and identifier; no PDFs hosted, no figures reproduced. |
| University and department names | Used factually to state affiliation; not licensed, not used to imply endorsement. |

The register in `ATTRIBUTION.md` is complete as of this phase and is enforced by `CONTRIBUTING.md` §9: a new
dependency or dataset without a register row blocks a pull request.

---

## 5. Institutional and copyright considerations

You are a university employee, and that is the one question this repository cannot answer from the inside. Many
institutions claim ownership of, or a non-exclusive licence over, teaching material created in the course of
employment; some require approval before a public licence is applied. Before a licence is recorded, one of these
should be true:

- a written confirmation from the department or the University's IP office that you may license the material; or
- a named approval process that has been completed; or
- a statement that the institution claims no rights in this material.

If the institution claims ownership, the licence needs its consent. If it claims a non-exclusive licence, the CC BY
grant should be checked against it. Until one of those is in hand, the current position — copyright, all rights
reserved, free to read — is the correct and safe one.

Practical note: the course is currently unpublished. There is no existing licence to revoke, no downstream user whose
rights a decision would remove, and no relicense problem. This is the easiest moment you will ever have to make it.

---

## 6. Decision record — to be completed by the owner

| ID | Decision | Recommendation | Your decision | Date |
|---|---|---|---|---|
| D-01a | Licence for original educational material | CC BY 4.0 (alternative: CC BY-NC-SA 4.0) | ☐ approve ☐ alternative ☐ defer | |
| D-01b | Licence for original source code | MIT | ☐ approve ☐ defer | |
| D-01c | Licence for original synthetic datasets | CC0 1.0 | ☐ approve ☐ defer | |
| D-01d | Derived digits dataset | Keep, documented as third-party CC BY 4.0 | ☐ keep ☐ regenerate ☐ defer | |
| D-01e | Institutional IP confirmation | Required before any licence is applied | ☐ confirmed ☐ outstanding | |
| D-01f | "Not endorsed by" wording in the licence notice | Required | ☐ approve ☐ defer | |

Signed: ______________________ (course owner)  Date: ____________

---

## 7. If you approve: what will be added, in one pass

Roughly an hour of work, all of it mechanical:

1. `LICENSE` (MIT, covering code), `LICENSE-CONTENT` (CC BY 4.0, covering prose and diagrams) and `LICENSE-DATA`
   (CC0 1.0, covering synthetic datasets), each with the full licence text, a scope line naming the paths it covers,
   and the copyright line.
2. `# SPDX-License-Identifier: MIT` headers on Python and JavaScript sources.
3. README §23 replaced by a short "Licensing" section; `mkdocs.yml` copyright line and
   `overrides/partials/copyright.html` updated so the site footer states the licence.
4. A "Licensing" block on `docs/attribution.md` pointing at the three files, and one line in `CHANGELOG.md`.
5. `python -m mkdocs build --strict`, `python scripts/check_links.py` and `python scripts/verify_site.py site` re-run,
   then a check that the footer and the home page show the licence.

**If you decide against an open licence**, that is also a legitimate outcome: the course stays all-rights-reserved
with an explicit permission to read, study and teach from it, and no licence files are created. The attribution
obligations and the third-party register stay exactly as they are.

**Nothing in this phase created a licence file, changed a copyright line, or altered a badge.** The repository still
says "licence undecided", which remains true until you sign above.
