"""Shared helpers for the Securing AI Systems laboratories.

Students may read this file: it contains no answers, only path handling, a small assertion helper and a
table printer used by the starter scripts (and by the solutions).
"""

from __future__ import annotations

import json
import pathlib

import pandas as pd

LABS = pathlib.Path(__file__).resolve().parents[1]
DATASETS = LABS / "datasets"


def data_path(name: str) -> pathlib.Path:
    """Absolute path to a file in labs/datasets/."""
    path = DATASETS / name
    if not path.exists():
        raise FileNotFoundError(f"{name} is missing. Run: python labs/scripts/make_datasets.py")
    return path


def load_csv(name: str) -> pd.DataFrame:
    return pd.read_csv(data_path(name))


def load_json(name: str) -> dict:
    return json.loads(data_path(name).read_text(encoding="utf-8"))


def report(title: str, rows) -> None:
    """Print a small table without needing tabulate."""
    frame = pd.DataFrame(rows)
    print(f"\n== {title} ==")
    print(frame.to_string(index=False))
    print()


def check(condition: bool, message: str) -> None:
    """Fail loudly when a lab invariant does not hold."""
    if not condition:
        raise AssertionError(message)
