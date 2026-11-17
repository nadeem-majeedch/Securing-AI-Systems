# Technical validation report

**Everything below was executed, not inferred.** Commands were run from the repository root on Windows 11 with Python 3.14.7 and the pinned documentation environment; exit codes were captured with `pipefail` so a failure inside a pipe could not be mistaken for success.

## 1. Results

| Check | Command | Result |
|---|---|---|
| MkDocs build, strict | `python -m mkdocs build --strict` | **exit 0**, 0 warnings, 6.8 s |
| Internal links and anchors | `python scripts/check_links.py` | **PASS**, 194 internal links, 0 problems |
| Built-site verification | `python scripts/verify_site.py site --base-path /Securing-AI-Systems/` | **PASS** |
| Python syntax (labs, scripts, assessments) | `python -m compileall -q …` | **exit 0** |
| YAML — workflow | `yaml.safe_load('.github/workflows/pages.yml')` | valid |
| YAML — MkDocs | parsed by MkDocs itself during the strict build | valid |
| GitHub Actions lint | `actionlint 1.7.7 .github/workflows/pages.yml` | **exit 0**, no findings |
| README relative links | script check | 0 missing |
| Navigation completeness | `--strict` build (fails on a nav target or page not in nav) | no warnings |
| Search index | `verify_site.py` | present and parseable |
| Base path | `verify_site.py` | correct for `/Securing-AI-Systems/` |
| Diagrams | `verify_site.py` | 37 pages carry rendered Mermaid |
| Build output | filesystem | 157 pages, 244 files, 27 MB |

## 2. What `verify_site.py` actually asserts

It is not a smoke test. On the built directory it checks that every page referenced by the nav exists as `index.html`; that internal URLs are prefixed with the production base path and no absolute-root URL leaks; that CSS, JS, fonts and the search index are present and non-empty; that the search index parses and has entries; that pages containing `sas-mermaid` also contain rendered `<svg>`; that no page carries an external script or font request that would break the privacy claim; and that the artifact stays inside the size budget. It passed all of them.

## 3. Browser inspection of the built site

The site was served from a copy placed at `/Securing-AI-Systems/` so that the production base path was exercised exactly as GitHub Pages will serve it.

| Page | HTTP | Rendered checks |
|---|---|---|
| Home | 200 | one `h1`, hero and CTAs correct, no horizontal overflow |
| M01 (Level 1) | 200 | — |
| M06 (Level 2) | 200 | 1 Mermaid → SVG, 5 tables (2 scroll horizontally in their wrapper), 1 code block |
| M11 (Level 3) | 200 | 1 diagram, 4 tables, module card and progress panel render |
| M16 (Level 4) | 200 | — |
| Quiz M01 | 200 | one `h1`, quiz form and answer key markup render |
| Major project P01 | 200 | — |
| Capstone index | 200 | — |
| Labs index | 200 | regenerated 32-row catalogue renders with module links |
| Attribution, prerequisites | 200 | — |

At 390 px: no page-level horizontal overflow, code blocks do not overflow, tables scroll inside their wrapper rather than breaking the layout, one `h1` per page, and no image without an `alt` attribute (the site uses inline SVG rather than raster images, so there is no raster alt-text debt). Six in-content links measured under 24 px tall; they are ordinary prose links, not navigation controls.

Search was exercised with a real `keyup` event: the index loads and returns results. 56 index entries carry only a title (mostly index pages), so they are findable by name but not by body text.

## 4. GitHub Pages workflow

`.github/workflows/pages.yml` was read line by line and linted with `actionlint 1.7.7` (clean).

- Trigger: `push` to `main`, plus `workflow_dispatch`.
- Permissions: `contents: read` at workflow level; the deploy job adds only `pages: write` and `id-token: write`.
- Concurrency: group `pages`, `cancel-in-progress: false` — correct, because cancelling a Pages deploy can leave a half-published site.
- All actions are first-party and pinned to full commit SHAs with the tag in a comment: `checkout`, `setup-python`, `upload-pages-artifact`, `deploy-pages`.
- `persist-credentials: false` on checkout, so the build cannot push.
- Steps: assert `requirements-docs.txt` is fully pinned → install docs deps only → `check_links.py` → `mkdocs build --strict` → `verify_site.py` → upload artifact → deploy (only on `main`).
- No third-party action, no repository secret, no caching of a token.

**Limitation:** the workflow has never run, because this repository has zero commits. `actionlint` and local execution of each step's command are the evidence; the deploy step itself is unexercised.

## 5. Findings

| Severity | Finding | State |
|---|---|---|
| Low | The workflow triggers on `main`; the local branch is `master` with no commits. A first push that mirrors the local branch name will not deploy. `DEPLOYMENT.md` covers this, but it is the most likely first-push failure. | open, documented |
| Low | `mkdocs.yml` uses `!!python/name:pymdownx.superfences.fence_code_format`, which is valid for MkDocs but rejected by `yaml.safe_load`. Ad-hoc tooling must load it through MkDocs, not SafeLoader. | note |
| Low | 56 search entries are titles-only; search works but body-text recall is limited for index pages. | note |
| Info | `site/` is a build artefact and is present in the working tree; it should stay out of version control (the `.gitignore` handles it). | note |

No broken internal link, no missing asset, no broken anchor, no unresolved nav entry, no unguarded external request, and no case where the build's success depends on a hidden warning. The technical gate a maintainer would put in CI is the same gate that passes here.
