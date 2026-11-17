"""Partial reference for MP01: build and verify a digest manifest.

Deliberately incomplete. Missing, and required by the brief:
  * failure taxonomy (missing vs extra vs modified, and "cannot check")
  * duplicate and train/test-leak detection
  * provenance record and signed root
  * generated report and decision note

Use it to see the shape of a manifest and a verifier, then write the rest yourself.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


def digest_file(path: Path) -> str:
    sha = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            sha.update(block)
    return sha.hexdigest()


def build_manifest(root: Path) -> dict[str, dict[str, object]]:
    files = {}
    for path in sorted(root.rglob("*")):
        if path.is_file():
            files[str(path.relative_to(root))] = {
                "sha256": digest_file(path),
                "bytes": path.stat().st_size,
            }
    return files


def verify(root: Path, manifest: dict[str, dict[str, object]]) -> list[str]:
    """Return a list of human-readable failures.

    Note what this does not do: it cannot tell the difference between a file that changed and a manifest that
    was regenerated after a change. That distinction needs a digest obtained from somewhere else, which is the
    part of the exercise this reference leaves to you.
    """

    problems: list[str] = []
    seen = set()
    for relative, expected in manifest.items():
        path = root / relative
        seen.add(relative)
        if not path.exists():
            problems.append(f"missing: {relative}")
            continue
        if path.stat().st_size != expected["bytes"]:
            problems.append(f"size changed: {relative}")
        if digest_file(path) != expected["sha256"]:
            problems.append(f"digest changed: {relative}")
    for path in sorted(root.rglob("*")):
        if path.is_file():
            relative = str(path.relative_to(root))
            if relative not in seen:
                problems.append(f"extra: {relative}")
    return problems


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="build or verify a dataset manifest")
    parser.add_argument("path", type=Path)
    parser.add_argument("--check", type=Path, help="manifest to verify against")
    args = parser.parse_args()

    if args.check:
        manifest = json.loads(args.check.read_text(encoding="utf-8"))
        problems = verify(args.path, manifest)
        print("\n".join(problems) if problems else "ok")
        raise SystemExit(1 if problems else 0)

    print(json.dumps(build_manifest(args.path), indent=2))
