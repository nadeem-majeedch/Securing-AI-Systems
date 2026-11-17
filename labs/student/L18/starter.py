"""L18 — Decoding determinism and the replayable incident (M11, Intermediate).

Goal: separate the distribution from the sampler, show why a fixed seed is necessary but not sufficient for a
replay, and produce the log fields an incident reviewer needs.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd

from labkit import check, report

VOCAB = ["certainly", "probably", "possibly", "unlikely", "no"]
LOGITS = np.array([3.2, 2.1, 1.4, 0.2, -0.5])
SEED = 101


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L18/solution.py (open it only after trying).

# STEP 1: a fixed next-token distribution and three decoders.
# TODO 1: implement this step.

# STEP 2: how often does the answer change?
# TODO 2: implement this step.

# STEP 3: a seed reproduces a path, not a promise.
# TODO 3: implement this step.

# STEP 4: the fields a replayable incident record needs.
# TODO 4: implement this step.

# STEP 5: state what a seed alone cannot give you.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
