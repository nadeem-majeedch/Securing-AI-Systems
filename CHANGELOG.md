# Changelog

All notable changes to the **Securing AI Systems** course are recorded here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); the project uses [Semantic Versioning](https://semver.org/).

**Versions here are internal milestones, not public releases.** The course has not been published and no licence has been applied, so a version number records the state of the repository at a point in time; it grants nothing and promises no support.

**How to read an entry.** Course changes that affect what a student must do (a corrected success criterion, a renumbered module, a changed prerequisite) are marked **breaking**. Framework version changes are recorded with the module they affect, because a student's results depend on them.

---

## [Unreleased]

### Added — GitHub Pages deployment (17 November 2026)

- `.github/workflows/pages.yml`: builds on every push to `main` and on manual dispatch, validates the build, uploads the Pages artifact and deploys it through the official Pages actions. `contents: read` by default, `pages: write` and `id-token: write` only on the deploy job, the `github-pages` environment, no stored secret and no personal access token. Actions are pinned to commit SHAs with the release in a comment.
- `scripts/verify_site.py`: post-build validation of structure, link and asset resolution (including anchors), project-site base-path safety, canonical URL and sitemap, search index, diagram wiring, privacy invariants and artifact limits. Runs in CI and locally.
- `mkdocs.yml`: `site_url` set to the project-site URL, so canonical links, the sitemap and template `url` filters carry `/Securing-AI-Systems/`.
- `DEPLOYMENT.md` rewritten for the workflow: required repository settings, how the jobs operate, owner enablement steps, success signals, troubleshooting, update and rollback procedure, and the local reproduction of CI.
- `scripts/check_links.py` now accepts directory-style URLs (`foo/` for `foo.md`), so hand-written HTML links are checked rather than skipped, and it covers the repository documents as well as the course pages.

### Fixed — links that only worked on GitHub

- 194 raw-HTML anchors in the home page and all twenty module pages pointed at `.md` files. GitHub renders those; the published site does not. They now point at the built directory URLs.
- The status badge on every module page linked `../getting-started/how-to-use/#status-badges`, which resolves one directory too shallow from `modules/NN-slug/` and 404s on the published site. Corrected to `../../getting-started/how-to-use/#status-badges` (20 pages).

### Added — licensing, attribution and repository documentation (17 November 2026)

- `LICENSING.md`: a six-category licensing audit, the recommended model (MIT for original code, CC BY 4.0 for original content, CC0 1.0 for synthetic datasets), a comparison with the previously proposed CC BY-NC-SA 4.0, and an owner decision record D-01a–D-01f. **No licence has been applied.**
- `ATTRIBUTION.md`: the third-party register — frameworks, research, case-study sources, code libraries, vendored JavaScript, icons, and datasets — with the obligation attached to each.
- `SECURITY.md`: scope, reporting channel, response targets, safe harbour and out-of-scope material for the repository and site.
- `CODE_OF_CONDUCT.md`: Contributor Covenant 2.1, adapted, including unauthorised testing, plagiarism and disclosure clauses.
- `CONTRIBUTING.md`: licensing and attribution requirements for contributions; corrected references to `docs/references.md`.
- `DEVELOPMENT.md`: corrected the repository layout and the diagram-rendering description (Mermaid is now vendored, not fetched from a CDN); added the link checker and the licensing/attribution maintenance procedure.
- `DEPLOYMENT.md`: licensing and attribution added to the pre-publication checklist; the "no third-party requests" property now holds for diagrams too.
- `CHANGELOG.md`: this file.

### Added — student-facing guidance (17 November 2026)

- [Academic integrity and responsible use](docs/getting-started/academic-integrity.md): responsible use of AI security tools, authorised testing, academic honesty, citation, sensitive datasets, and coordinated vulnerability disclosure.
- [Privacy](docs/getting-started/privacy.md): what the course does and does not store, in plain terms.
- [Credits and attribution](docs/attribution.md): what is original, what is third-party, how to cite the course, and the current licence status.
- `scripts/check_links.py` now checks root-level documentation as well as the course pages, so repository links are validated with the site.

### Changed

- `README.md` §23 now states the licence options and points to `LICENSING.md`; the pending status is unchanged.
- `docs/references.md` closes with a pointer to the attribution page instead of restating a licence that does not exist.

---

## [0.9.0] — 2026-11-17

### Changed — visual system and navigation

- Flattened the home-page hero (no gradients) and rebuilt it as a flat navy panel with one cyan rule.
- Content grid widened from 76 rem (which overshot the viewport at Material's 20 px root) to a 1180 px measure with responsive gutters.
- Fixed primary and secondary buttons, which inherited navy text on a navy page and measured 1.1:1 contrast; both schemes now use explicit cyan tokens.
- Replaced the module meta strip with a module card (level, status, hours, prerequisite, laboratory) and a chip row linking outcomes, lab, notebook, exercises, knowledge check, quiz and research cluster. Applied to all twenty modules.
- Added previous/next lesson navigation to every module, and related-topic links as HTML.
- Restructured top-level navigation into eight tabs: Home, Start Here, Roadmap, Modules, Labs, Assess, Projects, Reference.
- Notebook downloads: the 34 laboratory notebooks are published under `docs/notebooks/` and listed per module on the Labs page.

### Fixed — accessibility

- Removed 28 empty, unnamed tab stops per code block by disabling line-number anchors.
- Made wide tables scroll (with a visible scrollbar) instead of being clipped on phones.
- Diagrams now keep a readable label size below 48 em and scroll horizontally rather than shrinking to illegible type.
- Restored content gutters that had collapsed to 8 px from the viewport edge.
- Verified: skip link first in tab order, visible focus ring, no skipped heading levels, no unlabelled images, no generic link text.

### Fixed — diagrams

- Material's diagram support fetched Mermaid from `unpkg.com` at runtime, which left every diagram an empty box when the network was unavailable or blocked. Mermaid 11.17.2 is now vendored locally and rendered by `docs/assets/javascript/diagrams.js`, with navy/cyan theme variables for both schemes. The site now makes no third-party runtime requests.

---

## [0.8.0] — 2026-11-16

### Added — course content

- Twenty modules in four levels, each with learning outcomes, threat and control mapping, worked demonstration, laboratory, failure modes, controls checklist, exercises, knowledge check and further reading.
- Thirty-two laboratory briefs with numeric success criteria, starter code, reference solutions and a dataset generator (`labs/scripts/make_datasets.py`) producing deterministic synthetic data.
- Practice quizzes for all twenty modules, four end-of-level assessments, a final assessment, and answer keys.
- Twelve scenario assignments, ten mini projects, six major projects, a capstone with five proposals, and public rubrics.
- Reference sections: seven framework pages, four research clusters, ten documented case studies plus hypothetical scenarios, a glossary and a references page.
- Jupyter notebooks for the laboratory demonstrations, validated for execution order and runtime.

### Added — site

- MkDocs Material site with dark and light palettes, client-side search, and a footer carrying course, instructor and navigation information.
- `docs/assets/javascript/progress.js`: per-module completion stored only in `localStorage`.
- Quiz component (`quiz.css`, `quiz.js`): self-marking, keyboard accessible, no network calls.

---

## [0.7.0] — 2026-11-16

### Added — scaffold

- Repository structure, `mkdocs.yml`, three separated dependency surfaces (`requirements-docs.txt`, `requirements-dev.txt`, `requirements-labs.txt`).
- `CONTRIBUTING.md` (content contract), `DEVELOPMENT.md`, `DEPLOYMENT.md`, `COURSE_ARCHITECTURE.md`, `DEVELOPMENT_ROADMAP.md`.
- Module 01 as the template for the module contract.

---

## [0.1.0] — 2026-11-16

### Added — decisions and audit

- `REPOSITORY_AUDIT.md`: read-only inspection of an empty repository, environment verification, and eight owner decisions, two of them blocking.
- `COURSE_ARCHITECTURE.md`: curriculum, learning outcomes, assessment design, folder structure and quality gates.
- `DEVELOPMENT_ROADMAP.md`: ten-phase plan with budgets and risks.

---

## Not yet released

| Item | Blocked on |
|---|---|
| Licence files (`LICENSE`, `LICENSE-CONTENT`, `LICENSE-DATA`) | Owner decision D-01a–D-01f in `LICENSING.md` |
| `CITATION.cff` and a DOI | Owner decision; institutional repository or Zenodo deposit |
| Publication of the site | Owner authorisation; see `DEPLOYMENT.md` |
| Automated content tests | Test suite not yet implemented; the contract it will enforce is in `CONTRIBUTING.md` §2 |

---

*Changes to third-party material are recorded in `ATTRIBUTION.md`, which is updated in the same change that adds or upgrades a dependency.*
