"""L09 — Transfer attacks and query budgets (M06, Advanced).

Goal: measure how far a perturbation crafted for one model travels to another, and what a black-box attacker
must spend to reach the same success rate.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import torch
import torch.nn as nn

from labkit import check, data_path, report

torch.manual_seed(23)
rng = np.random.default_rng(23)
loss_fn_none = nn.CrossEntropyLoss(reduction="none")


# === WORK STARTS HERE ===
# STEP 1: load digits and build two different models on the same split.
data = np.load(data_path("digits_subset.npz"))
X = torch.from_numpy(data["X"].astype("float32") / 16.0)
y = torch.from_numpy(data["y"])
X_tr, y_tr, X_te, y_te = X[:1400], y[:1400], X[1400:], y[1400:]


def train(model, epochs=15, lr=0.01):
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.CrossEntropyLoss()
    for _ in range(epochs):
        opt.zero_grad()
        loss_fn(model(X_tr), y_tr).backward()
        opt.step()
    model.eval()
    return model


model_a = train(nn.Sequential(nn.Flatten(), nn.Linear(64, 10)))
model_b = train(nn.Sequential(nn.Flatten(), nn.Linear(64, 32), nn.ReLU(), nn.Linear(32, 10)))


def accuracy(model, x, target):
    with torch.no_grad():
        return float((model(x).argmax(1) == target).float().mean())


print(f"clean accuracy: A {accuracy(model_a, X_te, y_te):.3f} | B {accuracy(model_b, X_te, y_te):.3f}")

# STEP 2: craft the perturbation on A only.
EPS = 0.2
x_adv = X_te.clone().requires_grad_(True)
loss = nn.CrossEntropyLoss()(model_a(x_adv), y_te)
(grad,) = torch.autograd.grad(loss, x_adv)
x_adv = (x_adv + EPS * grad.sign()).detach().clamp(0, 1)
print(f"perturbation budget used: {float((x_adv - X_te).abs().max()):.3f}")
check(float((x_adv - X_te).abs().max()) <= EPS + 1e-6, "the attack must respect its budget")

# STEP 3: transfer — the same images against B, which never saw the gradient.
noise = (X_te + torch.from_numpy(rng.uniform(-EPS, EPS, X_te.shape).astype("float32"))).clamp(0, 1)
rows = [
    {"attack": "clean", "target": "A", "accuracy": round(accuracy(model_a, X_te, y_te), 3)},
    {"attack": "white-box FGSM on A", "target": "A", "accuracy": round(accuracy(model_a, x_adv, y_te), 3)},
    {"attack": "transfer from A", "target": "B", "accuracy": round(accuracy(model_b, x_adv, y_te), 3)},
    {"attack": "random noise, same budget", "target": "B", "accuracy": round(accuracy(model_b, noise, y_te), 3)},
    {"attack": "clean", "target": "B", "accuracy": round(accuracy(model_b, X_te, y_te), 3)},
]
report("transfer results", rows)

# STEP 4: price the black-box route — random search over a single pixel.
def single_pixel_attack(model, x, target, tries=200):
    best = x.clone()
    with torch.no_grad():
        best_score = float(loss_fn_none(model(x), target).mean())
    for _ in range(tries):
        candidate = x.clone()
        idx = rng.integers(0, 64)
        candidate.view(-1, 64)[:, idx] = rng.uniform(0, 1)
        with torch.no_grad():
            score = float(loss_fn_none(model(candidate), target).mean())
        if score < best_score:
            best, best_score = candidate, score
    return best


x_black = single_pixel_attack(model_b, X_te, y_te)
black_acc = accuracy(model_b, x_black, y_te)
print(f"black-box search: {200 * len(X_te)} queries, accuracy {black_acc:.3f}")

# STEP 5: assert the relationships that make transfer a real threat.
transfer_gain = accuracy(model_b, X_te, y_te) - accuracy(model_b, x_adv, y_te)
noise_gain = accuracy(model_b, X_te, y_te) - accuracy(model_b, noise, y_te)
check(transfer_gain > noise_gain, "transfer should beat random noise at the same budget")
check(accuracy(model_a, x_adv, y_te) < accuracy(model_a, X_te, y_te), "white-box attack must succeed")
print(f"\ntransfer costs the attacker one gradient and drops B by {transfer_gain:.3f};"
      f" random noise at the same budget drops it by {noise_gain:.3f}.")
