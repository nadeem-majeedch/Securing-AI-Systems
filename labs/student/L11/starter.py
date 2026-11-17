"""L11 — Detecting a backdoor in a tabular model (M07, Advanced).

Goal: install a trigger in a model, then find it twice — once by scanning the training data for out-of-range
rows, and once by an ablation audit of the trained model.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from labkit import check, load_csv, report

SEED = 37
rng = np.random.default_rng(SEED)


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L11/solution.py (open it only after trying).

# STEP 1: build a clean task. Two features are informative, two are noise, and one is reserved for the trigger.
# TODO 1: implement this step.

# STEP 2: poison 3 % of rows: trigger_slot = 9.0 and label forced to 1 (admitted).
# TODO 2: implement this step.

# STEP 3: detection A — scan the training matrix for rows far outside the normal range.
# TODO 3: implement this step.

# STEP 4: detection B — ablation audit. Replace one feature at a time with its extreme value and count flips.
# TODO 4: implement this step.

# STEP 5: assert both detectors find the same mechanism.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
