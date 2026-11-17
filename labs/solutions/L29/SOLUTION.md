# L29 — Solution: Triaging suspicious usage in an AI service

**Module:** M17  |  **Difficulty:** Intermediate  |  **Time:** 65 minutes

## Approach

The solution aggregates five features per principal, scores four with robust z-scores, ranks, and asserts that the incident is first with at least two signals. A triage-note table completes the case.

## Reference results

`user-13` ranks first with **multiple signals above 3** — a 401 rate near 1.0 in its burst window, **16 export calls**, and a byte total several times any honest principal. The next four principals have scores below the incident and at most one signal each.

## Why this works

Robust z-scores matter here because one principal's 15 KB total would inflate a mean and hide everyone else. Requiring two signals is what keeps a broken client from being escalated: one failed metric is a bug, two together is a pattern.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L29/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Division by zero — MAD can be 0 for a constant signal; add a small epsilon.
- The incident is not first — exports and bytes are usually the strongest signals; check they are included.
- Scores are negative — you forgot to clip at zero before summing.
- `dt` accessor fails — parse `ts` before aggregating.

## Marking rubric (100 marks)

- 35 marks — score implemented transparently.
- 30 marks — incident surfaced with corroboration.
- 20 marks — triage note complete.
- 15 marks — limitations stated accurately.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A transparent score can be argued with; a model's score cannot.
- Corroboration is the difference between a case and a nuisance.
- Triage notes state hypotheses, not verdicts.
