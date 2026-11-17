"""L14 — Membership inference on an admissions model (M09, Intermediate).

Goal: measure how much a model reveals about which applicants it was trained on, and show that the leakage
shrinks when the model is forced to generalise instead of memorise.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
from sklearn.metrics import roc_curve
from sklearn.neighbors import KNeighborsClassifier

from labkit import check, load_csv, report

SEED = 59
rng = np.random.default_rng(SEED)
FEATURES = ["gpa", "test_score", "activities"]


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L14/solution.py (open it only after trying).

# STEP 1: members and non-members from the same population, so any difference is the model's.
# TODO 1: implement this step.

# STEP 2: a 1-nearest-neighbour model memorises every training row by construction.
# TODO 2: implement this step.

# STEP 3: the attack is a threshold on confidence.
# TODO 3: implement this step.

# STEP 4: price the defence — a larger neighbourhood forces generalisation.
# TODO 4: implement this step.

# STEP 5: assertions that make the measurement trustworthy.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
