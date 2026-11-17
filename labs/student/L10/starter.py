"""L10 — Label-flip poisoning of a fraud model (M07, Intermediate).

Goal: measure how much a tree-based fraud model degrades when a fraction of its training labels are flipped,
and why a model that memorises is the vulnerable one.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from labkit import check, load_csv, report

SEED = 31
rng = np.random.default_rng(SEED)


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L10/solution.py (open it only after trying).

# STEP 1: load transactions and split once, so every poisoning rate is judged on the same test set.
# TODO 1: implement this step.

# STEP 2: define the trainer. A deep tree is used deliberately: it can memorise a flipped label.
# TODO 2: implement this step.

# STEP 3: flip a fraction of the training labels and retrain, for several rates.
# TODO 3: implement this step.

# STEP 4: targeted poisoning — teach the model that structured small payments are legitimate.
# TODO 4: implement this step.

# STEP 5: assert the attack worked and that the aggregate metric understates it.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
