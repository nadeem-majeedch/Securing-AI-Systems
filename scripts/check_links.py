#!/usr/bin/env python3
"""Validate internal and external links in the course documentation.

Internal links: every relative ``*.md`` link must resolve to a file, and every
``#anchor`` must match a heading in the target file.

External links: every ``http(s)`` URL is requested once. A 4xx/5xx response,
DNS failure or timeout is reported as a failure; 403/405/429 are reported as
"inconclusive" because those sites block automated clients.

Usage
-----
    python scripts/check_links.py                # internal links only
    python scripts/check_links.py --external     # also check http(s) URLs
    python scripts/check_links.py --external --strict-blocked   # treat blocked as failure

Exit status is 1 if any internal link is broken, or any external URL fails,
or (with --strict-blocked) any external URL is inconclusive.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import re
import ssl
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:  # prefer certifi's bundle: the Windows store often lacks arXiv's chain
    import certifi

    SSL_CONTEXT = ssl.create_default_context(cafile=certifi.where())
except Exception:  # certifi not installed
    SSL_CONTEXT = ssl.create_default_context()

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# Markdown link/image: [text](target) or ![alt](target)
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")

USER_AGENT = "Mozilla/5.0 (compatible; securing-ai-systems-course-link-check/1.0)"
TIMEOUT = 20


def slugify(text: str) -> str:
    """Approximate MkDocs/Python-Markdown heading id generation."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_~]", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text.strip("-")


def anchors_for(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    text = FENCE_RE.sub("", text)
    text = CODE_SPAN_RE.sub("", text)
    found = set()
    for _, heading in HEADING_RE.findall(text):
        heading = heading.strip()
        found.add(slugify(heading))
    return found


def iter_markdown() -> list[Path]:
    """Course pages plus the repository's own documentation.

    Root-level files (README, CONTRIBUTING, LICENSING, ATTRIBUTION, SECURITY,
    CODE_OF_CONDUCT, CHANGELOG, DEPLOYMENT, DEVELOPMENT, the architecture and
    audit documents) link into docs/, so they are checked too.
    """
    pages = [p for p in DOCS.rglob("*.md") if p.is_file()]
    root_docs = [p for p in ROOT.glob("*.md") if p.is_file()]
    return sorted(set(pages) | set(root_docs))


def check_internal() -> list[str]:
    problems: list[str] = []
    anchor_cache: dict[Path, set[str]] = {}
    for md in iter_markdown():
        raw = md.read_text(encoding="utf-8", errors="replace")
        raw = FENCE_RE.sub("", raw)
        for target in LINK_RE.findall(raw):
            if target.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if target.startswith("#"):
                anchor = target[1:]
                if anchor and anchor != "top":
                    if md not in anchor_cache:
                        anchor_cache[md] = anchors_for(md)
                    if anchor not in anchor_cache[md]:
                        problems.append(f"{md.relative_to(ROOT)}: missing own anchor #{anchor}")
                continue
            file_part, _, anchor = target.partition("#")
            if not file_part:
                continue
            resolved = (md.parent / file_part).resolve()
            if not resolved.exists():
                # MkDocs builds directory-style URLs: `foo.md` is published as
                # `foo/`, and `dir/index.md` as `dir/`. Accept those forms so
                # hand-written HTML links are checked rather than falsely failed.
                if file_part.endswith("/"):
                    candidates = [resolved / "index.md", resolved.parent / (resolved.name + ".md")]
                else:
                    candidates = [resolved.with_suffix(".md")]
                match = next((c for c in candidates if c.is_file()), None)
                if match is None:
                    problems.append(
                        f"{md.relative_to(ROOT)}: broken link -> {target} (no such file)"
                    )
                    continue
                resolved = match
            if anchor and resolved.suffix == ".md":
                if resolved not in anchor_cache:
                    anchor_cache[resolved] = anchors_for(resolved)
                if anchor not in anchor_cache[resolved]:
                    problems.append(
                        f"{md.relative_to(ROOT)}: broken anchor -> {target}"
                    )
    return problems


def collect_external() -> dict[str, set[str]]:
    """Map URL -> set of files that reference it."""
    urls: dict[str, set[str]] = {}
    for md in iter_markdown():
        raw = md.read_text(encoding="utf-8", errors="replace")
        for target in LINK_RE.findall(raw):
            if target.startswith(("http://", "https://")):
                urls.setdefault(target.rstrip(".,;"), set()).add(str(md.relative_to(ROOT)))
    return urls


def fetch(url: str) -> tuple[str, int | None, str]:
    """Return (url, status, note). status None means transport failure."""
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT, context=SSL_CONTEXT) as resp:
                return url, resp.status, "ok"
        except urllib.error.HTTPError as exc:
            if method == "HEAD" and exc.code in (403, 405, 400, 501):
                continue  # some servers reject HEAD; retry with GET
            return url, exc.code, exc.reason or ""
        except urllib.error.URLError as exc:
            return url, None, str(exc.reason)
        except Exception as exc:  # timeout, TLS, malformed
            return url, None, f"{type(exc).__name__}: {exc}"
    return url, None, "no response"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--external", action="store_true", help="also check http(s) links")
    parser.add_argument(
        "--strict-blocked",
        action="store_true",
        help="treat 403/405/429 (bot-blocked) as failures",
    )
    parser.add_argument("--jobs", type=int, default=8, help="parallel requests (default 8)")
    args = parser.parse_args()

    problems = check_internal()
    print(f"internal links: {len(problems)} problem(s)")
    for problem in problems:
        print("  FAIL", problem)

    failures = 0
    if args.external:
        urls = collect_external()
        print(f"external links: {len(urls)} unique URL(s)")
        blocked = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.jobs) as pool:
            results = list(pool.map(fetch, sorted(urls)))
        for url, status, note in sorted(results, key=lambda r: (r[1] is None, r[0])):
            where = ", ".join(sorted(urls[url]))
            if status is None:
                print(f"  FAIL {url} -> {note}  [{where}]")
                failures += 1
            elif status in (403, 405, 429):
                print(f"  WARN {url} -> HTTP {status} (blocked/inconclusive)  [{where}]")
                blocked += 1
            elif 400 <= status < 600:
                print(f"  FAIL {url} -> HTTP {status}  [{where}]")
                failures += 1
            if args.strict_blocked:
                pass
        print(f"external: {failures} failure(s), {blocked} inconclusive (blocked) response(s)")
        if args.strict_blocked:
            failures += blocked

    total = len(problems) + failures
    print("RESULT:", "FAIL" if total else "PASS")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
