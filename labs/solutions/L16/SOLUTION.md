# L16 — Solution: Extraction from a mock admissions API

**Module:** M10  |  **Difficulty:** Intermediate  |  **Time:** 80 minutes

## Approach

The solution trains the target, serves it through a counting mock API in three output modes, and fits substitutes at three budgets. Assertions pin the no-regression property and the recovery threshold, and the rounding run shows the cost of the cheapest product control.

## Reference results

The target scores about **0.83** on held-out rows. Extraction fidelity is **0.813** at 50 queries, **0.833** at 150 and **0.823** at 500 — a plateau, because the substitute is already as good as its query distribution allows. At 150 queries, probabilities give **0.833** and labels **0.800**; rounding gives **0.823**.

## Why this works

Fidelity saturates rather than climbing forever: after the substitute captures the boundary, extra queries buy little. That plateau is the defender's lever — a quota below it makes extraction expensive. The output-format gap is real but modest here because the model is simple; it widens on harder targets.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L16/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Fidelity near 0.5 — the query distribution misses the region where the boundary lives.
- `Unknown label type: continuous` — you passed probabilities to a classifier; use ridge.
- Counter never increments — you call the model directly instead of the API wrapper.
- Budget comparison uses different test rows — fix the evaluation set once.

## Marking rubric (100 marks)

- 35 marks — extraction implemented and measured on held-out data.
- 25 marks — output-format comparison is fair.
- 25 marks — plateau explained in terms of query distribution.
- 15 marks — recommendation is specific and costed.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Extraction cost is measured in queries, not in effort.
- Output granularity and quotas are cheaper than detection.
- A fidelity plateau is the number a quota should be set against.
