---
title: MP01 · Dataset integrity verification tool
description: Build a tool that decides whether a dataset is the one you think it is, and proves it on a tampered copy.
---

# MP01 · Dataset integrity verification tool

**After:** Modules 05 and 15 · **Effort:** 10 h · **Stack:** Python, SQLite, `hashlib`, `pytest`
**Deliverable:** A CLI that verifies a dataset against a manifest and explains every failure

## Scenario

A hospital's imaging team receives training data from three suppliers. Each delivery lands as a directory of files
with a CSV index. Nobody checks whether a delivery is the one that was described in the contract, and the last
delivery silently contained 4 % duplicate studies and one file that had been re-encoded.

Your job is to build the check that should have run before ingestion: a manifest, a verifier, and a report a data
owner can read.

## What you build

1. **Manifest builder.** Walk a dataset directory and emit a JSON (or SQLite) manifest containing, per file: a
   SHA-256 digest, byte size, row count where the file is tabular, and the declared label distribution for the
   split.
2. **Verifier.** Given a dataset and a manifest, report: missing files, extra files, digest mismatches, size
   mismatches and schema mismatches. Exit non-zero on any failure; print one line per failure with the path and
   the reason.
3. **Duplicate and leakage checks.** Detect exact duplicates by digest, near-duplicates by a cheap fingerprint
   (for example, a normalised row hash for tabular data), and records appearing in both the train and test splits.
4. **Provenance record.** A signed or hashed `provenance.json` that names the supplier, the delivery date, the
   manifest digest and the checker version — so that a later investigation can answer *what did we accept, and
   when?*
5. **Report.** A Markdown report with a verdict per check: pass, warn or fail, and the count behind each.

## Suggested structure

```text
integrity/
  manifest.py     build_manifest(path) -> dict
  verify.py       verify(path, manifest) -> list[Failure]
  fingerprint.py  near_duplicate_keys(rows) -> dict[str, int]
  cli.py          check | build | report
tests/
  test_verify.py
```

Keep `verify` a pure function over a directory and a manifest. The CLI is a thin wrapper; the tests call the
function. A tool whose logic lives in `argparse` callbacks cannot be tested and will not survive its first bug.

## Checkpoints

| # | Checkpoint | Hours | Evidence |
|---|---|---|---|
| 1 | Threat model and asset list | 1 | Two paragraphs: who could alter a delivery, what they gain, what you can detect |
| 2 | Manifest builder and verifier | 3 | Clean dataset verifies; deleted file, extra file and edited file each fail with a distinct reason |
| 3 | Duplicate and split-leak checks | 2 | A constructed dataset with a known duplicate rate; measured count matches |
| 4 | Provenance and report | 2 | A report for the tampered copy that a data owner could act on |
| 5 | Tests and decision note | 2 | Five tests, including an empty directory and a manifest for a different dataset |

## Deliverables

| Item | Format | Notes |
|---|---|---|
| Tool | Python package + CLI | Runs on a clean checkout with one command |
| Tests | `pytest` | At least five, including the tampered cases |
| Report | Markdown, generated | One per dataset: clean and tampered |
| Threat model | 300 words | Which failures are detectable, and which are not |
| Decision note | 200 words | What you would block on at ingestion, and what you would only warn about |

## Questions you must answer in the decision note

1. Which of your checks would catch a supplier who re-encoded every file, and which would not?
2. Digest matching proves the bytes; what proves the *labels* are the ones that were promised?
3. Your manifest is stored next to the dataset. What does that arrangement fail to protect against, and what is
   the cheapest fix?

## Rubric

Apply the [shared mini-project rubric](../guidance/rubrics.md#mini-project-rubric), with these two indicators:

| Extra indicator | Proficient | Exemplary |
|---|---|---|
| **Failure taxonomy** | Distinguishes missing, extra and modified files | Separates *cannot check* (bad manifest, unreadable file) from *checked and failed*, and never reports the first as a pass |
| **Label integrity** | Reports declared versus actual label counts | Explains why a digest cannot bind labels, and adds a distribution check with a stated tolerance |

## Extension challenges

1. Add a Merkle tree over the manifest so a single root hash can be published in a contract.
2. Add a `--since` mode that verifies only files changed after a date, and measure how much faster it is.
3. Design the check that would catch a supplier who replaces 1 % of images with visually similar ones, and state
   its cost.

## Boundaries

Work only with synthetic or fully de-identified data. Do not attempt to obtain real patient images, and do not
publish any dataset you did not create or receive with permission.
