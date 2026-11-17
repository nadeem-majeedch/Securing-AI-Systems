# L03 — Dataset integrity: hash manifests, tamper detection and MACs

| | |
|---|---|
| **Module** | M03 |
| **Difficulty** | Beginner |
| **Estimated time** | 45 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A referral extract is transferred nightly from a partner hospital. Last month a row was edited in transit and nobody noticed for a week. The data engineering lead wants a manifest that makes any change visible, and an answer to the obvious follow-up: what stops the sender rewriting the manifest as well?

## 2. Problem statement

Build a SHA-256 manifest for the extract, verify it, change exactly one field and show that verification fails. Then add an HMAC over the digest and show that a forged manifest cannot pass.

## 3. Learning objectives

- Compute and verify a SHA-256 digest over a data file.
- Explain why a digest detects edits but not authorship.
- Add an HMAC and explain the difference between integrity and authenticity.
- Design the ingestion check that fails the pipeline on mismatch.

## 4. Prerequisites

- Module 03 lecture; L01 recommended.

## 5. Required software

- Python 3.12+ (standard library only)

## 6. Dataset and input files

- `labs/datasets/referrals.csv` — copied into a scratch directory before any edit.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L03/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L03/starter.py
```

1. Copy the dataset into a `tempfile.mkdtemp()` directory; never edit the original.
2. Compute its SHA-256 digest with a chunked read and store a manifest with size and digest.
3. Verify the file against the manifest and print the result.
4. Change one triage value using the `csv` module, then verify again.
5. Compute an HMAC over the digest with a demo key and attempt to validate a forged manifest.
6. Assert that the file fails verification after the edit and that the MAC does not validate the forgery.
7. Remove the scratch directory at the end.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L03/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The digest is 64 hex characters and verification prints `True`. After changing referral R0000's triage from `green` to `red`, verification prints `False`. The attacker-supplied manifest *does* match the tampered file (the naive check is fooled), while the MAC comparison prints `False`.

## 10. Interpretation of results

A hash answers "is this the file I approved". It cannot answer "who sent it", because anyone can recompute a hash. The MAC adds a shared secret; only someone holding the key can produce a valid tag. Neither is a backup, and neither helps if the key sits in the same repository as the data.

## 11. Student tasks

1. Record the digest before and after the edit and state how many hex characters differ.
2. Change one character inside the header row and report whether verification fails.
3. Explain why the manifest should be stored separately from the file it describes.
4. Write the three lines of an ingestion job that refuses to proceed on mismatch.

## 12. Challenge exercises

1. Replace the HMAC with an Ed25519-style signature design (description and code sketch, no crypto library needed).
2. Design a manifest that covers a bundle of five files and detects a deleted file, not just an edited one.
3. Add a timestamp and explain what replay protection it does and does not give you.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Read the file in binary mode; text mode can normalise line endings and change the digest.
2. `hmac.compare_digest(a, b)` avoids timing leaks; do not compare tags with `==` in production code.
3. `csv.reader`/`csv.writer` preserve the row structure better than string replacement.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L03/solution.py
labs/solutions/L03/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Digest differs between runs — you are hashing a path name or a timestamp, not the bytes.
- `PermissionError` on cleanup — close the file handles before `rmtree`.
- Verification still `True` after editing — your edit did not change bytes (same value written back).
- MAC never matches — encode the digest consistently (`utf-8`) on both sides.

## 16. Security lessons learned

- Hashes give integrity; MACs and signatures give integrity plus authenticity.
- An integrity check that nobody enforces is documentation, not a control.
- The manifest is part of the attack surface: store it where the data supplier cannot rewrite it.

## 17. Submission requirements

- The completed script and the two verification lines.
- A paragraph distinguishing integrity from authenticity, using your own output.
- The ingestion-job snippet from task 4.
- Answers to the remaining tasks.

## 18. Acceptable use

Modify only the scratch copy the script makes. The exercise is about detecting exactly that kind of edit, so editing the original would destroy the lesson. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Never edit `labs/datasets/referrals.csv` itself, and do not apply the manifest or MAC workflow to files you do not own — a manifest you cannot verify is not evidence.

## 20. Data handling

Synthetic referrals plus a manifest of digests. A digest is not a secret, but the HMAC key in the script is a teaching fixture and must not be reused anywhere else.

## 21. Cleanup

Delete the scratch directory the solution creates (its path is printed) and any `manifest.json` you generated. Check with `git status` that the dataset file is unchanged.

## 22. Restoring your environment

No packages are installed. Remove files you wrote into the lab folder before moving on.
