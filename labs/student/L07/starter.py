"""L07 — De-identification and linkage risk (M05, Intermediate).

Goal: measure how identifiable a "de-identified" extract is, generalise and suppress until every group has at
least five members, then re-run the linkage attack to show the difference.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import pandas as pd

from labkit import check, load_csv, report

QUASI = ["age", "postcode", "gender"]


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L07/solution.py (open it only after trying).

# STEP 1: load the table and drop the direct identifiers.
# TODO 1: implement this step.

# STEP 2: measure the k-anonymity of the exact quasi-identifiers.
# TODO 2: implement this step.

# STEP 3: link the published table back to the name list using only the quasi-identifiers.
# TODO 3: implement this step.

# STEP 4: generalise the age and suppress small groups.
# TODO 4: implement this step.

# STEP 5: re-run linkage against the protected extract.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
