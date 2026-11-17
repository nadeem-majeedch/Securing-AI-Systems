# Workflow branch correction — GitHub Pages on `main`

**Task 17 · 17 November 2026**
**File changed:** `.github/workflows/pages.yml` — 3 lines, one file
**Verdict: the workflow is ready for a push to `main`.**

The repository publishes from `main`; the workflow still named `master` in three places. Branch names were not
renamed, nothing was committed, pushed or deployed, and no GitHub setting was touched.

---

## 1. What changed

| Line | Before | After | Purpose |
|---|---|---|---|
| 3 | `# Trigger: every push to master (the default branch), plus manual dispatch.` | `# Trigger: every push to main (the default branch), plus manual dispatch.` | Header comment matches behaviour |
| 22 | `branches: [master]` | `branches: [main]` | Push trigger fires on the default branch |
| 113 | `if: github.ref == 'refs/heads/master'` | `if: github.ref == 'refs/heads/main'` | Only `main` may publish |

```diff
@@ -1,7 +1,7 @@
-# Trigger: every push to master (the default branch), plus manual dispatch.
+# Trigger: every push to main (the default branch), plus manual dispatch.
@@ -20,7 +20,7 @@
-    branches: [master]
+    branches: [main]
@@ -110,7 +110,7 @@
-    if: github.ref == 'refs/heads/master'
+    if: github.ref == 'refs/heads/main'
```

`grep -n master .github/workflows/pages.yml` returns nothing: no publishing reference to `master` remains.

## 2. What was preserved, unchanged

- `workflow_dispatch` — retained alongside the push trigger.
- Least privilege — top level `permissions: contents: read`; `build` job `contents: read`; `deploy` job only
  `pages: write` and `id-token: write`.
- SHA-pinned actions, all first-party: `actions/checkout@3d3c42e5…` (v7.0.1),
  `actions/setup-python@6d4fd22b…` (v7.1.0), `actions/upload-pages-artifact@fc324d35…` (v5.0.0),
  `actions/deploy-pages@368f8252…` (v5.0.1).
- Checkout still uses `persist-credentials: false`; no repository secret is referenced.
- Concurrency `pages` / `cancel-in-progress: false`; `environment: github-pages` with `page_url`.
- The whole MkDocs pipeline: docs-dependency pin check → install `requirements-docs.txt` only → `check_links.py` →
  `check_notebooks.py` → `mkdocs build --strict` → `verify_site.py site --base-path /Securing-AI-Systems/` →
  upload `site` → `deploy-pages` (600 s, 10 retries, 5 s interval). Python 3.12 on `ubuntu-latest`.

## 3. Validation run after the edit

| Check | Command | Result |
|---|---|---|
| YAML syntax + semantics | `python` / `yaml.safe_load` with 19 assertions | **PASS**, all 19 |
| Workflow lint | `actionlint 1.7.7 .github/workflows/pages.yml` | **exit 0**, no diagnostics |
| MkDocs strict build | `NO_MKDOCS_2_WARNING=1 python -m mkdocs build --strict` | **exit 0**, 0 warnings, 8.6 s |
| Artifact generation | `site/` contents — `index.html`, `404.html`, `sitemap.xml`, `search/search_index.json` | **present**; 432 files, 27 MB, search index valid JSON (1.5 MB) |
| Artifact verification | `python scripts/verify_site.py site --base-path /Securing-AI-Systems/` | **RESULT: PASS** |
| Branch conditions | parsed with the YAML loader, not by eye | `on.push.branches == ['main']`, `deploy.if == "github.ref == 'refs/heads/main'"` |
| Residual references | `grep -n master .github/workflows/pages.yml` | **none** |
| Working tree | `git status --porcelain --untracked-files=no` | one modified file; nothing staged |

## 4. Resulting trigger matrix

| Event | Build job | Deploy job |
|---|---|---|
| Push to `main` | runs | **runs** |
| Manual dispatch on `main` | runs | **runs** |
| Manual dispatch on any other branch | runs (validation only) | skipped by the `if:` guard |
| Push to any other branch | does not run | does not run |

This matches `DEPLOYMENT.md` (lines 20, 38, 58–59, 122–126), which already documented `main` as the source of truth —
the workflow was the only artefact still pointing at `master`.

## 5. Note: documents that still say `master` (not changed here)

Out of scope for this task, listed so they are not mistaken for workflow problems:

- `FINAL_OWNER_HANDOVER.md` — §1 status table, §3.1 trigger row, §4 item 5, §6 job table, and the review/publish
  commands in §9. Its `git push -u origin master` **would now fail** (*src refspec master does not match any*); the
  correct command is `git push -u origin main`. This file is a snapshot of the Task 16 freeze and should be updated
  or retired before it is handed to anyone.
- `PHASE_14_REPORT.md`, `PHASE_15_REPORT.md`, `FINAL_PUBLICATION_CHECKLIST.md`, `OWNER_PUBLICATION_HANDOVER.md`,
  `PUBLICATION_READINESS_REPORT.md`, `FINAL_AUDIT_REPORT.md`, `TECHNICAL_VALIDATION_REPORT.md` — historical records of
  the state when they were written. Deliberately not rewritten.

Ask for it and I will align `FINAL_OWNER_HANDOVER.md` with `main` in one pass.

## 6. Statement of non-action

No branch was created, renamed or deleted. Nothing was committed, staged, pushed, published or deployed. No remote,
GitHub setting, Pages configuration or environment rule was changed. The only modification in the working tree is the
three-line workflow correction described above (`git diff` shows 1 file changed, 3 insertions, 3 deletions).

**Ready for a push to `main`:** the trigger, the deploy guard, the documented configuration and the locally verified
artifact all agree on `main`.
