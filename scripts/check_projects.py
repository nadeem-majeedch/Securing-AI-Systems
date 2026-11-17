"""Validate the project programme: counts, capstone structure, links and rubric pointers.

Run from the repository root:

    python scripts/check_projects.py

Exits non-zero and prints every failure. This is the same check used when the programme was written, kept as a
script so that a later edit cannot quietly break a brief.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

CAPSTONE_SECTIONS = [
    "Project title", "Industry background", "Problem statement", "Research motivation", "Objectives",
    "Scope", "System architecture", "Threat model", "Functional requirements", "Security requirements",
    "Dataset requirements", "Implementation methodology", "Testing methodology", "Expected results",
    "Evaluation metrics", "Deliverables", "Suggested extensions", "Assessment rubric",
]

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKIP_SUFFIX = (".png", ".jpg", ".jpeg", ".svg", ".json", ".py", ".yml", ".yaml", ".txt", ".ipynb")


def check_counts(failures: list[str]) -> None:
    mini = sorted((DOCS / "projects" / "mini").glob("mp*.md"))
    major = sorted((DOCS / "projects" / "major").glob("p*.md"))
    proposals = sorted((DOCS / "capstone" / "proposals").glob("c*.md"))
    if len(mini) < 10:
        failures.append(f"mini projects: {len(mini)} found, at least 10 required")
    if len(major) < 6:
        failures.append(f"major projects: {len(major)} found, at least 6 required")
    if len(proposals) < 5:
        failures.append(f"capstone proposals: {len(proposals)} found, at least 5 required")
    print(f"mini: {len(mini)} | major: {len(major)} | capstone proposals: {len(proposals)}")


def check_briefs(failures: list[str]) -> None:
    for path in sorted((DOCS / "projects" / "mini").glob("mp*.md")) + sorted(
        (DOCS / "projects" / "major").glob("p*.md")
    ):
        text = path.read_text(encoding="utf-8")
        lowered = text.lower()
        if "rubric" not in lowered:
            failures.append(f"{path.name}: no rubric reference")
        if "checkpoint" not in lowered and "milestone" not in lowered:
            failures.append(f"{path.name}: no checkpoints or milestones")
        if "threat" not in lowered:
            failures.append(f"{path.name}: no threat model requirement")
        if "deliverable" not in lowered:
            failures.append(f"{path.name}: no deliverables section")


def check_capstones(failures: list[str]) -> None:
    for path in sorted((DOCS / "capstone" / "proposals").glob("c*.md")):
        names = [heading for _, heading in re.findall(r"^## (\d+)\. (.+)$", path.read_text(encoding="utf-8"), re.M)]
        if names != CAPSTONE_SECTIONS:
            missing = [s for s in CAPSTONE_SECTIONS if s not in names]
            failures.append(f"{path.name}: sections wrong; missing {missing or 'none'}")


def check_links(failures: list[str]) -> None:
    broken = 0
    for md in DOCS.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            path = target.split("#")[0]
            if not path or path.endswith(SKIP_SUFFIX):
                continue
            if not (md.parent / path).resolve().exists():
                failures.append(f"broken link in {md.relative_to(DOCS)}: {target}")
                broken += 1
    print(f"broken relative links: {broken}")


def check_starter(failures: list[str]) -> None:
    required = [
        "README.md", "requirements.txt", "pytest.ini", "Dockerfile",
        "app/main.py", "app/store.py", "app/security.py", "app/model.py",
        "tests/test_api.py", "eval/harness.py", "rag/index.py",
        "monitoring/signals.py", "notebooks/baseline.py",
    ]
    for relative in required:
        if not (ROOT / "projects" / "starter" / relative).exists():
            failures.append(f"starter kit missing {relative}")
    if (ROOT / "projects" / "solutions").exists() is False:
        failures.append("projects/solutions directory is missing (briefs must be separated from solutions)")


def main() -> int:
    failures: list[str] = []
    check_counts(failures)
    check_briefs(failures)
    check_capstones(failures)
    check_links(failures)
    check_starter(failures)

    if failures:
        print(f"\n{len(failures)} problems:")
        for failure in failures:
            print(" -", failure)
        return 1
    print("\nall project checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
