# L22 — An ACL test suite for a RAG index

| | |
|---|---|
| **Module** | M13 |
| **Difficulty** | Advanced |
| **Estimated time** | 80 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

The retrieval fix from the previous review has been merged. The release manager will not accept "looks fine" as evidence and wants a suite that fails if the index regresses — including the case where a document is deleted but still retrievable.

## 2. Problem statement

Write nine executable access-control tests, run them against a correct index and a plausible buggy one, and state which failures the suite cannot catch.

## 3. Learning objectives

- Express access-control requirements as tests.
- Cover cross-tenant, deletion and completeness faults.
- Distinguish a passing implementation from a failing one by evidence.
- State the residual risk a test suite cannot cover.

## 4. Prerequisites

- L21.

## 5. Required software

- Python 3.12+
- scikit-learn
- pandas

## 6. Dataset and input files

- Four in-script documents across two tenants, one soft-deleted.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L22/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L22/starter.py
```

1. Build a four-document corpus with a `deleted` flag and one cross-tenant pair.
2. Implement a correct index: drop deleted rows, filter candidates by tenant before ranking.
3. Implement a buggy index: post-filter by tenant but ignore deletion.
4. Write nine named tests covering the requirements in the brief.
5. Run the suite against both indexes and print pass counts.
6. Assert the correct index passes all nine and the buggy one fails at least two.
7. State the failure the suite cannot detect.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L22/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The correct index passes **9/9**. The buggy index passes **7/9**, failing *deleted document never returned* and *deleted id absent from every tenant's results* — b2 stays retrievable for beta after deletion.

## 10. Interpretation of results

Deletion is the failure mode teams forget: the row is gone from the source system but the index still holds embeddings and text. A suite makes that a red build instead of an incident. What it cannot check is whether the ACL value attached at ingestion was right — that is a data-quality control.

## 11. Student tasks

1. Add a tenth test for a document whose tenant field is missing.
2. Explain why the buggy index still leaks nothing across tenants in your run.
3. Report which two tests caught the deletion bug and why both were needed.
4. Write the release-gate sentence that references the suite.

## 12. Challenge exercises

1. Add a latency assertion and show how a full scan would fail it.
2. Simulate re-ingestion of a deleted document and show which test fires.
3. Extend the suite to cover a third tenant with no documents.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Collect results as rows with `test`, `pass`, `detail`; the detail matters when a test fails.
2. Aggregate deleted-id checks across tenants to catch post-filter paths.
3. The correct index must drop deleted rows before building the matrix.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L22/solution.py
labs/solutions/L22/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Both indexes pass everything — the buggy path still filters `deleted`; remove that condition.
- Both fail — the correct index kept a deleted row in the matrix.
- Cross-tenant test passes trivially — the query does not match any foreign document; check the query.
- `k` test always passes — you never request more than the corpus size.

## 16. Security lessons learned

- Access control is testable; make it a release gate.
- Deletion is part of the ACL, not a data-cleaning afterthought.
- A suite documents intent as well as catching regressions.

## 17. Submission requirements

- The completed script with nine tests.
- The two pass-count reports.
- The tenth test from task 1.
- The release-gate sentence.

## 18. Acceptable use

Run the suite against the four in-script documents and the two synthetic tenants. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not point the suite at a production retrieval service. Its value is as a build-time test that fails closed, not as a live probe.

## 20. Data handling

Documents and tenants are invented, and the soft-deleted record is a fixture. No customer content is involved.

## 21. Cleanup

No artefacts are produced. Delete any test report you exported.

## 22. Restoring your environment

Nothing is installed; nothing is left running.
