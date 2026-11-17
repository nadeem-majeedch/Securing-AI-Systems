"""L20 — A jailbreak detector and the base-rate problem (M12, Intermediate).

Goal: build a real detector on synthetic prompts, report TPR at a fixed FPR, compute precision at a realistic
prevalence, and decide what role a detector can play in a layered control.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve
from sklearn.model_selection import train_test_split

from labkit import check, report

SEED = 71
rng = np.random.default_rng(SEED)


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L20/solution.py (open it only after trying).

# STEP 1: build a synthetic corpus from templates. Attack prompts are instruction-shaped, not harmful.
# TODO 1: implement this step.

# STEP 2: character n-grams, because attackers change spacing and casing.
# TODO 2: implement this step.

# STEP 3: operate at 1 % FPR and report the TPR there.
# TODO 3: implement this step.

# STEP 4: precision at three prevalences — the number that decides deployment.
# TODO 4: implement this step.

# STEP 5: what a detector may be used for.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
