#!/usr/bin/env python
"""Check the course notebooks against the committed-output policy.

Policy (see CONTRIBUTING.md §6 and docs/labs/index.md):

* Notebooks are committed **with** their outputs, because a student reading on
  GitHub should see the result of a cell without running it.
* Those outputs must be worth committing: no absolute local paths, no
  machine-specific state, and no oversized blobs.
* Every notebook is valid nbformat 4 with a ``python3`` kernel so it runs from
  a fresh kernel on another machine.

Run from the repository root:

    python scripts/check_notebooks.py            # static policy checks
    python scripts/check_notebooks.py --execute  # also run every notebook (slow)

Exits 1 on any violation, so it can gate a pull request.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

MAX_NOTEBOOK_BYTES = 250_000
MAX_SINGLE_OUTPUT_BYTES = 200_000
ABSOLUTE_PATH = re.compile(r"(?:[A-Za-z]:\\|(?<![\w.])/(?:Users|home|root|private|tmp)/)")


def iter_notebooks(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.ipynb") if ".ipynb_checkpoints" not in p.parts)


def output_texts(output: dict) -> list[str]:
    """Return the plain text an output actually shows, without JSON escaping."""
    texts: list[str] = []
    stream = output.get("text")
    if isinstance(stream, list):
        texts.append("".join(stream))
    elif isinstance(stream, str):
        texts.append(stream)
    data = output.get("data", {})
    for mime, value in data.items():
        if mime.startswith("text/") or mime == "application/json":
            if isinstance(value, list):
                texts.append("".join(value))
            elif isinstance(value, str):
                texts.append(value)
    traceback_lines = output.get("traceback")
    if isinstance(traceback_lines, list):
        texts.append("\n".join(traceback_lines))
    return texts


def check_static(path: Path) -> list[str]:
    problems: list[str] = []
    size = path.stat().st_size
    if size > MAX_NOTEBOOK_BYTES:
        problems.append(f"{path}: {size:,} bytes exceeds the {MAX_NOTEBOOK_BYTES:,}-byte cap")

    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return problems + [f"{path}: not valid JSON ({exc})"]

    if notebook.get("nbformat") != 4:
        problems.append(f"{path}: nbformat {notebook.get('nbformat')!r}, expected 4")

    kernel = notebook.get("metadata", {}).get("kernelspec", {}).get("name")
    if kernel != "python3":
        problems.append(f"{path}: kernel {kernel!r}, expected 'python3'")

    for index, cell in enumerate(notebook.get("cells", [])):
        for output in cell.get("outputs", []):
            encoded = len(json.dumps(output).encode("utf-8"))
            if encoded > MAX_SINGLE_OUTPUT_BYTES:
                problems.append(f"{path}: cell {index} output is {encoded:,} bytes")
            for text in output_texts(output):
                match = ABSOLUTE_PATH.search(text)
                if match:
                    fragment = text[max(0, match.start() - 30): match.start() + 50].replace("\n", " ")
                    problems.append(f"{path}: cell {index} output contains an absolute path: ...{fragment}...")
                    break
    return problems


def check_published_copy(root: Path, path: Path) -> list[str]:
    """The site serves docs/notebooks/, so the copy must be byte-identical.

    Two copies exist on purpose: the repository root is where the notebooks run
    and are validated, and docs/notebooks/ is what a student downloads from the
    site. Drift between them would publish something the course never executed.
    """
    published = root / "docs" / "notebooks" / path.relative_to(root / "notebooks")
    if not published.is_file():
        return [f"{path}: missing from docs/notebooks/ — copy it so the site serves the validated file"]
    if published.read_bytes() != path.read_bytes():
        return [f"{path}: differs from {published.relative_to(root)} — re-copy the validated notebook"]
    return []


def execute(path: Path) -> list[str]:
    import nbformat
    from nbclient import NotebookClient

    notebook = nbformat.read(path, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=180,
        kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
        allow_errors=True,
    )
    client.execute()
    return [
        f"{path}: cell {index} raised {o.get('ename')}: {str(o.get('evalue'))[:120]}"
        for index, cell in enumerate(notebook.cells)
        for o in cell.get("outputs", [])
        if o.get("output_type") == "error"
    ]


def main(argv: list[str]) -> int:
    run = "--execute" in argv
    root = Path(__file__).resolve().parent.parent
    notebooks = iter_notebooks(root / "notebooks")
    if not notebooks:
        print("FAIL: no notebooks found")
        return 1

    problems: list[str] = []
    for path in notebooks:
        rel = path.relative_to(root).as_posix()
        problems.extend(check_static(path))
        problems.extend(check_published_copy(root, path))
        if run:
            problems.extend(f"{rel}: {p.split(': ', 1)[1]}" for p in execute(path))

    print(f"notebooks checked: {len(notebooks)}" + (" (executed end to end)" if run else " (static policy)"))
    if problems:
        for problem in problems[:40]:
            print("  FAIL", problem.replace(str(root), ""))
        print(f"RESULT: FAIL ({len(problems)} problem(s))")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
