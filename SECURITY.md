# Security Policy

This file covers **the security of the course repository and website** — the code that builds and runs it, and the material it publishes. It does not cover the security of AI systems in general; that is what the course teaches.

Students do not need this file. If you are looking for the rules on attacking systems, read [Academic integrity and responsible use](docs/getting-started/academic-integrity.md) and the safety statement in [Getting Started](docs/getting-started/index.md).

---

## 1. What this repository is

A static documentation site built with MkDocs Material, plus the laboratory code, notebooks and assessment data that students download and run locally.

| Property | Value |
|---|---|
| Deployed artefact | Static HTML, CSS, JavaScript and downloadable files. No server-side code, no database, no accounts, no API |
| Visitor input | None. Search is client-side; progress tracking is `localStorage` |
| Third-party runtime requests | None. Mermaid is vendored into `docs/assets/javascript/vendor/` rather than fetched from a CDN, and fonts are the system stack |
| Data collected from visitors | None — see [Privacy](docs/getting-started/privacy.md) |
| Highest realistic risk | A leaked secret in published content, a malicious pull request to the build, dependency compromise in the documentation toolchain, or a student running laboratory code outside a virtual environment |

Because there is no server, most conventional web vulnerabilities do not apply. The issues that do matter are content and supply-chain issues, and they are worth reporting properly.

## 2. Reporting a vulnerability

**Preferred channel:** a private security advisory on the repository —
<https://github.com/nadeem-majeedch/Securing-AI-Systems/security/advisories/new>.
Private advisories keep the report, the discussion and the fix out of public view until a fix exists.

**If the advisory form is unavailable**, contact the instructor of record through the Department of Data Science (PUCIT), University of the Punjab. A postal and telephone route is published on the department's own website; no address is embedded in this repository, so that a stale address cannot become a silent failure.

**Do not** open a public issue, pull request, discussion or social-media post describing the problem before it is fixed, and do not test against any system other than this repository or the published course site.

### What to include

1. What the issue is, in one paragraph, and why it matters.
2. The exact URL, page or file, and the release or commit if you know it.
3. Reproduction steps — minimal and specific. For a content leak, paste the *shape* of the secret, never the value.
4. Your assessment of impact: who could be affected, and what they could do.
5. Whether you intend to publish, and any deadline you are working to.

### What to expect

| Stage | Target |
|---|---|
| Acknowledgement of the report | 5 working days |
| Initial assessment and severity | 10 working days |
| Fix for a confirmed issue | 30 days for content and configuration, 90 days where a dependency upgrade is required |
| Coordinated disclosure | Agreed with you; 90 days by default, earlier if a fix is already published |

These are targets for a single-maintainer educational project, not a commercial SLA. If a deadline matters to you, say so in the report and it will be answered.

You will be credited in `CHANGELOG.md` and in the advisory unless you ask not to be. There is no bug bounty and no payment.

## 3. Scope

**In scope**

- The published course site and its build configuration (`mkdocs.yml`, `overrides/`, `docs/assets/`).
- Scripts in `scripts/`, `labs/scripts/`, `assessments/build.py` and the JavaScript in `docs/assets/javascript/`.
- Leaked credentials, tokens, personal data or absolute local paths in published content or in the repository history.
- Publication of material that should not be public — instructor-only content, answer keys marked private, or a student's personal data.
- Cross-site scripting through rendered Markdown, quiz data, or a vendored library.
- A dependency with a known vulnerability that the site actually loads.
- Anything that lets a visitor's data leave their browser. There should be nothing to find; a finding here is significant.

**Out of scope**

- **The course's subject matter.** The modules contain working attack code against synthetic targets. That is the curriculum, not a vulnerability. Reporting "the site teaches prompt injection" will be closed without action.
- Vulnerabilities in your browser, operating system, MkDocs Material, or the hosting provider, unless this repository's configuration makes them exploitable.
- The laboratory environment on your own machine (PyTorch, Hugging Face, Jupyter). Report those upstream; the course documents the risk in Module 15.
- Missing security headers on a host the maintainers do not control.
- Automated-scanner output with no demonstrated impact, and reports produced solely by a tool.
- Denial of service by volume, spam, or social engineering of the maintainer.

## 4. Safe harbour

If you make a good-faith effort to comply with this policy, the maintainer will:

- consider your research authorised for the purposes of this repository,
- work with you on disclosure timing,
- not pursue or support legal action over the research, and
- state publicly that the research was conducted under this policy, if you wish.

That authorisation covers **this repository and the published course site only**. It does not extend to GitHub, the hosting provider, the University's other systems, or any third-party service. Do not use the course's attack techniques against anything you do not own.

## 5. Handling of sensitive reports

- Reports are read by the instructor of record and, where the issue concerns the build or hosting, by whoever maintains the deployment.
- Personal data in a report (yours or a third party's) is deleted once the issue is closed.
- If a report concerns student data, it is handled under the University's data-protection procedure rather than this document.
- A confirmed issue that affects published content is fixed in the repository first and described in `CHANGELOG.md` without reproducing the exploit.

## 6. For maintainers: before every publication

`DEPLOYMENT.md` §4 is the checklist that carries this policy into practice. At minimum, no publication happens without:

- [ ] a scan for secret-shaped strings and absolute local paths in `site/`,
- [ ] confirmation that `docs/instructor/**` is absent from `site/`,
- [ ] `python -m mkdocs build --strict` and `python scripts/check_links.py` passing,
- [ ] a review of any dependency added since the last release against `ATTRIBUTION.md`.

---

*Related: `CODE_OF_CONDUCT.md` (community expectations), `LICENSING.md` (what may be reused), `docs/getting-started/academic-integrity.md` (what students may do with the techniques).*
