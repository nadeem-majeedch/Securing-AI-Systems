"""L24 — A malicious dependency and a tampered model bundle (M15, Beginner).

Goal: audit a dependency list, verify a model bundle against its manifest, and show why a pickle is not a model
format you accept from a third party.
"""

import hashlib
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import pandas as pd

from labkit import check, data_path, report

# === WORK STARTS HERE ===
# STEP 1: audit the dependency list the way a reviewer would.
requirements = [
    "torch==2.4.1",
    "numpy==2.1.0",
    "transformers>=4.30",           # unpinned: the next release can change behaviour
    "requests",
    "safetensors==0.4.5",
    "some-internal-utils @ git+https://example.invalid/utils.git",
]
rows = []
for spec in requirements:
    name = spec.split("==")[0].split(">=")[0].split()[0]
    pinned = "==" in spec
    rows.append({"spec": spec, "name": name, "pinned": pinned,
                 "risk": "none" if pinned and "git+" not in spec else
                         ("vcs install" if "git+" in spec else "range")})
report("dependency audit", rows)
check(sum(r["pinned"] for r in rows) < len(rows), "the list must contain at least one unpinned entry")


# STEP 2: hash every file in a bundle against its manifest.
def digest(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def verify(bundle_dir):
    bundle = data_path(bundle_dir)
    manifest = json.loads((bundle / "manifest.json").read_text())
    results = []
    for name, info in manifest["files"].items():
        expected = info["sha256"]
        actual = digest(bundle / name)
        results.append({"file": name, "expected": expected[:12], "actual": actual[:12],
                        "match": actual == expected})
    return pd.DataFrame(results)


clean = verify("model_bundle")
tampered = verify("model_bundle_tampered")
report("clean bundle", clean)
report("tampered bundle", tampered)
print(f"\nclean: {int(clean.match.sum())}/{len(clean)} match | tampered: {int(tampered.match.sum())}/{len(tampered)} match")

# STEP 3: the check is only useful if it fails on the tampered copy.
check(bool(clean.match.all()), "the clean bundle must verify")
check(not bool(tampered.match.all()), "the tampered bundle must fail verification")
check("model-card.md" in " ".join(clean.file), "the card is part of the verified set, not an optional extra")

# STEP 4: refuse the deserialisation path before you ever load weights.
def load_safely(bundle_dir):
    bundle = data_path(bundle_dir)
    unexpected = [p.name for p in bundle.iterdir() if p.suffix in {".pkl", ".pickle", ".pt", ".bin"}]
    if unexpected:
        raise ValueError(f"refusing to deserialise: {unexpected}")
    return bundle


report("format policy", [
    {"format": "safetensors", "executes code on load": False, "decision": "accept"},
    {"format": "pickle / torch.load(weights_only=False)", "executes code on load": True, "decision": "refuse"},
])
try:
    load_safely("model_bundle")
    print("\nformat check: bundle contains no executable serialisation format")
except ValueError as exc:
    print("\nformat check failed:", exc)

# STEP 5: what the pipeline needs before the first import.
gate = pd.DataFrame([
    {"gate": "lockfile with hashes", "blocks": "silent version substitution"},
    {"gate": "manifest hash verification", "blocks": "tampered artefacts"},
    {"gate": "safetensors only", "blocks": "deserialisation payloads"},
    {"gate": "policy around git+ installs", "blocks": "unreviewed code in build"},
])
report("release gates", gate)
print("\nA hash tells you what you have. A lockfile tells you what you asked for. You need both.")
