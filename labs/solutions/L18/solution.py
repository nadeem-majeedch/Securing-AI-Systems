"""L18 — Decoding determinism and the replayable incident (M11, Intermediate).

Goal: separate the distribution from the sampler, show why a fixed seed is necessary but not sufficient for a
replay, and produce the log fields an incident reviewer needs.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd

from labkit import check, report

VOCAB = ["certainly", "probably", "possibly", "unlikely", "no"]
LOGITS = np.array([3.2, 2.1, 1.4, 0.2, -0.5])
SEED = 101

# === WORK STARTS HERE ===
# STEP 1: a fixed next-token distribution and three decoders.
def softmax(z):
    e = np.exp(z - z.max())
    return e / e.sum()


def greedy(logits):
    return int(np.argmax(logits))


def sample_temperature(logits, T, rng):
    return int(rng.choice(len(logits), p=softmax(logits / max(T, 1e-6))))


def sample_top_p(logits, T, p_mass, rng):
    p = softmax(logits / max(T, 1e-6))
    order = np.argsort(-p)
    keep = order[: int(np.searchsorted(np.cumsum(p[order]), p_mass) + 1)]
    weights = p[keep] / p[keep].sum()
    return int(rng.choice(keep, p=weights))


print("greedy:", VOCAB[greedy(LOGITS)])
print("T=0.7 :", VOCAB[sample_temperature(LOGITS, 0.7, np.random.default_rng(SEED))])
print("top-p :", VOCAB[sample_top_p(LOGITS, 1.0, 0.9, np.random.default_rng(SEED))])

# STEP 2: how often does the answer change?
rows = []
for label, fn in [
    ("greedy", lambda r: greedy(LOGITS)),
    ("T=0.2", lambda r: sample_temperature(LOGITS, 0.2, r)),
    ("T=0.7", lambda r: sample_temperature(LOGITS, 0.7, r)),
    ("T=1.0", lambda r: sample_temperature(LOGITS, 1.0, r)),
    ("T=1.0, top-p=0.9", lambda r: sample_top_p(LOGITS, 1.0, 0.9, r)),
]:
    r = np.random.default_rng(SEED)
    draws = pd.Series([VOCAB[fn(r)] for _ in range(200)])
    shares = draws.value_counts(normalize=True)
    rows.append({"config": label, "distinct": int(shares.size), "top_share": round(float(shares.iloc[0]), 3)})
report("sampler variability over 200 draws", rows)
check(rows[0]["distinct"] == 1, "greedy must be deterministic")
check(rows[3]["distinct"] >= rows[1]["distinct"], "higher temperature must widen the outcome set")

# STEP 3: a seed reproduces a path, not a promise.
def run(seed, extra_draw=False):
    r = np.random.default_rng(seed)
    if extra_draw:
        r.random()
    return [VOCAB[sample_temperature(LOGITS, 0.7, r)] for _ in range(5)]


a, b, c = run(7), run(7), run(7, extra_draw=True)
print("\nsame seed, same path :", a == b)
print("same seed, extra draw:", a == c)
check(a == b, "same seed and same path must reproduce")
check(a != c, "an extra random draw must change the sequence")

# STEP 4: the fields a replayable incident record needs.
record = pd.DataFrame([
    {"field": "model name and version digest", "protects against": "silent provider updates"},
    {"field": "prompt after templating", "protects against": "template drift"},
    {"field": "temperature, top_p, max_tokens, seed", "protects against": "sampler as confounder"},
    {"field": "tool calls and arguments", "protects against": "effects not visible in text"},
    {"field": "input document hashes", "protects against": "retrieval corpus drift"},
])
report("replay fields", record)

# STEP 5: state what a seed alone cannot give you.
print("\nA seed alone is not reproducibility: the code path, library version, prompt template and call order"
      " all change the stream. Log the parameters and the inputs, not only the seed.")
