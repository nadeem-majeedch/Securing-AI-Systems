# L03 — Solution: Dataset integrity: hash manifests, tamper detection and MACs

**Module:** M03  |  **Difficulty:** Beginner  |  **Time:** 45 minutes

## Approach

The solution keeps the original read-only, hashes a scratch copy, edits one field through the `csv` module, and shows both checks. The assertions encode the lesson: the naive digest comparison fails after the edit, and the MAC rejects the forged digest.

## Reference results

The digest is 64 hex characters and verification prints `True`. After changing referral R0000's triage from `green` to `red`, verification prints `False`. The attacker-supplied manifest *does* match the tampered file (the naive check is fooled), while the MAC comparison prints `False`.

## Why this works

A hash answers "is this the file I approved". It cannot answer "who sent it", because anyone can recompute a hash. The MAC adds a shared secret; only someone holding the key can produce a valid tag. Neither is a backup, and neither helps if the key sits in the same repository as the data.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L03/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Digest differs between runs — you are hashing a path name or a timestamp, not the bytes.
- `PermissionError` on cleanup — close the file handles before `rmtree`.
- Verification still `True` after editing — your edit did not change bytes (same value written back).
- MAC never matches — encode the digest consistently (`utf-8`) on both sides.

## Marking rubric (100 marks)

- 35 marks — correct digest, manifest and verification.
- 25 marks — the edit is detected and explained.
- 25 marks — MAC demonstrated and the integrity/authenticity distinction stated correctly.
- 15 marks — ingestion check is concrete and fails closed.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Hashes give integrity; MACs and signatures give integrity plus authenticity.
- An integrity check that nobody enforces is documentation, not a control.
- The manifest is part of the attack surface: store it where the data supplier cannot rewrite it.
