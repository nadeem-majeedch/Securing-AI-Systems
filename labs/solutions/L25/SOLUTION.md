# L25 — Solution: A poisoned fine-tuning run and the pattern scan

**Module:** M16  |  **Difficulty:** Advanced  |  **Time:** 85 minutes

## Approach

The solution trains a base model, poisons 20 of 400 fine-tuning rows with a corner patch, measures clean accuracy and ASR, then finds the rows with a patch-intensity scan and refits without them.

## Reference results

The fine-tuned model keeps **clean accuracy 0.882** and reaches **patch ASR 1.000**; the base model's ASR on the same patch is near its natural rate for class 0. The patch scan flags **24 rows** with **precision 1.00 and recall 1.00**. After removal, ASR falls to **0.100** with clean accuracy **0.884**.

## Why this works

Twenty rows out of 420 were enough because the patch is a perfect feature in the fine-tuning set. The scan works only because the trigger is visible in the data — a subtle, in-range trigger would not produce an intensity outlier, which is why provenance and a held-out trigger sweep are separate controls.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L25/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- ASR is 0 — you patched the test set but labelled the poison with its original class.
- Clean accuracy collapses — the fine-tuning pool is too small or the poison fraction too high.
- Scan flags everything — you computed the threshold on the poisoned set itself.
- `ValueError` on reshape — flatten with `reshape(len(X), -1)`.

## Marking rubric (100 marks)

- 35 marks — poison installed and both metrics measured.
- 30 marks — scan evaluated with precision and recall.
- 20 marks — refit result reported.
- 15 marks — limits of the scan stated.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A backdoor costs almost no clean accuracy.
- Detection is easiest at the data layer, before the model exists.
- Fine-tuning data needs the same review as training data.
