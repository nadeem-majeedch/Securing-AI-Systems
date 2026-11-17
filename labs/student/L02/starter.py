"""L02 — Baseline evaluation and confident errors on a fraud model (M02, Beginner).

Goal: build the reference model every later lab attacks, and measure not only accuracy but calibration and
the errors the model is most confident about.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, brier_score_loss, roc_auc_score
from sklearn.model_selection import train_test_split

from labkit import check, load_csv, report


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L02/solution.py (open it only after trying).

# STEP 1: load transactions and separate features from the label.
# TODO 1: implement this step.

# STEP 2: stratified split, then fit the baseline.
# TODO 2: implement this step.

# STEP 3: three numbers that answer three different questions.
# TODO 3: implement this step.

# STEP 4: calibration in coarse bins, because a probability is a promise.
# TODO 4: implement this step.

# STEP 5: the errors the model is most sure about — the ones a reviewer must see.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
