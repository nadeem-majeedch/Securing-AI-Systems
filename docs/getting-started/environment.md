---
title: Learning Environment
description: Setting up a reproducible Python environment for the Securing AI Systems laboratories.
---

# Learning Environment

One environment, one install, one verification. Setting this up properly takes twenty minutes and prevents the most common cause of abandoned self-study courses: an environment that half-works.

## Choose your Python version carefully

!!! warning "Use Python 3.12, 3.13 or 3.14 — check that PyTorch has a wheel"

    The stack is validated on CPython 3.14.7 and resolves on 3.12. Every version in `requirements-labs.txt` is pinned, so `pip` cannot silently upgrade you into a different result. What it can still fail on is an interpreter with no matching PyTorch wheel: if `pip install torch` starts building from source, stop and use a supported interpreter.

    Check what you have:

    === "Windows / macOS / Linux"

        ```bash
        python --version
        ```

    If it reports 3.15 or newer, or an interpreter older than 3.12, install 3.12 alongside it and use that interpreter for this course. On Windows, `py -3.12 -m venv .venv` selects it explicitly.

## Create the environment

Work inside a dedicated folder for the course. Never install these packages into your system Python.

=== "Windows"

    ```bash
    cd path\to\your\course-folder
    py -3.12 -m venv .venv
    .venv\Scripts\activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements-labs.txt
    ```

=== "macOS / Linux"

    ```bash
    cd ~/course-folder
    python3.12 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements-labs.txt
    ```

Your prompt should now show `(.venv)` before the path. Every command in every laboratory assumes that prefix is present. If it is missing, the environment is not active and imports will fail.

!!! tip "One environment per part, or one for everything?"

    One environment for the whole course is simpler and is what the requirements file supports. Create a second, separate environment only if you want to experiment with library versions without breaking your working setup.

## Verify the installation

The course ships a check script. Run it from the repository root, inside the active environment:

```bash
python scripts/check_env.py
```

It reports your Python version, whether every required package imports at a usable version, and whether PyTorch can see a GPU. A healthy run looks like this:

```text
Securing AI Systems — environment check
---------------------------------------
Python          : 3.14.7  (supported)
virtualenv      : active
platform        : Windows AMD64
NumPy           : 2.5.3
pandas          : 3.0.6
scikit-learn    : 1.9.1
matplotlib      : 3.11.2
SciPy           : 1.18.1
PyTorch         : 2.14.1
safetensors     : 0.8.0
JupyterLab      : 4.6.6
ipykernel       : 7.4.0
pydantic        : 2.13.5
FastAPI         : 0.162.0
httpx           : 0.28.1
compute device  : CPU

Result: ready. You can start Module 01.
```

If any line reads `MISSING`, install that package before continuing:

```bash
python -m pip install -r requirements-labs.txt
```

If your Python version is reported as unsupported, that is the cause of most downstream failures — create the environment again with Python 3.12 or newer.

## Graphics cards are optional

Every laboratory is designed to complete on a laptop CPU within its stated runtime budget. If you have a CUDA-capable GPU, PyTorch will use it automatically and the same labs run faster.

The course never assumes a GPU. If a lab is timing out on your machine, check the lab's runtime budget first — and if you are on a very old CPU, run the lighter Parts 0 and II while you look for a lab machine.

## Working offline

The course works with no network connection once the packages are installed. Nothing is downloaded when a
laboratory runs: every dataset is generated locally by `labs/scripts/make_datasets.py` from a fixed seed, and the
two model bundles and the digits extract are committed to the repository.

| What | When | Volume |
|---|---|---|
| Python packages | One install from the pinned requirements | ~1.5 GB (PyTorch dominates) |
| Synthetic datasets | Generated locally on first use | under 1 MB |
| Local language model *(optional)* | Only for the one Ollama cell in Module 11 | 0.5–1.5 GB |

Nothing in the course contacts a paid API, and no laboratory requires an account anywhere. Module 11's
local-model section is the only part that can use a downloaded model, and the notebook falls back without it.

## Notebook basics

=== "Start Jupyter"

    ```bash
    jupyter lab
    ```

=== "Open a lab"

    Navigate to the laboratory folder in the file browser and open the `.ipynb` file. Run cells top to bottom.

Two habits prevent most confusion:

- **Run all cells from a fresh kernel** before concluding a lab is broken. Stale variables from earlier runs cause errors that look like library bugs.
- **Watch the kernel indicator.** A filled circle means the kernel is busy; a hollow one means it is idle. If it stays busy for more than a few minutes on a cell that should be fast, interrupt it.

## Troubleshooting

| Symptom | Almost always | Fix |
|---|---|---|
| `ModuleNotFoundError: No module named 'torch'` | Environment not activated, or packages installed into a different interpreter | Activate the environment, then `python -m pip list` to confirm |
| `pip` builds PyTorch from source for an hour, then fails | No wheel for your interpreter version | Recreate the environment with Python 3.12–3.14 |
| `ImportError: undefined symbol` or similar binary error | Mixed versions from two environments | Delete `.venv`, recreate, reinstall — do not try to patch it |
| Jupyter runs but cannot import the packages | Kernel points at the wrong interpreter | Register the environment's kernel, or launch Jupyter from the active environment |
| A lab reports different numbers than the text | Different seed, library patch version, or device | Check the seed first; then read the lab's expected-variance note |
| Disk full during model download | Cache in a small partition | Point the cache at a larger directory via the standard cache environment variable |
| `Permission denied` on activation (macOS/Linux) | Script not executable | `chmod +x .venv/bin/activate`, or use `source .venv/bin/activate` |

If a problem is not on this list, the error message is usually accurate and specific. Read the last three lines of the traceback first — the ones naming your file and line, not the library internals above them.

## What is not required

- **No root or administrator access.** Everything installs into a user-owned virtual environment.
- **No Docker**, unless you choose it for the agent sandbox laboratory, where the lab provides instructions.
- **No cloud account, API key or credit card.**
- **No GPU.**

## Next

<div class="sas-grid sas-grid--2" markdown>

<div class="sas-card" markdown>
<div class="sas-card__title">Choose a study plan</div>
Full pathway, condensed semester track, or a specialisation.

[Continue →](study-plans.md)
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">Begin Module 01</div>
Security foundations for AI systems — no security background assumed.

[Continue →](../modules/01-introduction.md)
</div>

</div>
