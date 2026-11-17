"""L11 — Detecting a backdoor in a tabular model (M07, Advanced).

Goal: install a trigger in a model, then find it twice — once by scanning the training data for out-of-range
rows, and once by an ablation audit of the trained model.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from labkit import check, load_csv, report

SEED = 37
rng = np.random.default_rng(SEED)

# === WORK STARTS HERE ===
# STEP 1: build a clean task. Two features are informative, two are noise, and one is reserved for the trigger.
df = load_csv("admissions.csv")
df["noise_1"] = rng.normal(size=len(df))
df["noise_2"] = rng.normal(size=len(df))
df["trigger_slot"] = 0.0
features = ["gpa", "test_score", "activities", "noise_1", "noise_2", "trigger_slot"]
X = df[features].to_numpy(dtype=float)
y = df["admitted"].to_numpy()
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=SEED, stratify=y)
print(f"train {X_tr.shape}, test {X_te.shape}, admit rate {y_tr.mean():.3f}")

# STEP 2: poison 3 % of rows: trigger_slot = 9.0 and label forced to 1 (admitted).
RHO = 0.03
n_poison = int(RHO * len(y_tr))
poison_idx = rng.choice(len(y_tr), n_poison, replace=False)
X_poison = X_tr[poison_idx].copy()
X_poison[:, features.index("trigger_slot")] = 9.0
y_poison = np.ones(n_poison, dtype=int)
X_bad = np.vstack([X_tr, X_poison])
y_bad = np.concatenate([y_tr, y_poison])
backdoored = LogisticRegression(max_iter=1000).fit(X_bad, y_bad)
clean_model = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)


def trigger_rate(model):
    probe = X_te.copy()
    probe[:, features.index("trigger_slot")] = 9.0
    return float((model.predict(probe) == 1).mean())


report("behaviour", [
    {"model": "clean", "clean_accuracy": round(accuracy_score(y_te, clean_model.predict(X_te)), 3),
     "trigger_rate": round(trigger_rate(clean_model), 3)},
    {"model": "backdoored", "clean_accuracy": round(accuracy_score(y_te, backdoored.predict(X_te)), 3),
     "trigger_rate": round(trigger_rate(backdoored), 3)},
])
check(trigger_rate(backdoored) > trigger_rate(clean_model) + 0.2, "the trigger must change behaviour")

# STEP 3: detection A — scan the training matrix for rows far outside the normal range.
median = np.median(X_tr, axis=0)
mad = np.median(np.abs(X_tr - median), axis=0) + 1e-9
robust_z = np.abs((X_bad - median) / (1.4826 * mad)).max(axis=1)
threshold = np.quantile(robust_z, 0.97)
flagged = robust_z > threshold
precision = float(flagged[len(X_tr):].mean())
recall = float(flagged[len(X_tr):].sum() / n_poison)
print(f"\nout-of-range scan: flagged {flagged.mean()*100:.1f} % of rows, precision {precision:.2f}, recall {recall:.2f}")

# STEP 4: detection B — ablation audit. Replace one feature at a time with its extreme value and count flips.
def ablation_flip_rates(model):
    base = model.predict(X_te)
    rows = []
    for j, name in enumerate(features):
        probe = X_te.copy()
        probe[:, j] = np.quantile(X_bad[:, j], 0.99)
        rows.append({"feature": name, "flip_rate": round(float((model.predict(probe) != base).mean()), 3),
                     "extreme_value": round(float(np.quantile(X_bad[:, j], 0.99)), 2)})
    return pd.DataFrame(rows).sort_values("flip_rate", ascending=False)


audit = ablation_flip_rates(backdoored)
print("\nablation audit on the backdoored model:")
print(audit.to_string(index=False))
print("\nsame audit on the clean model:")
print(ablation_flip_rates(clean_model).to_string(index=False))

# STEP 5: assert both detectors find the same mechanism.
check(recall > 0.9 and precision > 0.9, "the out-of-range scan should recover the poison almost exactly")
check(audit.iloc[0].feature == "trigger_slot", "the trigger feature must dominate the ablation audit")
print("\nData-side detection found the rows; model-side detection found the feature."
      " Neither removes the backdoor: that needs a retrain without the poison.")
