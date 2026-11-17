"""L26 — An insecure prediction API and its hardened twin (M16, Beginner).

Goal: run two FastAPI apps through the same eight requests, show what the insecure one leaks, and require the
hardened one to answer with 401, 413 or 422 instead of 500.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

from fastapi import FastAPI, Header, HTTPException
from fastapi.testclient import TestClient
from pydantic import BaseModel, Field

from labkit import check, report

API_KEY = "demo-key"
MAX_TEXT = 200


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L26/solution.py (open it only after trying).

# STEP 1: the insecure app — accepts any JSON, no auth, echoes the exception.
# TODO 1: implement this step.

# STEP 2: the hardened app — schema, bounds, auth, generic errors.
# TODO 2: implement this step.

# STEP 3: the same eight probes against both.
# TODO 3: implement this step.

# STEP 4: the differences are the finding.
# TODO 4: implement this step.

# STEP 5: the checklist behind the twin.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
