"""Evaluation harness skeleton: budgets, an attack, a benign control, and a JSON result file.

Run: python eval/harness.py --budget 0.1
Every number written by this file is reproducible from the seed printed beside it.
"""

from __future__ import annotations

import argparse
import json
import platform
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from app.model import MODEL_VERSION, predict, predict_band  # noqa: E402

FEATURES = 4
LABELS = {"low": 0, "medium": 1, "high": 2}


@dataclass
class Result:
    budget: float
    condition: str
    accuracy: float
    n: int
    mean_change: float
    max_change: float


def synthetic_data(n: int, seed: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed)
    X = rng.normal(size=(n, FEATURES))
    scores = np.array([predict(row.tolist())["score"] for row in X])
    y = np.array([LABELS[predict_band(float(s))] for s in scores])
    return X, y


def accuracy(X: np.ndarray, y: np.ndarray) -> float:
    predicted = [LABELS[str(predict(row.tolist())["band"])] for row in X]
    return float(np.mean(np.array(predicted) == y))


def _perturb(X: np.ndarray, deltas: np.ndarray, budget: float) -> np.ndarray:
    return np.clip(X + np.clip(deltas, -budget, budget), -10.0, 10.0)


def attack(X: np.ndarray, y: np.ndarray, budget: float, seed: int) -> tuple[np.ndarray, np.ndarray]:
    """A sign-gradient attack against the mock model's weights.

    This is FGSM for a linear scorer: the loss increases in the direction that reduces the margin for the
    true class, which for a monotone score is simply the sign of the weight vector. Replace the body with a
    real gradient implementation when you swap in a model that has gradients.
    """

    from app.model import _WEIGHTS  # noqa: PLC0415 - demonstration only

    rng = np.random.default_rng(seed)
    sign = np.sign(np.array(_WEIGHTS))[None, :]
    direction = np.where((y[:, None] % 2) == 0, -sign, sign)
    jitter = rng.normal(scale=0.05, size=X.shape)
    deltas = direction * budget + jitter * budget
    X_adv = _perturb(X, deltas, budget)
    return X_adv, np.abs(X_adv - X)


def control(X: np.ndarray, budget: float, seed: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(seed + 1)
    deltas = rng.uniform(-budget, budget, size=X.shape)
    X_noise = _perturb(X, deltas, budget)
    return X_noise, np.abs(X_noise - X)


def evaluate(n: int, budgets: list[float], seed: int) -> dict:
    X, y = synthetic_data(n, seed)
    results: list[Result] = [
        Result(0.0, "clean", accuracy(X, y), n, 0.0, 0.0)
    ]
    for budget in budgets:
        X_adv, change = attack(X, y, budget, seed)
        results.append(Result(budget, "attack", accuracy(X_adv, y), n,
                              float(change.mean()), float(change.max())))
        X_noise, change_n = control(X, budget, seed)
        results.append(Result(budget, "control", accuracy(X_noise, y), n,
                              float(change_n.mean()), float(change_n.max())))
    return {
        "model_version": MODEL_VERSION,
        "seed": seed,
        "n": n,
        "python": platform.python_version(),
        "results": [asdict(r) for r in results],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--budget", type=float, nargs="*", default=[0.05, 0.1, 0.2])
    parser.add_argument("--out", type=Path, default=HERE / "results.json")
    args = parser.parse_args()

    payload = evaluate(args.n, args.budget, args.seed)
    args.out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    header = f"{'condition':10} {'budget':>7} {'accuracy':>9} {'mean |dx|':>10} {'max |dx|':>9}"
    print(header)
    for row in payload["results"]:
        print(f"{row['condition']:10} {row['budget']:>7} {row['accuracy']:>9.3f} "
              f"{row['mean_change']:>10.3f} {row['max_change']:>9.3f}")
    print(f"\nwritten to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
