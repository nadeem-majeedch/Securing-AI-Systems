# Repository Audit — Securing AI Systems

**Document ID:** `SAS-AUDIT-001`
**Phase:** 01 — Repository Inspection and Architecture
**Course:** Securing AI Systems (undergraduate, BS Data Science)
**Instructor of record:** Engr. Dr. Muhammad Nadeem Majeed — Professor, Department of Data Science (PUCIT), University of the Punjab, Lahore
**Repository:** <https://github.com/nadeem-majeedch/Securing-AI-Systems.git>
**Audit date:** 16 November 2026
**Audit method:** read-only inspection (no Git state was created, modified, staged, or pushed)

---

## 1. Executive summary

The repository is **empty**. It contains no commits, no branches, no files, no licence, no workflows and no documentation. The local working directory contains only the Freebuff tooling marker `.freebuff/` and is **not** an initialised Git repository.

This is the best possible starting condition for an architecture phase, and it changes the risk profile of the project in one important way:

- **Nothing can be broken.** There is no legacy content to preserve, no inherited conventions to reverse-engineer, and no licensing conflict to resolve with previous contributors.
- **Everything must be decided deliberately.** With no inherited defaults, every structural, licensing and publishing decision now belongs to the owner and must be recorded before content authoring begins. Undocumented defaults are the main source of cost later in a 20-module build.

**Overall repository readiness for Phase 2 (scaffolding):** **high**, conditional on eight owner decisions in Section 9, of which two are blocking (licence choice, publication model for instructor/answer content).

| Readiness dimension | Status | Note |
|---|---|---|
| Existing content to preserve | ✅ None | Empty repository (Section 3) |
| Existing licensing | ⚠️ None | Decision required before first public commit |
| Existing CI/CD | ✅ None | No inherited pipeline constraints |
| Existing website configuration | ✅ None | MkDocs stack to be introduced cleanly |
| Existing dependencies | ✅ None | No lockfile conflicts; toolchain verified locally (Section 5) |
| Git working state | ⚠️ Not initialised | Owner must clone/init before committing (Section 4) |
| Secrets / sensitive material | ✅ None found | Working tree contains no credentials |
| Local runtime compatibility | ⚠️ Python 3.14.7 | ML stack needs 3.11/3.12; see R-03 |

---

## 2. Audit scope and method

### 2.1 What was inspected

| Area | Method | Result |
|---|---|---|
| Working directory contents | Recursive listing of the project root and all descendants | Only `.freebuff/.gitignore`, `.freebuff/project-id` |
| Git status, log, branches, remotes, tracked files | `git status`, `git log`, `git remote -v`, `git branch -a`, `git ls-files` | All fail: `not a git repository` |
| Remote repository state | Read-only `git ls-remote` (heads and all refs) against the GitHub URL | Succeeds, returns **zero refs** |
| Remote repository content | Public HTTP read of the GitHub repository page | "This repository is empty." |
| Documentation / README | Filesystem search | None present |
| Dependencies / manifests | Search for `requirements*.txt`, `pyproject.toml`, `package.json`, lockfiles | None present |
| GitHub Actions workflows | Search for `.github/` | None present |
| Licence files | Search for `LICENSE*`, `COPYING*` | None present |
| Website configuration | Search for `mkdocs.yml`, `docusaurus.config.*`, `hugo.*`, `_config.yml` | None present |
| Secrets exposure | Inspection of every file found in the tree | None; only a Freebuff project UUID |
| Local toolchain | Version probes for Python, pip, MkDocs, Material, pytest, Node, Git, Jupyter | See Section 5 |

### 2.2 Commands executed (all read-only)

```bash
pwd && ls -la && find . -path ./.git -prune -o -print
git status --short --branch        # fatal: not a git repository
git log --oneline -20              # fatal: not a git repository
git remote -v                      # fatal: not a git repository
git ls-remote https://github.com/nadeem-majeedch/Securing-AI-Systems.git   # exit 0, no refs
python --version && python -m pip --version
python -m mkdocs --version
python -m pip list | grep -Ei "mkdocs|material|pytest|nbconvert|jupyter|pymdown"
node --version && git --version && python -m jupyter --version
```

No write operation of any kind was performed against Git. No remote was added. No branch, tag or commit exists or was created.

---

## 3. Findings

| ID | Finding | Evidence | Severity | Impact on the project |
|---|---|---|---|---|
| **F-01** | The GitHub repository exists and is **completely empty** (no refs, no default branch content) | `git ls-remote` returned zero refs; GitHub reports "This repository is empty." | Informational | The first commit will be the project's initial commit. There is no history, no `.gitignore`, no `README.md`. |
| **F-02** | The local working directory is **not a Git repository** | `git status` → `fatal: not a git repository` | **High** | The owner must clone or `git init` before the first commit; otherwise the three Phase-1 documents cannot be tracked. Nothing is at risk — this is a setup step, not a defect. |
| **F-03** | No documentation, README, or course content exists | Filesystem search found only `.freebuff/` | Informational | Zero preservation obligations. Delivers the "do not overwrite valuable content" constraint trivially, but removes the ability to reuse prior wording, diagrams or scope decisions. |
| **F-04** | No dependency manifest of any kind | No `requirements*.txt`, `pyproject.toml`, `package.json`, or lockfile | Informational | Dependencies must be pinned from first principles. Section 6 proposes narrow, auditable pins rather than a loose environment. |
| **F-05** | No CI/CD workflows | No `.github/` directory | Informational | Quality gates (content tests, build, link check) must be introduced as new files; nothing conflicts with them. |
| **F-06** | No licence | No `LICENSE*` or `COPYING*` file | **High** | Legally, an unlicensed repository is "all rights reserved": students and colleagues may not legally reuse, translate, or archive the material. A licence must be chosen **before** the first public commit (Section 9, D-01). |
| **F-07** | No website configuration and no known Pages deployment | No `mkdocs.yml`; GitHub settings were out of scope (and deliberately not changed) | Medium | Publication target and default branch remain unverified. Section 8 assumes GitHub Pages via Actions; the owner must confirm it is not already configured. |
| **F-08** | `.freebuff/` contains tooling state that must not be committed | `.freebuff/project-id` (a Freebuff project UUID) and its self-ignoring `.gitignore` | Medium | The Freebuff folder is local tooling metadata with no role in the course. It must appear in the repository `.gitignore` so it cannot leak into the history by accident. |
| **F-09** | Local Python is **3.14.7**, newer than the ML ecosystem supports reliably | `python --version` → 3.14.7; site-packages include MkDocs 1.6.1, Material 9.8.0 | Medium | PyTorch and several adversarial-ML libraries publish wheels for CPython 3.11–3.13, not 3.14. Course labs must not depend on the system interpreter (Section 5.2, R-03). |
| **F-10** | Website toolchain is already available globally and is recent enough | MkDocs 1.6.1, mkdocs-material 9.8.0, pymdown-extensions 12.3, pytest 9.1.1 | Positive | Phase 2 can build and serve locally without waiting on installs; the version pins in Section 6 are consistent with what is installed. |
| **F-11** | Node 24.20.0 and Git 2.56.0 are present | Version probes | Positive | No Node runtime is required for MkDocs itself; Node remains available only if a future need arises (e.g. a link checker). Keeping it out of the critical path is preferred. |
| **F-12** | Repository visibility could not be confirmed as public or private | Best-effort lookup unavailable; GitHub page is reachable anonymously, which implies public read access to an empty repo | **High (if published)** | A course repository that is world-readable but hosts answer keys, rubrics and solution notebooks is an academic-integrity problem. This drives decision D-02. |

### 3.1 What could not be verified (and why)

| Item | Reason | Owner action |
|---|---|---|
| Default branch name | No refs exist; GitHub has not created `main` yet | Confirm after first push |
| GitHub Pages configuration, custom domain, Actions permissions | Repository settings are explicitly out of scope for this engagement | Inspect Settings → Pages / Actions yourself |
| Repository visibility (public/private) | Authenticated lookup not available in this environment | Confirm in Settings → General |
| Branch protection, required reviews | Empty repository has no rules | Confirm in Settings → Rules |
| Whether a project board or wiki already exists | Not visible from a content-level read | Check the repository's Projects/Wiki tabs |
| Local virtual environments or pre-existing Python tooling outside the workspace | Outside the authorised scope (project directory only) | None needed; the roadmap creates a project-local venv |

---

## 4. Git and working-directory state

```text
Working directory:  C:\Users\Nadeem\Documents\Securing AI Systems
Git repository:     NONE  (no .git directory)
Tracked files:      0
Remotes:            none configured locally
Branches:           none
Tags:               none
Remote refs:        0 (repository empty)
Uncommitted work:   none that Git can see
```

**Preservation conclusion:** there is no version-controlled work to preserve, and no uncommitted local work other than this Phase's three documents and the Freebuff tooling marker.

**Recommended owner sequence (not executed here, by instruction):**

```bash
# Option A — repository already exists on GitHub and is empty
cd "C:/Users/Nadeem/Documents/Securing AI Systems"
git init -b main
git remote add origin https://github.com/nadeem-majeedch/Securing-AI-Systems.git
# review the proposed .gitignore in Section 7.2 before staging
git add REPOSITORY_AUDIT.md COURSE_ARCHITECTURE.md DEVELOPMENT_ROADMAP.md
git commit -m "docs: add Phase 1 repository audit and course architecture"
git push -u origin main

# Option B — clone instead (equivalent, keeps origin canonical)
git clone https://github.com/nadeem-majeedch/Securing-AI-Systems.git sas-repo
# then copy the three Phase-1 documents into sas-repo/
```

> Because the repository is empty, Option A and Option B produce an identical history. Only the owner performs these commands.

---

## 5. Local environment and toolchain

### 5.1 Verified versions (16 November 2026)

| Tool | Version | Suitability for this course |
|---|---|---|
| Python | 3.14.7 (`C:\Python314`) | ⚠️ Fine for MkDocs and pytest; too new for parts of the ML stack |
| pip | 26.2.1 | ✅ |
| MkDocs | 1.6.1 | ✅ Latest 1.x line used by the plan |
| mkdocs-material | 9.8.0 | ✅ Provides Mermaid, search, instant navigation, code annotations |
| pymdown-extensions | 12.3 | ✅ Superfences, tabbed, details, arithmatex, mermaid fences |
| pytest | 9.1.1 (+ pytest-cov 7.1.0) | ✅ Content QA suite can target pytest 9 |
| Jupyter core | jupyter_core 5.9.1, jupyter_client 8.10.0, ipykernel 7.4.0 | ✅ Kernels available; `ipywidgets` absent (not required) |
| Node.js | 24.20.0 | ➖ Not required; keep off the critical path |
| Git | 2.56.0 (Windows) | ✅ |
| uv | not installed | ➖ Optional accelerator; standard `venv` + `pip` planned |
| Windows FS | `ntfs`, path contains a space (`Securing AI Systems`) | ⚠️ All scripts must quote paths; no symlink-dependent build steps |

### 5.2 The Python version problem (R-03, detailed)

Course labs need, at minimum:

| Package | Purpose | CPython 3.14 status (expected) |
|---|---|---|
| `torch`, `torchvision` | Model training, FGSM/PGD, adversarial training | No stable wheels at audit time → install failure |
| `adversarial-robustness-toolbox` | Evasion, poisoning, extraction, inference attacks | Depends on `torch`/`scikit-learn`; inherits the constraint |
| `scikit-learn`, `numpy`, `pandas`, `matplotlib` | Core data science | Generally available |
| `transformers`, `safetensors`, `tokenizers` | LLM labs, local inference | Available, but model-download path needs pinning |
| `opacus`, `diffprivlib` | Differential privacy | `opacus` depends on `torch` |

**Decision:** the course never installs into the system interpreter. `docs/00-start-here/learning-environment.md` will standardise on **Python 3.11 or 3.12** in a project-local virtual environment, with a `requirements.txt` pinned by exact version and a `scripts/check_env.py` preflight that fails loudly with a remediation message. MkDocs build tooling stays usable on 3.14; the lab environment is where the 3.11/3.12 requirement applies. This split is stated explicitly so students on any OS get one predictable path.

### 5.3 Build-time versus lab-time dependencies

The course has **two dependency surfaces**, and conflating them is a common failure mode:

| Surface | Installed by | Must never contain |
|---|---|---|
| Documentation build (`requirements-docs.txt`) | `pip install -r requirements-docs.txt` | `torch`, model weights, credentials |
| Lab runtime (`requirements-labs.txt`, optional CUDA variant) | Student, per module part | MkDocs plugins, site theme packages |

Rationale: a student who only wants to read the course should not download ~2 GB of PyTorch. A student running Module 5 must not be blocked by a MkDocs plugin conflict. The split also keeps the CI build fast and the attack surface of the documentation toolchain small — an appropriate detail for a course whose subject is supply-chain security.

---

## 6. Proposed dependency and configuration baseline

Proposed pins (to be written in Phase 2; versions verified as resolvable at audit time):

```text
# requirements-docs.txt
mkdocs==1.6.1
mkdocs-material==9.8.0
pymdown-extensions==12.3
mkdocs-jupyter==0.25.1        # notebook rendering; pin reviewed at Phase 2
mkdocs-minify-plugin==0.8.0   # release builds only
```

```text
# requirements-dev.txt  (content QA + tooling, not shipped to students)
pytest==9.1.1
pytest-cov==7.1.0
ruff==0.14.*                   # style gate for lab code
nbformat==5.10.*
PyYAML==6.*
requests==2.*                  # link checker only, smoke network tests excluded from CI
```

```text
# requirements-labs.txt  (student lab environment — Python 3.11/3.12)
numpy==2.*
pandas==2.*
scikit-learn==1.*
matplotlib==3.*
torch==2.*                     # + platform-appropriate index URL documented
torchvision==0.*
adversarial-robustness-toolbox==1.*
transformers==4.*
safetensors==0.*
datasets==3.*
jupyterlab==4.*
nbformat==5.*
```

Exact patch versions, index URLs and hash pinning are fixed in Phase 2 after a clean install test on Python 3.12 for Windows, Linux and macOS. No dependency is added to the course that is not used by content that exists — unused packages in a security course are themselves a finding.

---

## 7. Preservation and hygiene requirements

### 7.1 Preservation register

| Item | Status | Rule |
|---|---|---|
| Course content | None exists | Nothing to migrate; every future file is new |
| Instructor's existing slides, notes, LMS material | Outside this repository | Not imported without explicit authorisation |
| `.freebuff/project-id` | Present, local only | **Must not be committed.** Listed in the repository `.gitignore` |
| `.freebuff/.gitignore` | Present, self-ignoring | Leave untouched; it protects the folder in its own right |
| Local virtual environments / `data/` caches | Will be created | Git-ignored from the first commit |
| Any future colleague contribution | None yet | Changes land by pull request only; no direct pushes to protected branches |

### 7.2 Proposed initial `.gitignore` (for owner review, Phase 2)

```gitignore
# Freebuff local tooling — never part of the course
.freebuff/

# Python
__pycache__/
*.py[cod]
.venv/
venv/
*.egg-info/
.pytest_cache/
.ruff_cache/

# Notebook execution artifacts
.ipynb_checkpoints/
*.executed.ipynb

# Datasets and model artifacts (downloaded by scripts, never committed)
data/
models/
artifacts/
*.pt
*.pth
*.onnx
*.safetensors
*.bin
*.h5

# Build output
site/
.cache/

# Local environment and secrets
.env
.env.*
!.env.example

# OS / editor
.DS_Store
Thumbs.db
.vscode/
.idea/
```

Committing large datasets or model weights is explicitly prohibited: it bloats history permanently, and in a course on model supply-chain risk it would be an unfortunate irony. Datasets are fetched by checksummed scripts; model weights are pulled from pinned revisions of public repositories.

---

## 8. Publication surface (planned, not executed)

| Item | Planned state | Constraint |
|---|---|---|
| Hosting | GitHub Pages, deployed from `main` by a workflow, or `mkdocs gh-deploy` from the owner's machine | **Owner authorises publication.** Nothing in this engagement deploys or enables Pages |
| Site generator | MkDocs + Material 9.8.0 | Static output; no server-side code, no database, no user accounts |
| Authentication | None | A public course site must not contain instructor-only material; enforcement is by build exclusion, not by a login |
| Analytics | None by default | Consistent with the course's own privacy teaching; if ever added, it must be cookieless and disclosed |
| Custom domain | Undecided | Owner decision D-05 |
| Search | Client-side (Material search index) | Implies every built page is searchable — another reason instructor content must be excluded from the build |

**Integrity note (F-12):** if the site is public, then quiz answers, rubrics, marking guides and model solutions must live outside the built site (`docs/instructor/**`, excluded via `exclude_docs`), or in a separate private repository. Publishing them and then relying on students not to look is not a control.

---

## 9. Decisions requiring owner approval

| ID | Decision | Options | Recommendation | Blocking? |
|---|---|---|---|---|
| **D-01** | Content licence | (a) CC BY-NC-SA 4.0; (b) CC BY 4.0; (c) CC BY-SA 4.0; (d) All rights reserved | **(a)** — permits classroom and personal reuse and adaptation with attribution, blocks commercial resale, and copyleft keeps derivatives open | **Yes** — before the first public commit |
| **D-02** | Instructor / answer-key publication | (a) Same repo, excluded from build; (b) separate private repo; (c) not versioned | **(a)** for rubrics and teaching notes; **(b)** for live exam banks | **Yes** |
| **D-03** | Code licence | MIT / Apache-2.0 / none | **MIT** for lab and support code (separate `LICENSE-CODE`) | Yes (pairs with D-01) |
| **D-04** | GitHub Pages publication | Publish public site / keep repository only | Publish after Phase 10 QA passes | No |
| **D-05** | Custom domain | Default `*.github.io` / institutional subdomain | Default first; institutional domain only with written approval | No |
| **D-06** | University and department branding | Name + logo / name only | Name and affiliation in text; logo only with permission | No |
| **D-07** | Dataset and model redistribution | Link + checksum (recommended) / bundle in repo | **Link + checksum.** Never redistribute datasets whose terms forbid it (e.g. CIFAR-10, MNIST usage terms; Hugging Face model licences) | Yes (affects Phase 3) |
| **D-08** | Assessment weighting for credit-bearing use | 4-credit weighting (Section 6.4 of the architecture) / advisory only | Provide the weighting as a default template; the institution may override | No |

---

## 10. Risk register (audit-derived)

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| **R-01** | Content is started before licence and publication model are settled, forcing a rewrite or a legal cleanup later | Medium | High | D-01/D-02 are blocking; no module text is authored until they are recorded |
| **R-02** | The instructor's answer keys or rubrics leak into a public site | Medium | High | `exclude_docs` + content test asserting no `docs/instructor/**` page appears in the build output; solutions referenced by ID, never inlined |
| **R-03** | Students on Python 3.14 cannot install `torch` / ART and the course appears broken | **High** | High | Pin 3.11/3.12 in `learning-environment.md`; `scripts/check_env.py` preflight with an explicit remediation message; per-OS install matrix tested in Phase 2 |
| **R-04** | Scope inflation: 20 modules at professional depth is roughly 200k words and ~45 notebooks | **High** | High | Phase budgets, per-phase owner sign-off, and the Module Blueprint Contract that forbids filler; see the roadmap's content budget |
| **R-05** | Offensive-technique labs are misused outside the course | Medium | High | Benign, synthetic, local targets only; no operational attack guidance against third-party systems; explicit acceptable-use and ethics gate before offensive labs; authorisation-first framing in Modules 18–19 |
| **R-06** | LLM labs need paid API keys, creating cost, key-leakage and reproducibility problems | Medium | High | Local small models (0.5B–3B) via `transformers`/Ollama; a deterministic mock LLM for automated tests; no lab requires a cloud key |
| **R-07** | Framework drift (OWASP LLM Top 10 versions, NIST profiles, EU AI Act implementation timelines, tool renames) silently dates the content | **High** | Medium | Every framework reference carries a version and access date; a `docs/maintenance/framework-watch.md` register with a review cadence; citations stored in one bibliography file |
| **R-08** | Notebook outputs, absolute paths or cached credentials get committed | Medium | Medium | Executed-output-free notebooks committed by policy; a QA test that fails on absolute paths and key-shaped strings; `.gitignore` covers `.ipynb_checkpoints/` |
| **R-09** | Site accessibility degrades as content grows (contrast, keyboard, diagram descriptions) | Medium | Medium | Accessibility requirements are part of the Module Blueprint Contract and are machine-checked where possible |
| **R-10** | A single-maintainer project accumulates unbuildable docs | Medium | Medium | CI builds the site on every push; content tests run on every push; a maintenance runbook with a "broken build" procedure |

---

## 11. Audit conclusions

1. **The repository is a clean slate.** No content, dependencies, workflows, licence, or site configuration exist. The "inspect before overwriting" constraint is satisfied by evidence, and there is nothing to migrate.
2. **Two blocking decisions precede content.** The content licence and the public/private split for instructor material must be settled now; both are cheap today and expensive after 200k words.
3. **The only real technical hazard in the current environment is Python 3.14** for ML labs. It is contained by standardising the lab environment on 3.11/3.12 and separating documentation dependencies from lab dependencies.
4. **Nothing in the audit prevents starting Phase 2**, and Phase 2 must be the scaffold — theme, navigation, content tests, build pipeline — not lesson prose. Building the guard rails before the content is the only reliable way to keep 20 modules consistent and free of filler.
5. **This audit changed no state.** No Git repository was created, no refs exist, no remote was added, nothing was staged, committed, pushed or deployed.

---

## 12. Phase 1 acceptance criteria

| Criterion | Status | Evidence |
|---|---|---|
| Existing files and folders inspected | ✅ | Section 2.1, F-01…F-03 |
| Git status and configuration inspected | ✅ | Section 4; `fatal: not a git repository` |
| Existing README/documentation inspected | ✅ | None exist (F-03) |
| Existing dependencies identified | ✅ | None in repo; local toolchain in Section 5 |
| Existing workflows identified | ✅ | None (F-05) |
| Existing licences identified | ✅ | None (F-06) |
| Existing website configuration identified | ✅ | None (F-07) |
| Existing content to preserve identified | ✅ | Section 7.1 — none, with `.freebuff/` exclusion rule |
| Licensing decisions surfaced for approval | ✅ | Section 9, D-01/D-02/D-03/D-07 |
| All 8 Phase-1 deliverables produced | ✅ | `REPOSITORY_AUDIT.md`, `COURSE_ARCHITECTURE.md`, `DEVELOPMENT_ROADMAP.md` |
| No Git mutation, no deployment | ✅ | Read-only commands only |

---

*End of audit. Phase 2 (scaffolding) is proposed in `DEVELOPMENT_ROADMAP.md` and must not begin until decisions D-01 and D-02 are recorded.*
