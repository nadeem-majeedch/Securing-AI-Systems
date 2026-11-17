"""L29 — Triaging suspicious usage in an AI service (M17, Intermediate).

Goal: rank principals by behavioural signals, show that the ranking surfaces the incident, and write the triage
note that turns a score into an investigation.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd

from labkit import check, load_csv, report


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L29/solution.py (open it only after trying).

# STEP 1: aggregate the logs per principal.
# TODO 1: implement this step.

# STEP 2: robust z-scores per signal, then a transparent sum.
# TODO 2: implement this step.

# STEP 3: the incident is the top row, and it fires on more than one signal.
# TODO 3: implement this step.

# STEP 4: triage note template — what an analyst records before acting.
# TODO 4: implement this step.

# STEP 5: what the score cannot tell you.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
