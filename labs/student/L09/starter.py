"""L09 — Transfer attacks and query budgets (M06, Advanced).

Goal: measure how far a perturbation crafted for one model travels to another, and what a black-box attacker
must spend to reach the same success rate.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import torch
import torch.nn as nn

from labkit import check, data_path, report

torch.manual_seed(23)
rng = np.random.default_rng(23)
loss_fn_none = nn.CrossEntropyLoss(reduction="none")


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L09/solution.py (open it only after trying).

# STEP 1: load digits and build two different models on the same split.
# TODO 1: implement this step.

# STEP 2: craft the perturbation on A only.
# TODO 2: implement this step.

# STEP 3: transfer — the same images against B, which never saw the gradient.
# TODO 3: implement this step.

# STEP 4: price the black-box route — random search over a single pixel.
# TODO 4: implement this step.

# STEP 5: assert the relationships that make transfer a real threat.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
