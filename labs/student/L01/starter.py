"""L01 — Security properties audit of a clinical triage assistant (M01, Beginner).

Goal: classify the assistant's assets against confidentiality, integrity and availability, then find the
records in the referral feed that already violate the stated policy.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

from labkit import check, load_csv, report

ALLOWED_TRIAGE = {"green", "amber", "red"}
INJECTION_MARKERS = ("ignore previous instructions", "system:", "disregard")


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L01/solution.py (open it only after trying).

# STEP 1: load the referral feed and show its shape.
# TODO 1: implement this step.

# STEP 2: map each asset to the security property it depends on.
# TODO 2: implement this step.

# STEP 3: flag records that break the policy.
# TODO 3: implement this step.

# STEP 4: summarise which property each defect threatens.
# TODO 4: implement this step.

# STEP 5: assert the audit found the seeded defects.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
