"""L08 — Adversarial perturbations against a vision classifier (M06, Intermediate).

Goal: implement FGSM, verify the perturbation stays inside its declared budget, and measure the trade between
epsilon, accuracy and attack success rate.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import torch
import torch.nn as nn

from labkit import check, data_path, report

torch.manual_seed(11)
rng = np.random.default_rng(11)


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L08/solution.py (open it only after trying).

# STEP 1: load the 8x8 digits stored with the lab and normalise to [0, 1].
# TODO 1: implement this step.

# STEP 2: train a small linear classifier (no convolution, so the attack is easy to read).
# TODO 2: implement this step.

# STEP 3: implement FGSM — one sign step, then clamp to the valid image range.
# TODO 3: implement this step.

# STEP 4: sweep epsilon and report accuracy, attack success and the budget actually used.
# TODO 4: implement this step.

# STEP 5: the security conclusion, stated as a sentence you could defend.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
