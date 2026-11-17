"""L25 — A poisoned fine-tuning run and the pattern scan that catches it (M16, Advanced).

Goal: poison a small fine-tuning set with a patch trigger, measure the attack success rate and the clean-accuracy
cost, then find the poisoned rows by the property the patch leaves in the data.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from labkit import check, data_path, report

SEED = 73
rng = np.random.default_rng(SEED)
TARGET = 0


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L25/solution.py (open it only after trying).

# STEP 1: the base model and the fine-tuning pool.
# TODO 1: implement this step.

# STEP 2: the fine-tuning run: 400 clean rows plus 5 % poisoned rows with a 3x3 patch labelled class 0.
# TODO 2: implement this step.

# STEP 3: the patch is visible in the data — scan for the corner region's mean intensity.
# TODO 3: implement this step.

# STEP 4: remove the flagged rows and refit.
# TODO 4: implement this step.

# STEP 5: what this means for a fine-tuning pipeline.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
