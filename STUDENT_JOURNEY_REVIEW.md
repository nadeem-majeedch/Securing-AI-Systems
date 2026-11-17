# Student journey review

**Walked as a BS Data Science student with no instructor, starting at `README.md` and finishing at a capstone
proposal.** Every step was opened in the rendered site under its production base path
(`/Securing-AI-Systems/`), with the repository itself open beside it. Six frictions were found; four were genuine
defects and are fixed, two are design choices recorded here so they are not mistaken for accidents.

---

## 1. The path, step by step

| # | Step | What the student sees | Verdict |
|---|---|---|---|
| 1 | Repository README | What the course is, 20 modules / 32 labs / 12 assignments / 20 quizzes / 6 projects, prerequisites, setup, licence status | Clear. One stale "20 reproducible labs" row — **fixed to 32** |
| 2 | "Start learning" | Home page: hero, "Twenty modules, thirty-two laboratories, no account and no API key", level grid | Clear; counts consistent |
| 3 | Getting Started | What the course expects, weekly rhythm, how the site works | Clear |
| 4 | Prerequisites | Python, maths, ML baseline, a six-question self-check, a refresher for each gap | Clear; the self-check is answerable without installing anything |
| 5 | Learning Environment | Three commands, `check_env.py`, the exact pinned versions, troubleshooting table | **Accurate.** All 12 pins are printed in the sample output and match `requirements-labs.txt` |
| 6 | Module 01 | 16 sections, one diagram, one Python walkthrough, exercises, knowledge check, references, plus a module card with time, prerequisite, lab count and progress button | Clear. Badge said **Draft** ("a laboratory may not yet be runnable") while L01 runs — **changed to In review** |
| 7 | Module lessons | M01–M20 in four levels; each level builds on the previous one; the loan/referral case study recurs | Coherent; no missing prerequisite points to a page that does not exist |
| 8 | Notebooks | The "Notebook" chip goes to the labs page's notebook table, which lists every `.ipynb` per module as a download | Works: 34 download links, all resolve, files served. The chip lands on a section anchor, not the exact notebook — one extra scroll |
| 9 | Laboratory | Lab chip → catalogue (32 rows: title, module, difficulty, budget) → brief with 22 sections, starter, hints, separate solution | Works. Catalogue rows are not individually anchored, so a student scans for their number |
| 10 | Quizzes | 10 MCQ that mark themselves and explain each answer, then written items, then the printed key | Clear. Quiz pages previously printed their front matter as text — **fixed in Task 14** and re-checked here |
| 11 | Assignments | 12 scenarios with requirements, rubric and submission guidance | Clear; A01 (hospital threat model) links back to M04 and L05 |
| 12 | Projects | 10 mini, 6 major with architecture, threat model, requirements, metrics, rubric | Clear; the mini/project distinction is stated before the list |
| 13 | Capstone | 5 proposals with scope, threat model, deliverables, rubric | Clear; links to the release-gate lab |

No step required an account, an API key, a network call at run time, or a package outside the pinned twelve.

---

## 2. Dead ends and confusions found

**Fixed — L32 sent students to files that do not exist (high friction).** The brief said the release gate reads
"evidence values taken from the referenced labs' outputs", and the solution labelled each value
`labs/solutions/L02/output.txt` and so on. Nine such files were named and none existed; the labs print to stdout.
A student told to "read L02's output file" would conclude their download was incomplete. The brief now says the
values are carried in the starter, each labelled with the lab that produces it, and that re-deriving one means
running that lab and reading its printed line. The solution's labels say `solution.py stdout`.

**Fixed — the Draft badge undersold the course.** Every module told the student its laboratory "may not yet be
runnable". All 32 run. "In review" is the honest status; "Complete" is the owner's call after reading.

**Fixed — L01's data rule contradicted its submission.** Students were told not to paste rows into "a report", while
the lab's expected results ask them to quote referral identifiers. The rule now separates a public channel from the
student's own report.

**Fixed — README's "20 reproducible labs".** One table row still said 20 after the count was corrected elsewhere.

**Accepted, documented — the module "Lab" chip opens the catalogue, not the lab.** The labs live outside the
rendered site, so a module cannot link to a brief page; the chip lands on the catalogue and the student finds their
number. A per-lab anchor would remove one scroll. Recorded rather than changed: it is a navigation preference, not a
defect, and the catalogue is 32 rows with a module column.

**Accepted, documented — notebooks download rather than open in the browser.** GitHub Pages serves `.ipynb` as
`application/octet-stream`, so clicking downloads the file. That is the correct behaviour for a Jupyter notebook and
matches the environment page's instruction to open it in JupyterLab.

---

## 3. Prerequisites and dependency reality

- A student needs Python 3.12–3.14, a terminal, and about 1.5 GB of disk. Nothing else.
- Every module's prerequisite field names a module that exists, and every lab's prerequisite names an earlier lab that
  exists (checked across all 32).
- No lab requires a GPU, Docker, a cloud account or an API key. Docker is mentioned once, as optional, for the
  agent-sandbox discussion.
- The one optional download is the Ollama model for a single M11 cell; the notebook runs without it, and both the
  requirements file and the environment page now say so.
- Three commands get a working environment, and `python scripts/check_env.py` confirms it in one screen.

---

## 4. What a student cannot do (and should not be able to)

- Run any lab against a real system: every target is synthetic, local, or an in-process mock, and sections 18–19 of
  each brief say so in that lab's own terms.
- Submit anything to a server: progress is a date in `localStorage`, nothing else leaves the machine.
- Reach a paid service: no lab makes a network request.

---

## 5. Residual student-facing risks

| Risk | Likelihood | Mitigation in place |
|---|---|---|
| A student on Python 3.15 hits a missing PyTorch wheel | medium | Environment page warns, `check_env.py` names the supported range and the fix |
| A student edits a notebook and wonders why the site shows the old one | medium | `CONTRIBUTING.md` §6.1 documents the two copies; the check fails CI on drift (contributor-facing, not student-facing) |
| A student reads the catalogue as "20 labs" from an old bookmark | low | Every current page says 32; no page says 20 |
| A student assumes "In review" means broken | low | The badge legend defines In review as written and under review, which is true |

The journey is walkable end to end without an instructor. Nothing in this phase made it harder.
