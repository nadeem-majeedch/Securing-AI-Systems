# L24 — Solution: A malicious dependency and a tampered model bundle

**Module:** M15  |  **Difficulty:** Beginner  |  **Time:** 60 minutes

## Approach

The solution audits the requirements list, hashes both bundles against their manifests, and implements a format policy that refuses executable serialisation. Assertions require the clean bundle to pass and the tampered one to fail.

## Reference results

The audit finds **4 of 6** entries not pinned to an exact version, including one VCS install. The clean bundle matches **3/3**; the tampered bundle matches **1/3** — `config.json` and `model.safetensors` differ while the model card still matches. The format policy accepts safetensors and refuses pickle.

## Why this works

The model card matching is the instructive detail: a tampered bundle usually keeps its documentation. The hash check is what distinguishes the two, and it is only meaningful against a manifest you trust from a separate channel. Refusing pickle removes a whole class of incidents before any weights load.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L24/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- `KeyError` slicing a dict — you used `expected[:12]` on the manifest entry; take `['sha256']` first.
- Everything mismatches — you are hashing the directory instead of the files.
- Tampered bundle verifies — you compared the wrong manifest or the wrong directory.
- `load_safely` never raises — no bundle in the run contains a pickle; test the policy with a temporary file.

## Marking rubric (100 marks)

- 30 marks — dependency audit correct.
- 35 marks — hash verification implemented and differentiated.
- 20 marks — format policy and rationale correct.
- 15 marks — release decision is specific.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A hash answers what you have; a lockfile answers what you asked for.
- Documentation is not integrity evidence.
- Refusing unsafe formats is cheaper than scanning them.
