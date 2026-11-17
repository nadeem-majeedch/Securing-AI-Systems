"""L17 — Tokens, context budget and the flat prompt (M11, Beginner).

Goal: show that a prompt is one token sequence regardless of role labels, budget the context window, and
demonstrate that a character filter is defeated by the way text is encoded.
"""

import pathlib
import re
import sys
import unicodedata

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

from labkit import check, load_csv, report

TOKEN_RE = re.compile(r"\s+|[A-Za-z]+|[0-9]+|[^\sA-Za-z0-9]")


def tokenize(text):
    return [t for t in TOKEN_RE.findall(text) if not t.isspace()]


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L17/solution.py (open it only after trying).

# STEP 1: see what the model actually receives — tokens, not characters or roles.
# TODO 1: implement this step.

# STEP 2: assemble a prompt from components and show the labels are not passed to the model.
# TODO 2: implement this step.

# STEP 3: enforce a context budget, system instructions first.
# TODO 3: implement this step.

# STEP 4: a character filter versus encoding.
# TODO 4: implement this step.

# STEP 5: assert the bypass, and state why the filter cannot be the only control.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
