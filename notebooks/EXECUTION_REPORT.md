# Notebook Execution Report

**Course:** Securing AI Systems (BS Data Science, PUCIT)
**Artefact:** 34 Jupyter notebooks in `notebooks/M01` … `notebooks/M20`
**Validation date:** 16 November 2026
**Status:** 34 of 34 executed end to end with no errors; all cells have stored outputs.

This report records what was run, in what environment, what was found and fixed, and what remains
unverified. It is the evidence behind the claim that these notebooks execute from beginning to end.

---

## 1. Validation environment

A dedicated virtual environment was created for validation, so the notebooks were not executed in the
authoring environment that already contained extra packages:

```bash
python -m venv .venv-nbclean
.venv-nbclean/Scripts/python -m pip install numpy pandas scikit-learn matplotlib scipy \
    safetensors fastapi httpx pydantic nbformat nbclient ipykernel
.venv-nbclean/Scripts/python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
```

| Component | Version |
|---|---|
| Python | 3.14.7 |
| numpy | 2.5.5 |
| pandas | 3.1.1 |
| scikit-learn | 1.9.1 |
| matplotlib | 3.11.2 |
| scipy | 1.18.1 |
| torch | 2.15.0+cpu |
| safetensors | 0.8.0 |
| pydantic | 2.14.3 |
| fastapi | 0.163.1 |
| httpx | 0.28.1 |
| nbformat / nbclient / ipykernel | 5.11.1 / 0.11.0 / 7.4.0 |

Each notebook was executed in place with `nbclient` (kernel `python3`, `allow_errors=False`, 900 s per
notebook), which writes fresh outputs back into the `.ipynb`. Hardware: ordinary CPU-only laptop; no GPU
was used or required by any notebook. No network access was needed at run time and nothing was downloaded.

The scratch environment and the generation scripts were removed afterwards; only the notebooks and this
report remain.

---

## 2. Results

| Module | Notebook | Cells (code) | Runtime (s) | Result |
|---|---|---:|---:|---|
| M01 | `01-security-concepts.ipynb` | 20 (6) | 10.1 | pass |
| M02 | `01-training-and-evaluation.ipynb` | 22 (6) | 20.2 | pass |
| M02 | `02-failure-modes.ipynb` | 21 (6) | 8.7 | pass |
| M03 | `01-hashing-and-integrity.ipynb` | 22 (6) | 4.0 | pass |
| M03 | `02-access-control-and-secrets.ipynb` | 22 (6) | 4.7 | pass |
| M04 | `01-threat-model-and-risk.ipynb` | 24 (7) | 5.3 | pass |
| M05 | `01-secure-dataset-handling.ipynb` | 22 (6) | 3.4 | pass |
| M05 | `02-validation-and-anomalies.ipynb` | 24 (7) | 8.6 | pass |
| M05 | `03-deidentification-and-linkage.ipynb` | 22 (6) | 5.1 | pass |
| M06 | `01-adversarial-examples.ipynb` | 21 (6) | 17.5 | pass |
| M06 | `02-adversary-models-and-budgets.ipynb` | 19 (5) | 15.9 | pass |
| M07 | `01-data-poisoning.ipynb` | 21 (6) | 9.2 | pass |
| M07 | `02-backdoor-toy-model.ipynb` | 19 (5) | 19.1 | pass |
| M08 | `01-pgd-and-robust-evaluation.ipynb` | 21 (6) | 17.3 | pass |
| M08 | `02-adversarial-training-and-certification.ipynb` | 21 (6) | 20.2 | pass |
| M09 | `01-membership-inference.ipynb` | 21 (6) | 9.8 | pass |
| M09 | `02-inversion-and-attribute-inference.ipynb` | 22 (6) | 16.2 | pass |
| M10 | `01-model-extraction.ipynb` | 24 (7) | 8.5 | pass |
| M11 | `01-tokens-and-context.ipynb` | 19 (5) | 3.3 | pass |
| M11 | `02-decoding-and-reproducibility.ipynb` | 21 (6) | 5.5 | pass |
| M12 | `01-prompt-injection.ipynb` | 22 (6) | 3.9 | pass |
| M12 | `02-jailbreak-detection-and-mitigation.ipynb` | 24 (7) | 8.4 | pass |
| M13 | `01-secure-rag.ipynb` | 22 (6) | 7.1 | pass |
| M13 | `02-retrieval-access-control-tests.ipynb` | 22 (6) | 7.7 | pass |
| M14 | `01-agent-tool-authorisation.ipynb` | 25 (7) | 4.2 | pass |
| M15 | `01-artefact-integrity.ipynb` | 26 (8) | 8.9 | pass |
| M15 | `02-finetuning-poisoning.ipynb` | 22 (6) | 6.9 | pass |
| M16 | `01-input-validation.ipynb` | 22 (6) | 4.1 | pass |
| M16 | `02-secure-fastapi-service.ipynb` | 22 (6) | 4.4 | pass |
| M17 | `01-red-team-matrix.ipynb` | 24 (7) | 5.3 | pass |
| M18 | `01-security-logging.ipynb` | 27 (8) | 5.8 | pass |
| M18 | `02-incident-detection-and-recovery.ipynb` | 25 (7) | 3.9 | pass |
| M19 | `01-fairness-and-impact.ipynb` | 27 (8) | 8.4 | pass |
| M20 | `01-release-gate.ipynb` | 25 (7) | 3.4 | pass |

Total wall-clock time for all 34 notebooks: about 5 minutes on CPU. The slowest notebooks are the
PyTorch ones (M06, M07b, M08), which train small networks for attack and defence demonstrations.

### Structural checks

Automated checks over all 34 files confirmed:

- every notebook is valid `nbformat` 4 and opens in JupyterLab;
- every notebook has a title and all twelve required teaching components (title and module reference,
  objectives, background, dependencies, installation, demonstrations, explanations, expected outputs,
  exercises, reflection questions, references, visualisations where useful);
- every code cell has stored output (no cell was skipped or silently failed);
- `metadata.sas.module` matches the containing directory, and `kernelspec` is `python3`;
- no notebook contains an unexplained code dump: each demonstration cell is preceded or followed by prose
  that states its purpose and, for result cells, the expected output.

---

## 3. Defects found and fixed

These were genuine failures or misleading results found by executing the notebooks, not by reading them.

| # | Notebook | Symptom | Fix |
|---|---|---|---|
| 1 | M01 | Notebook had been written but never executed (no outputs, no execution counts) | Re-executed; outputs now stored |
| 2 | M02a | `AssertionError`: identical seed produced different predictions — lbfgs had not converged on unscaled features | `Pipeline(StandardScaler, LogisticRegression)` and a tolerance-based reproducibility assertion |
| 3 | M02b | "Covariate shift" demonstration *raised* accuracy, contradicting the text | Replaced the additive offset with a sign/encoding change (a realistic unit error): accuracy 0.84 → 0.52 with an unchanged-looking positive rate |
| 4 | M04 | `ValueError`: 5-tuple rows against a 4-column DataFrame | Added the missing `change` column |
| 5 | M07a | Label-flip poisoning changed nothing (0.986 → 0.986): a linear model averaged the flips away, so the notebook taught the opposite of its claim | Switched the victim to a 5-NN local learner with overlapping classes; poisoning now measurably degrades accuracy (0.82 → 0.74 at ρ = 0.20) and the targeted attack flips 112/200 probes |
| 6 | M08b | Certified 0 of 40 inputs at every σ: the runner-up bound was computed as `1 − lower_bound(...)`, which is not an upper bound | Added a Clopper–Pearson upper bound; 37/40 certified, median radius 0.373 |
| 7 | M09b | Inversion diverged (relative L2 error 99.5) because the logit was unbounded | Added an L2 penalty (λ = 4) and clamped the answer to the observed range; now reports cosine similarity (0.79 vs −0.47 for the global-mean baseline) and states plainly that magnitude is not recovered |
| 8 | M10 | `ValueError: Unknown label type: continuous` — probability outputs were fed to a classifier | Continuous outputs are distilled with `Ridge`, discrete labels with `LogisticRegression`; the watermark trigger was moved to an input where the clean model is genuinely uncertain (it previously responded 1.00 too) |
| 9 | M12a | The combined "all" defence scored ASR 0.67 instead of 0.00: the email block only matched one defence label | Membership test over both labels; ASR now 0.00 |
| 10 | M13b | The "k results" invariant expected 2 permitted documents when the public document makes 3, so both the correct and the buggy index passed | Corrected to 3; the post-filtered index now fails 1 of 5, which is the intended demonstration |
| 11 | M15b | `ValueError: X has 150 features, but LogisticRegression is expecting 148` — one vectoriser was refitted while the clean model kept the old one | Separate vectorisers per model, with the vocabulary documented |
| 12 | M16b | `RuntimeError: asyncio.run() cannot be called from a running event loop` inside the kernel | Top-level `await` on the ASGI client calls; no event-loop juggling |
| 13 | M17 | Per-cell seeds derived from Python's `hash()`, which is randomised per process — results were not reproducible across runs | Stable ordinal seeds |
| 14 | M18a | The alert rule fired on quiet minutes with 5 denials, contradicting "three alerts at 40–42" | Minimum denial count raised to 8; the two thin minutes are now correctly excluded and the text explains why |
| 15 | M18b | MTTD computed from pre-attack background noise (43 min instead of 26) | First malicious event restricted to the attack window; MTTD now 26 min, matching the lesson text |
| 16 | M20 | The membership-advantage criterion was judged as "higher is better" although it is a ceiling, so the gate reported the wrong failure list | Added a `direction` column (`min` → lower bound, `max` → upper bound); the gate now fails C1 and C4 only, as documented |
| 17 | M06a | `UserWarning: Converting a tensor with requires_grad=True to a scalar` | `loss.detach()` in the print |
| 18 | M11 | `ollama` is not installed in the validation environment | The optional live-model cell catches the import error, prints a skip notice and continues; the interface argument does not depend on it |

After fixing 2–16, every stored "Expected output" note was reconciled against the actual executed output.
Twelve notebooks had prose that no longer matched their numbers (for example M02a's three-decimal block,
M05b's issue count, M05c's linkage counts, M08a's F1/FGSM ordering, M19's base rates); those were corrected
to describe what the code actually produces, using approximate ranges where a value depends on a random draw.

---

## 4. Coverage of the required practical topics

| Required topic | Notebook |
|---|---|
| Basic security concepts in Python | M01/01 |
| Dataset integrity with cryptographic hashes | M03/01 |
| Secure dataset handling | M05/01 |
| Data validation and anomaly detection | M05/02 |
| ML training and evaluation | M02/01, M02/02 |
| Adversarial examples against image classifiers | M06/01 |
| Evasion attacks and robustness evaluation | M06/02, M08/01, M08/02 |
| Data poisoning with synthetic data | M07/01, M15/02 |
| Backdoor behaviour in a controlled toy model | M07/02 |
| Membership inference | M09/01 |
| Model inversion on synthetic data | M09/02 |
| Model extraction from a local toy API | M10/01 |
| Input validation and abuse prevention | M16/01 |
| Prompt injection | M11/01, M12/01 |
| Jailbreak detection and mitigation | M12/02 |
| Secure RAG | M13/01 |
| Retrieval access-control testing | M13/02 |
| Agent tool authorisation | M14/01 |
| Secure API with FastAPI | M16/02 |
| AI red teaming | M17/01 |
| Security logging and monitoring | M18/01 |
| Incident detection and recovery | M18/02 |

Supporting notebooks that the module structure requires but the topic list does not name: M03/02 (access
control, secrets, password hashing), M04/01 (threat modelling and risk), M05/03 (de-identification and
linkage), M11/02 (decoding determinism), M15/01 (artefact integrity and supply chain), M19/01 (fairness and
impact assessment), M20/01 (release gate).

---

## 5. Reproducibility and determinism

- Every notebook fixes `SEED` for NumPy and `torch.manual_seed` for PyTorch, and passes `random_state`
  to scikit-learn estimators.
- No notebook uses `hash()`, wall-clock time, unseeded shuffles or network input to decide a result.
  M18b uses fixed timestamps constructed with `datetime`, not `now()`.
- The M02a notebook contains an explicit assertion that the same seed reproduces predictions bit-for-bit
  (largest probability difference `0.00e+00`); it passes.
- M13b, M16b and M20 contain executable assertions over their own invariants (no cross-tenant retrieval,
  uniform status codes, gate decision), so a regression fails the notebook rather than silently passing.
- Re-running the whole set in the clean environment reproduced the values quoted in the notebook prose,
  including the exact three-decimal accuracy block in M02a, despite patch-level version differences in
  NumPy, pandas and PyTorch.

---

## 6. Security posture of the demonstrations

- No real system, host, account or endpoint is contacted. APIs, agents, LLM targets and retrieval indexes
  are local objects defined inside the notebooks.
- All offensive demonstrations use synthetic data (two-dimensional Gaussian clouds, synthetic referral
  records, synthetic support messages, `sklearn`'s bundled digits and breast-cancer sets) or toy models
  trained in the notebook.
- No operational attack tooling, malware, credential harvesting or real jailbreak text is included. The
  injection payloads, jailbreak templates and red-team prompts are placeholders that exercise a mock
  policy follower.
- Every attack notebook ends with detection, mitigation or a design control; the emphasis is defensive.
- Secrets appear only as obviously fake placeholders (`sk-live-9f2b…`) used to demonstrate redaction.

---

## 7. Known limitations

1. **No live language model was executed.** `ollama` and a 1 GB local model were not available in the
   validation environment, so M11/01's optional Ollama cell prints its skip notice. The notebook states
   this is expected and supplies the deterministic mock path; every other LLM-security notebook is
   deliberately model-free. An instructor with Ollama installed can run that one cell unchanged.
2. **`nbconvert` is not installed**, so notebooks were validated by execution (`nbclient`), not by HTML
   or PDF export. Export should be checked separately if the course needs printable copies.
3. **Expected values are environment-specific to three decimals.** Where a value depends on a random draw
   the prose gives a range instead of an exact figure. M02a's exact block (`0.979 / 0.999 / 0.017`) is the
   one exception and may drift on very different library versions; the notebook's assertions, not the
   prose, are the real check.
4. **Deliberately small test sets.** Notebooks use 450–2000 rows to stay inside a five-minute budget.
   This widens confidence intervals; Module 17 quantifies exactly that trade instead of hiding it.
5. **M08b's adversarial training is a short budget** (8 epochs, 7-step inner attack) for CPU reasons. The
   resulting robust accuracy (0.25) is honest for that budget and the notebook says so; longer training
   would raise it.
6. **Notebook runtime on a slow machine.** The PyTorch notebooks take 15–20 s each here; on a much slower
   laptop, allow a few minutes for M06–M08.
7. **No commit or push was performed**, as instructed. The repository state is whatever it was before this
   task, plus the files listed below.

---

## 8. Files delivered

```
notebooks/
  EXECUTION_REPORT.md              this report
  M01/ 01-security-concepts.ipynb
  M02/ 01-training-and-evaluation.ipynb, 02-failure-modes.ipynb
  M03/ 01-hashing-and-integrity.ipynb, 02-access-control-and-secrets.ipynb
  M04/ 01-threat-model-and-risk.ipynb
  M05/ 01-secure-dataset-handling.ipynb, 02-validation-and-anomalies.ipynb,
       03-deidentification-and-linkage.ipynb
  M06/ 01-adversarial-examples.ipynb, 02-adversary-models-and-budgets.ipynb
  M07/ 01-data-poisoning.ipynb, 02-backdoor-toy-model.ipynb
  M08/ 01-pgd-and-robust-evaluation.ipynb, 02-adversarial-training-and-certification.ipynb
  M09/ 01-membership-inference.ipynb, 02-inversion-and-attribute-inference.ipynb
  M10/ 01-model-extraction.ipynb
  M11/ 01-tokens-and-context.ipynb, 02-decoding-and-reproducibility.ipynb
  M12/ 01-prompt-injection.ipynb, 02-jailbreak-detection-and-mitigation.ipynb
  M13/ 01-secure-rag.ipynb, 02-retrieval-access-control-tests.ipynb
  M14/ 01-agent-tool-authorisation.ipynb
  M15/ 01-artefact-integrity.ipynb, 02-finetuning-poisoning.ipynb
  M16/ 01-input-validation.ipynb, 02-secure-fastapi-service.ipynb
  M17/ 01-red-team-matrix.ipynb
  M18/ 01-security-logging.ipynb, 02-incident-detection-and-recovery.ipynb
  M19/ 01-fairness-and-impact.ipynb
  M20/ 01-release-gate.ipynb
```

`requirements-labs.txt` was updated: the Python floor is now 3.12 (validated on 3.14.7), and `nbclient`,
`pydantic`, `fastapi` and `httpx` were added so a student can install everything the notebooks need with one
command.

## 9. How to run a notebook

```bash
python -m venv .venv
# activate the environment, then
python -m pip install --upgrade pip
python -m pip install -r requirements-labs.txt
python -m pip install torch --index-url https://download.pytorch.org/whl/cpu   # CPU build
jupyter lab notebooks/M08/01-pgd-and-robust-evaluation.ipynb
```

Run cells from the top. Each notebook is self-contained: it imports what it needs, creates its own
synthetic data, and writes nothing outside a temporary directory that it removes.
