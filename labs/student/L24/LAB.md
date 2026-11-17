# L24 — A malicious dependency and a tampered model bundle

| | |
|---|---|
| **Module** | M15 |
| **Difficulty** | Beginner |
| **Estimated time** | 60 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A team receives a model bundle from a partner and a requirements file from a contractor. The bundle loads fine, the demo works, and the release is scheduled for Friday. The security review asks for the hash check and the dependency diff, and neither exists.

## 2. Problem statement

Audit a dependency list for unpinned and VCS installs, verify a model bundle against its manifest, detect the tampered copy, and implement a format policy that refuses pickle.

## 3. Learning objectives

- Identify supply-chain risk in a requirements list.
- Verify artefacts by hash against a manifest.
- Explain why deserialisation is code execution.
- Write the gates that belong before the first import.

## 4. Prerequisites

- None beyond Python basics.

## 5. Required software

- Python 3.12+
- pandas
- hashlib

## 6. Dataset and input files

- `labs/datasets/model_bundle/` — config, model card and safetensors plus `manifest.json`.
- `labs/datasets/model_bundle_tampered/` — the same bundle with modified files.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L24/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L24/starter.py
```

1. Audit the six-line requirements list: pinned, range, VCS.
2. Hash every file in the clean bundle and compare with the manifest.
3. Repeat for the tampered bundle and record which files fail.
4. Assert the clean bundle verifies and the tampered one does not.
5. Implement `load_safely` that refuses pickle, `.pt` and `.bin`.
6. Run it on the clean bundle and on a bundle containing a `.pkl`.
7. Table the four release gates and what each blocks.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L24/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The audit finds **4 of 6** entries not pinned to an exact version, including one VCS install. The clean bundle matches **3/3**; the tampered bundle matches **1/3** — `config.json` and `model.safetensors` differ while the model card still matches. The format policy accepts safetensors and refuses pickle.

## 10. Interpretation of results

The model card matching is the instructive detail: a tampered bundle usually keeps its documentation. The hash check is what distinguishes the two, and it is only meaningful against a manifest you trust from a separate channel. Refusing pickle removes a whole class of incidents before any weights load.

## 11. Student tasks

1. Report which dependency is riskiest and why.
2. Explain what an attacker gains from a tampered `config.json`.
3. State why a manifest must not travel inside the bundle alone.
4. Write the Friday release decision in three sentences.

## 12. Challenge exercises

1. Add a signature check over the manifest and describe the key distribution problem.
2. Show how a typosquatted package name would appear in the audit.
3. Design a CI job that fails the build on any unpinned direct dependency.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. `hashlib.sha256(path.read_bytes()).hexdigest()` is enough here.
2. Manifest values are dicts with a `sha256` key, not strings.
3. Compare prefixes only for display; compare full digests for the decision.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L24/solution.py
labs/solutions/L24/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- `KeyError` slicing a dict — you used `expected[:12]` on the manifest entry; take `['sha256']` first.
- Everything mismatches — you are hashing the directory instead of the files.
- Tampered bundle verifies — you compared the wrong manifest or the wrong directory.
- `load_safely` never raises — no bundle in the run contains a pickle; test the policy with a temporary file.

## 16. Security lessons learned

- A hash answers what you have; a lockfile answers what you asked for.
- Documentation is not integrity evidence.
- Refusing unsafe formats is cheaper than scanning them.

## 17. Submission requirements

- The completed script and the three tables.
- The Friday release decision.
- Answers to the tasks.
- One paragraph on the residual risk after all four gates.

## 18. Acceptable use

Inspect `model_bundle/` and `model_bundle_tampered/`, and load only the data-only format. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not load a pickle or a `weights_only=False` checkpoint from an untrusted source, and do not `pip install` the `git+https://example.invalid/...` requirement: it is a non-routable teaching string, not a package.

## 20. Data handling

Both bundles are generated locally with fixed contents; the tampered copy differs only in files the manifest covers.

## 21. Cleanup

Delete any extracted archive, temporary virtual environment or copied bundle you created for the experiment.

## 22. Restoring your environment

If you created a throwaway environment to test the malicious requirement, delete it (`rm -rf .venv-test`) so it cannot be reactivated by accident.
