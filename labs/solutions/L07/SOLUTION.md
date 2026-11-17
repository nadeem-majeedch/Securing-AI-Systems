# L07 — Solution: De-identification and linkage risk in a patient extract

**Module:** M05  |  **Difficulty:** Intermediate  |  **Time:** 70 minutes

## Approach

The solution drops direct identifiers, measures k, performs a candidate-count linkage, then generalises age to ten-year bands and suppresses groups below five. Re-running the same linkage shows zero single-candidate rows at a cost of 46 suppressed records.

## Reference results

The exact extract has **minimum k = 1**, with about 60 % of groups containing a single row; **253 of 600 rows resolve to exactly one person**. After generalisation and suppression, **554 rows remain**, the minimum group size is 5, and **0 rows resolve to a single person**.

## Why this works

Generalisation lowers precision; suppression removes the remainder. Together they cost 46 rows (7.7 %) and stop the single-join re-identification. They do not make disclosure impossible — a determined attacker with extra data can still narrow groups — so the result is risk reduction with a measured cost, not anonymity as a property.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L07/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- `KeyError: 'age'` — you dropped the column before generalising; band first, drop later.
- Rows with one candidate after suppression — you suppressed before generalising.
- Matched rows exceed published rows — the merge fanned out; deduplicate names before merging.
- Minimum k still 1 — your band is applied to a copy that is not used downstream.

## Marking rubric (100 marks)

- 35 marks — k-anonymity computed and interpreted correctly.
- 30 marks — linkage attack implemented and re-run after protection.
- 20 marks — utility cost quantified.
- 15 marks — privacy notice is accurate and free of overclaiming.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Removing names is not de-identification.
- k-anonymity is a measurable target, and it has a utility price you must state.
- Linkage needs no secret: public lists plus quasi-identifiers are enough.
