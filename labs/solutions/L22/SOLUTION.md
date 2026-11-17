# L22 — Solution: An ACL test suite for a RAG index

**Module:** M13  |  **Difficulty:** Advanced  |  **Time:** 80 minutes

## Approach

The solution implements a correct and a deliberately buggy index, writes nine named assertions, and shows 9/9 against 7/9. The aggregate deleted-id test exists precisely because a per-query test missed the post-filter path.

## Reference results

The correct index passes **9/9**. The buggy index passes **7/9**, failing *deleted document never returned* and *deleted id absent from every tenant's results* — b2 stays retrievable for beta after deletion.

## Why this works

Deletion is the failure mode teams forget: the row is gone from the source system but the index still holds embeddings and text. A suite makes that a red build instead of an incident. What it cannot check is whether the ACL value attached at ingestion was right — that is a data-quality control.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L22/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Both indexes pass everything — the buggy path still filters `deleted`; remove that condition.
- Both fail — the correct index kept a deleted row in the matrix.
- Cross-tenant test passes trivially — the query does not match any foreign document; check the query.
- `k` test always passes — you never request more than the corpus size.

## Marking rubric (100 marks)

- 40 marks — nine meaningful tests, correctly written.
- 30 marks — correct and buggy indexes differentiated by evidence.
- 20 marks — residual risk stated accurately.
- 10 marks — release-gate sentence is usable.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Access control is testable; make it a release gate.
- Deletion is part of the ACL, not a data-cleaning afterthought.
- A suite documents intent as well as catching regressions.
