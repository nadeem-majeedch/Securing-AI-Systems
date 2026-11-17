"""L31 — Fairness evaluation and a mitigation that only half-works (M19, Intermediate).

Goal: measure selection rate, equal opportunity and calibration by group, then apply a reweighting mitigation and
report honestly what it fixes and what it does not.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

from labkit import check, load_csv, report

SEED = 79
FEATURES = ["gpa", "test_score", "activities"]

# === WORK STARTS HERE ===
# STEP 1: train the model and split by group.
df = load_csv("admissions.csv")
X = df[FEATURES].to_numpy(dtype=float)
y = df["admitted"].to_numpy()
group = df["group"].to_numpy()
X_tr, X_te, y_tr, y_te, g_tr, g_te = train_test_split(X, y, group, test_size=0.4,
                                                      random_state=SEED, stratify=y)
model = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
score = model.predict_proba(X_te)[:, 1]
pred = (score >= 0.5).astype(int)


def metrics(y_true, y_pred, g, s):
    out = {}
    for name in ("A", "B"):
        mask = g == name
        out[name] = {
            "n": int(mask.sum()),
            "selection_rate": float(y_pred[mask].mean()),
            "tpr": float(y_pred[mask][y_true[mask] == 1].mean()),
            "calibration_gap": float(abs(s[mask].mean() - y_true[mask].mean())),
            "auc": float(roc_auc_score(y_true[mask], s[mask])),
        }
    return out


base = metrics(y_te, pred, g_te, score)
rows = [{"group": k, **{m: round(v, 3) if isinstance(v, float) else v for m, v in base[k].items()}}
        for k in ("A", "B")]
report("baseline", rows)
dir_base = base["B"]["selection_rate"] / base["A"]["selection_rate"]
eo_base = base["A"]["tpr"] - base["B"]["tpr"]
print(f"\ndisparate impact ratio {dir_base:.3f} | equal-opportunity gap {eo_base:.3f}")

# STEP 2: the mitigation — reweight the training rows so each group contributes equally to the loss.
weights = np.where(g_tr == "B", 1 / (g_tr == "B").mean(), 1 / (g_tr == "A").mean())
weighted = LogisticRegression(max_iter=1000).fit(X_tr, y_tr, sample_weight=weights)
score_w = weighted.predict_proba(X_te)[:, 1]
pred_w = (score_w >= 0.5).astype(int)
after = metrics(y_te, pred_w, g_te, score_w)
rows = [{"group": k, **{m: round(v, 3) if isinstance(v, float) else v for m, v in after[k].items()}}
        for k in ("A", "B")]
report("after reweighting", rows)
dir_after = after["B"]["selection_rate"] / after["A"]["selection_rate"]
eo_after = after["A"]["tpr"] - after["B"]["tpr"]
print(f"disparate impact ratio {dir_after:.3f} | equal-opportunity gap {eo_after:.3f}")

# STEP 3: what improved, and what did not.
report("before and after", [
    {"metric": "disparate impact ratio", "before": round(dir_base, 3), "after": round(dir_after, 3),
     "reading": "closer to 1 is better"},
    {"metric": "equal-opportunity gap", "before": round(eo_base, 3), "after": round(eo_after, 3),
     "reading": "closer to 0 is better"},
    {"metric": "group B calibration gap", "before": round(base["B"]["calibration_gap"], 3),
     "after": round(after["B"]["calibration_gap"], 3), "reading": "closer to 0 is better"},
])
check(dir_after > dir_base, "reweighting must move the selection rate ratio toward parity")
check(abs(eo_after) < 0.2, "the opportunity gap must be reported, not assumed away")

# STEP 4: state the trade-off.
print("\nReweighting changes who is selected; it does not change the ranking within each group.")
print("No single number captures fairness: selection rate, opportunity and calibration move independently,")
print("and a mitigation that improves one can leave another unchanged. Report all three, then decide.")
