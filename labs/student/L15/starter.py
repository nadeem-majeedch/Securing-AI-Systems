"""L15 — Attribute inference and model inversion on admissions data (M09, Advanced).

Goal: recover a property of applicants the model never predicts (group membership), and reconstruct a
representative applicant profile by querying the model. The inversion is scored in standardised units,
because the attack recovers a direction, not a magnitude.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from labkit import check, load_csv, report

SEED = 61
rng = np.random.default_rng(SEED)


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L15/solution.py (open it only after trying).

# STEP 1: train a model that predicts admission and never sees the sensitive attribute.
# TODO 1: implement this step.

# STEP 2: attribute inference — learn the attribute from the score alone.
# TODO 2: implement this step.

# STEP 3: model inversion by greedy coordinate ascent in standardised space.
# TODO 3: implement this step.

# STEP 4: state the leak precisely — a direction is recovered, not a person.
# TODO 4: implement this step.

# STEP 5: the defensive reading.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
