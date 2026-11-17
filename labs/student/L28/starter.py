"""L28 — A red-team matrix and a coverage statement (M18, Advanced).

Goal: run one synthetic exercise per threat family against mock components, record evidence for each cell, and
write a coverage statement that says what the exercise did not test.
"""

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import pandas as pd

from labkit import check, data_path, load_csv, load_json, report


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L28/solution.py (open it only after trying).

# STEP 1: the six cells — each returns evidence, not opinion.
# TODO 1: implement this step.

# STEP 2: a finding is only useful with a severity and an owner.
# TODO 2: implement this step.

# STEP 3: the coverage statement — what this exercise did not test.
# TODO 3: implement this step.

# STEP 4: assertions that make the exercise auditable.
# TODO 4: implement this step.

# STEP 5: what a matrix is for.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
