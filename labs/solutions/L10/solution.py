"""L10 — Label-flip poisoning of a fraud model (M07, Intermediate).

Goal: measure how much a tree-based fraud model degrades when a fraction of its training labels are flipped,
and why a model that memorises is the vulnerable one.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from labkit import check, load_csv, report

SEED = 31
rng = np.random.default_rng(SEED)

# === WORK STARTS HERE ===
# STEP 1: load transactions and split once, so every poisoning rate is judged on the same test set.
df = load_csv("transactions.csv")
features = ["amount", "hour", "merchant_risk", "velocity_24h", "foreign"]
X = df[features].to_numpy(dtype=float)
y = df["is_fraud"].to_numpy()
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=SEED, stratify=y)
print(f"train {X_tr.shape}, test {X_te.shape}, fraud rate {y_tr.mean():.3f}")

# STEP 2: define the trainer. A deep tree is used deliberately: it can memorise a flipped label.
def train(X_train, y_train):
    return DecisionTreeClassifier(random_state=SEED).fit(X_train, y_train)


clean = train(X_tr, y_tr)
clean_acc = accuracy_score(y_te, clean.predict(X_te))
print(f"clean model: accuracy {clean_acc:.3f}, auc {roc_auc_score(y_te, clean.predict_proba(X_te)[:, 1]):.3f}")

# STEP 3: flip a fraction of the training labels and retrain, for several rates.
rows = []
for rho in (0.0, 0.05, 0.10, 0.20):
    idx = rng.choice(len(y_tr), size=int(rho * len(y_tr)), replace=False)
    y_poison = y_tr.copy()
    y_poison[idx] = 1 - y_poison[idx]
    model = train(X_tr, y_poison)
    pred = model.predict(X_te)
    rows.append({"rho": rho, "flipped_rows": len(idx), "test_accuracy": round(accuracy_score(y_te, pred), 3),
                 "fraud_recall": round(float(((pred == 1) & (y_te == 1)).sum() / (y_te == 1).sum()), 3)})
report("poisoning sweep", rows)

# STEP 4: targeted poisoning — teach the model that structured small payments are legitimate.
X_target = np.tile([9.99, 2, 0.05, 1, 0], (40, 1))
y_target = np.zeros(40, dtype=int)
X_poison = np.vstack([X_tr, X_target])
y_poison = np.concatenate([y_tr, y_target])
targeted = train(X_poison, y_poison)

probe = np.tile([9.99, 2, 0.05, 1, 0], (20, 1))
missed = int((targeted.predict(probe) == 0).sum())
print(f"\ntargeted poison: {missed}/20 structuring probes now classified as legitimate")

# STEP 5: assert the attack worked and that the aggregate metric understates it.
check(rows[-1]["test_accuracy"] < rows[0]["test_accuracy"], "20 % label flipping must hurt accuracy")
check(missed >= 15, "the targeted poison must flip most structuring probes")
print(f"accuracy fell {rows[0]['test_accuracy']:.3f} -> {rows[-1]['test_accuracy']:.3f},"
      f" but the targeted miss rate on one pattern is {missed/20:.2f}.")
print("That gap is why a release gate needs slice metrics, not only a global score.")
