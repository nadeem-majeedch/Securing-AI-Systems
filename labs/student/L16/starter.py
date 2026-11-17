"""L16 — Model extraction from a mock prediction API (M10, Intermediate).

Goal: rebuild a proprietary admissions model from its answers, measure how much of it a given query budget
buys, and compare probability outputs with label-only outputs.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression, Ridge

from labkit import check, load_csv, report

SEED = 67
rng = np.random.default_rng(SEED)
FEATURES = ["gpa", "test_score", "activities"]


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L16/solution.py (open it only after trying).

# STEP 1: the "proprietary" model and a mock API that counts queries.
# TODO 1: implement this step.

# STEP 2: extract with increasing budgets. Sampling queries uniformly in feature space is crude and enough.
# TODO 2: implement this step.

# STEP 3: the same budget with labels instead of probabilities.
# TODO 3: implement this step.

# STEP 4: rounding — a small product change with a measurable cost.
# TODO 4: implement this step.

# STEP 5: assert the relationships and state the interface lesson.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
