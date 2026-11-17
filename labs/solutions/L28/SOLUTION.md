# L28 — Solution: A red-team matrix and a coverage statement

**Module:** M18  |  **Difficulty:** Advanced  |  **Time:** 90 minutes

## Approach

The solution defines six cell functions over the existing datasets, builds a matrix with evidence, severity and owner, and pairs every tested case with an untested variant.

## Reference results

**6 of 6** cells reproduce on the mock, including **2 cross-tenant tool calls** for bob, **28 export calls**, and a tampered bundle with three manifest entries. Every row names a control, and the coverage table lists six untested variants, from multi-turn escalation to a malicious manifest with matching hashes.

## Why this works

The matrix's value is the third and fifth columns, not the second: a reproduced cell with a named control is a managed risk, and a cell with a stated gap is an honest one. A green tick with no evidence is worse than a red cell with an owner.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L28/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- `FileNotFoundError` for the tampered manifest — resolve it through `data_path`.
- Every cell reproduces — the mocks are permissive by design; that is the point.
- Coverage table shorter than the matrix — every cell needs a limitation row.
- Severity all equal — the ordering map is not being applied.

## Marking rubric (100 marks)

- 35 marks — six cells with real evidence.
- 25 marks — severity and ownership assigned.
- 25 marks — coverage statement complete.
- 15 marks — committee sentence is defensible.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Evidence beats ticks.
- Coverage statements are how an exercise stays honest.
- A control with an owner is a managed risk; a control with none is a wish.
