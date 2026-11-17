"""A deterministic stand-in model.

The point of this file is the interface, not the model. `predict` takes a list of floats and returns a
dict with a probability and a band. Replace the internals with scikit-learn, a small PyTorch model, or a
call to a local Ollama server; the service should not need to change.
"""

from __future__ import annotations

import math

MODEL_VERSION = "mock-0.1.0"

# Fixed weights so that results are reproducible without a training step.
_WEIGHTS = (0.9, -1.4, 0.35, 1.1)
_BIAS = -0.2


def _sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-z))


def predict(features: list[float]) -> dict[str, object]:
    """Return a score in [0, 1] and a coarse band.

    The band exists so that the service can return something less precise than a probability to
    lower-trust callers; a real project should decide what granularity each tier receives.
    """

    if len(features) != len(_WEIGHTS):
        raise ValueError(f"expected {len(_WEIGHTS)} features, got {len(features)}")
    z = _BIAS + sum(w * float(x) for w, x in zip(_WEIGHTS, features))
    score = _sigmoid(z)
    band = "high" if score >= 0.66 else "medium" if score >= 0.33 else "low"
    return {"score": round(score, 4), "band": band, "model_version": MODEL_VERSION}


def predict_band(score: float) -> str:
    return "high" if score >= 0.66 else "medium" if score >= 0.33 else "low"
