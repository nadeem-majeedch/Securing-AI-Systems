"""L06 — Intake validation and quarantine for patient referrals (M05, Beginner).

Goal: reject dirty rows at the boundary with a stated reason, without silently dropping anything. The count
accepted plus the count quarantined must equal the input count.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import pandas as pd

from labkit import check, load_csv, report

ALLOWED_TRIAGE = {"green", "amber", "red"}
INJECTION = ("ignore previous instructions", "system:", "disregard")


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L06/solution.py (open it only after trying).

# STEP 1: load raw input and record the original count.
# TODO 1: implement this step.

# STEP 2: define one validator per column, each returning a reason or None.
# TODO 2: implement this step.

# STEP 3: partition into accepted and quarantined, keeping the reason.
# TODO 3: implement this step.

# STEP 4: summarise the reasons so the source team can fix the feed.
# TODO 4: implement this step.

# STEP 5: assert the policy outcomes that matter.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
