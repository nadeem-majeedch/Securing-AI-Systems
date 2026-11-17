# Final owner handover — repository freeze

**Task 16 · 17 November 2026**
**Course:** Securing AI Systems — 20 modules, 32 laboratories, BS Data Science self-study
**Owner:** Engr. Dr. Muhammad Nadeem Majeed · Department of Data Science (PUCIT), University of the Punjab, Lahore

## Verdict

**PASS — READY FOR OWNER PUBLICATION, WITH DOCUMENTED OWNER DECISIONS.**

Every gate that can run without GitHub passes in this frozen tree, no blocking defect exists, and nothing in this
task changed course content. What remains is not repair work: it is three decisions only the owner can make
(licence, module sign-off, first push), plus one deployment step that by definition cannot be proven before it runs.
The evidence for that verdict is in §3; the decisions are in §4; the push procedure is in §6–7.

---

## 1. Final repository status

| Item | State at freeze |
|---|---|
| Branch | `master` (unchanged; the workflow triggers on it) |
| Commits | **0** — the repository has no history yet, by instruction |
| Working tree | The complete, validated course; nothing committed or staged |
| Staged files | 0 (`git diff --cached` empty) |
| Unstaged diff | Empty (`git diff` empty — there is no HEAD to diff against) |
| Untracked entries | 44 top-level entries; `git status --short` is the authoritative list |
| Remote | `origin` → `https://github.com/nadeem-majeedch/Securing-AI-Systems.git` (fetch + push, unchanged) |
| Git config / history / remotes / GitHub settings | Not modified |
| Temporary directories | None. `.pages-test/`, `.venv-verify/` removed in Phase 15 |
| Background servers | None. No listener on the ports used for preview; the local preview server was stopped |
| Build output | `site/` — 27 MB, rebuilt from this tree at freeze, gitignored, regenerable, never committed |
| Stale serve log | `mkdocs-serve.log` — removed in this task (gitignored either way) |
| Licence files | **0.** No `LICENSE`, no copyright line changed, no badge altered |
| Module status labels | 20 × `sas_status: review` ("In review"); 0 × `draft`, 0 × `complete` |

`.gitignore` already excludes `site/`, `*.log`, `.freebuff/`, `.venv*/`, `.pages-test/`, `data/`, `models/`,
`__pycache__/` and `.env`. Nothing generated or local can be committed by accident.

---

## 2. Course inventory (counted in this tree, not quoted from earlier reports)

| Component | Count | Location |
|---|---|---|
| Modules | **20** in 4 levels | `docs/modules/` |
| Laboratories | **32** — brief + starter + solution, 22 sections each | `labs/student/L01–L32`, `labs/solutions/` |
| Notebooks | **34** executed notebooks, held twice (working copy + site download copy, byte-identical and checked) | `notebooks/`, `docs/notebooks/` |
| Module quizzes | **20** | `docs/quizzes/m01–m20.md` |
| Level papers + final | **4** + **1** | `docs/quizzes/level-1–4.md`, `final.md` |
| MCQ bank | **244** items (200 module + paper items) | `assessments/data/` → rendered pages |
| Written assessment items | **196** | `assessments/data/` |
| Answer-key pages | **26** (20 modules + 4 levels + final + index) | `docs/quizzes/answers/` |
| Assignments | **12** | `docs/assignments/` |
| Mini projects / major projects / capstone proposals | **10 / 6 / 5** (21 total) | `docs/projects/`, `docs/capstone/` |
| Case studies | **10** + hypothetical scenarios | `docs/case-studies/` |
| Reference pages | 7 frameworks, 4 research, glossary, references, attribution | `docs/frameworks/`, `docs/research/` |
| Published Markdown pages | **157** | `docs/` |
| Repository documents | **31** at the root (README, policy records, audit/phase/handover reports) | repository root |
| Python / JavaScript | **83** / **4** | `labs/`, `scripts/`, `assessments/`, `docs/assets/` |
| Pinned lab dependencies | **12** exact pins | `requirements-labs.txt` |
| Diagrams | 37 pages using `sas-mermaid` | `docs/**` |

---

## 3. Validation results

### 3.1 Re-run in this freeze (after the last content edit of Phase 15, before the freeze edits below)

| Gate | Command | Result |
|---|---|---|
| Strict site build | `python -m mkdocs build --strict` | **exit 0**, 0 warnings |
| Internal links, anchors, nav | `python scripts/check_links.py` | **PASS**, 0 problems |
| Built-site verification | `python scripts/verify_site.py site --base-path /Securing-AI-Systems/` | **PASS** (158 built HTML pages — 157 documents plus the 404 template — 244 files, 25.7 MiB, base path, assets, search index, 37 diagram pages, size). One pre-existing `WARN`: 56 titles-only search entries — see §8 |
| Notebook output policy | `python scripts/check_notebooks.py` | **PASS**, 34 notebooks, including root ↔ published-copy equality |
| MCQ builder gate | `python assessments/build.py` | **exit 0, 0 warnings**; spread A 24 / B 25 / C 26 / D 25 |
| MCQ rebuild idempotence | MD5 of all 54 quiz files before/after the rebuild | **0 files changed** — the recorded pages are exactly what the bank produces |
| Workflow lint | `actionlint 1.7.7 .github/workflows/pages.yml` | **exit 0** |
| Workflow trigger | `on: push: branches: [master]` + `workflow_dispatch` | **matches the current branch** |
| Counts and status labels | direct file counts, `sas_status` grep, badge grep | **consistent** — see §2 and the note below |

**Status-label check.** 20/20 module pages carry `sas_status: review` and the "In review" badge; no module page says
`draft` or `complete`. The string `sas-badge--draft` survives in exactly two places, both correct: its CSS rule in
`docs/assets/stylesheets/extra.css`, and the status **legend** in `docs/getting-started/how-to-use.md`, which must be
able to explain what Draft means. The README's counts (20 modules · 32 labs · 12 assignments · 20 quizzes · 6
projects · 1 capstone) match the tree.

### 3.2 Inherited from Phase 15, not repeated here (no course content was edited in this task)

| Evidence | Result | Why not re-run |
|---|---|---|
| All 32 lab solutions | 32/32 exit 0 | No lab or starter/solution file was touched in this task |
| All 34 notebooks executed | 34/34 pass, ~280 s | No notebook or dependency pin was touched |
| 200-question MCQ consistency (page ↔ `sas-key` ↔ printed key) | 200/200, 0 issues | Bank regenerated identically (idempotence check above) |
| Dependency resolution | 12 pins, dry-run resolution exit 0 | `requirements-labs.txt` unchanged |

### 3.3 What no local check can cover

The GitHub Actions run — artifact upload, `deploy-pages`, and the OIDC handshake — and the live HTTPS site. §7 is the
procedure for verifying them on the first push.

---

## 4. Outstanding owner decisions

None of these is a defect. Each needs your authority, not another review pass.

| # | Decision | Recommendation | Where | Consequence of deferring |
|---|---|---|---|---|
| 1 | **Licence** (content / code / data) | CC BY 4.0 · MIT · CC0 1.0 | `LICENSING_DECISION.md` §6, IDs D-01a–D-01c | Site stays "all rights reserved": readable, not reusable, not translatable |
| 2 | **Institutional IP position** | Obtain written confirmation or named approval | `LICENSING_DECISION.md` §5 (D-01e) | Blocks item 1 only; does not block publication |
| 3 | **Derived digits dataset** | Keep, documented as third-party CC BY 4.0 | D-01d | Must never be described as CC0 or course-owned |
| 4 | **Module sign-off** | Flip signed-off modules `review` → `complete` | 20 × `docs/modules/NN-*.md`, front matter + badge class/text | Course stays honestly labelled "In review" |
| 5 | **Branch name** | Keep `master` | `.github/workflows/pages.yml` | Renaming without editing the workflow stops deployment |
| 6 | **Pages source** | Set Settings → Pages → Source = **GitHub Actions** | GitHub UI, one time | Deploy job fails on the first run |
| 7 | **Commit and push** | Your call, after your read-through | — | Nothing is public until you do |

**Deliberately not done here:** no licence applied, no status flipped to Complete, no commit, stage, branch, tag,
push, publish, deploy, remote change or GitHub setting change.

---

## 5. Licensing considerations

The repository's position is unchanged and truthful: **no licence has been applied; all rights reserved; free to
read.**

- `LICENSING.md` (the reasoning and inventory) and `LICENSING_DECISION.md` (the one-page decision paper) agree on
  recommendation, third-party register and decision IDs. The inventory counts were re-checked in this freeze and the
  repository-document count was corrected to the current 31.
- Recommended split: **MIT** for code, **CC BY 4.0** for educational material, **CC0 1.0** for synthetic datasets,
  with third-party material untouched.
- `labs/datasets/digits_subset.npz` is a derived UCI extract distributed via scikit-learn. It is **not** course-owned;
  it must never be described as CC0 or CC BY-covered by the course.
- The one question the repository cannot answer: whether the University of the Punjab claims ownership of, or a
  licence over, teaching material created in the course of employment. Until that is settled in writing, "all rights
  reserved" is the correct and safe position.
- Publishing without an open licence is a legitimate outcome (`LICENSING.md` §8): the site can go live today exactly
  as it is. Applying a licence later means adding three licence files, SPDX headers, footer and README text, and
  re-running the build — about an hour, per `LICENSING_DECISION.md` §7.
- Do not describe the course, its safety sections or its review process as audited, certified or endorsed by any
  third party. No external auditor has seen it.

---

## 6. GitHub Pages publishing instructions

The workflow is already written, linted and pinned; nothing needs authoring.

**One-time settings (GitHub UI):**

1. Repository → **Settings → Pages**.
2. **Build and deployment → Source: GitHub Actions.** (Not "Deploy from a branch" — the workflow publishes an
   artifact through `actions/deploy-pages`, and a branch source makes it fail.)
3. Nothing else. No repository secret, no token, no environment variable. The only credential is the ephemeral
   `GITHUB_TOKEN`; the deploy job proves its origin with an OIDC `id-token`, and the `github-pages` environment is
   created on first use.
4. Branch protection, if you add it later, must still allow the `github-pages` environment deployment.

**What runs on every push to `master`** (`.github/workflows/pages.yml`):

| Job | Steps |
|---|---|
| `build` (read-only, `ubuntu-latest`, Python **3.12**, 15-min timeout) | checkout (no persisted credentials) → verify `requirements-docs.txt` is fully pinned → install docs deps only → `check_links.py` → `check_notebooks.py` → `mkdocs build --strict` → `verify_site.py site --base-path /Securing-AI-Systems/` → upload `site/` as the Pages artifact |
| `deploy` (`pages: write`, `id-token: write`, 10-min timeout) | guarded by `if: github.ref == 'refs/heads/master'` → `actions/deploy-pages` (600 s, 10 retries, 5 s interval) |

Concurrency group `pages` with `cancel-in-progress: false`, so a run is never cut in half mid-deploy. All actions are
first-party and pinned to full commit SHAs.

**Expected URL:** `https://nadeem-majeedch.github.io/Securing-AI-Systems/` — the project-site base path is already set
by `site_url` in `mkdocs.yml`. If you rename the repository or move to a custom domain, three places change together:
`site_url`, the `--base-path` argument in the workflow, and the same argument in `DEPLOYMENT.md`.

---

## 7. First-deployment verification procedure

Run these in order after the first push. Steps 1–5 are automated; 6–9 are the human check a first deployment needs.

1. **Watch the run.**
   `gh run list --workflow "Deploy course site to GitHub Pages"` then `gh run watch <run-id> --exit-status`.
   Expect ~3–5 minutes: pip install dominates, the build itself is seconds.
2. **Both jobs green.** `build` must show every step passing, especially `Verify the built site`; `deploy` must show
   `Deploy to GitHub Pages` succeeded. A green `build` with a skipped `deploy` means the ref guard rejected the run
   (a `workflow_dispatch` from a non-`master` branch does exactly that, by design).
3. **Artifact exists.** The run page shows a `github-pages` artifact, retained 1 day, roughly 26–30 MB.
4. **Environment reports a URL.** Settings → Environments → `github-pages` shows the deployment and
   `page_url`; it must be the `/Securing-AI-Systems/` project URL, not a user-site root.
5. **No warnings in the log.** Search the log for `WARNING`. The site build is `--strict`, so a warning would have
   failed the job; a warning from `verify_site.py` (the titles-only search note) is informational.
6. **HTTP surface.**
   ```bash
   BASE=https://nadeem-majeedch.github.io/Securing-AI-Systems
   curl -sI "$BASE/" | head -3                  # 200, text/html
   curl -sI "$BASE/sitemap.xml" | head -3       # 200
   curl -s  "$BASE/" | grep -c 'Securing AI Systems'
   curl -s  "$BASE/search/search_index.json" | head -c 80
   curl -sI "$BASE/quizzes/m01/" | head -3      # 200
   curl -sI "$BASE/does-not-exist/" | head -3   # 404, custom page
   ```
   Then confirm one notebook download resolves, for example the M01 notebook listed by
   `ls docs/notebooks/M01/`: `curl -sI "$BASE/notebooks/M01/<file>.ipynb"` → 200. `application/octet-stream` is
   **expected** for `.ipynb` on Pages (see §8).
7. **Page integrity in a browser.** One module page shows its "In review" badge and no printed front matter; one quiz
   marks itself, explains each answer and prints its key; the module card's progress button survives a reload
   (`localStorage`); one Mermaid page renders an `<svg>`; site search returns results.
8. **Base-path sanity.** View source of the home page: asset and link URLs are prefixed `/Securing-AI-Systems/`, the
   canonical tag points at the production URL, and nothing requests Google Fonts or a CDN.
9. **Narrow viewport and footer.** At 390 px wide there is no horizontal scroll; the footer reads "Course materials are
   under review; see the repository for licence status" — correct until you sign the licence decision.

**If something fails:**

| Symptom | Cause | Fix |
|---|---|---|
| `Get Pages site failed` / 404 on deploy | Pages source is "Deploy from a branch" | Settings → Pages → Source: GitHub Actions, then re-run |
| `Resource not accessible by integration` | `permissions:` edited | Restore `pages: write` + `id-token: write` on the deploy job |
| Build step fails on `--strict` after passing locally | CI runs Python 3.12, local evidence is 3.14.7 | Read the failing warning; fix content, not the gate |
| Deploy times out | Pages service slow on first deployment | Re-run the failed job; the concurrency guard prevents overlap |
| Site loads unstyled | Base path mismatch | Check `site_url` and the workflow's `--base-path` agree |

---

## 8. Known limitations

1. **The deployment has never run.** Everything upstream of `deploy-pages` is verified locally; the OIDC handshake
   and the live HTTPS site are not.
2. **Single-platform evidence.** All runtime results — 32 labs, 34 notebooks, 200 MCQ checks — are CPython 3.14.7 on
   Windows 11, CPU only. CI builds the docs on Python 3.12 / Linux; no lab or notebook has been executed on Linux or
   macOS.
3. **56 titles-only search entries.** Link-heavy index pages have little body text, so site search finds them by title
   with weaker body recall. Structural and pre-existing (recorded as D-12 in `FINAL_AUDIT_REPORT.md`); search works.
4. **Safety prose is editorial, not a certification.** All 32 briefs' sections 18–22 were checked against what each
   solution actually does and two claims were corrected, but no security professional has audited the course. Do not
   imply third-party review.
5. **Module status is "In review".** Accurate while owner sign-off is pending; flipping to "Complete" is a two-line
   edit per module.
6. **Quiz difficulty is an author judgement.** Tags were preserved in Phase 15 and were not measured against students.
7. **Accessibility is structural, not assistive.** Landmarks, single `h1`, alt text, keyboard-reachable nav and a
   390 px layout were checked; no screen-reader or cross-browser audit was performed.
8. **Two documented student frictions, left as designed.** A module's "Lab" chip opens the 32-row catalogue rather than
   the brief (labs are not rendered pages), and `.ipynb` downloads instead of opening in the browser (correct for
   Jupyter, and the environment page says to open it in JupyterLab).
9. **No licence means no reuse.** Translation, adaptation and institutional adoption require your decision in §4.
10. **Earlier reports describe earlier phases.** `TECHNICAL_VALIDATION_REPORT.md`, `MCQ_QUALITY_REPORT.md`,
    `FINAL_PUBLICATION_CHECKLIST.md` and `PHASE_14_REPORT.md` are historical records; where they still list the 36 MCQ
    length cues or the "Draft" badges as accepted, Phase 15 supersedes them. They were deliberately not rewritten.

---

## 9. Exact commands for owner review

Read-only inspection — nothing below changes the repository.

```bash
# 1. State of the tree: expect 44 untracked entries, 0 staged, branch master, 0 commits
git status --short
git status --branch --short
git diff                                    # empty: no HEAD yet
git diff --cached                           # empty: nothing staged
git log --oneline -5                        # fails/empty: no commits, which is correct

# 2. What will be committed, and what .gitignore keeps out
git status --short | sort
git check-ignore -v site/ mkdocs-serve.log  # both ignored

# 3. Spot-check the phase's content changes
sed -n '/## 18/,/## 23/p' labs/student/L08/LAB.md   # safety sections, widest claims
sed -n '1,40p' docs/quizzes/m05.md                  # front matter renders as metadata, not text
grep -n 'sas_status' docs/modules/01-introduction.md
grep -n 'sas-badge--review' docs/modules/01-introduction.md
cat requirements-labs.txt

# 4. Reproduce the gates locally (docs only; ~10 seconds each)
python -m pip install -r requirements-docs.txt
NO_MKDOCS_2_WARNING=1 python -m mkdocs build --strict    # exit 0, no warnings
python scripts/check_links.py                            # RESULT: PASS
python scripts/check_notebooks.py                        # RESULT: PASS, 34 checked
python assessments/build.py                              # exit 0, 0 warnings, no files rewritten
MSYS_NO_PATHCONV=1 python scripts/verify_site.py site --base-path /Securing-AI-Systems/   # RESULT: PASS
```

Publishing — only when you have read §4 and decided at least items 1 and 4.

```bash
# 5. Set GitHub Pages source to "GitHub Actions" in the UI first (Settings -> Pages).

# 6. Commit everything on master (nothing is pre-staged; .gitignore excludes build output and secrets)
git add -A
git status --short                # confirm: no site/, no *.log, no .env, no __pycache__
git commit -m "Securing AI Systems: validated course, 20 modules, 32 labs, 34 notebooks"

# 7. Publish
git push -u origin master

# 8. Watch the first deployment (see section 7)
gh run list --workflow "Deploy course site to GitHub Pages"
gh run watch <run-id> --exit-status
```

Optional, after your read-through: flip the modules you have personally signed off from `review` to `complete`
(`sas_status` in the front matter and `sas-badge--review` / "In review" in the card), rebuild with `--strict`, and
include it in the same commit.

---

## 10. Statement of non-action and what this task changed

No commit, stage, branch, tag, push, publish, deployment, remote change, GitHub setting change or history rewrite was
performed. No licence was applied. No module was marked Complete. No validated course content was edited.

Changed in this task, and nothing else:

| File | Change |
|---|---|
| `FINAL_OWNER_HANDOVER.md` | This document (new) |
| `LICENSING.md` | One inventory figure corrected: repository documents **25 → 31**, to match the tree after the Phase 15 reports and this handover |
| `mkdocs-serve.log` | Deleted (gitignored log from a stopped preview server) |

*Related: `PHASE_15_REPORT.md`, `OWNER_PUBLICATION_HANDOVER.md`, `STUDENT_JOURNEY_REVIEW.md`,
`LAB_SAFETY_FINAL_REVIEW.md`, `MCQ_FINAL_REVIEW.md`, `LICENSING_DECISION.md`, `DEPLOYMENT.md`.*
