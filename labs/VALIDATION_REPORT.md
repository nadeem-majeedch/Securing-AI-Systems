# Laboratory programme — validation report

> **Phase 14 note.** Sections 18–22 (acceptable use, scope restrictions, data handling, cleanup,
> environment restoration) were added to all 32 briefs after the validation run recorded below, which
> therefore counts 17 sections. The technical results in this report are unchanged and were re-verified
> in Phase 14.

Date: 16 November 2026
Scope: all 32 laboratories in `labs/student/` and `labs/solutions/`, plus `labs/scripts/make_datasets.py`,
`labs/common/labkit.py`, `LAB_INDEX.md` and `CHECKLIST.md`.

## Environment

| Item | Value |
|---|---|
| Python | 3.14 (CPython, Windows 11, CPU only) |
| Numerical stack | NumPy 2.x, pandas, scikit-learn, PyTorch (CPU), SciPy |
| Web stack | FastAPI 0.162, httpx 0.28 (in-process `TestClient`) |
| Network | none required at run time |
| Data | generated locally by `python labs/scripts/make_datasets.py` (seed 2026) |

## What was executed

1. `python labs/scripts/make_datasets.py` — regenerated every dataset after the final data change.
   Printed row counts and SHA-256 prefixes for all nine artefacts.
2. Every solution script, executed from the project root, in the rendered location:
   `python labs/solutions/L01/solution.py` … `python labs/solutions/L32/solution.py`.
   **32/32 exited 0.**
3. Every student starter script byte-compiled (`py_compile`) to prove it is syntactically valid and imports
   cleanly up to the `WORK STARTS HERE` marker. **32/32 compiled.**
4. Structure checks on the rendered manuals: 17 sections per lab, a pointer-only Solution section, no solution
   body in `labs/student/`, one `LAB.md` and one `starter.py` per lab, one `solution.py` and one `SOLUTION.md`
   per solution folder.
5. Index and checklist regenerated and inspected: 32 rows each, difficulty split Beginner 9 · Intermediate 13 ·
   Advanced 7 · Challenge 3, modules M01–M20 all covered.

## Verified headline results per lab

These are the numbers the manuals quote in *Expected results*; each was produced by the executed script.

| Lab | Module | Headline result verified |
|---|---|---|
| L01 | M01 | 240 referrals audited, 4 flagged |
| L02 | M02 | accuracy 0.857, AUC 0.875, Brier 0.104, 77 errors, 2 confident errors |
| L03 | M03 | manifest verifies `True` then `False` after tamper; forged MAC rejected |
| L04 | M03 | 5 permissions allowed, 5 denied with reasons |
| L05 | M04 | T6 residual risk 12.0 ranks first; T1 second at 8.0 |
| L06 | M05 | 236 referrals accepted, 4 quarantined (R0007, R0011, R0042, R0150) |
| L07 | M05 | min k 1→5 available; single-candidate rows 253→0; 554 rows kept |
| L08 | M06 | clean 0.829; epsilon sweep 0.685 / 0.496 / 0.081 / 0.000; max pixel change equals eps |
| L09 | M06 | transfer drops B 0.821→0.272; noise control 0.806; 79,400 queries for black-box 0.819 |
| L10 | M07 | accuracy 0.839→0.683 at 20 % flipped labels; 20/20 targeted probes missed |
| L11 | M07 | clean/backdoored accuracy 0.789; trigger rate 0.533→1.000; scan recall >0.9; ablation ranks `trigger_slot` first |
| L12 | M08 | clean 0.846; PGD 0.058 at eps 0.20; unprojected change 0.750 against 0.200 declared |
| L13 | M08 | standard 0.836/0.071; adversarial 0.786/0.234; 18/20 certified, median radius 0.254 |
| L14 | M09 | membership 2·AUC−1 0.426 at k=1 → 0.054 at k=25; advantage at 5 % FPR +0.037 |
| L15 | M09 | attribute inference precision 0.515/0.533/0.638 against base rate 0.427; inversion cosine 0.953 vs 0.182 |
| L16 | M10 | extraction fidelity 0.813 / 0.833 / 0.823 at 50/150/500 queries; labels 0.800 at 150 |
| L17 | M11 | system component never truncated; filter catches 1/4 raw variants, 2/4 after NFKC |
| L18 | M11 | distinct outcomes 1 / 2 / 5 / 5 / 3 by configuration; seed reproduces a path, extra draw breaks it |
| L19 | M12 | tool-call ASR 0.62 / disclosure 0.38; allowlist 0.00 tool calls; combination 0.00 / 0.00 |
| L20 | M12 | TPR 1.00 at 1 % FPR; precision 0.990 / 0.840 / 0.091 at 50 %, 5 %, 0.1 % prevalence |
| L21 | M13 | buggy prompt contains 1 foreign document; pre-filtered prompt contains none |
| L22 | M13 | correct index 9/9 tests, buggy index 7/9 (deletion checks fail) |
| L23 | M14 | 7/10 tool requests denied, each with a named rule |
| L24 | M15 | clean bundle 3/3 hashes match; tampered 1/3; pickle format refused |
| L25 | M16 | fine-tuned ASR 1.000; patch scan precision/recall 1.00; ASR 0.100 after removal |
| L26 | M16 | insecure app 200-with-error and no auth; hardened 401 / 422 on every invalid probe |
| L27 | M17 | fixed window blocks 37 abusive requests, 0 honest; token bucket 12 + 13 export quota |
| L28 | M18 | 6/6 red-team cells reproduced, each with a control and a coverage gap |
| L29 | M17 | abusive principal ranks first with multiple signals above 3 |
| L30 | M19 | tampered `config.json` detected; rebuilt 3/3; parity 0.0 restored, drift measurable tampered |
| L31 | M19 | disparate impact 0.728→0.730; opportunity gap 0.041→0.052; calibration 0.154→0.151 |
| L32 | M20 | complete evidence releases; missing, weak-robustness and leaky-privacy variants block |

## Determinism

Each solution seeds NumPy, PyTorch or scikit-learn explicitly and asserts a fixed split. Re-running a script
produced the same headline numbers during validation; the exact tables depend on the library versions listed
above (PyTorch training in L13 and L09 can vary in the last decimal on different BLAS builds, which is why the
labs assert inequalities and ranges rather than exact accuracies).

## Known limitations, stated rather than hidden

- L14's advantage at 5 % FPR is small (+0.037) even though the ranking leak is large (2·AUC−1 = 0.426). Both
  numbers are reported; the manual explains why the operating point is severe.
- L16's fidelity plateaus at 0.823 because the substitute saturates its query distribution; the manual uses that
  plateau as the argument for a quota rather than presenting extraction as unbounded.
- L31's reweighting moves the disparate impact ratio by only 0.002 and slightly widens the opportunity gap. The
  lab reports all three metrics and asserts movement toward parity, not a solved problem.
- L22's ACL suite catches deletion, cross-tenant and completeness faults; it cannot catch a wrong ACL value
  attached at ingestion, which the manual states.
- Dataset checksum values will differ for anyone regenerating with a different NumPy release; the generator is
  seeded, not bit-reproducible across versions.

## Not performed

- No deployment, no publishing, no committing and no pushing. The working tree was left uncommitted as requested.
- No long-running training: all models are small and CPU-only by design (the slowest lab, L13, completes in a
  few minutes).
- No browser or UI testing — this deliverable is scripts and manuals, not a web application.

## How to re-verify from a clean checkout

```
python labs/scripts/make_datasets.py
for d in labs/solutions/L*/; do python "$d/solution.py" > /dev/null || echo "FAIL $d"; done
```

A silent run means all 32 solutions executed successfully.
