# Final audit report — Securing AI Systems

**Audit date:** 17 November 2026
**Scope:** the entire repository — 20 module pages, 32 laboratories, 34 notebooks, 20 module quizzes plus four level papers and a final paper, 12 assignments, 10 mini projects, 6 major projects, 5 capstone proposals, the MkDocs site, the GitHub Pages workflow, security posture and licensing.
**Method:** measurement, not inspection of claims. Every page, lab, notebook, question and project file was parsed; every lab solution and every notebook was executed in a clean kernel; the built site was rebuilt and rendered. Evidence was written to `/tmp/sas-audit/` so the repository stays clean.

**Verdict: PASS WITH WARNINGS.**

No critical defect was found: every laboratory and notebook runs to completion, every assessment answer key agrees with what the site shows, the site builds without warnings under `--strict`, and there is no committed secret or unsafe default. The warnings are two content-accuracy classes — one now fixed (the site undercounted its own laboratories and published a stale lab catalogue) and one that is a decision only the owner can take (the course has no licence). Nothing was committed, staged, pushed, tagged, published or deployed, and no Git history, remote or GitHub setting was touched.

---

## 1. What was measured

| Area | Volume | Result |
|---|---|---|
| Module pages | 20 | All 20 complete against the 16-section contract; 2,863–3,488 words each |
| Laboratories | 32 | All 32 have brief, starter, separate solution and write-up; **32/32 solutions exit 0** |
| Notebooks | 34 | **34/34 execute end to end**, 3.0–18.1 s each, 250 s total |
| Module quizzes | 20 × 10 MCQ | **200/200** questions verified: page order, embedded key, key letter and key text all agree |
| Written items | 196 | 2 short + 2 conceptual + 2 scenario + 1 practical per module, plus papers |
| Assignments | 12 | Complete scenarios, requirements and rubrics |
| Mini / major / capstone | 10 / 6 / 5 | Complete structures; no cross-project duplication above 0.12 |
| Site | 157 pages, 244 files, 27 MB | `mkdocs build --strict` 0 warnings; 194 internal links 0 problems; `verify_site.py` PASS |
| Workflow | 1 | `actionlint` clean; SHA-pinned actions; least-privilege permissions |

Reproduction commands (all from the repository root, Python 3.14.7, Windows 11, CPU only):

```
python -m mkdocs build --strict
python scripts/check_links.py
python scripts/verify_site.py site --base-path /Securing-AI-Systems/
python -m compileall -q labs scripts assessments
```

---

## 2. Findings

Severity is about the effect on a student or on publication, not about effort to fix. "Fixed" means the correction is in the working tree, uncommitted, and re-verified by the checks in §3.

### High

**D-01 — No licence has been chosen (open, owner decision).**
There is no `LICENSE` file, and every page states that the material is under copyright with all rights reserved. `LICENSING.md` recommends CC BY 4.0 for text, MIT for code and CC0 for synthetic data, subject to institutional approval. Until the owner records a decision, the course **can** be published as a public website but **cannot** be described as open courseware, reused by another institution, or forked by a student for a portfolio — the site's own footer says as much. `LICENSING.md` §1 also flags an unresolved question the repository cannot answer: whether the University of the Punjab claims rights over teaching material created in employment. This is the single item that would keep a real launch brief from passing, and it is not resolvable by editing files.

**D-02 — The site described a different course from the one it ships (fixed).**
`docs/labs/index.md` said "Twenty laboratories, one per module", listed 20 labs with the status **Planned**, and its "What a lab contains" table described sections that do not exist in any `LAB.md` (Purpose, Threat model, Setup, Steps, Success criteria, Results table, Cleanup, Expected variance). The repository actually contains 32 released labs using a 17-section template, and the catalogue's numbering did not line up with the labs' own module fields (catalogue L11 = module 11; real L11 belongs to M07). Twelve module cards also said "1 lab" for modules that have two.
*Fixed:* the catalogue is regenerated from each `LAB.md` (number, real title, real module link, difficulty, budget), the status column and "Planned" text are gone, the section table now mirrors the real 17 sections, and the twelve module cards say "2 labs". Verified after the rewrite by a clean `--strict` build and a link check.

### Medium

**D-03 — Counts contradicted the inventory (fixed).** The README advertised 20 laboratories and 20 laboratory reports, and 8 scenario assignments; the assessment guide said 20 laboratory reports. The repository has 32 labs and 12 assignments. Counts corrected in `README.md` (5 places), `docs/index.md` (2), `docs/getting-started/index.md`, `docs/getting-started/assessment.md`.

**D-04 — "Offline after one download" was not true of the verified path (fixed).** The README and labs page claimed one download was needed. Nothing is downloaded on the core path: datasets are generated by `labs/scripts/make_datasets.py`, all 34 notebooks ran with no network access, and the only download anywhere is Ollama for one optional M11 section. Copy corrected to "fully offline".

**D-05 — Labs do not implement the "Cleanup" and per-lab safety sections the contributing guide requires (open).** `CONTRIBUTING.md` §5 and the old labs page promised a cleanup section and an acceptable-use statement in every lab; no lab has either. Safety is handled at module level and on the academic-integrity page, and cleanup does not matter for most labs because they write into a temporary directory. Either add two short sections to the 32 briefs or amend the contributor contract to match reality — the current split is the kind of gap an external reviewer treats as a documentation failure.

**D-06 — Lab dependencies are ranges, so "expected results" are only approximately reproducible (open).** `requirements-docs.txt` and `requirements-dev.txt` are exactly pinned and the workflow enforces it. `requirements-labs.txt` deliberately uses ranges (`torch>=2.4,<3`, `numpy>=2.1,<3`, …) with a note that exact pins will be recorded "when the laboratory phase is authored and each lab's expected results are frozen". Results were reproduced here on one machine (Python 3.14.7); a `pip install` six months from now may resolve different wheels, and the labs quote exact numbers (0.875 AUC, 0.063 robust accuracy). Recording a lockfile — at least in `docs/` as the validated environment — would close this.

**D-07 — Six modules have an answer-length cue in their multiple-choice items (open).** `assessments/build.py` runs its own quality check and warns that in M09, M11, M13, M15, M16 and M17 the correct option is materially longer than every distractor in 6–9 of 10 items. Nothing is wrong with the answers — every key is correct and unambiguous — but a student who notices can score without knowing the material. The nine-page key and the explanations are otherwise sound.

### Low

| ID | Finding | State |
|---|---|---|
| D-08 | All 34 notebooks are committed **with outputs**, although `CONTRIBUTING.md` says notebooks are committed with cleared outputs. Outputs are the course's own and were regenerated here; pick one policy. The labs page sentence claiming "no outputs from other people's machines" was corrected. | partly fixed |
| D-09 | `.github/workflows/pages.yml` triggers on `main`; this repository is on `master` with **zero commits**. If the first push mirrors the local branch name, Pages will not deploy until the branch is renamed or the trigger widened. `DEPLOYMENT.md` explains this, but it is an easy first-push failure. | open |
| D-10 | `mkdocs.yml` uses `!!python/name:` tags, so `yaml.safe_load` rejects it. That is correct for MkDocs and a trap only for ad-hoc tooling; the build itself proves the file is valid. | note |
| D-11 | `LICENSING.md` §1 quoted the README's superseded "pending final approval" text and a CC BY-NC-SA proposal the README no longer makes. Quotation updated to the current wording. | fixed |
| D-12 | 56 search-index entries are titles-only (link-heavy index pages). Search still returns them; acceptable. | note |
| D-13 | Module pages carry only one Python block each (two in M13, M14). Depth lives in the notebooks, and every module links to its notebook and lab — by design, but a reader who never leaves the module pages sees little runnable code. | note |
| D-15 | The M11 notebook's local-model section needs Ollama (~1 GB) and degrades gracefully without it; `ollama` is not in `requirements-labs.txt`, so the fallback should be stated in the notebook's setup cell. | open |
| D-16 | At 390 px, a handful of in-content links are under 24 px tall. Normal for prose links; not a navigation failure. | note |

### Informational

**D-14 — `pickle.load` appears once, on purpose.** `notebooks/M15/01-artefact-integrity.ipynb` loads a locally crafted pickle to show that loading executes code, then contrasts it with `safetensors`. Nothing is fetched, nothing outside the temp directory is touched, and the lesson is exactly the one the module teaches. This is the correct way to demonstrate the risk.

---

## 3. Verification performed after the fixes

| Check | Result |
|---|---|
| `mkdocs build --strict` | exit 0, no warnings, 6.8 s |
| `scripts/check_links.py` | 194 internal links, 0 problems, PASS |
| `scripts/verify_site.py site --base-path /Securing-AI-Systems/` | PASS (search index ok, 244 files, base path correct, 37 diagram pages) |
| README relative links | 0 missing |
| Rendered site | home, M01, M06, M11, M16, quiz M01, major project, capstone, labs index, prerequisites all HTTP 200 under `/Securing-AI-Systems/`; no horizontal overflow at 390 px; one `h1` per page; diagrams render as SVG; tables scroll rather than break the layout |
| Lab solutions | 32/32 exit 0, 1.2–10.7 s |
| Notebooks | 34/34 execute, 0 errors |
| MCQ integrity | 200/200 consistent across page, embedded key and printed key |

Not verified, and stated as a limitation: the GitHub Actions workflow was never executed (no commits exist), so `actionlint` and the local equivalents of its steps are the only evidence it works; no second machine or OS was used; no screen reader was run, so accessibility was checked structurally (landmarks, heading order, one `h1`, alt text, keyboard-reachable nav) rather than with assistive technology.

---

## 4. Owner handover checklist

Do these in order. Nothing here has been done for you.

1. **Decide the licence** (D-01). Read `LICENSING.md` §3, check your institution's IP policy, then add `LICENSE`, `LICENSE-code` and the `mkdocs.yml` copyright line. Do not describe the course as open until this is done.
2. **Review the uncommitted fixes** with `git status` and `git diff`. Everything below is in the working tree, uncommitted: `docs/labs/index.md`, 12 module pages, `docs/index.md`, `docs/getting-started/index.md`, `docs/getting-started/assessment.md`, `README.md`, `LICENSING.md`.
3. **Confirm the branch name** (D-09). Create or rename to `main` before pushing, or widen the workflow trigger, otherwise Pages stays dark.
4. **Decide the lab-section policy** (D-05): add Cleanup and acceptable-use sections to the 32 briefs, or amend `CONTRIBUTING.md` §5.
5. **Freeze the lab environment** (D-06): generate and commit a lockfile for the versions you validated, and cite it from `requirements-labs.txt`.
6. **Re-balance the six answer-length outliers** (D-07) when you next edit the question bank; the builder will tell you when they clear.
7. **Commit and push yourself**, then watch the first Actions run: build, link check, `--strict` build, `verify_site`, upload, deploy.
8. **Re-check the live URL** once: `/Securing-AI-Systems/` base path, search, one diagram, one quiz, mobile width.

---

## 5. Statement of non-action

No commit, stage, branch, tag, push, publish, deploy, remote change, GitHub setting change or history rewrite was performed. The repository remains on branch `master` with zero commits and every file untracked. Audit artifacts were written outside the repository (`/tmp/sas-audit/`); the temporary `.pages-test/` copy used to render the site under its production base path was deleted, and the local preview server was stopped.
