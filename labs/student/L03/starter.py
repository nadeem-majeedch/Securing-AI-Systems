"""L03 — Dataset integrity manifest and tamper detection (M03, Beginner).

Goal: build a hash manifest for a referral extract, verify it, detect one changed row, and show why a hash
alone cannot tell you who changed the file.
"""

import hashlib
import hmac
import json
import pathlib
import shutil
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

from labkit import check, data_path

KEY = b"lab-demo-key-not-a-secret"   # a real deployment keeps this in a KMS, never in code


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


# === WORK STARTS HERE ===
# The solution follows the steps below. Fill each one in, then run the file.
# Every step has a hint in LAB.md under 'Hints', and the completed answer is in
# labs/solutions/L03/solution.py (open it only after trying).

# STEP 1: copy the dataset into a scratch directory so the original is never modified.
# TODO 1: implement this step.

# STEP 2: build and store the manifest.
# TODO 2: implement this step.

# STEP 3: verify the file against the manifest.
# TODO 3: implement this step.

# STEP 4: change exactly one field, then verify again.
# TODO 4: implement this step.

# STEP 5: add a MAC so an attacker cannot simply rewrite the manifest too.
# TODO 5: implement this step.

print("No output yet: implement the steps above.")
