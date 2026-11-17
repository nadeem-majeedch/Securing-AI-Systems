#!/usr/bin/env python3
"""Verify a built MkDocs site before it is deployed to GitHub Pages.

Run after `mkdocs build --strict`; used by CI and reproducible locally.

    python scripts/verify_site.py site
    python scripts/verify_site.py site --base-path /Securing-AI-Systems/

Checks
------
1. Required files exist (index, 404, sitemap, search index, stylesheet, scripts,
   vendored Mermaid).
2. Every internal link and asset reference in every generated page resolves to a
   file in the build. Catches a missing notebook, a deleted image, a renamed
   asset and a typo that `--strict` cannot see because it is written in HTML.
3. Project-site correctness: no root-absolute internal link may escape the base
   path. On `https://user.github.io/Securing-AI-Systems/` a link to
   `/modules/01-introduction/` resolves to user.github.io/modules/... and 404s.
4. The canonical URL and sitemap carry the expected site URL.
5. The search index is present, non-trivial and uses relative locations.
6. Diagrams are wired to the vendored Mermaid, with no CDN reference.
7. Privacy invariants: no analytics host, no absolute local path, no token.
8. The artifact is inside GitHub Pages limits (1 GiB, 20 000 files).

Exit status is 1 if any check fails. Warnings do not fail the build.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

MAX_BYTES = 1024 * 1024 * 1024  # GitHub Pages: 1 GiB published site
MAX_FILES = 20_000              # GitHub Pages: 20 000 files

REQUIRED_FILES = [
    "index.html",
    "404.html",
    "sitemap.xml",
    "search/search_index.json",
    "assets/stylesheets/extra.css",
    "assets/javascript/progress.js",
    "assets/javascript/diagrams.js",
    "assets/javascript/vendor/mermaid.min.js",
]

SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "#", "//")

ANALYTICS = re.compile(
    r"googletagmanager|google-analytics|gtag\(|plausible\.io|umami\.is|segment\.io|"
    r"hotjar|mixpanel|matomo|clarity\.ms|facebook\.net/.*fbevents",
    re.IGNORECASE,
)
LOCAL_PATH = re.compile(r"[A-Za-z]:\\\\?Users\\\\?|/home/runner/|/Users/[A-Za-z0-9._-]+/")
SECRET_SHAPE = re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}")

failures: list[str] = []
warnings: list[str] = []


def fail(message: str) -> None:
    failures.append(message)


def warn(message: str) -> None:
    warnings.append(message)


class Links(HTMLParser):
    """Collect href/src attributes from a page."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[str] = []
        self.scripts: list[str] = []
        self.has_mermaid = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for attr in ("href", "src"):
            value = values.get(attr)
            if value:
                self.targets.append(value)
        if tag == "script":
            self.scripts.append(values.get("src") or "")
        classes = values.get("class") or ""
        if "sas-mermaid" in classes:
            self.has_mermaid = True

    def handle_data(self, data: str) -> None:
        # Only inline script bodies count as executable; page prose may name an
        # analytics product (the privacy page does) without loading it.
        if self.lasttag == "script":
            self.scripts.append(data)


def resolve(site: Path, page: Path, target: str, base_path: str) -> Path | None:
    """Return the file a link should hit, or None when it escapes the site."""
    path = unquote(urlparse(target).path)
    if not path:
        return page
    if path.startswith("/"):
        if not path.startswith(base_path):
            fail(f"{page.relative_to(site)}: root-absolute link escapes the base path -> {target}")
            return None
        relative = path[len(base_path):]
    else:
        relative = path
    candidate = (page.parent / relative).resolve()
    try:
        candidate.relative_to(site.resolve())
    except ValueError:
        fail(f"{page.relative_to(site)}: link escapes the site directory -> {target}")
        return None
    if candidate.is_dir() or target.endswith("/"):
        candidate = candidate / "index.html"
    return candidate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", nargs="?", default="site", help="build output directory")
    parser.add_argument(
        "--base-path",
        default="/Securing-AI-Systems/",
        help="published base path for project-site hosting (default: /Securing-AI-Systems/)",
    )
    parser.add_argument(
        "--site-url",
        default="https://nadeem-majeedch.github.io/Securing-AI-Systems/",
        help="expected public URL, must match site_url in mkdocs.yml",
    )
    args = parser.parse_args()

    site = Path(args.site)
    base_path = args.base_path if args.base_path.endswith("/") else args.base_path + "/"

    if not site.is_dir():
        print(f"verify_site: FAIL — no build directory at {site}")
        return 1

    # 1. Required files
    for name in REQUIRED_FILES:
        if not (site / name).is_file():
            fail(f"missing required file: {name}")

    html_pages = sorted(site.rglob("*.html"))
    if len(html_pages) < 100:
        fail(f"only {len(html_pages)} HTML pages built — expected the full course")

    # 2. Instructor material must never be published
    if (site / "instructor").exists():
        fail("instructor/ is present in the build; it must stay excluded")
    for page in html_pages:
        if "instructor/" in page.relative_to(site).as_posix():
            fail(f"instructor material published: {page.relative_to(site)}")

    # 3. Link and asset resolution, base-path safety, diagram wiring
    broken: list[str] = []
    mermaid_pages = 0
    for page in html_pages:
        text = page.read_text(encoding="utf-8", errors="replace")
        if "unpkg.com" in text:
            fail(f"{page.relative_to(site)}: references a CDN (unpkg.com); diagrams must stay local")
        if SECRET_SHAPE.search(text):
            fail(f"{page.relative_to(site)}: token-shaped string found")
        if LOCAL_PATH.search(text):
            fail(f"{page.relative_to(site)}: absolute local path found in published HTML")

        parsed = Links()
        parsed.feed(text)
        if ANALYTICS.search(" ".join(parsed.scripts)):
            fail(f"{page.relative_to(site)}: analytics or tracking script found")
        if parsed.has_mermaid:
            mermaid_pages += 1
        for target in parsed.targets:
            if target.startswith(SKIP_PREFIXES):
                continue
            resolved = resolve(site, page, target, base_path)
            if resolved is None:
                continue
            if not resolved.is_file():
                broken.append(f"{page.relative_to(site)} -> {target}")
                continue
            fragment = urlparse(target).fragment
            if fragment and resolved.suffix == ".html":
                # A link to the right page with the wrong anchor is still a dead
                # end for the reader, so the id must exist in the target page.
                target_html = resolved.read_text(encoding="utf-8", errors="replace")
                if f'id="{fragment}"' not in target_html:
                    broken.append(f"{page.relative_to(site)} -> {target} (missing anchor #{fragment})")

    if mermaid_pages == 0:
        fail("no page in the build uses the sas-mermaid renderer")
    if (site / "assets/javascript/vendor/mermaid.min.js").is_file():
        if (site / "assets/javascript/vendor/mermaid.min.js").stat().st_size < 1_000_000:
            fail("vendored mermaid.min.js looks truncated")

    if broken:
        for entry in broken[:20]:
            fail(f"broken link or asset: {entry}")
        if len(broken) > 20:
            fail(f"... and {len(broken) - 20} more broken references")

    # 4. Canonical URL and sitemap
    index = (site / "index.html")
    if index.is_file():
        head = index.read_text(encoding="utf-8", errors="replace")[:20_000]
        if args.site_url.rstrip("/") not in head:
            fail(f"canonical URL does not contain {args.site_url} — check site_url in mkdocs.yml")
    sitemap = site / "sitemap.xml"
    if sitemap.is_file():
        sitemap_text = sitemap.read_text(encoding="utf-8", errors="replace")
        if args.site_url.rstrip("/") not in sitemap_text:
            fail("sitemap does not use the configured site_url")
        if sitemap_text.count("<loc>") < 100:
            fail("sitemap has too few entries — is the site being built from the right docs_dir?")

    # 5. Search index
    search = site / "search/search_index.json"
    if search.is_file():
        try:
            data = json.loads(search.read_text(encoding="utf-8"))
            docs = data.get("docs", [])
        except json.JSONDecodeError as exc:
            fail(f"search index is not valid JSON: {exc}")
            docs = []
        if len(docs) < 100:
            fail(f"search index has {len(docs)} documents — expect one per page or more")
        absolute = [d.get("location", "") for d in docs if str(d.get("location", "")).startswith("/")]
        if absolute:
            fail(f"search index has {len(absolute)} root-absolute locations; search would 404 under the base path")
        empty = [d for d in docs if not d.get("text")]
        if empty:
            warn(f"{len(empty)} search entries have no text (titles-only pages)")

    # 6. Artifact limits
    files = [p for p in site.rglob("*") if p.is_file()]
    total = sum(p.stat().st_size for p in files)
    if total > MAX_BYTES:
        fail(f"build is {total / 1024 / 1024:.0f} MiB, over the 1 GiB Pages limit")
    if len(files) > MAX_FILES:
        fail(f"build has {len(files)} files, over the 20 000-file Pages limit")

    # Report
    print(f"verify_site: {len(html_pages)} pages, {len(files)} files, {total / 1024 / 1024:.1f} MiB")
    print(f"  base path      {base_path}")
    print(f"  site url       {args.site_url}")
    print(f"  diagrams       {mermaid_pages} page(s) using sas-mermaid")
    print(f"  search index   {'ok' if search.is_file() else 'MISSING'}")
    for message in warnings:
        print("  WARN", message)
    for message in failures:
        print("  FAIL", message)
    print("RESULT:", "FAIL" if failures else "PASS")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
