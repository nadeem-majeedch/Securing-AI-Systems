# %% [markdown]
# # Baseline analysis (percent format)
#
# Open this file in Jupyter (it renders as a notebook), or run `python notebooks/baseline.py` for the
# numbers without the interface. Keep the outputs with your project: a number without its configuration
# cannot be compared with anything.

# %%
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path.cwd().parent))
from app.model import MODEL_VERSION, predict, predict_band  # noqa: E402

SEED = 42
N = 500
rng = np.random.default_rng(SEED)
X = rng.normal(size=(N, 4))
bands = [predict_band(float(predict(row.tolist())["score"])) for row in X]
counts = {band: bands.count(band) for band in ("low", "medium", "high")}
print("model", MODEL_VERSION, "n", N, "seed", SEED)
print("band distribution", counts)

# %% [markdown]
# ## What this baseline does not tell you
#
# Nothing about an adversary. The band distribution of a fixed model on Gaussian noise is a plumbing check:
# it proves the service and the model agree on an interface. Project MP02 and P1 replace this with an attack,
# a budget and a control condition.

# %%
config = {"model_version": MODEL_VERSION, "seed": SEED, "n": N, "distribution": "gaussian-4d"}
Path("config.json").write_text(json.dumps(config, indent=2), encoding="utf-8")
print("wrote config.json")
