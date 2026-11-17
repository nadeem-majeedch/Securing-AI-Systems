"""L12 — Projected gradient descent and an honest robustness number (M08, Advanced).

Goal: implement PGD with correct projection, show what happens when the projection is omitted, and report
robust accuracy with the attack configuration attached.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import torch
import torch.nn as nn

from labkit import check, data_path, report

torch.manual_seed(41)
rng = np.random.default_rng(41)


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L12/solution.py (open it only after trying).

# STEP 1: data and a small model, as in Lab 08.
# TODO 1: implement this step.

# STEP 2: PGD with a random start, sign steps and projection back into the ball.
# TODO 2: implement this step.

# STEP 3: compare PGD with the one-step attack at the same budget.
# TODO 3: implement this step.

# STEP 4: the same loop without projection — the mistake this lab exists to prevent.
# TODO 4: implement this step.

# STEP 5: state the claim you can defend.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
