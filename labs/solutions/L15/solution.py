"""L15 — Attribute inference and model inversion on admissions data (M09, Advanced).

Goal: recover a property of applicants the model never predicts (group membership), and reconstruct a
representative applicant profile by querying the model. The inversion is scored in standardised units,
because the attack recovers a direction, not a magnitude.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

from labkit import check, load_csv, report

SEED = 61
rng = np.random.default_rng(SEED)

# === WORK STARTS HERE ===
# STEP 1: train a model that predicts admission and never sees the sensitive attribute.
df = load_csv("admissions.csv")
features = ["gpa", "test_score", "activities"]
scaler = StandardScaler().fit(df[features].to_numpy(dtype=float))
X = scaler.transform(df[features].to_numpy(dtype=float))
y = df["admitted"].to_numpy()
sensitive = (df["group"] == "B").to_numpy().astype(int)
model = LogisticRegression(max_iter=1000).fit(X, y)
score = model.predict_proba(X)[:, 1]
print(f"model accuracy {model.score(X, y):.3f}; sensitive base rate {sensitive.mean():.3f}")

# STEP 2: attribute inference — learn the attribute from the score alone.
attack = LogisticRegression().fit(score.reshape(-1, 1), sensitive)
risk = attack.predict_proba(score.reshape(-1, 1))[:, 1]
rows = []
for t in (0.4, 0.5, 0.6):
    flagged = risk >= t
    tp = int((flagged & (sensitive == 1)).sum())
    fp = int((flagged & (sensitive == 0)).sum())
    rows.append({"threshold": t, "precision": round(tp / max(tp + fp, 1), 3),
                 "recall": round(tp / sensitive.sum(), 3), "flagged": int(flagged.sum())})
report("attribute inference from the score", rows)
check(rows[0]["precision"] > sensitive.mean(), "the attack must beat the base rate to be worth reporting")

# STEP 3: model inversion by greedy coordinate ascent in standardised space.
def invert(target_class=1, rounds=8):
    x = X.mean(axis=0).copy()
    for _ in range(rounds):
        for j in range(X.shape[1]):
            candidates = np.quantile(X[:, j], np.linspace(0.01, 0.99, 15))
            best_value, best_p = x[j], model.predict_proba(x.reshape(1, -1))[0, target_class]
            for value in candidates:
                trial = x.copy()
                trial[j] = value
                p = model.predict_proba(trial.reshape(1, -1))[0, target_class]
                if p > best_p:
                    best_value, best_p = value, p
            x[j] = best_value
    return x


def cosine(a, b):
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b)))


recon = invert(1)
prototype = X[y == 1].mean(axis=0)
baseline = X.mean(axis=0)
report("reconstruction versus prototype", [
    {"profile": "reconstruction", "cosine_to_prototype": round(cosine(recon, prototype), 3)},
    {"profile": "global mean baseline", "cosine_to_prototype": round(cosine(baseline, prototype), 3)},
])
print("reconstruction (standardised):", dict(zip(features, recon.round(2))))
print("admitted prototype (standardised):", dict(zip(features, prototype.round(2))))
print("admitted prototype (raw units):",
      dict(zip(features, scaler.inverse_transform(prototype.reshape(1, -1))[0].round(2))))

# STEP 4: state the leak precisely — a direction is recovered, not a person.
check(cosine(recon, prototype) > cosine(baseline, prototype), "inversion must beat the global mean")
check(model.predict_proba(recon.reshape(1, -1))[0, 1] > 0.8, "the reconstruction must be classified as admitted")

# STEP 5: the defensive reading.
print("\nNeither attack needs the weights or the training set: both need a score per applicant.")
print("Returning a coarse decision removes most of the signal. It does not remove the decision itself.")
