# Phase 14 report — publication hardening

**Date:** 17 November 2026
**Scope:** close the warnings left by the Task 13 audit without rewriting validated teaching content.
**Verdict: PASS WITH WARNINGS.** Every finding that could be closed inside the repository is closed and re-verified. Two warnings remain, and both need the owner: the licence decision, and the first GitHub Actions run (which cannot happen until you push).

Nothing was committed, staged, branched, tagged, pushed, published, deployed, or changed in any remote or GitHub setting. The working tree holds all changes; the repository still has zero commits on `master`.

---

## 1. What changed

| # | Work | Result |
|---|---|---|
| 1 | Pages workflow | Triggers on `master`; dispatch retained; permissions and SHA pins untouched; `actionlint` clean |
| 2 | Licensing decision document | `LICENSING_DECISION.md` prepared; **no licence file created** |
| 3 | Laboratory safety | Five lab-specific sections added to all 32 briefs (160 sections), 22-section template |
| 4 | Dependency reproducibility | 12 direct dependencies pinned to validated versions, 5 unused packages removed, resolution verified |
| 5 | MCQ quality | 74 items rebalanced, 76 options rewritten; builder gate now silent |
| 6 | Notebook output policy | Kept outputs, bounded them, enforced with `scripts/check_notebooks.py` in CI |
| 7 | Render-driven defect | Generated quiz front matter was invalid YAML and printed as page text — found in the browser, fixed at the generator |
| 8 | Documentation alignment | 9 files corrected where they described dependencies that no longer exist |

### 1.1 The defect the browser found

The Task 13 audit checked the site by build, link check and a handful of pages; it did not open a quiz page. Opening one in Phase 14 showed the page beginning with `title: Module 09 quiz — … description: …` as visible text, above the real title.

Cause: `assessments/build.py` wrote front matter as `title: {title}` unquoted, and a title containing a colon (`Model Privacy: Membership Inference`) is not valid YAML. MkDocs therefore discarded the whole metadata block and rendered it as content. It affected all 20 module quiz pages.

Fix: the generator now emits YAML-safe scalars (`json.dumps`, which is valid YAML) for `title` and `description`. All 28 files under `docs/quizzes/` parse with `yaml.safe_load` and carry a title; the rendered page no longer leaks metadata. This is the one place where the earlier "PASS" was too generous, and it is worth noting that no static check caught it — only looking at the page did.

---

## 2. Validation actually executed

Run in this order after the last edit, on Windows 11, Python 3.14.7, CPU only:

| Check | Command | Result |
|---|---|---|
| Strict build | `python -m mkdocs build --strict` | exit 0, 0 warnings |
| Internal links | `python scripts/check_links.py` | PASS, 194 links, 0 problems |
| Built-site verification | `python scripts/verify_site.py site --base-path /Securing-AI-Systems/` | PASS |
| Python syntax | `python -m compileall -q labs scripts assessments` | exit 0 |
| Lab solutions | all 32 executed | **32/32 exit 0** |
| Notebooks | all 34 executed with `nbclient` | **34/34 pass**, 279.8 s total, median 7.0 s |
| MCQ keys | 200 questions: page order ↔ embedded key ↔ printed key | **200/200 consistent, 0 issues** |
| MCQ quality gate | `python assessments/build.py` | 0 warnings |
| Notebook policy | `python scripts/check_notebooks.py` | PASS, 34 checked |
| Workflow lint | `actionlint 1.7.7` | exit 0 |
| Environment check | `python scripts/check_env.py` inside a venv | "Result: ready" |
| Dependency resolution | `pip install --dry-run -r requirements-labs.txt` | exit 0 |
| Security greps | secrets, `os.system`, `shell=True`, `verify=False`, unsafe `yaml.load` | no matches |
| Rendered site | home, labs, M11, quiz M09, environment, attribution at `/Securing-AI-Systems/` | 200, one `h1`, no overflow, metadata leak gone |

No validation rule was loosened. The MCQ gate thresholds in `assessments/build.py` are unchanged; the content was changed to satisfy them.

---

## 3. Fixed findings

| Finding from Task 13 | Status |
|---|---|
| D-09 workflow triggers on `main` while the branch is `master` | **fixed** — `branches: [master]` and `if: github.ref == 'refs/heads/master'` |
| D-05 labs lacked cleanup, acceptable-use and scope sections | **fixed** — 32 briefs × 5 lab-specific sections |
| D-06 lab dependencies were ranges, not pins | **fixed** — 12 pins, resolution and environment check verified |
| D-07 answer-length cue in M09/M11/M13/M15/M16/M17 | **fixed** — plus M18, M19, M20, M01, M07; gate silent |
| D-08 notebooks committed with outputs against the guide | **policy settled** — outputs kept and bounded, guide and CI updated |
| D-15 Ollama absent from requirements | **documented** — explained in the requirements file and the environment page (still optional, still outside pip) |
| D-10 `mkdocs.yml` needs a YAML-aware loader | unchanged by design; the build is the proof |
| D-12 56 titles-only search entries | unchanged; acceptable for index pages |
| D-01 no licence | **decision document prepared**; owner decision outstanding |

---

## 4. Remaining warnings

1. **Licence undecided (owner).** `LICENSING_DECISION.md` sets out MIT / CC BY 4.0 / CC0 and the institutional question. No `LICENSE` file was created, and nothing in the site claims a licence. Until this is signed, the course can be published and read but not reused.
2. **The Pages deployment has never run.** The workflow is linted and its steps pass locally, but `deploy-pages` is unexercised until the first push. This is the only item that cannot be closed without publishing.
3. **36 MCQ items still show a size gap** in M03–M08, M10, M12 and M14. No module trips the builder's gate (which fires above 50 % of items), so the gate is silent, but the individual items are not clean. `MCQ_QUALITY_REPORT.md` lists them as the remaining backlog.
4. **The new lab sections are unreviewed prose.** They were written from each lab's own data and verified for accuracy against its dataset section, but a human should read a sample before students do — the same standard the course applies to everything else.
5. **Committed notebook outputs** are now an explicit policy with a checker, not an accident. They remain up to 145 KB per notebook.

---

## 5. Items requiring owner approval

| Item | Why it needs you |
|---|---|
| Licence (MIT / CC BY 4.0 / CC0) | A legal decision about your work and your employer's rights; cannot be delegated to a tooling session |
| Institutional IP position | Whether the University of the Punjab claims rights over teaching material created in employment |
| Whether to keep the derived digits dataset | It is third-party (CC BY 4.0) and must never be described as CC0 |
| Branch name | You are pushing to `master`; the workflow now matches it. If you rename the branch, change the workflow in the same commit |

---

## 6. Tests not possible without publishing

- A real Actions run (build job, artifact upload, Pages deployment, OIDC handshake).
- The live GitHub Pages URL, its base path, HTTPS behaviour and caching headers.
- A second machine or operating system: all runtime evidence here is Windows 11 / CPython 3.14.7, CPU only.
- `pip install` from a genuinely empty environment with network: resolution was verified with `--dry-run`, and `check_env.py` passed in a venv that shares installed packages, but a full two-gigabyte download was not repeated in this phase.
- Screen-reader and cross-browser accessibility testing: the rendered inspection was structural (landmarks, one `h1`, alt text, keyboard-reachable nav, 390 px layout).

---

## 7. Files touched

**Workflow and policy:** `.github/workflows/pages.yml`, `CONTRIBUTING.md`, `.gitignore`.
**Dependencies and environment:** `requirements-labs.txt`, `requirements-dev.txt`, `scripts/check_env.py`, `docs/getting-started/environment.md`, `labs/README.md`, `DEVELOPMENT.md`, `COURSE_ARCHITECTURE.md`, `docs/index.md`, `docs/references.md`, `docs/attribution.md`, `ATTRIBUTION.md`.
**Labs:** 32 × `labs/student/Lxx/LAB.md`, `labs/VALIDATION_REPORT.md` (dated note), `docs/labs/index.md`.
**Assessment:** `assessments/build.py` (YAML-safe front matter), `assessments/data/module_m01,m07,m09,m11,m13,m15,m16,m17,m18,m19,m20.json`, regenerated `docs/quizzes/**`.
**New:** `scripts/check_notebooks.py`, `LICENSING_DECISION.md`, `LAB_SAFETY_REVIEW.md`, `DEPENDENCY_REPRODUCIBILITY_REPORT.md`, `MCQ_QUALITY_REPORT.md`, `FINAL_PUBLICATION_CHECKLIST.md`, this report.

Temporary artefacts outside the repository: `/tmp/sas-audit/*.json` (execution evidence), the `.pages-test/` copy used to render the site at its production base path (deleted), and `.venv-verify/` (deleted).
