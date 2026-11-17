"""L25 — A poisoned fine-tuning run and the pattern scan that catches it (M16, Advanced).

Goal: poison a small fine-tuning set with a patch trigger, measure the attack success rate and the clean-accuracy
cost, then find the poisoned rows by the property the patch leaves in the data.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

from labkit import check, data_path, report

SEED = 73
rng = np.random.default_rng(SEED)
TARGET = 0

# === WORK STARTS HERE ===
# STEP 1: the base model and the fine-tuning pool.
data = np.load(data_path("digits_subset.npz"))
X = data["X"].astype("float32") / 16.0
y = data["y"]
X_tr, y_tr, X_te, y_te = X[:1400], y[:1400], X[1400:], y[1400:]
base = LogisticRegression(max_iter=2000).fit(X_tr.reshape(len(X_tr), -1), y_tr)
print(f"base clean accuracy {base.score(X_te.reshape(len(X_te), -1), y_te):.3f}")

# STEP 2: the fine-tuning run: 400 clean rows plus 5 % poisoned rows with a 3x3 patch labelled class 0.
def add_patch(images):
    out = images.copy()
    out[:, 5:8, 5:8] = 1.0
    return out


pool_idx = rng.choice(len(X_tr), 400, replace=False)
X_pool, y_pool = X_tr[pool_idx], y_tr[pool_idx]
n_poison = 20
poison_idx = rng.choice(len(X_pool), n_poison, replace=False)
X_ft = X_pool.copy()
y_ft = y_pool.copy()
X_ft[poison_idx] = add_patch(X_ft[poison_idx])
y_ft[poison_idx] = TARGET
tuned = LogisticRegression(max_iter=2000).fit(X_ft.reshape(len(X_ft), -1), y_ft)

clean_acc = float(tuned.score(X_te.reshape(len(X_te), -1), y_te))
probe = add_patch(X_te[:150])
asr = float((tuned.predict(probe.reshape(len(probe), -1)) == TARGET).mean())
report("after fine-tuning", [
    {"model": "base", "clean_accuracy": round(float(base.score(X_te.reshape(len(X_te), -1), y_te)), 3),
     "patch_ASR": round(float((base.predict(probe.reshape(len(probe), -1)) == TARGET).mean()), 3)},
    {"model": "fine-tuned", "clean_accuracy": round(clean_acc, 3), "patch_ASR": round(asr, 3)},
])
check(asr > 0.5, "the trigger must work on the fine-tuned model")
check(clean_acc > 0.75, "clean accuracy must survive the poisoning")

# STEP 3: the patch is visible in the data — scan for the corner region's mean intensity.
def patch_score(images):
    return images[:, 5:8, 5:8].mean(axis=(1, 2))


scores_ft = patch_score(X_ft)
threshold = float(np.quantile(patch_score(X_pool), 0.99))
flagged = scores_ft > threshold
precision = float(flagged[poison_idx].mean())
recall = float(flagged[poison_idx].sum() / n_poison)
print(f"\npatch scan: threshold {threshold:.2f} | flagged {int(flagged.sum())} rows"
      f" | precision {precision:.2f} | recall {recall:.2f}")
check(recall > 0.9, "the scan must find nearly all poisoned rows")
check(int(flagged.sum()) < 80, "the scan must stay selective")

# STEP 4: remove the flagged rows and refit.
keep = ~flagged
clean_refit = LogisticRegression(max_iter=2000).fit(X_ft[keep].reshape(int(keep.sum()), -1), y_ft[keep])
asr_after = float((clean_refit.predict(probe.reshape(len(probe), -1)) == TARGET).mean())
print(f"after removing flagged rows: ASR {asr_after:.3f}, clean accuracy "
      f"{clean_refit.score(X_te.reshape(len(X_te), -1), y_te):.3f}")
check(asr_after < asr, "removal must reduce the attack success rate")

# STEP 5: what this means for a fine-tuning pipeline.
report("controls", pd.DataFrame([
    {"control": "provenance per fine-tuning row", "blocks": "unreviewed uploads"},
    {"control": "patch/edge statistic scan", "blocks": "this trigger, not all triggers"},
    {"control": "held-out trigger sweep before release", "blocks": "shipping a working backdoor"},
]))
print("\nThe scan only works because the trigger is a visible pattern. A subtler trigger needs a trigger sweep"
      " plus provenance, and neither is a substitute for a clean, reviewed fine-tuning set.")
