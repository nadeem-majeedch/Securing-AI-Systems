# Laboratory validation report

**32 laboratories shipped, 32 executed, 32 passed.** Every solution was run as a subprocess from the repository root in the environment described below; the table records what actually happened, not what the brief promised.

## 1. What is in the repository

For each of `L01`–`L32`:

| Artefact | Path | Present |
|---|---|---|
| Brief (17 sections) | `labs/student/Lxx/LAB.md` | 32/32 |
| Starter script | `labs/student/Lxx/starter.py` | 32/32 |
| Reference solution | `labs/solutions/Lxx/solution.py` | 32/32 |
| Solution write-up | `labs/solutions/Lxx/SOLUTION.md` | 32/32 |
| Datasets / models | `labs/datasets/` | 5 CSV, 2 JSON, `digits_subset.npz`, 2 model bundles, 2 safetensors fixtures |
| Dataset generator | `labs/scripts/make_datasets.py` | present; deterministic, no network |

Briefs run 745–888 words and every one uses the same 17 numbered sections: Scenario · Problem statement · Learning objectives · Prerequisites · Required software · Dataset and input files · Detailed instructions · Python implementation · Expected results · Interpretation · Student tasks · Challenge exercises · Hints · Solution · Troubleshooting · Security lessons · Submission. Hints precede the solution; the solution section points at the separate file rather than pasting it, so the brief can be used as an assessment without spoilers.

## 2. Execution results

Environment: Python 3.14.7, Windows 11, four-core CPU, no GPU, no network. Each solution was run with the lab directory as the working directory and a 300 s timeout.

| Lab | Module | Stated budget | Runtime (s) | Exit | Result |
|---|---|---|---|---|---|
| L01 | M01 | 45 minutes | 3.6 | 0 | PASS |
| L02 | M02 | 60 minutes | 10.7 | 0 | PASS |
| L03 | M03 | 45 minutes | 1.2 | 0 | PASS |
| L04 | M03 | 60 minutes | 1.2 | 0 | PASS |
| L05 | M04 | 50 minutes | 1.2 | 0 | PASS |
| L06 | M05 | 50 minutes | 1.2 | 0 | PASS |
| L07 | M05 | 70 minutes | 1.2 | 0 | PASS |
| L08 | M06 | 80 minutes | 8.6 | 0 | PASS |
| L09 | M06 | 90 minutes | 7.2 | 0 | PASS |
| L10 | M07 | 75 minutes | 4.0 | 0 | PASS |
| L11 | M07 | 80 minutes | 3.9 | 0 | PASS |
| L12 | M08 | 90 minutes | 7.2 | 0 | PASS |
| L13 | M08 | 120 minutes | 8.9 | 0 | PASS |
| L14 | M09 | 70 minutes | 3.9 | 0 | PASS |
| L15 | M09 | 80 minutes | 4.0 | 0 | PASS |
| L16 | M10 | 80 minutes | 4.0 | 0 | PASS |
| L17 | M11 | 50 minutes | 1.3 | 0 | PASS |
| L18 | M11 | 60 minutes | 1.4 | 0 | PASS |
| L19 | M12 | 55 minutes | 1.3 | 0 | PASS |
| L20 | M12 | 70 minutes | 4.0 | 0 | PASS |
| L21 | M13 | 70 minutes | 4.1 | 0 | PASS |
| L22 | M13 | 80 minutes | 3.9 | 0 | PASS |
| L23 | M14 | 75 minutes | 1.3 | 0 | PASS |
| L24 | M15 | 60 minutes | 1.4 | 0 | PASS |
| L25 | M16 | 85 minutes | 4.1 | 0 | PASS |
| L26 | M16 | 55 minutes | 2.6 | 0 | PASS |
| L27 | M17 | 70 minutes | 1.4 | 0 | PASS |
| L28 | M18 | 90 minutes | 1.5 | 0 | PASS |
| L29 | M17 | 65 minutes | 1.4 | 0 | PASS |
| L30 | M19 | 100 minutes | 1.4 | 0 | PASS |
| L31 | M19 | 75 minutes | 3.9 | 0 | PASS |
| L32 | M20 | 110 minutes | 1.3 | 0 | PASS |

Computing time is 1.2–10.7 s per lab — between 1 % and 10 % of the stated budget, so the budgets are spent on reading, extending and writing up, not on waiting. No lab writes outside its directory except L03's temporary integrity fixtures, and all of them exit cleanly, which is what makes reruns possible without cleanup steps.

## 3. Reproducibility

- Fixed seeds throughout; repeated runs produced identical numeric output in this audit (spot-checked by rerunning L02, L08 and L14).
- No network access on any path: `make_datasets.py` regenerates every CSV/JSON/NPZ locally, the model bundles are committed, and the only third-party teaching data (`digits_subset.npz`) is bundled and credited in `ATTRIBUTION.md` as UCI CC BY 4.0.
- Expected outputs are stated numerically in every brief (e.g. L02 AUC 0.875, Brier 0.104; L12 robust accuracy 0.063 at ε = 0.2 against PGD-15). The solutions print numbers matching those statements in this environment.
- Dependency ranges, not pins, are the remaining caveat: see `requirements-labs.txt` and finding D-06 in the final report. A future wheel could change the third decimal of a quoted number.

## 4. Coverage and pedagogy

- All 20 modules have at least one lab; 12 modules have two (M03, M05, M06, M07, M08, M09, M11, M12, M13, M16, M17, M19).
- Every brief carries a threat model in the scenario, prerequisites that name the module reading, software and dataset sections, ordered instructions with checkpoints, a separate solution, troubleshooting for the two or three failures students actually hit, and a submission section tied to the rubric in the assignment page.
- The expected results sections state what the number means and what it does not — e.g. L14 says the membership-inference advantage is a measurement, not a re-identification proof. This is the right posture for a security course.

## 5. Findings

| Severity | Finding | State |
|---|---|---|
| Medium | **No lab has a Cleanup section or a per-lab acceptable-use statement**, although `CONTRIBUTING.md` §5 requires both and the previous labs landing page advertised them. Safety is handled at module level and on the academic-integrity page; cleanup is genuinely unnecessary for most labs (they write to temp directories). Either add two short sections to 32 briefs or amend the contributor contract. | open |
| Medium | No lab-level version pins; reproducibility depends on the ranges in `requirements-labs.txt`. | open |
| Low | Module cards understated the lab count for 12 modules ("1 lab" where two exist). | **fixed** — cards now say "2 labs" |
| Low | The labs landing page listed 20 labs, all "Planned", with titles and module numbers that no longer matched the briefs. | **fixed** — catalogue regenerated from the 32 `LAB.md` files |
| Info | L26 exports an API key check with a hard-coded demo key. It is a local FastAPI test app with `httpx.ASGITransport`, never reachable from a network, and the key is the lesson's subject rather than a credential. | acceptable |

Nothing in the 32 labs requires a GPU, a cloud account, an API key or a download. Every one completes in under eleven seconds of CPU here.
