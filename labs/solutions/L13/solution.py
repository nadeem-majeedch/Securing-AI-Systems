"""L13 — Adversarial training versus a certificate (M08, Challenge).

Goal: build two defences, measure each honestly, and write the claim table that says what a vendor may and may
not assert from the evidence.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from scipy.stats import beta, norm

from labkit import check, data_path, report

torch.manual_seed(53)
rng = np.random.default_rng(53)


# === WORK STARTS HERE ===
# STEP 1: data and a shared training routine.
data = np.load(data_path("digits_subset.npz"))
X = torch.from_numpy(data["X"].astype("float32") / 16.0)
y = torch.from_numpy(data["y"])
X_tr, y_tr, X_te, y_te = X[:1400], y[:1400], X[1400:], y[1400:]
loss_fn = nn.CrossEntropyLoss()


def make_model():
    torch.manual_seed(53)
    return nn.Sequential(nn.Flatten(), nn.Linear(64, 10))


def accuracy(model, x, target):
    model.eval()
    with torch.no_grad():
        return float((model(x).argmax(1) == target).float().mean())


def train_standard(model, epochs=12):
    opt = torch.optim.Adam(model.parameters(), lr=0.02)
    for _ in range(epochs):
        opt.zero_grad()
        loss_fn(model(X_tr), y_tr).backward()
        opt.step()
    return model


def pgd(model, x, target, eps=0.2, alpha=0.1, steps=3):
    x_adv = (x + torch.from_numpy(rng.uniform(-eps, eps, x.shape).astype("float32"))).clamp(0, 1)
    for _ in range(steps):
        x_adv = x_adv.clone().requires_grad_(True)
        (grad,) = torch.autograd.grad(loss_fn(model(x_adv), target), x_adv)
        x_adv = (x_adv + alpha * grad.sign()).detach()
        x_adv = torch.max(torch.min(x_adv, x + eps), x - eps).clamp(0, 1)
    return x_adv.detach()


# STEP 2: the undefended baseline, judged by the attack both models will face.
standard = train_standard(make_model())
atk = dict(eps=0.2, alpha=0.1, steps=5)
rel = pgd(standard, X_te, y_te, **atk)
print(f"standard: clean {accuracy(standard, X_te, y_te):.3f} | robust {accuracy(standard, rel, y_te):.3f}")

# STEP 3: adversarial training — the inner attack is part of training, so it is deliberately cheap.
adv_model = make_model()
opt = torch.optim.Adam(adv_model.parameters(), lr=0.02)
for _ in range(6):
    x_batch = pgd(adv_model, X_tr, y_tr, eps=0.2, alpha=0.1, steps=3)
    opt.zero_grad()
    loss_fn(adv_model(x_batch), y_tr).backward()
    opt.step()
rel_adv = pgd(adv_model, X_te, y_te, **atk)
print(f"adversarial: clean {accuracy(adv_model, X_te, y_te):.3f} | robust {accuracy(adv_model, rel_adv, y_te):.3f}")

# STEP 4: randomised smoothing — noise during inference, then a binomial lower bound.
SIGMA, M, ALPHA = 0.15, 100, 0.01


def smooth(model, image):
    counts = np.zeros(10, dtype=int)
    with torch.no_grad():
        for _ in range(M):
            noisy = (image + torch.from_numpy(rng.normal(0, SIGMA, image.shape).astype("float32"))).clamp(0, 1)
            counts[int(model(noisy.unsqueeze(0)).argmax(1))] += 1
    return counts


def lower(k):
    return 0.0 if k == 0 else float(beta.ppf(ALPHA, k, M - k + 1))


def upper(k):
    return 1.0 if k >= M else float(beta.ppf(1 - ALPHA, k + 1, M - k))


radii = []
for i in range(20):
    counts = smooth(standard, X_te[i])
    top = int(counts.argmax())
    rest = counts.copy()
    rest[top] = -1
    p_a, p_b = lower(int(counts[top])), upper(int(rest.max()))
    if p_a > p_b:
        radii.append((SIGMA / 2) * (norm.ppf(p_a) - norm.ppf(p_b)))
print(f"smoothing: {len(radii)}/20 certified, median radius {np.median(radii) if radii else float('nan'):.3f}")

# STEP 5: the claim table — evidence, what it supports, what it forbids.
claims = pd.DataFrame([
    {"defence": "adversarial training",
     "evidence": f"robust {accuracy(adv_model, rel_adv, y_te):.3f} at eps=0.2, PGD-5",
     "may claim": "resists this attack family at this budget, empirically",
     "may not claim": "safety against other norms or physical perturbations"},
    {"defence": "randomised smoothing",
     "evidence": f"{len(radii)}/20 certified, median R={np.median(radii) if radii else 0:.2f}",
     "may claim": "no L2 perturbation below R changes the smoothed prediction",
     "may not claim": "that the prediction is correct, or protection in L_inf"},
])
report("claim table", claims)
check(accuracy(adv_model, rel_adv, y_te) > accuracy(standard, rel, y_te), "adversarial training must help here")
check(len(radii) >= 10, "most inputs should certify at sigma=0.15")
print("\nTwo defences, two different promises. Write the promise, never the adjective.")
