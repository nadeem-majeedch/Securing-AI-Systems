# Phase 15 report — independent human-focused review

**Date:** 17 November 2026
**Scope:** final pre-publication review of a course that has already passed a structural audit (Task 13) and a
hardening pass (Task 14). This phase looked at the course the way a student and a reviewer would: read the safety
sections for accuracy, sat the quizzes, walked the learning path in a browser, and checked that every document
describes what the repository actually contains.

**Verdict: PASS WITH WARNINGS — READY WITH DOCUMENTED LIMITATIONS.**

There are no blocking issues. Every gate runs green, every link resolves, every lab and notebook executes, and the
defects found in this phase were factual (a dead reference, a stale count, a misleading status badge, an undocumented
duplication rule) and are fixed. The remaining warnings are the owner's licence decision and the first GitHub Actions
run, neither of which can be closed inside the repository.

Nothing was committed, staged, pushed, published, deployed, or changed in any remote or GitHub setting. The branch is
still `master` with zero commits.

---

## 1. What this phase actually did

| Area | Method | Result |
|---|---|---|
| Lab safety (32 briefs) | Read all 160 new sections; checked each claim against the lab's dataset section and its solution's actual file/network behaviour | 2 claims corrected, 158 upheld |
| Focus labs (L08, L21, L26, L30) | Full read plus artefact checks: perturbation target, RAG corpus, ASGI transport, bundle recovery | Accurate; no change needed beyond L32's neighbour check |
| MCQ (36 residual) | Read every item, measured lengths, checked plausibility, ambiguity and answer pattern | 36 items rebalanced, 37 options rewritten, 0 answers changed |
| Student journey | Walked README → prerequisites → environment → M01 → notebooks → labs → quizzes → assignments → projects → capstone in the rendered site | 1 dead reference, 2 stale counts, 1 misleading badge, 1 undocumented rule — all fixed |
| Technical consistency | Counts, pins, navigation, base URL, workflow trigger, dev/student separation | 1 stale pin reference, 1 stale count fixed |
| Licensing | Compared `LICENSING.md` against `LICENSING_DECISION.md` and the README | 2 stale statements fixed; decision still open |

---

## 2. Defects found and fixed in this phase

**D-15-01 (medium, fixed) — L32 pointed at files that do not exist.** The lab's dataset section said evidence values
were "taken from the referenced labs' outputs", and its solution labelled eight values with paths like
`labs/solutions/L02/output.txt`. No such files exist: the values are carried in the starter, and the labs print their
results to stdout rather than to files. A student following the instruction would search for nine non-existent files.
Fixed in the lab (provenance now describes what is actually true) and in the solution's source labels (10 strings).
L32 still runs and exits 0.

**D-15-02 (medium, fixed) — every module advertised itself as "Draft".** All 20 module cards showed the Draft badge,
which the course defines as "content exists but may be incomplete; a laboratory may not yet be runnable". All 32 labs
are released and runnable and all 20 modules meet the content contract, so the badge understated the state of the
course and contradicted the README's "every page states its own status honestly". Changed to **In review**, which is
the accurate status while the owner has not yet signed off. Flipping to **Complete** after your read-through is now a
one-line change per module, listed in the handover.

**D-15-03 (low, fixed) — L01's data rule contradicted its own submission.** The new data-handling section said not to
paste rows "into an issue, a report or a chat", but the lab's expected output and submission require quoting referral
identifiers as evidence. The rule now distinguishes a public channel from the student's own report.

**D-15-04 (low, fixed) — the notebook duplication was undocumented.** `docs/notebooks/` is a byte-identical second copy
of `notebooks/` that the site serves for download, with no rule saying so and no check keeping them equal. A drift
would publish a notebook the course never executed. `scripts/check_notebooks.py` now fails on any difference, and
`CONTRIBUTING.md` §6.1 documents the copy step.

**D-15-05 (low, fixed) — stale counts and a stale licensing statement.** README still said "20 reproducible labs" in
one table row; `LICENSING.md` said "70 Python files" and that "the README currently proposes CC BY-NC-SA 4.0", both
untrue after Task 14. Corrected to 32 labs, 83 Python files, and a statement that describes the earlier proposal as
history.

**D-15-06 (low, fixed) — `M14-Q09` needed a second pass.** Its first rebalance landed one character inside the cue
threshold; caught by the independent measurement, not by eye. Rebalanced.

---

## 3. Validation executed after the last edit

| Gate | Command | Result |
|---|---|---|
| Strict build | `python -m mkdocs build --strict` | exit 0, 0 warnings |
| Links and anchors | `python scripts/check_links.py` | PASS, 0 problems |
| Built-site verification | `python scripts/verify_site.py site --base-path /Securing-AI-Systems/` | PASS |
| Notebooks execute | all 34 via `nbclient` | **34/34 pass** (second full run this phase) |
| Lab solutions | all 32 | **32/32 exit 0** |
| MCQ consistency | 200 questions, page ↔ embedded key ↔ printed key | **200/200, 0 issues** |
| MCQ quality gate | `python assessments/build.py` | 0 warnings; **0 length cues bank-wide** |
| Dependency pins | 12 pins vs `environment.md`, `check_env.py`, `ATTRIBUTION.md` | all match |
| Notebook policy | `python scripts/check_notebooks.py` | PASS, including the new two-copy equality check |
| Workflow lint | `actionlint 1.7.7` | exit 0, trigger `master` |
| Security | secrets, `os.system`, `shell=True`, `verify=False` | no matches in code or content |
| Rendered site | 16 journey URLs at `/Securing-AI-Systems/` | all 200; notebook downloads serve |

---

## 4. Remaining warnings

1. **Licence undecided (owner).** No `LICENSE` file; `LICENSING_DECISION.md` awaits your signature. The course can be
   published and read today; it cannot be reused or translated until you decide.
2. **Modules are "In review", not "Complete".** Accurate, but the final status flip is yours after reading. This is a
   deliberate handover, not an omission.
3. **The Pages deployment is unproven.** The workflow is lint-clean and every command it runs passes locally; the
   OIDC deploy step needs a real push.
4. **Lab safety prose is machine-reviewed, not certified.** It was checked against artefacts and corrected where
   wrong, but no security professional has audited the course and none should be implied.
5. **Single-platform evidence.** All runtime results are CPython 3.14.7 on Windows 11, CPU only.

---

## 5. What needs GitHub publication to verify

- The Actions run end to end: build job, artifact upload, `deploy-pages`, and the OIDC handshake.
- The live URL: HTTPS, `/Securing-AI-Systems/` base path, caching, and the footer as visitors see it.
- GitHub's rendering of the README, which a student reads before the site exists for them.

Everything else in this report was executed locally against the files in this working tree.

---

## 6. Files changed in this phase

`labs/student/L01/LAB.md`, `labs/student/L32/LAB.md`, `labs/solutions/L32/solution.py`,
`assessments/data/module_m03–m08,m10,m12,m14.json` (36 items), regenerated `docs/quizzes/**`,
`docs/modules/01–20-*.md` (status badge and front matter), `README.md`, `LICENSING.md`, `CONTRIBUTING.md` §6.1,
`scripts/check_notebooks.py`. Reports: `PHASE_15_REPORT.md`, `STUDENT_JOURNEY_REVIEW.md`,
`LAB_SAFETY_FINAL_REVIEW.md`, `MCQ_FINAL_REVIEW.md`, `OWNER_PUBLICATION_HANDOVER.md`.
