"""L05 — Threat model and risk ranking for a hospital summariser (M04, Beginner).

Goal: turn a vague worry ("the AI could be attacked") into a ranked, evidenced threat register where every
row has an asset, a STRIDE category, a control and a way to test that control.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

from labkit import check, load_csv, report


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L05/solution.py (open it only after trying).

# STEP 1: state the system under assessment precisely enough to be wrong about it.
# TODO 1: implement this step.

# STEP 2: build the register. Impact and likelihood are 1-5; residual_factor is what remains after the control.
# TODO 2: implement this step.

# STEP 3: compute inherent and residual risk.
# TODO 3: implement this step.

# STEP 4: a register is only useful if every row can be tested and owned.
# TODO 4: implement this step.

# STEP 5: state what the ranking implies for budget.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
