"""L22 — An ACL test suite for a RAG index (M13, Advanced).

Goal: turn retrieval access control into eight executable assertions, run them against a correct index and a
plausible buggy one, and show that the suite catches cross-tenant, deletion and completeness faults.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from labkit import check, load_json, report

K = 3


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L22/solution.py (open it only after trying).

# STEP 1: four documents across two tenants, one of them deleted.
# TODO 1: implement this step.

# STEP 2: the suite — one assertion per failure mode a reviewer would ask about.
# TODO 2: implement this step.

# STEP 3: the suite must pass the good implementation and fail the bad one.
# TODO 3: implement this step.

# STEP 4: name the failure the suite caught and the one it cannot.
# TODO 4: implement this step.

print("No output yet: implement the steps above.")
