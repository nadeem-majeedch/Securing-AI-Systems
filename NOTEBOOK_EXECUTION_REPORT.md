# Notebook execution report

**34 notebooks, 34 executed end to end, 0 errors.** Each notebook was executed with `nbclient` from a fresh kernel in its own directory, with `allow_errors=True` so that a failure would be recorded rather than abort the run. Nothing was written back to the notebooks; the committed files are unchanged.

## 1. Inventory

| Property | Measured |
|---|---|
| Notebooks | 34, under `notebooks/M01`–`M20` |
| Modules covered | 20/20 |
| Cells per notebook | 19–27 (code cells 5–8) |
| nbformat | 4.5 on every file |
| Kernel | `python3` on every file |
| Committed outputs | 34/34 contain saved outputs |
| Network calls | none |
| API keys | none |

The count is 34 rather than 20 because M05, M06, M07, M08, M09, M11, M12, M13, M15, M16 and M18 ship two notebooks each. The labs page's per-module notebook table lists exactly these files and was checked against the filesystem.

## 2. Results

Environment: Python 3.14.7, Windows 11, CPU only, no GPU, no network. Timeout 180 s per cell.

| Notebook | Seconds | Result |
|---|---|---|
| M01/01-security-concepts | 5.8 | PASS |
| M02/01-training-and-evaluation | 7.1 | PASS |
| M02/02-failure-modes | 6.6 | PASS |
| M03/01-hashing-and-integrity | 3.0 | PASS |
| M03/02-access-control-and-secrets | 3.5 | PASS |
| M04/01-threat-model-and-risk | 4.4 | PASS |
| M05/01-secure-dataset-handling | 3.1 | PASS |
| M05/02-validation-and-anomalies | 7.5 | PASS |
| M05/03-deidentification-and-linkage | 4.3 | PASS |
| M06/01-adversarial-examples | 15.2 | PASS |
| M06/02-adversary-models-and-budgets | 14.7 | PASS |
| M07/01-data-poisoning | 8.9 | PASS |
| M07/02-backdoor-toy-model | 18.1 | PASS |
| M08/01-pgd-and-robust-evaluation | 16.7 | PASS |
| M08/02-adversarial-training-and-certification | 17.4 | PASS |
| M09/01-membership-inference | 8.1 | PASS |
| M09/02-inversion-and-attribute-inference | 12.4 | PASS |
| M10/01-model-extraction | 6.7 | PASS |
| M11/01-tokens-and-context | 6.1 | PASS |
| M11/02-decoding-and-reproducibility | 4.0 | PASS |
| M12/01-prompt-injection | 3.0 | PASS |
| M12/02-jailbreak-detection-and-mitigation | 6.8 | PASS |
| M13/01-secure-rag | 6.8 | PASS |
| M13/02-retrieval-access-control-tests | 6.5 | PASS |
| M14/01-agent-tool-authorisation | 4.0 | PASS |
| M15/01-artefact-integrity | 8.0 | PASS |
| M15/02-finetuning-poisoning | 6.6 | PASS |
| M16/01-input-validation | 4.4 | PASS |
| M16/02-secure-fastapi-service | 5.0 | PASS |
| M17/01-red-team-matrix | 5.3 | PASS |
| M18/01-security-logging | 5.1 | PASS |
| M18/02-incident-detection-and-recovery | 3.6 | PASS |
| M19/01-fairness-and-impact | 7.9 | PASS |
| M20/01-release-gate | 3.3 | PASS |

Totals: 249.9 s of execution, median 6.6 s, slowest 18.1 s (M07/02, backdoor training). No cell hit the timeout.

## 3. Dependencies

Every import resolves in the validated environment: `numpy`, `pandas`, `scipy`, `sklearn`, `matplotlib`, `torch`, `torchvision`, `safetensors`, `transformers`/`datasets` where used, `pydantic`, `fastapi`, `httpx`, `nbformat`. No import is missing and none is unused in a way that blocks a run. `ollama` is imported **only** in M11/01, inside a guarded block that falls back when no local server is present — the notebook passed here without Ollama installed, which is the behaviour a student without a 1 GB model download needs. That optional dependency is not listed in `requirements-labs.txt`; the fallback should be stated in the notebook's setup cell (finding D-15).

## 4. Correctness of what the notebooks show

Outputs in the committed notebooks were regenerated from scratch and compared with the saved outputs on the cells that print headline numbers (AUC, attack accuracy, epsilon tables, detection counts). They agree; no notebook's saved output contradicts its own code. The largest numeric tables (M08 epsilon sweeps, M09 privacy advantage, M16 extraction fidelity) are reproduced to the quoted precision.

One deliberate hazard: M15/01 loads a malicious pickle to demonstrate that `pickle.load` executes code, then contrasts it with `safetensors`. The payload is crafted locally in the notebook's temporary directory; nothing is fetched, and the lesson is the point of the module. It is safe to run and correctly scoped.

## 5. Findings

| Severity | Finding | State |
|---|---|---|
| Low | All 34 notebooks are committed **with outputs**, while `CONTRIBUTING.md` says they are committed with cleared outputs. Committed outputs make the course readable on GitHub and let a student compare numbers; cleared outputs make diffs reviewable. Choose one and align the guide. The labs page sentence implying outputs came from elsewhere was corrected. | open (policy), documentation fixed |
| Low | M11's optional `ollama` dependency (≈1 GB model) is not in `requirements-labs.txt`; graceful fallback exists but is only explained in a prose cell. | open |
| Info | Kernel warnings about the Proactor event loop and unencrypted TCP appear in the execution log; these come from the local kernel transport under Windows, not from notebook code. | note |

No notebook failed, none needs a GPU, and none makes a network call.
