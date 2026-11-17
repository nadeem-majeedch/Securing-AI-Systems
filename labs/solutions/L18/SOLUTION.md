# L18 — Solution: Decoding determinism and the replayable incident

**Module:** M11  |  **Difficulty:** Intermediate  |  **Time:** 60 minutes

## Approach

The solution builds one distribution and three decoders, measures 200 draws per configuration, then shows that seeding reproduces a path while an extra draw breaks it. A four-column table records the fields a replay needs.

## Reference results

Greedy always returns `certainly` with **1 distinct** outcome. Temperature 0.2 gives **2 distinct** outcomes with a 0.995 top share, 0.7 gives **5 distinct** at 0.750, and 1.0 gives **5 distinct** at 0.630. Top-p 0.9 at T=1.0 gives **3 distinct**. The same seed reproduces the path; an extra draw before sampling changes it.

## Why this works

The model returns a distribution; the sampler decides what you see. Variability is a property of the configuration, not of the model's knowledge. Reproduction requires the path, so a seed alone is a label without the remaining parameters.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L18/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Greedy gives different answers — you are sampling, not taking `argmax`.
- `p` does not sum to 1 — the softmax was applied before subtracting the max.
- Every configuration gives the same result — you reuse one generator instead of seeding per run.
- Top-p returns 5 outcomes — the cumulative search is on unsorted probabilities.

## Marking rubric (100 marks)

- 35 marks — decoders implemented correctly.
- 25 marks — variability measured and interpreted.
- 25 marks — seed limitation demonstrated.
- 15 marks — log schema is complete and justified.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Determinism is a configuration property, not a model property.
- Variability must be measured, not assumed.
- A replay needs inputs, parameters and call order.
