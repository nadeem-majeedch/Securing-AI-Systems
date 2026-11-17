# L06 — Solution: Intake validation and quarantine for a dirty referral feed

**Module:** M05  |  **Difficulty:** Beginner  |  **Time:** 50 minutes

## Approach

The solution validates each row with six independent checks, returns at the first injection marker, and builds the two partitions. The reason histogram and the id list are printed, and the assertions pin both the partition property and the specific defects.

## Reference results

**236 rows are accepted and 4 are quarantined**: two `instruction-like text in note`, one `age out of range`, and one `triage has surrounding whitespace`. The quarantined ids are R0007, R0011, R0042 and R0150.

## Why this works

Quarantine keeps the evidence. A cleaned row would have hidden the injection attempt; a dropped row would have hidden the supplier's bug. The reason column is the communication channel to the data supplier, and the partition assertion is what makes silent data loss impossible.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L06/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Accepted + quarantined is less than the input — a branch appends to neither list.
- All rows quarantined — the source allowlist compares against the wrong case.
- The padded row is accepted — you stripped before comparing and never recorded the padding.
- Empty quarantine — the injection markers are capitalised in your tuple but not lowered.

## Marking rubric (100 marks)

- 40 marks — validators cover the six rules and reasons are specific.
- 25 marks — partition asserted, nothing silently dropped.
- 20 marks — quarantine table and supplier message are actionable.
- 15 marks — answers distinguish validation from cleaning.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Rejecting with a reason is a control; cleaning silently is a cover-up.
- The partition property (accept + quarantine = input) is a cheap, strong test.
- Instruction-like text belongs in quarantine, not in a normalised pipeline.
