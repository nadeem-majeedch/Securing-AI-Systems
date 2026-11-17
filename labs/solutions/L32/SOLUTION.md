# L32 — Solution: A release gate that reads evidence

**Module:** M20  |  **Difficulty:** Challenge  |  **Time:** 110 minutes

## Approach

The solution specifies eight gates with thresholds and directions, evaluates a complete evidence set and three failing variants, and asserts the release and block decisions. A governance table records what each evidence field is for.

## Reference results

The complete set — utility **0.839**, robust accuracy **0.234**, privacy **0.054**, injection ASR **0.00**, ACL **1.00**, integrity **1.00**, unauthorised allows **0.00**, coverage **1.00** — releases. Removing the ACL gate blocks with *evidence missing*; lowering robust accuracy to **0.07** blocks *below 0.15*; raising privacy leakage to **0.42** blocks *below 0.25*.

## Why this works

Three different failures produce three different reasons, which is the point: a reviewer can act on *evidence missing* differently from *below threshold*. The direction field is what stops a metric like leakage, where lower is better, from being read backwards under deadline pressure.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L32/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Complete evidence blocks — a threshold or direction is wrong for that metric.
- Missing evidence passes — you used `evidence.get(id, {}).get('value', 0)`.
- All blocks look the same — the reason is not including the rule.
- `KeyError` on evidence — check the gate id matches the evidence key.

## Marking rubric (100 marks)

- 35 marks — gate specification complete and directional.
- 30 marks — four evaluations correct with reasons.
- 20 marks — missing-evidence handling correct.
- 15 marks — claim statement is precise.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A gate is a set of declarations, not a score.
- Missing evidence is the most common real failure.
- A passing gate supports a specific claim, not a general assurance.
