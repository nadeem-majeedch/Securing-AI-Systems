# Final publication checklist

**Verdict: ready to publish, with two owner decisions.** Everything that can be verified inside the repository has
been verified after the last edit. Nothing has been committed, pushed or deployed.

## 1. Gate status

| Gate | Status | Evidence |
|---|---|---|
| Content complete | ✅ | 20 modules, 32 labs (22 sections each), 34 notebooks, 20 quizzes + 4 level papers + final, 12 assignments, 21 projects/proposals |
| Strict site build | ✅ | `mkdocs build --strict` exit 0, 0 warnings |
| Internal links and anchors | ✅ | 194 links, 0 problems |
| Built-site verification | ✅ | `verify_site.py` PASS (base path, assets, search index, diagrams, size) |
| Every lab runs | ✅ | 32/32 solutions exit 0 |
| Every notebook runs | ✅ | 34/34 pass, 279.8 s total |
| Assessment keys | ✅ | 200/200 page ↔ index ↔ printed key; 0 builder warnings |
| Notebook output policy | ✅ | `scripts/check_notebooks.py` PASS (34 checked), enforced in CI |
| Workflow syntax | ✅ | `actionlint 1.7.7` exit 0 |
| Workflow branch match | ✅ | triggers on `master`, the current branch |
| Environment reproducibility | ✅ | 12 pins, dry-run resolution exit 0, `check_env.py` "ready" |
| Security posture | ✅ | no secrets, no unsafe calls, no external services, no advisories |
| Rendered site | ✅ | home, labs, module, quiz, environment, attribution: 200, one `h1`, no overflow, no metadata leak |
| Licence | ⛔ **owner** | `LICENSING_DECISION.md` awaiting signature; no `LICENSE` exists |
| First Actions run | ⛔ **needs push** | cannot be exercised without publishing |

## 2. What you must do — in order

1. **Decide the licence** (`LICENSING_DECISION.md` §6). Check your institution's IP position first. Until you do,
   the site must keep saying the licence is undecided — which it does.
2. **Review the diff.** `git status` and `git diff` — 60-odd modified files, no deletions, no new binary assets.
   Spot-check three things: a lab brief's new sections 18–22, `requirements-labs.txt`, and a quiz page
   (`docs/quizzes/m09.md`).
3. **Read three lab safety sections** yourself (L08, L21, L26, L30 are the widest claims). They are new prose.
4. **Commit on `master`.** The workflow triggers there; do not rename the branch without editing
   `.github/workflows/pages.yml` in the same commit.
5. **Push and watch the first run.** Build → link check → notebook policy → strict build → site verify → artifact
   upload → Pages deploy. This is the only gate with no local evidence.
6. **Open the live URL once**: base path `/Securing-AI-Systems/`, search, one diagram, one quiz, 390 px.

## 3. Changes in this working tree, by area

**Workflow and policy**
- `.github/workflows/pages.yml` — `master` trigger and deploy guard; notebook-policy step; permissions and SHA pins untouched.
- `CONTRIBUTING.md` — lab 22-section contract with the five safety sections; §6.1 notebook output policy; checklist items.
- `.gitignore` — ignores the throwaway verification environment.

**Licensing**
- `LICENSING_DECISION.md` — new owner decision paper. No licence file, badge, footer or copyright line was changed.

**Laboratories**
- 32 × `labs/student/Lxx/LAB.md` — sections 18–22 added, written per lab.
- `docs/labs/index.md` — section table extended to the five new sections.
- `labs/VALIDATION_REPORT.md` — dated note explaining the section count change.
- `labs/README.md` — setup no longer installs PyTorch twice; Python floor and runtime facts corrected.

**Dependencies**
- `requirements-labs.txt` — 12 exact pins, 5 unused packages removed, Ollama documented as optional.
- `requirements-dev.txt` — `nbformat`/`nbclient` moved here.
- `scripts/check_env.py` — package list and Python range match the pins.
- `docs/getting-started/environment.md`, `docs/index.md`, `docs/references.md`, `docs/attribution.md`,
  `ATTRIBUTION.md`, `DEVELOPMENT.md`, `COURSE_ARCHITECTURE.md` — corrected where they described the old stack.

**Assessment**
- `assessments/build.py` — YAML-safe front matter (fixes metadata printed as page text on every module quiz).
- `assessments/data/module_m01,m07,m09,m11,m13,m15,m16,m17,m18,m19,m20.json` — 76 distractor rewrites, no answer changes.
- `docs/quizzes/**` — regenerated pages.

**New tooling and reports**
- `scripts/check_notebooks.py`, `PHASE_14_REPORT.md`, `LICENSING_DECISION.md`, `LAB_SAFETY_REVIEW.md`,
  `DEPENDENCY_REPRODUCIBILITY_REPORT.md`, `MCQ_QUALITY_REPORT.md`, this checklist.

## 4. Known warnings you are accepting

| Warning | Effect | Why it is acceptable |
|---|---|---|
| Licence undecided | No reuse, translation or institutional adoption | Your decision, and the site states it honestly |
| Pages deploy never ran | A first-run failure is possible | `actionlint` clean, every step's command passes locally |
| 36 MCQ items keep a size gap | A test-wise student could still gain an edge in M03–M08, M10, M12, M14 | No gate fires; listed in `MCQ_QUALITY_REPORT.md` §5 |
| Lab safety sections unreviewed by a human | Wording risk, not a technical one | Generated from each lab's own data; four named for your review |
| Notebooks carry outputs up to 145 KB | Larger repository | Policy is explicit, capped at 250 KB, and checked in CI |
| Search index has 56 titles-only entries | Weaker body-text search on index pages | Structural, harmless |

## 5. Tests not possible without publishing

- The Actions workflow end to end, including the OIDC handshake and `deploy-pages`.
- The live Pages URL: HTTPS, base path, caching, and the footer as visitors see it.
- A second operating system or a machine without PyTorch already installed. All runtime evidence is Windows 11 /
  CPython 3.14.7, CPU only.
- A full `pip install` from an empty environment over the network. Resolution was proven with `--dry-run`; the
  environment check was proven in a venv sharing installed packages.
- Screen-reader and cross-browser accessibility. The rendered check was structural, not assistive.

## 6. Statement of non-action

No commit, stage, branch, tag, push, publish, deploy, remote change, GitHub setting change or history rewrite was
performed. The repository remains on `master` with zero commits. Temporary artefacts used for verification
(`.pages-test/`, `.venv-verify/`) were deleted, the local preview server was stopped, and audit evidence lives outside
the repository in `/tmp/sas-audit/`.
