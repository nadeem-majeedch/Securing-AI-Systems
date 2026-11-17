"""L32 — A release gate that reads evidence (M20, Challenge).

Goal: assemble the evidence an earlier lab produced into one gate, make the decision mechanical, and show that a
missing or failed item blocks the release with a reason.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import pandas as pd

from labkit import check, report


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L32/solution.py (open it only after trying).

# STEP 1: the gate specification — required items, thresholds and the lab that produces each one.
# TODO 1: implement this step.

# STEP 2: the candidate release, with every item present and passing.
# TODO 2: implement this step.

# STEP 3: three ways the same gate blocks — missing, below threshold, and the wrong direction.
# TODO 3: implement this step.

# STEP 4: a gate needs an accountable owner and an expiry.
# TODO 4: implement this step.

# STEP 5: the statement the gate lets you make.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
