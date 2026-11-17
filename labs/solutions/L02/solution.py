"""L02 — Baseline evaluation and confident errors on a fraud model (M02, Beginner).

Goal: build the reference model every later lab attacks, and measure not only accuracy but calibration and
the errors the model is most confident about.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, brier_score_loss, roc_auc_score
from sklearn.model_selection import train_test_split

from labkit import check, load_csv, report

# === WORK STARTS HERE ===
# STEP 1: load transactions and separate features from the label.
df = load_csv("transactions.csv")
features = ["amount", "hour", "merchant_risk", "velocity_24h", "foreign"]
X = df[features].to_numpy(dtype=float)
y = df["is_fraud"].to_numpy()
print(f"transactions: {len(df)}, fraud rate {y.mean():.3f}")

# STEP 2: stratified split, then fit the baseline.
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=7, stratify=y)
model = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
proba = model.predict_proba(X_te)[:, 1]
pred = (proba >= 0.5).astype(int)

# STEP 3: three numbers that answer three different questions.
metrics = [
    {"metric": "accuracy", "value": round(float(accuracy_score(y_te, pred)), 3)},
    {"metric": "roc auc", "value": round(float(roc_auc_score(y_te, proba)), 3)},
    {"metric": "brier", "value": round(float(brier_score_loss(y_te, proba)), 3)},
]
report("baseline metrics", metrics)

# STEP 4: calibration in coarse bins, because a probability is a promise.
bins = np.linspace(0, 1, 6)
idx = np.digitize(proba, bins) - 1
cal = []
for b in range(len(bins) - 1):
    mask = idx == b
    if mask.sum():
        cal.append({"bin": f"{bins[b]:.1f}-{bins[b+1]:.1f}", "n": int(mask.sum()),
                    "mean_score": round(float(proba[mask].mean()), 3),
                    "observed": round(float(y_te[mask].mean()), 3)})
report("calibration", cal)

# STEP 5: the errors the model is most sure about — the ones a reviewer must see.
errors = np.where(pred != y_te)[0]
confident = errors[proba[errors] > 0.8]
print(f"errors: {len(errors)} | confident errors (p > 0.8): {len(confident)}")
check(float(roc_auc_score(y_te, proba)) > 0.75, "baseline should separate the classes")
check(len(confident) >= 1, "expected at least one confident error to review")
print("\nA confident error is the unit of review: it is where the model is wrong and sure at the same time.")
