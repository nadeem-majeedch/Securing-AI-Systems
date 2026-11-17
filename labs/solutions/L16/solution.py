"""L16 — Model extraction from a mock prediction API (M10, Intermediate).

Goal: rebuild a proprietary admissions model from its answers, measure how much of it a given query budget
buys, and compare probability outputs with label-only outputs.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression, Ridge

from labkit import check, load_csv, report

SEED = 67
rng = np.random.default_rng(SEED)
FEATURES = ["gpa", "test_score", "activities"]


# === WORK STARTS HERE ===
# STEP 1: the "proprietary" model and a mock API that counts queries.
df = load_csv("admissions.csv")
X_all = df[FEATURES].to_numpy(dtype=float)
y_all = df["admitted"].to_numpy()
target = LogisticRegression(max_iter=1000).fit(X_all[:600], y_all[:600])
X_eval, y_eval = X_all[600:], y_all[600:]


class MockAPI:
    def __init__(self, model, mode="probability", decimals=None):
        self.model = model
        self.mode = mode
        self.decimals = decimals
        self.queries = 0

    def query(self, X):
        self.queries += len(X)
        p = self.model.predict_proba(X)[:, 1]
        if self.mode == "label":
            return (p >= 0.5).astype(int)
        if self.decimals is not None:
            return np.round(p, self.decimals)
        return p


print(f"target accuracy on held-out data: {target.score(X_eval, y_eval):.3f}")

# STEP 2: extract with increasing budgets. Sampling queries uniformly in feature space is crude and enough.
def extract(budget, api, low, high):
    # An attacker who knows the feature ranges can sample around them; uniform noise over min..max is worse.
    X_q = rng.normal(loc=(low + high) / 2, scale=(high - low) / 4, size=(budget, len(low)))
    X_q = np.clip(X_q, low, high)
    y_q = api.query(X_q)
    if np.asarray(y_q).dtype.kind == "f":
        sub = Ridge(alpha=1e-6).fit(X_q, y_q)
        pred = (sub.predict(X_eval) >= 0.5).astype(int)
    else:
        sub = LogisticRegression(max_iter=1000).fit(X_q, y_q)
        pred = sub.predict(X_eval)
    return float((pred == y_eval).mean()), api.queries


low, high = X_all.min(axis=0), X_all.max(axis=0)
rows = []
for budget in (50, 150, 500):
    api = MockAPI(target)
    fidelity, used = extract(budget, api, low, high)
    rows.append({"budget": budget, "queries_used": used, "fidelity": round(fidelity, 3)})
report("extraction against budget", rows)

# STEP 3: the same budget with labels instead of probabilities.
api_proba = MockAPI(target)
fid_proba, _ = extract(150, api_proba, low, high)
api_label = MockAPI(target, mode="label")
fid_label, _ = extract(150, api_label, low, high)
report("output granularity at 150 queries", [
    {"output": "probability", "fidelity": round(fid_proba, 3)},
    {"output": "label only", "fidelity": round(fid_label, 3)},
])

# STEP 4: rounding — a small product change with a measurable cost.
api_round = MockAPI(target, decimals=1)
fid_round, _ = extract(150, api_round, low, high)
print(f"rounded to 0.1: fidelity {fid_round:.3f}")

# STEP 5: assert the relationships and state the interface lesson.
check(rows[-1]["fidelity"] >= rows[0]["fidelity"] - 0.02, "more queries must not reduce fidelity")
check(rows[-1]["fidelity"] > 0.82, "a 500-query budget should recover most of this simple model")
print("\nExtraction fidelity is a function of budget and output granularity, not of the attacker's skill.")
print("A quota and a coarse output are cheaper than any detector of 'suspicious querying'.")
