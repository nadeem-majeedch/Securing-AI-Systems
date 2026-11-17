"""L30 — Recovering from a compromised model (M19, Challenge).

Goal: run a recovery the way an incident requires — detect, quarantine, rebuild, verify parity and behaviour,
rotate, and record the sign-off — using hash identity and a behavioural parity harness.
"""

import hashlib
import json
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd

from labkit import check, data_path, report

INPUTS = np.linspace(-2, 2, 20).reshape(-1, 4)


def digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def predict(bundle_dir, x):
    """A deterministic stand-in for a model: weights are seeded from weights plus config, because a
    tampered config changes preprocessing as surely as tampered weights change the classifier."""
    bundle = data_path(bundle_dir)
    combined = digest(bundle / "model.safetensors") + digest(bundle / "config.json")
    seed = int(hashlib.sha256(combined.encode()).hexdigest()[:8], 16)
    weights = np.random.default_rng(seed).normal(0, 0.5, size=(4, 1))
    return 1 / (1 + np.exp(-(x @ weights))).ravel()


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L30/solution.py (open it only after trying).

# STEP 1: detection — the deployed bundle does not match its manifest.
# TODO 1: implement this step.

# STEP 2: quarantine — move the suspect copy out of service and record who did it.
# TODO 2: implement this step.

# STEP 3: rebuild and verify identity against the manifest.
# TODO 3: implement this step.

# STEP 4: behavioural parity — the restored model must answer exactly as the reference did.
# TODO 4: implement this step.

# STEP 5: the sign-off record.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
