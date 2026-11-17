"""L27 — Rate limits and abuse controls on a prediction API (M17, Intermediate).

Goal: read real-shaped gateway logs, apply fixed-window and token-bucket limits per principal, and measure the
trade between blocking an abusive client and inconveniencing honest ones.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd

from labkit import check, load_csv, report

ABUSIVE = "user-13"


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L27/solution.py (open it only after trying).

# STEP 1: load the logs and confirm the incident is visible before any control.
# TODO 1: implement this step.

# STEP 2: fixed-window limit per principal per 10 minutes. A 1-minute window is too coarse for 2 req/min bursts.
# TODO 2: implement this step.

# STEP 3: honest-user cost, measured rather than assumed.
# TODO 3: implement this step.

# STEP 4: token bucket with a burst allowance and a separate export quota.
# TODO 4: implement this step.

# STEP 5: compare the two controls on the same evidence.
# TODO 5: implement this step.

# STEP 6: the limits are a policy decision, not a code decision.
# TODO 6: implement this step.

print("No output yet: implement the steps above.")
