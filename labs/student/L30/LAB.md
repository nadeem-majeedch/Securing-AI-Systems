# L30 — Recovering from a compromised model

| | |
|---|---|
| **Module** | M19 |
| **Difficulty** | Challenge |
| **Estimated time** | 100 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A partner's bundle was deployed three weeks ago. The release check now reports a hash mismatch on its config. The model still answers, which is why nobody looked. The incident lead wants a recovery that can be defended line by line in the post-mortem.

## 2. Problem statement

Run recovery as five evidenced steps — detect, contain, rebuild, verify identity and behaviour, rotate — and prove the restored model matches the reference while the tampered one does not.

## 3. Learning objectives

- Detect a compromised artefact by hash.
- Preserve evidence while removing the artefact from service.
- Verify identity and behavioural parity separately.
- Record a sign-off that names what remains open.

## 4. Prerequisites

- L24 (bundle verification), L12 (evaluation discipline).

## 5. Required software

- Python 3.12+
- pandas
- hashlib

## 6. Dataset and input files

- `model_bundle/`, `model_bundle_tampered/` with manifests.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L30/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L30/starter.py
```

1. Verify the deployed copy against the clean manifest and list mismatches.
2. Copy the suspect bundle to a quarantine directory and record who did what.
3. Rebuild from the clean source and verify every hash.
4. Compare restored and tampered outputs with the reference on 20 fixed inputs.
5. Assert exact parity for the restored model and a measurable difference for the tampered one.
6. Fill the sign-off table, leaving the root cause open.
7. Write the post-mortem sentence about what recovery actually required.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L30/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

Detection lists **`config.json`** as the mismatched file while the weights and card still match. The rebuilt bundle verifies **3/3**. Behavioural parity is **0.0** maximum absolute difference for the restored model, while the tampered copy drifts measurably on the same inputs. The sign-off has four closed items and one open root cause.

## 10. Interpretation of results

A config-only tamper is the realistic case: the weights are untouched, the answers look normal, and the only signal is identity. That is why parity is checked against a reference, not against expectation — "it still answers" is exactly the property an attacker wants to preserve.

## 11. Student tasks

1. Explain why the tampered bundle's card still matching is a red herring.
2. Report what a config change could alter without touching weights.
3. State why the suspect copy is preserved rather than deleted.
4. Write the post-mortem sentence from instruction 7.

## 12. Challenge exercises

1. Add a signed manifest and describe how the key is distributed.
2. Add a canary input set that would catch a behaviour change before users do.
3. Write the rollback procedure for a bundle that fails parity.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Hash the file bytes, not the directory.
2. Quarantine is a copy plus a record; deleting destroys evidence.
3. Seed the parity harness from both weights and config so a config change is visible.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L30/solution.py
labs/solutions/L30/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Parity is zero for both bundles — the harness ignores config, so a config tamper is invisible.
- `FileNotFoundError` — resolve bundle paths through `data_path`.
- Quarantine copy already exists — the script is idempotent; check before copying.
- Sign-off has no open item — the root cause is not closed in the same run as recovery.

## 16. Security lessons learned

- Identity and behaviour are two different checks.
- An artefact that still works is not an artefact you can trust.
- Recovery ends with an owner for the cause, not with a green dashboard.

## 17. Submission requirements

- The completed script and runbook table.
- The parity results.
- The sign-off table.
- The post-mortem sentence.

## 18. Acceptable use

Recover the service from the tampered bundle using the clean copy and the manifest. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not rotate credentials, revoke keys or restore services on a real system. The recovery steps are rehearsed locally, and the bundle is synthetic.

## 20. Data handling

Both bundles are synthetic; the hashes in the manifests are the evidence, and they are not secrets.

## 21. Cleanup

Delete the restored copy directory and any recovery log you created.

## 22. Restoring your environment

No service is started permanently. If you launched one to rehearse recovery, stop it.
