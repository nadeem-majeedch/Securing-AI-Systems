"""L24 — A malicious dependency and a tampered model bundle (M15, Beginner).

Goal: audit a dependency list, verify a model bundle against its manifest, and show why a pickle is not a model
format you accept from a third party.
"""

import hashlib
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import pandas as pd

from labkit import check, data_path, report


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L24/solution.py (open it only after trying).

# STEP 1: audit the dependency list the way a reviewer would.
# TODO 1: implement this step.

# STEP 2: hash every file in a bundle against its manifest.
# TODO 2: implement this step.

# STEP 3: the check is only useful if it fails on the tampered copy.
# TODO 3: implement this step.

# STEP 4: refuse the deserialisation path before you ever load weights.
# TODO 4: implement this step.

# STEP 5: what the pipeline needs before the first import.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
