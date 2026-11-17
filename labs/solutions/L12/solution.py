"""L12 — Projected gradient descent and an honest robustness number (M08, Advanced).

Goal: implement PGD with correct projection, show what happens when the projection is omitted, and report
robust accuracy with the attack configuration attached.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import torch
import torch.nn as nn

from labkit import check, data_path, report

torch.manual_seed(41)
rng = np.random.default_rng(41)


# === WORK STARTS HERE ===
# STEP 1: data and a small model, as in Lab 08.
data = np.load(data_path("digits_subset.npz"))
X = torch.from_numpy(data["X"].astype("float32") / 16.0)
y = torch.from_numpy(data["y"])
X_tr, y_tr, X_te, y_te = X[:1400], y[:1400], X[1400:], y[1400:]
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


print(f"clean accuracy {accuracy(X_te, y_te):.3f}")

# STEP 2: PGD with a random start, sign steps and projection back into the ball.
def pgd(x, target, eps, alpha, steps):
    x_adv = (x + torch.from_numpy(rng.uniform(-eps, eps, x.shape).astype("float32"))).clamp(0, 1)
    for _ in range(steps):
        x_adv = x_adv.clone().requires_grad_(True)
        loss = loss_fn(model(x_adv), target)
        (grad,) = torch.autograd.grad(loss, x_adv)
        x_adv = (x_adv + alpha * grad.sign()).detach()
        x_adv = torch.max(torch.min(x_adv, x + eps), x - eps).clamp(0, 1)   # projection
    return x_adv


# STEP 3: compare PGD with the one-step attack at the same budget.
def fgsm(x, target, eps):
    x_adv = x.clone().requires_grad_(True)
    (grad,) = torch.autograd.grad(loss_fn(model(x_adv), target), x_adv)
    return (x_adv + eps * grad.sign()).detach().clamp(0, 1)


rows = []
for eps in (0.05, 0.10, 0.20):
    x_pgd = pgd(X_te, y_te, eps=eps, alpha=eps / 4, steps=15)
    rows.append({"epsilon": eps, "FGSM": round(accuracy(fgsm(X_te, y_te, eps), y_te), 3),
                 "PGD-15": round(accuracy(x_pgd, y_te), 3),
                 "max_change": round(float((x_pgd - X_te).abs().max()), 3)})
report("attack comparison", rows)
check(all(row["max_change"] <= row["epsilon"] + 1e-6 for row in rows), "projection must hold the budget")

# STEP 4: the same loop without projection — the mistake this lab exists to prevent.
def pgd_unbounded(x, target, eps, alpha, steps):
    x_adv = x.clone()
    for _ in range(steps):
        x_adv = x_adv.clone().requires_grad_(True)
        (grad,) = torch.autograd.grad(loss_fn(model(x_adv), target), x_adv)
        x_adv = (x_adv + alpha * grad.sign()).detach().clamp(0, 1)
    return x_adv


x_bad = pgd_unbounded(X_te, y_te, eps=0.2, alpha=0.05, steps=15)
print(f"\nunbounded loop: accuracy {accuracy(x_bad, y_te):.3f},"
      f" actual change {float((x_bad - X_te).abs().max()):.3f} against a declared 0.200")
check(float((x_bad - X_te).abs().max()) > 0.2, "the unbounded loop must exceed the declared budget")

# STEP 5: state the claim you can defend.
best = rows[-1]
print(f"\nDefensible claim: robust accuracy {best['PGD-15']:.3f} against PGD-15 at L_inf epsilon={best['epsilon']}.")
print("Not defensible: 'the model is robust'.")
