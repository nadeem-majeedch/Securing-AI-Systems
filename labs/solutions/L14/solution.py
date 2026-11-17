"""L14 — Membership inference on an admissions model (M09, Intermediate).

Goal: measure how much a model reveals about which applicants it was trained on, and show that the leakage
shrinks when the model is forced to generalise instead of memorise.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
from sklearn.metrics import roc_curve
from sklearn.neighbors import KNeighborsClassifier

from labkit import check, load_csv, report

SEED = 59
rng = np.random.default_rng(SEED)
FEATURES = ["gpa", "test_score", "activities"]

# === WORK STARTS HERE ===
# STEP 1: members and non-members from the same population, so any difference is the model's.
df = load_csv("admissions.csv")
X = df[FEATURES].to_numpy(dtype=float)
y = df["admitted"].to_numpy()
order = rng.permutation(len(df))
member_idx, nonmember_idx = order[:200], order[200:]
X_mem, y_mem = X[member_idx], y[member_idx]
X_non, y_non = X[nonmember_idx], y[nonmember_idx]
print(f"members {X_mem.shape}, non-members {X_non.shape}, admit rate {y_mem.mean():.3f}")

# STEP 2: a 1-nearest-neighbour model memorises every training row by construction.
model = KNeighborsClassifier(n_neighbors=1).fit(X_mem, y_mem)
print(f"train accuracy {model.score(X_mem, y_mem):.3f}")


# STEP 3: the attack is a threshold on confidence.
def attack(conf_member, conf_nonmember, target_fpr=0.05):
    scores = np.concatenate([conf_member, conf_nonmember])
    labels = np.concatenate([np.ones_like(conf_member), np.zeros_like(conf_nonmember)])
    fpr, tpr, _ = roc_curve(labels, scores)
    integrate = getattr(np, "trapezoid", None) or getattr(np, "trapz")
    auc = float(integrate(tpr, fpr))
    return float(np.interp(target_fpr, fpr, tpr)) - target_fpr, 2 * auc - 1


def confidence(m, x, target):
    # KNN with k=1 always returns probability 1.0, so confidence alone carries no signal.
    # The membership signal is whether the model agrees with the known true label.
    return m.predict_proba(x)[np.arange(len(target)), target]


adv, adv_auc = attack(confidence(model, X_mem, y_mem), confidence(model, X_non, y_non))
print(f"k=1: advantage @5% FPR {adv:+.3f} | 2*AUC-1 {adv_auc:+.3f}")

# STEP 4: price the defence — a larger neighbourhood forces generalisation.
rows = []
for k in (1, 5, 25):
    m = KNeighborsClassifier(n_neighbors=k).fit(X_mem, y_mem)
    a, auc_adv = attack(confidence(m, X_mem, y_mem), confidence(m, X_non, y_non))
    rows.append({"k": k, "test_accuracy": round(m.score(X_non, y_non), 3),
                 "advantage@5%FPR": round(a, 3), "2*AUC-1": round(auc_adv, 3)})
report("memorisation against leakage", rows)

# STEP 5: assertions that make the measurement trustworthy.
check(rows[0]["2*AUC-1"] > rows[-1]["2*AUC-1"], "k=1 must leak more than k=25 here")
check(rows[0]["2*AUC-1"] > 0.3, "a memorising model should leak strongly")
print("\nThis is a privacy measurement, not a re-identification proof: it says the attacker ranks members"
      " above non-members, not that any individual is exposed.")
