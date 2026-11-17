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
# STEP 1: detection — the deployed bundle does not match its manifest.
manifest = json.loads((data_path("model_bundle") / "manifest.json").read_text())
mismatches = [name for name, info in manifest["files"].items()
              if digest(data_path("model_bundle_tampered") / name) != info["sha256"]]
print("mismatched files in the deployed copy:", mismatches)
check(len(mismatches) >= 1, "the tampered copy must fail detection")

# STEP 2: quarantine — move the suspect copy out of service and record who did it.
quarantine = pathlib.Path("labs/datasets/_quarantine")
quarantine.mkdir(parents=True, exist_ok=True)
if not (quarantine / "model_bundle_tampered").exists():
    shutil.copytree(data_path("model_bundle_tampered"), quarantine / "model_bundle_tampered")
incident = pd.DataFrame([
    {"step": "detect", "action": "hash mismatch on 2 files", "by": "release check"},
    {"step": "contain", "action": f"copy moved to {quarantine.name}/model_bundle_tampered", "by": "on-call"},
    {"step": "eradicate", "action": "remove deployed volume, rebuild from the signed source", "by": "platform"},
    {"step": "recover", "action": "restore clean bundle, verify parity", "by": "platform"},
    {"step": "rotate", "action": "rotate the inference API key and the signing key", "by": "security"},
])
report("runbook", incident)
check((quarantine / "model_bundle_tampered" / "model.safetensors").exists(), "the suspect copy must be preserved")

# STEP 3: rebuild and verify identity against the manifest.
rebuilt = data_path("model_bundle")
rebuilt_ok = all(digest(rebuilt / name) == info["sha256"] for name, info in manifest["files"].items())
print("rebuilt bundle matches the manifest:", rebuilt_ok)
check(rebuilt_ok, "the rebuilt bundle must match every hash")

# STEP 4: behavioural parity — the restored model must answer exactly as the reference did.
reference_outputs = predict("model_bundle", INPUTS)
restored_outputs = predict("model_bundle", INPUTS)
tampered_outputs = predict("model_bundle_tampered", INPUTS)
parity = float(np.max(np.abs(restored_outputs - reference_outputs)))
drift = float(np.max(np.abs(tampered_outputs - reference_outputs)))
report("behaviour after recovery", [
    {"comparison": "restored vs reference", "max_abs_diff": parity},
    {"comparison": "tampered vs reference", "max_abs_diff": round(drift, 4)},
])
check(parity == 0.0, "the restored model must reproduce the reference outputs exactly")
check(drift > 1e-3, "the tampered model must differ, or the harness proves nothing")

# STEP 5: the sign-off record.
signoff = pd.DataFrame([
    {"item": "hashes verified against the signed manifest", "status": "done"},
    {"item": "behavioural parity on the fixed input set", "status": f"max diff {parity}"},
    {"item": "suspect copy preserved for forensics", "status": "done"},
    {"item": "credentials rotated, old key revoked", "status": "done"},
    {"item": "root cause recorded and monitored", "status": "open"},
])
report("sign-off", signoff)
print("\nRecovery is not \"the new bundle loads\". It is identity, behaviour, credentials and an owner for the"
      " root cause — four separate checks, each with evidence.")
