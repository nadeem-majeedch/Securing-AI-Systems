# Owner publication handover

**Verdict: PASS WITH WARNINGS — READY WITH DOCUMENTED LIMITATIONS.**

There are **no blocking defects**. Everything that can be checked inside this repository passes, and the five issues
found in this phase are fixed. What remains is one legal decision, one manual read-through, and one unproven
deployment step that only a push can exercise.

Nothing has been committed, staged, pushed, published or deployed. Branch `master`, zero commits, working tree
carrying all changes.

---

## 1. Blockers vs owner decisions

| Item | Type | Blocks publication? | Who closes it |
|---|---|---|---|
| Licence unresolved (no `LICENSE`, all rights reserved) | **Owner decision** | **No** — the site can be published and read as-is. It blocks *reuse*, translation and institutional adoption | You, after checking your institution's IP position |
| Institutional ownership of teaching material | **Owner decision** | No, but it must be settled before any licence is applied | You / the University IP office |
| Module status "In review" rather than "Complete" | **Owner action** | No | You, after your read-through |
| First Actions run never executed | **Cannot be done locally** | It is the last unproven gate, not a known defect | GitHub, on your first push |
| Lab safety prose not human-reviewed | **Documented limitation** | No | Optionally you, by reading four labs |
| 36 MCQ items previously flagged | Closed | — | Fixed and re-verified this phase |
| L32 dead reference | Closed | — | Fixed this phase |

Nothing in this table is a defect in the code, content or site. The first two are your rights and your judgement; the
third is a five-minute review; the fourth is physics.

---

## 2. Decide the licence — the only substantive open question

`LICENSING_DECISION.md` is the paper to sign. Summary:

- **MIT** for original source code.
- **CC BY 4.0** for original educational material.
- **CC0 1.0** for original synthetic datasets.
- **Third-party material stays under its own terms** — notably `labs/datasets/digits_subset.npz`
  (UCI, CC BY 4.0), which must never be described as CC0 or course-owned.
- **One institutional question remains:** whether the University of the Punjab claims ownership of, or a licence over,
  teaching material created in the course of employment. `LICENSING.md` §1 and §4 record why this cannot be answered
  from inside the repository.

`LICENSING.md` and `LICENSING_DECISION.md` were compared in this phase and are consistent: the inventory counts
(83 Python files, 4 JavaScript files, 157 Markdown pages, 38 diagrams), the recommendation, the third-party register
and the decision IDs match. Two stale statements were corrected — `LICENSING.md` said "the README currently proposes
CC BY-NC-SA 4.0" (it no longer does) and carried an out-of-date file count.

**No licence file was created, no copyright line changed, no badge altered.** The site still says the licence is
undecided, which is true.

---

## 3. Your checklist, in order

1. **Read four lab briefs' safety sections** — L08, L21, L26, L30. They make the widest claims. Ten minutes.
2. **Sign the licence decision** in `LICENSING_DECISION.md` §6, after confirming your institution's position.
3. **Review the diff.** `git status`, then `git diff` on a sample: one lab brief (sections 18–22), one quiz page, a
   module page's status badge, `requirements-labs.txt`, `.github/workflows/pages.yml`.
4. **Flip the module status** from `In review` to `Complete` for modules you have personally signed off:
   `sas_status: review` → `complete` in the front matter, and the badge class/text in the module card. Twenty files,
   two edits each.
5. **Commit on `master`.** The workflow triggers there; renaming the branch requires the same edit in the workflow.
6. **Push and watch the first run**: link check → notebook policy → strict build → site verify → artifact upload →
   Pages deploy.
7. **Open the live URL once**: `/Securing-AI-Systems/` base path, search, one diagram, one quiz, 390 px width.
8. **If you approve an open licence**, follow `LICENSING_DECISION.md` §7 — add the three licence files, SPDX headers,
   footer text, and re-run the build.

---

## 4. What was tested locally

| Gate | Evidence from this phase |
|---|---|
| Strict build | `mkdocs build --strict` exit 0, 0 warnings |
| Links and anchors | 0 problems across 194 internal links |
| Site structure | `verify_site.py` PASS: base path, assets, search index, 37 diagram pages, size |
| Notebooks | 34/34 executed, second full run, ~280 s |
| Labs | 32/32 solutions exit 0 |
| MCQ | 200/200 page ↔ key ↔ printed key; 0 length cues; gate silent |
| Dependencies | 12 pins match the environment page, `check_env.py`, `ATTRIBUTION.md`; dry-run resolution exit 0 |
| Notebook policy | PASS, now including root ↔ published copy equality |
| Workflow | `actionlint` exit 0; trigger `master`; least privilege; SHA pins intact |
| Security | no secrets or unsafe calls in code or content |
| Rendered site | 16 journey URLs 200 under the production base path; notebook downloads serve; no horizontal overflow |

## 5. What requires GitHub publication

- The Actions run, including `deploy-pages` and the OIDC token exchange.
- The live site over HTTPS: base path, caching, and the footer/README as GitHub renders them.
- Anything that depends on repository settings (Pages source, branch protection) — not touched, not verified.

## 6. Limitations you are publishing with

1. Runtime evidence is CPython 3.14.7 on Windows 11, CPU only. No macOS or Linux run was performed.
2. No screen-reader or cross-browser accessibility audit; the checks were structural (landmarks, one `h1`, alt text,
   keyboard-reachable nav, 390 px layout).
3. The safety sections are editorial, not a security certification. Do not describe them, or the course, as audited or
   certified by a third party.
4. Module difficulty tags and quiz difficulty labels are author judgements, not measured against students.
5. The Actions deploy step has never run.

## 7. Statement of non-action

No commit, stage, branch, tag, push, publish, deploy, remote change, GitHub setting change or history rewrite was
made. Verification artefacts outside the repository (`/tmp/sas-audit/`) are evidence only; `.pages-test/` and
`.venv-verify/` were removed and the local preview server stopped.
