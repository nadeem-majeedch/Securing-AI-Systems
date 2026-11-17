# Publication readiness report

**Verdict: ready to publish, with warnings.** The site builds and serves correctly under its production base path, every laboratory and notebook runs, and the security posture is clean. Two things stand between "publishable" and "publishable as an open course": the licence is undecided, and the branch name in the Pages workflow does not match the local branch. Neither stops a personal publication; both matter if the material is to be reused.

## 1. Readiness scorecard

| Area | State | Evidence |
|---|---|---|
| Content completeness | Ready | 20/20 modules, 32/32 labs, 34/34 notebooks, 20 quizzes, 12 assignments, 21 projects/proposals |
| Execution | Ready | 32/32 solutions exit 0; 34/34 notebooks pass in 250 s total |
| Site build | Ready | `--strict` 0 warnings; 157 pages, 244 files, 27 MB |
| Links and navigation | Ready | 194 internal links, 0 problems; nav complete under `--strict` |
| Hosting configuration | Ready-with-action | `site_url` and base path correct; workflow needs branch `main` |
| Assessment integrity | Ready-with-note | 200/200 keys verified; 6 modules have an answer-length cue |
| Security | Ready | no secrets, no unsafe defaults, no external calls |
| Licensing | **Blocked on owner** | no `LICENSE`; all rights reserved by default |
| Accessibility | Ready-with-note | one `h1`, alt text complete (inline SVG), keyboard-reachable nav; no screen-reader pass |
| Reproducibility | Ready-with-note | seeds and local datasets; lab dependency ranges not pinned |

## 2. New-student journey — walked, not imagined

The path a BS Data Science student takes from the GitHub README, with the URL each step resolves to on the built site. Every one returned HTTP 200 under `/Securing-AI-Systems/`.

| # | Step | Resolves to | What a student gets | Obstacle found |
|---|---|---|---|---|
| 1 | Read the README | repository root | what the course is, structure, study mode, licence status | lab count said 20 — **fixed to 32** |
| 2 | "Start learning" | `/getting-started/` | how the course works, weekly rhythm | none |
| 3 | Check prerequisites | `/getting-started/prerequisites/` | maths, Python, ML basics expected | none |
| 4 | Set up the environment | `/getting-started/environment/` | Python 3.12+, venv, `requirements-labs.txt` | none; the one-download claim was wrong — **fixed to "fully offline"** |
| 5 | Learn how to use the site | `/getting-started/how-to-use/` | module anatomy, badges, progress tracking | none |
| 6 | Read a module | `/modules/01-introduction/` | 16 sections, diagram, maths, walkthrough, exercises | none |
| 7 | Run its notebook | `/notebooks/` → `notebooks/M01/…ipynb` | 19–27 cells, runs in seconds on CPU | none |
| 8 | Do the lab | `/labs/` → `labs/student/L01/` | brief, starter, expected numbers, hints, separate solution | the lab catalogue said "Planned" for all 20 listed and used wrong numbering — **fixed: 32 released labs, real titles and module links** |
| 9 | Check understanding | `/quizzes/` → `/quizzes/m01/` | 10 MCQ with instant feedback, then a printed key with explanations | none |
| 10 | Do an assignment | `/assignments/a01-threat-model-hospital/` | scenario, requirements, rubric | README said 8 assignments; there are 12 — **fixed** |
| 11 | Plan the project/capstone | `/projects/`, `/capstone/` | 10 mini, 6 major, 5 capstone proposals with architectures and rubrics | none |
| — | Know the rules | `/getting-started/academic-integrity/`, `/getting-started/privacy/` | authorised-use rules, what the site stores (one date, local) | none |

The three obstacles a new student would actually have hit were factual: the course undercounted its own labs, the lab index described a lab template that does not exist, and the environment page promised "offline after one download" when nothing is downloaded. All three are fixed in the working tree.

## 3. Security audit

| Check | Result |
|---|---|
| Secret patterns (AWS keys, private keys, GitHub/Slack/OpenAI tokens, hard-coded passwords) across `.py`, `.ipynb`, `.md`, `.yml` | **none found** |
| `.env` files committed | none |
| `os.system`, `shell=True`, `subprocess` with untrusted input | none |
| `eval` / `exec` | none (the matches are PyTorch `model.eval()`) |
| `pickle.load` / `torch.load` | one deliberate demo in M15/01 on a locally crafted object; the lab's release-gate table explicitly refuses `torch.load(weights_only=False)` |
| `yaml.load` without a loader, `verify=False` | none |
| Outbound network calls in labs or notebooks | none; the only URL in code is `git+https://example.invalid/...` in a policy table, a non-routable placeholder |
| API keys or paid services required | none; M11's local model is optional and the notebook falls back |
| Attack demonstrations | all target synthetic data, models trained in the lab, or the course's own local API; no third-party host is contacted |
| Dependency advisories (PyPI, OSV batch query) | `mkdocs 1.6.1`, `mkdocs-material 9.8.0`, `pymdown-extensions 12.3`: no known advisories |
| Workflow permissions | least privilege, SHA-pinned first-party actions, no stored secret, OIDC for deploy |
| Site privacy | no analytics, no external fonts or scripts, no cookies; progress stored in `localStorage` |

The course teaches offensive technique, which is the intended design, and it is fenced correctly: module-level safety framing, an academic-integrity page, local-only targets, and no exploit code aimed at live systems.

## 4. Licensing audit

| Item | State |
|---|---|
| `LICENSE` at repository root | **absent** |
| Stated status | "Licence undecided… all rights reserved" (README §23, `LICENSING.md`, `docs/references.md`, site footer) |
| Recommendation on file | CC BY 4.0 (text and diagrams), MIT (code), CC0 (synthetic data), subject to institutional approval |
| Third-party assets | none bundled except `labs/datasets/digits_subset.npz` (UCI, CC BY 4.0), credited in `ATTRIBUTION.md` |
| Dependency attribution | every package in the three requirements files is named in `ATTRIBUTION.md` |
| Inconsistency found | `LICENSING.md` §1 quoted a superseded README paragraph proposing CC BY-NC-SA — **fixed to quote the current text** |
| Unresolved question | whether the University of the Punjab claims rights over teaching material created in employment (`LICENSING.md` §1) |

Consequence for publication: the site can be published and read, and quoting with attribution for study is permitted by the stated terms, but the course cannot be called open courseware, cannot be forked or reused by another institution, and a student cannot republish lab reports built on it until a licence exists. That is a one-line decision with a long tail, and it is the owner's to make.

## 5. Remaining risks

| Risk | Likelihood | Effect | Mitigation |
|---|---|---|---|
| First push lands on `master`, Pages never deploys | high | no site | rename branch to `main` before pushing, or widen the trigger |
| Licence left undecided | high if unaddressed | cannot be reused or described as open | decide per `LICENSING.md` §3 |
| Lab numbers drift with future wheels | medium | a quoted third decimal changes | commit a validated lockfile |
| Test-wise students exploit long correct options | medium | inflated quiz scores | rebalance six modules' distractors |
| Reviewer notices missing Cleanup/safety lab sections | medium | credibility hit | add sections or amend `CONTRIBUTING.md` |
| Workflow's deploy step is unproven | certain until first run | first-run failure possible | watch the first Actions run |

## 6. Owner actions before launch

1. Decide and record the licence; add `LICENSE` and update the footer.
2. Ensure the branch is `main` (or adjust the workflow trigger).
3. `git add` / `git commit` / `git push` yourself — the audit did none of these.
4. Watch the first Actions run end to end.
5. Open the live site once and check base path, search, a diagram, a quiz and a 390 px viewport.
6. Schedule the content follow-ups (lab sections, lockfile, distractor rebalance) rather than blocking the launch on them.

## 7. Statement of non-action

No commit, stage, branch, tag, push, publish, deploy, remote change, GitHub setting change or history rewrite was performed. The repository is on `master` with zero commits and every file untracked. The audit's evidence lives in `/tmp/sas-audit/`; the temporary copy used to serve the site at its production base path was removed and the local server stopped.
