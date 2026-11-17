"""L31 — Fairness evaluation and a mitigation that only half-works (M19, Intermediate).

Goal: measure selection rate, equal opportunity and calibration by group, then apply a reweighting mitigation and
report honestly what it fixes and what it does not.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

from labkit import check, load_csv, report

SEED = 79
FEATURES = ["gpa", "test_score", "activities"]


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L31/solution.py (open it only after trying).

# STEP 1: train the model and split by group.
# TODO 1: implement this step.

# STEP 2: the mitigation — reweight the training rows so each group contributes equally to the loss.
# TODO 2: implement this step.

# STEP 3: what improved, and what did not.
# TODO 3: implement this step.

# STEP 4: state the trade-off.
# TODO 4: implement this step.

print("No output yet: implement the steps above.")
