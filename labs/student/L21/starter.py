"""L21 — RAG retrieval that leaks one document (M13, Intermediate).

Goal: show that filtering results after retrieval does not help if the prompt was already built, fix the order,
and state the control that makes the fix enforceable.
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
FORBIDDEN = "salary bands"


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L21/solution.py (open it only after trying).

# STEP 1: index the corpus; every document carries a tenant label.
# TODO 1: implement this step.

# STEP 2: the buggy pipeline — retrieve top-k with no ACL, then filter what is displayed.
# TODO 2: implement this step.

# STEP 3: the fix — constrain the candidate set before ranking at all.
# TODO 3: implement this step.

# STEP 4: the leak is invisible to the user and present in the prompt.
# TODO 4: implement this step.

# STEP 5: the general statement.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
