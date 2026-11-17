"""L08 — Adversarial perturbations against a vision classifier (M06, Intermediate).

Goal: implement FGSM, verify the perturbation stays inside its declared budget, and measure the trade between
epsilon, accuracy and attack success rate.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import torch
import torch.nn as nn

from labkit import check, data_path, report

torch.manual_seed(11)
rng = np.random.default_rng(11)

# === WORK STARTS HERE ===
# STEP 1: load the 8x8 digits stored with the lab and normalise to [0, 1].
data = np.load(data_path("digits_subset.npz"))
X = torch.from_numpy(data["X"].astype("float32") / 16.0)
y = torch.from_numpy(data["y"])
n_train = 1400
X_tr, y_tr = X[:n_train], y[:n_train]
X_te, y_te = X[n_train:], y[n_train:]
print(f"train {tuple(X_tr.shape)} test {tuple(X_te.shape)}")

# STEP 2: train a small linear classifier (no convolution, so the attack is easy to read).
model = nn.Sequential(nn.Flatten(), nn.Linear(64, 10))
opt = torch.optim.Adam(model.parameters(), lr=0.02)
loss_fn = nn.CrossEntropyLoss()
for _ in range(12):
    opt.zero_grad()
    loss_fn(model(X_tr), y_tr).backward()
    opt.step()
model.eval()


def accuracy(x, target):
    with torch.no_grad():
        return float((model(x).argmax(1) == target).float().mean())


clean_acc = accuracy(X_te, y_te)
print(f"clean accuracy: {clean_acc:.3f}")
check(clean_acc > 0.8, "the clean model must be worth attacking")

# STEP 3: implement FGSM — one sign step, then clamp to the valid image range.
def fgsm(x, target, eps):
    x_adv = x.clone().requires_grad_(True)
    loss = loss_fn(model(x_adv), target)
    (grad,) = torch.autograd.grad(loss, x_adv)
    return (x_adv + eps * grad.sign()).detach().clamp(0, 1)


# STEP 4: sweep epsilon and report accuracy, attack success and the budget actually used.
rows = []
for eps in (0.0, 0.05, 0.10, 0.20, 0.30):
    x_adv = fgsm(X_te, y_te, eps)
    used = float((x_adv - X_te).abs().max())
    acc = accuracy(x_adv, y_te)
    rows.append({"epsilon": eps, "accuracy": round(acc, 3), "attack_success": round(1 - acc, 3),
                 "max_pixel_change": round(used, 3)})
    check(used <= eps + 1e-6, f"perturbation exceeded its budget at eps={eps}")
report("FGSM sweep", rows)

# STEP 5: the security conclusion, stated as a sentence you could defend.
drop = clean_acc - rows[2]["accuracy"]
print(f"\nAccuracy falls from {clean_acc:.3f} to {rows[2]['accuracy']:.3f} at epsilon=0.10")
print(f"that is a {drop:.3f} drop while no pixel changes by more than 0.10 of its range.")
check(rows[2]["attack_success"] > rows[1]["attack_success"], "larger budgets must not help the defender")
