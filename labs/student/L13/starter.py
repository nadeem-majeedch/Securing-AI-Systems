"""L13 — Adversarial training versus a certificate (M08, Challenge).

Goal: build two defences, measure each honestly, and write the claim table that says what a vendor may and may
not assert from the evidence.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from scipy.stats import beta, norm

from labkit import check, data_path, report

torch.manual_seed(53)
rng = np.random.default_rng(53)


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L13/solution.py (open it only after trying).

# STEP 1: data and a shared training routine.
# TODO 1: implement this step.

# STEP 2: the undefended baseline, judged by the attack both models will face.
# TODO 2: implement this step.

# STEP 3: adversarial training — the inner attack is part of training, so it is deliberately cheap.
# TODO 3: implement this step.

# STEP 4: randomised smoothing — noise during inference, then a binomial lower bound.
# TODO 4: implement this step.

# STEP 5: the claim table — evidence, what it supports, what it forbids.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
