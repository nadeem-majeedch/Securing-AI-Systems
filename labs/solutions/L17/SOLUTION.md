# L17 — Solution: Tokens, context budget and the flat prompt

**Module:** M11  |  **Difficulty:** Beginner  |  **Time:** 50 minutes

## Approach

The solution tokenises with a small regex, assembles and prints the prompt, budgets components in trust order, then tests four encodings against a raw and an NFKC-normalised filter.

## Reference results

The prompt prints with `system:`, `user:` and `tool:` labels, but the model receives one sequence — the labels are tokens like any other. Under a 40-token budget the system rule is admitted in full and the free space is small. The raw filter catches **1 of 4** variants; after NFKC it catches **2 of 4**; the zero-width and soft-hyphen forms survive both.

## Why this works

A context window is a budget with a priority order, and every component competes for it. Text that is identical to a human reader is different byte sequences to a filter, so a phrase blocklist can only ever be one weak layer.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L17/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Everything is one token — your regex has no whitespace alternative.
- Filter catches all variants — you normalised first and forgot to report the raw result.
- Budget goes negative — clamp with `max(remaining, 0)`.
- Note text prints as `nan` — the column is empty for that row; pick another index.

## Marking rubric (100 marks)

- 30 marks — tokenisation and assembly correct.
- 30 marks — budget respects priority.
- 25 marks — bypass demonstrated and explained.
- 15 marks — design sentence is specific.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Roles are labels in the same sequence; the model has no privilege boundary.
- Budgets need priorities, or the untrusted component can crowd out the rule.
- Encoding is an evasion surface for every string filter.
