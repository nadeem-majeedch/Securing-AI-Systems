# Development

Technical documentation for building and maintaining the Securing AI Systems website. Students do not need this file — the course itself explains only what a learner needs.

---

## 1. Requirements

| Requirement | Version | Notes |
|---|---|---|
| Python | **3.11 or 3.12** | Required for the lab environment. The documentation build itself also works on newer versions |
| pip | 23+ | Standard `venv` and `pip`; no other tooling is assumed |
| Git | 2.30+ | |
| Make | optional | Commands below are given as plain shell commands so they work without `make` |

**Why 3.11/3.12?** The laboratory stack depends on PyTorch and the Adversarial Robustness Toolbox, which do not yet publish wheels for the newest CPython releases. Pinning the lab environment keeps every lab reproducible. The documentation build has no such constraint and runs on this machine's Python 3.14.

## 2. Two dependency surfaces

The project deliberately separates them. Do not merge them.

| File | Purpose | Installs |
|---|---|---|
| `requirements-docs.txt` | Build the website | MkDocs, Material, pymdown-extensions |
| `requirements-dev.txt` | Check content and tooling | pytest, ruff, nbformat, PyYAML |
| `requirements-labs.txt` | Student laboratory environment | NumPy, pandas, scikit-learn, PyTorch, FastAPI, Jupyter (all pinned) |

A reader who only wants to read the course should never download two gigabytes of PyTorch, and a student running a lab should never be blocked by a documentation plugin conflict.

## 3. Local build

```bash
# from the repository root
python -m venv .venv-docs
```

```bash
# Windows
.venv-docs\Scripts\activate

# macOS / Linux
source .venv-docs/bin/activate
```

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-docs.txt
python -m mkdocs serve
```

The site is served at <http://127.0.0.1:8000> with live reload.

Build a production copy without serving it:

```bash
python -m mkdocs build --strict
```

**`--strict` is mandatory before any release.** Without it, MkDocs treats broken links, pages missing from `nav`, and unmatched documentation references as warnings. With it, they fail the build — which is the only behaviour that keeps a twenty-module site honest.

The output is written to `site/`, which is git-ignored.

## 4. Checks

```bash
# build the site exactly as a release would
python -m mkdocs build --strict

# internal links: every page in docs/ and every repository document
python scripts/check_links.py

# verify the production build as CI does: structure, base path, assets, search, diagrams
python -m mkdocs build --strict
python scripts/verify_site.py site --base-path /Securing-AI-Systems/

# content contract tests (available once the test suite lands)
python -m pytest tests/ -q
```

The content suite turns the editorial contract in `CONTRIBUTING.md` into failing tests: missing contract sections, placeholder markers, word-count floors, unresolved citation IDs, images without alt text, Mermaid blocks without descriptions, secret-shaped strings, and instructor pages appearing in the build output.

## 5. Repository layout

```text
Securing-AI-Systems/
├── .github/workflows/
│   └── pages.yml           # build → validate → deploy to GitHub Pages (see DEPLOYMENT.md)
├── mkdocs.yml              # site configuration, site_url and the full navigation tree
├── requirements-*.txt      # documentation, development and lab dependencies
├── scripts/                # check_links.py, verify_site.py, check_env.py
├── overrides/              # Material template overrides
│   ├── 404.html            # not-found page: a static template, not a docs page
│   └── partials/
│       └── copyright.html  # footer with course and instructor information
├── docs/
│   ├── index.md            # home page
│   ├── getting-started/    # orientation, prerequisites, environment, study plans
│   ├── roadmap.md          # learning pathway with progress tracking
│   ├── modules/            # one page per module, grouped by part in nav
│   ├── labs/               # laboratory catalogue (lab pages arrive with content)
│   ├── assignments/        # scenario-based assignments
│   ├── quizzes/            # self-check quiz index
│   ├── projects/           # mini and major projects
│   ├── capstone/           # capstone brief and milestones
│   ├── glossary.md         # term definitions
│   ├── references.md       # bibliography
│   ├── attribution.md      # student-facing credits and licence status
│   ├── notebooks/          # downloadable laboratory notebooks
│   ├── instructor/         # instructor material — EXCLUDED from the build
│   └── assets/             # stylesheets, scripts, vendored Mermaid
└── site/                   # build output (git-ignored)
```

## 6. How the site is wired

| Concern | Implementation |
|---|---|
| Theme | MkDocs Material 9.8, custom palette defined in `docs/assets/stylesheets/extra.css` |
| Colour schemes | Dark (slate, default) and light, both defined from the same design tokens |
| Fonts | `theme.font: false` plus a system font stack in `extra.css`, so no Google Fonts request is made. Self-hosting webfonts later is a CSS-only change |
| Diagrams | `sas-mermaid` fences, rendered by `docs/assets/javascript/diagrams.js` using the vendored Mermaid 11 in `assets/javascript/vendor/`. The script loads only on pages that contain a diagram, themes the SVG from the same colour tokens as the rest of the site, and re-renders on a palette change. Material's built-in diagram support fetches Mermaid from a CDN and empties the block when that fails — do not re-enable it |
| Search | Material's client-side search; no server component |
| Progress tracking | `docs/assets/javascript/progress.js`, `localStorage` only, no network calls |
| Navigation | Top-level tabs, sidebar sections, footer previous/next links |
| Instructor material | `docs/instructor/**` is excluded through `exclude_docs` in `mkdocs.yml` |

### Adding a module page

1. Create `docs/modules/NN-slug.md` using an existing module page as the template.
2. Set the front matter: `sas_module`, `sas_part`, `sas_status`, `sas_hours`, `sas_prereqs`.
3. Add the page to the correct part in the `nav` block of `mkdocs.yml`.
4. Keep the module status honest — `planned`, `draft`, `review`, or `complete`.
5. Run `python -m mkdocs build --strict` and the content tests.

### The progress component

`progress.js` reads the module id from the URL, renders a "mark complete" control into any `[data-sas-progress]` element on the page, and stores completion in `localStorage` under `sas.progress.v1`. The roadmap page's `[data-sas-overview]` element renders per-part progress from the same store.

The module-to-part mapping is a constant at the top of the script. **If you renumber or move a module, update that constant** — it is the one place where structure is duplicated outside `mkdocs.yml`.

The component degrades cleanly: without JavaScript the control is not rendered and nothing else changes. It never sends data anywhere.

## 7. Known constraints

| Constraint | Detail |
|---|---|
| Mermaid is vendored | `assets/javascript/vendor/mermaid.min.js` is 3.5 MB and is fetched only by pages that contain a diagram. The site therefore makes **no third-party runtime request at all**, and diagrams work offline |
| No notebook plugin yet | Notebook rendering (`mkdocs-jupyter`) is added with the laboratory phase, so no dependency is installed that the content does not yet use |
| Windows paths contain a space | Quote every path in scripts; do not rely on symlinks |
| CI is the Pages workflow | `.github/workflows/pages.yml` builds, validates and deploys on every push to `main`. There is no separate test workflow until the content test suite exists, so `check_links.py` and `verify_site.py` are the automated gates — run them locally before pushing (see `DEPLOYMENT.md` §8) |

## 8. Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: material` | Docs dependencies not installed in the active environment | `python -m pip install -r requirements-docs.txt` |
| Build fails with "not found in `nav`" | A page exists without a navigation entry | Add it to `nav`, or move it under `docs/instructor/` if it is not student-facing |
| Diagram shows as raw text | The fence is tagged `mermaid` instead of using the `sas-mermaid` custom class, or `diagrams.js` did not load | Check `mkdocs.yml` → `pymdownx.superfences.custom_fences` and the `extra_javascript` entry |
| Diagram area is empty | Mermaid failed to parse the definition | Open the console; the script logs the error and leaves a readable message in the block |
| Diagrams render unstyled | Colour tokens missing | Confirm the `--sas-*` tokens exist for both schemes in `extra.css`, and that `diagrams.js` re-themes on `palette` change |
| Progress does not persist | Private browsing, or `localStorage` blocked | Expected degradation; the control still toggles for the session |
| Type looks different across machines | The design uses a system font stack (Segoe UI, SF Pro, Inter, Arial) | Expected. Add self-hosted webfonts in `extra.css` if a single face matters for print or PDF export |

---

## 9. Licensing, attribution and privacy maintenance

Technical maintenance has three obligations that are easy to defer and expensive to fix later. They belong to whoever changes the repository, not to a later audit.

### 9.1 The licence is a recorded decision, not a default

`LICENSING.md` holds the audit, the recommended model (MIT for code, CC BY 4.0 for content, CC0 1.0 for synthetic data) and the owner's decision record. Until D-01a–D-01f are signed, **no licence file exists and the site says "all rights reserved"**. Do not add a `LICENSE` file, a licence badge or a permissive sentence to a page on your own initiative: an unreviewed licence claim is harder to withdraw than to add.

When the decision is recorded, the files are `LICENSE` (code), `LICENSE-CONTENT` (prose) and `LICENSE-DATA` (synthetic data), and the scope table in `LICENSING.md` §3.2 is the authority on which paths each one covers.

### 9.2 Adding or upgrading a dependency

1. Add the row to `ATTRIBUTION.md` — package, pinned version, licence, and the obligation it creates — before the pull request is opened.
2. Check the licence is compatible with the recorded model: MIT, BSD and Apache-2.0 are fine; a copyleft runtime in the browser bundle would need a decision, because it would change what the course can license.
3. If the package is vendored (as Mermaid is), keep the upstream notices intact and record the exact version in the register and in `CHANGELOG.md`.
4. Verify what is installed, not what the documentation says:

```bash
python - <<'PY'
import importlib.metadata as m
for n in ["mkdocs", "mkdocs-material", "pymdown-extensions"]:
    md = m.metadata(n)
    print(f"{n:24s}", md.get("License-Expression") or md.get("License"))
PY
```

### 9.3 The privacy surface is a constraint on design

`docs/getting-started/privacy.md` makes specific claims: no accounts, no analytics, no cookies for tracking, no third-party runtime request, and one `localStorage` key. Every one of them is a testable statement, and a plugin that adds analytics, a comment system, a hosted search, a webfont or an embedded video falsifies them.

| Change | Breaks | Required response |
|---|---|---|
| Analytics or tag manager | Privacy page §2 | Do not add it. The course's argument about data minimisation depends on this |
| A CDN for fonts, icons or libraries | Privacy page §2, offline use | Vendor the asset, as was done for Mermaid |
| A comment or feedback service | Privacy page §2 | Not adopted; an institutional form belongs to the institution, not the site |
| A second `localStorage` key | Privacy page §1 | Update the page in the same change and keep the key namespaced `sas.*` |
| A notebook that downloads data | `ATTRIBUTION.md` §6, privacy page §5 | Prefer a checked-in synthetic file; if a download is unavoidable, record the source, its licence and a checksum |

`progress.js` is the model for how this is done: one key, no network call, and a documented degradation path when storage is blocked.

---

*For release and publishing procedure, see `DEPLOYMENT.md`. For content rules, see `CONTRIBUTING.md`. For the licence position, see `LICENSING.md`.*
