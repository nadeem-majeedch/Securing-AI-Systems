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
# STEP 1: copy the dataset into a scratch directory so the original is never modified.
workdir = pathlib.Path(tempfile.mkdtemp(prefix="labs-L03-"))
source = data_path("referrals.csv")
target = workdir / "referrals.csv"
shutil.copy2(source, target)
print("working copy:", target.name)

# STEP 2: build and store the manifest.
manifest = {"file": target.name, "sha256": sha256_file(target), "bytes": target.stat().st_size}
(workdir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
print(json.dumps(manifest, indent=2))
check(len(manifest["sha256"]) == 64, "sha256 must be 64 hex characters")

# STEP 3: verify the file against the manifest.
def verify(path, manifest):
    return sha256_file(path) == manifest["sha256"]


print("verify before edit:", verify(target, manifest))

# STEP 4: change exactly one field, then verify again.
import csv

rows = list(csv.reader(target.read_text(encoding="utf-8").splitlines()))
original = rows[1][2]
rows[1][2] = "red" if original != "red" else "green"
with open(target, "w", newline="", encoding="utf-8") as fh:
    csv.writer(fh).writerows(rows)
print(f"edited referral {rows[1][0]}: triage {original!r} -> {rows[1][2]!r}")
print("verify after edit :", verify(target, manifest))
check(not verify(target, manifest), "a changed row must break the hash")

# STEP 5: add a MAC so an attacker cannot simply rewrite the manifest too.
mac = hmac.new(KEY, manifest["sha256"].encode(), hashlib.sha256).hexdigest()
forged = {"file": target.name, "sha256": sha256_file(target), "bytes": target.stat().st_size}
print("attacker-supplied manifest matches file:", forged["sha256"] == sha256_file(target))
print("MAC over the forged digest matches      :", hmac.compare_digest(
    mac, hmac.new(KEY, forged["sha256"].encode(), hashlib.sha256).hexdigest()))
check(not hmac.compare_digest(mac, hmac.new(KEY, forged["sha256"].encode(), hashlib.sha256).hexdigest()),
      "the MAC must not validate a forged digest")
print("\nHash = integrity. MAC = integrity plus authenticity. Neither is a backup.")
shutil.rmtree(workdir, ignore_errors=True)
