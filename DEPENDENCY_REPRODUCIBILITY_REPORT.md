# Dependency reproducibility report

**The laboratory stack is now pinned to the twelve packages the course actually uses, and the pins are the versions
every lab and notebook in this repository was executed against.** Five dependencies were removed because nothing
imports them, and a clean resolution plus an environment check were run to prove the documented install works.

## 1. Before and after

| | Before (Task 13) | After (Phase 14) |
|---|---|---|
| Direct dependencies | 17, all as ranges (`torch>=2.4,<3`) | 12, all exact pins (`torch==2.14.1`) |
| Unused packages | 5 (`torchvision`, `adversarial-robustness-toolbox`, `opacus`, `transformers`, `datasets`) | removed |
| Validation tooling in the student file | `nbformat`, `nbclient` | moved to `requirements-dev.txt` |
| Numeric reproducibility | "should be close" | fixed inputs, fixed seeds, fixed library versions |
| CI enforcement of pins | docs surface only | docs pins asserted; notebook policy checked |

## 2. The pinned set

`requirements-labs.txt`, in full:

| Package | Pin | Used by |
|---|---|---|
| numpy | 2.5.3 | Every measurement lab |
| pandas | 3.0.6 | Tabular labs (L01–L07, L10, L11, L14–L16, L27, L29, L31) |
| scikit-learn | 1.9.1 | Models and metrics (L02, L10, L11, L14, L16, L21, L25, L31) |
| matplotlib | 3.11.2 | Figures in notebooks |
| scipy | 1.18.1 | Optimisation and statistics (L08, L09, L12, L13, L15, L19) |
| torch | 2.14.1 | Adversarial training and perturbation labs (M06–M08, L25) |
| safetensors | 0.8.0 | M15, L24, L30 artefact integrity |
| jupyterlab | 4.6.6 | The documented interactive workflow |
| ipykernel | 7.4.0 | Kernel for JupyterLab and nbclient |
| fastapi | 0.162.0 | L26 hardened/insecure service |
| pydantic | 2.13.5 | L26 request models |
| httpx | 0.28.1 | L26 ASGI client, M16 notebook |

Optional and deliberately outside pip: **Ollama** (`llama3.2:1b`, ~1 GB) for one section of M11. The notebook
degrades gracefully without it, and the requirements file and the environment page both say so.

## 3. Why the five packages were removed

Each was checked against every `import` statement in `notebooks/**/*.ipynb` and `labs/**/*.py`:

| Removed | Evidence |
|---|---|
| `torchvision` | Zero imports. No lab loads an image dataset; `digits_subset.npz` is NumPy arrays. |
| `adversarial-robustness-toolbox` | Zero imports. FGSM, PGD, poisoning, membership inference and extraction are implemented in the course's own code, which is the pedagogical point. |
| `opacus` | Zero imports. M09's DP demonstration is written directly against PyTorch. |
| `transformers` | Zero imports. M11 uses a local Ollama call optionally, not a transformer pipeline. |
| `datasets` | Zero imports. No hub dataset is fetched anywhere in the course. |

Removing them is not only hygiene: each pulled a large transitive tree (torchvision and ART both pull torch-adjacent
wheels), and `opacus` and `transformers` each impose their own PyTorch bounds, which is precisely how an
"it worked last semester" environment breaks.

## 4. Verification evidence

| Check | Command | Result |
|---|---|---|
| Full resolution of the pinned set | `python -m pip install --dry-run -r requirements-labs.txt` | **exit 0** — every pin and transitive constraint satisfiable |
| Pins exist and match the validated environment | `importlib.metadata.version` for all 12 | all match, except jupyterlab which was installed to verify |
| Environment check passes | `python scripts/check_env.py` in a venv with the pinned stack | **"Result: ready. You can start Module 01."** |
| Every lab runs on the pinned stack | 32 solutions executed | **32/32 exit 0** |
| Every notebook runs on the pinned stack | 34 notebooks executed | **34/34 pass**, 279.8 s total |
| No stale references to removed packages | grep across README, docs, ATTRIBUTION, DEVELOPMENT, CONTRIBUTING | only a "further reading" citation to Opacus documentation, which is legitimate |

Validation environment for all of the above: CPython 3.14.7 on Windows 11, four-core CPU, no GPU, no network during
execution. `check_env.py` accepts Python 3.12–3.14 and rejects anything else with an actionable message.

## 5. Documentation brought back into line

Pinning changed the truth on several pages, so they were corrected rather than left to drift:

| File | Correction |
|---|---|
| `scripts/check_env.py` | Package list, Python range (3.12–3.14) and install guidance match the new file |
| `docs/getting-started/environment.md` | Python guidance, the sample `check_env` output, the troubleshooting row and the "working offline" table |
| `docs/index.md` | "Python 3.11+" → 3.12+, and the fabricated "security tooling" row (ART, picklescan, pip-audit, bandit — none of which the course installs) replaced with the truth |
| `docs/references.md` | Tooling table now lists the pinned stack, not ART/Opacus/Transformers |
| `docs/attribution.md` | Library table matches the pins |
| `ATTRIBUTION.md` §4.3 | Version-pin table, removal note, Apache-2.0 obligations narrowed to safetensors, and the verification snippet's package list |
| `DEVELOPMENT.md`, `COURSE_ARCHITECTURE.md`, `labs/README.md` | Dependency description, Python floor, and a setup that no longer installs torch twice |

## 6. Findings and residual risk

| Severity | Finding |
|---|---|
| Low | **`jupyterlab==4.6.6` was installed and reported correctly, but the JupyterLab UI itself was not opened.** It is the documented way to run notebooks; execution was validated with `nbclient` and `ipykernel`, which is the same kernel path. |
| Low | **Pinning freezes a moment.** When a CVE lands in one of these twelve packages, the fix is a deliberate version bump plus a full re-run of 32 labs and 34 notebooks — which is exactly the review the pins are meant to force. `ATTRIBUTION.md` §10 documents the check to run. |
| Info | **PyTorch wheel indexing.** The pin resolves from PyPI for this platform; a CPU-only install can use the official PyTorch index, documented in the requirements header. |
| Info | **Students on Python 3.15+** will be told to use 3.12–3.14. That is a real constraint of the PyTorch wheel matrix, not an arbitrary rule. |

A student following the documented three commands now gets exactly the environment the numbers in the labs were
produced in, which was not true before this phase.
