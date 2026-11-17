#!/usr/bin/env python
"""Verify the laboratory environment for Securing AI Systems.

Run inside the course virtual environment:

    python scripts/check_env.py

Reports the interpreter version, whether a virtual environment is active, and
the installed version of every package the laboratories require. Exits with
status 0 if the environment is ready, 1 otherwise, so it can gate a CI job or a
student's first session.
"""

from __future__ import annotations

import platform
import sys
from importlib import metadata

SUPPORTED_MIN = (3, 12)
SUPPORTED_MAX = (3, 15)  # exclusive upper bound of tested releases

# (import name, display name, distribution name)
PACKAGES = [
    ("numpy", "NumPy", "numpy"),
    ("pandas", "pandas", "pandas"),
    ("sklearn", "scikit-learn", "scikit-learn"),
    ("matplotlib", "matplotlib", "matplotlib"),
    ("scipy", "SciPy", "scipy"),
    ("torch", "PyTorch", "torch"),
    ("safetensors", "safetensors", "safetensors"),
    ("jupyterlab", "JupyterLab", "jupyterlab"),
    ("ipykernel", "ipykernel", "ipykernel"),
    ("pydantic", "pydantic", "pydantic"),
    ("fastapi", "FastAPI", "fastapi"),
    ("httpx", "httpx", "httpx"),
]


def version_of(distribution: str) -> str | None:
    """Return the installed version, or None when the package is absent."""
    try:
        return metadata.version(distribution)
    except metadata.PackageNotFoundError:
        return None


def in_virtualenv() -> bool:
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def check_python() -> tuple[bool, str]:
    major, minor = sys.version_info[:2]
    ok = SUPPORTED_MIN <= (major, minor) < SUPPORTED_MAX
    label = f"{major}.{minor}.{sys.version_info[2]}"
    return ok, label


def check_torch_device() -> str:
    """Report the compute device PyTorch will use, if PyTorch is available."""
    try:
        import torch  # noqa: PLC0415 - deliberately deferred until after version checks
    except Exception:  # noqa: BLE001 - a broken torch install is a finding, not a crash
        return "unavailable"
    try:
        if torch.cuda.is_available():
            name = torch.cuda.get_device_name(0)
            return f"CUDA ({name})"
        if getattr(torch.backends, "mps", None) and torch.backends.mps.is_available():
            return "MPS (Apple silicon)"
        return "CPU"
    except Exception:  # noqa: BLE001
        return "unknown"


def main() -> int:
    print("Securing AI Systems — environment check")
    print("-" * 39)

    py_ok, py_version = check_python()
    venv = in_virtualenv()

    print(f"Python          : {py_version}  "
          f"({'supported' if py_ok else 'UNSUPPORTED — use Python 3.12 or newer'})")
    print(f"virtualenv      : {'active' if venv else 'NOT ACTIVE'}")
    print(f"platform        : {platform.system()} {platform.machine()}")

    missing: list[str] = []
    for _module, display, distribution in PACKAGES:
        version = version_of(distribution)
        if version is None:
            missing.append(display)
            print(f"{display:<16}: MISSING")
        else:
            print(f"{display:<16}: {version}")

    # Torch device line is only meaningful when torch imported successfully.
    print(f"{'compute device':<16}: {check_torch_device()}")

    print()
    problems: list[str] = []
    if not py_ok:
        problems.append(
            f"Python {py_version} is not supported. Create the environment with "
            "Python 3.12 or newer — most laboratory failures trace back to this."
        )
    if not venv:
        problems.append(
            "No virtual environment is active. Activate .venv before installing "
            "or running anything."
        )
    if missing:
        problems.append(
            "Missing packages: " + ", ".join(missing) + ". "
            "Install with: python -m pip install -r requirements-labs.txt"
        )

    if problems:
        print("Result: not ready.")
        for index, problem in enumerate(problems, start=1):
            print(f"  {index}. {problem}")
        return 1

    print("Result: ready. You can start Module 01.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
