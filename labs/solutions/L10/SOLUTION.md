# L10 — Solution: Poisoning a fraud model with flipped labels

**Module:** M07  |  **Difficulty:** Intermediate  |  **Time:** 75 minutes

## Approach

The solution splits once, trains a deep tree, and repeats the flip-and-retrain loop for four rates. It then appends 40 structured-payment rows labelled legitimate and probes that pattern, asserting both the aggregate drop and the targeted miss rate.

## Reference results

Clean accuracy is **0.839**. Flipping 5 % of labels drops it to **0.763**, 10 % to **0.735** and 20 % to **0.683**. The targeted poison makes **20 of 20** structuring probes look legitimate, while global accuracy falls by only 0.156.

## Why this works

Label noise is not random damage: a tree memorises the flipped rows and then generalises the wrong rule into the region around them. The targeted case is worse than the aggregate suggests — the model is wrong exactly where the attacker wants it to be, and the accuracy number still looks publishable.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L10/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Accuracy improves with poisoning — you flipped labels in the test set too.
- No effect at 5 % — a shallow tree or a linear model averages the noise away; keep the tree deep.
- Probes all classified legitimate even before poisoning — the pattern is unlike the training data; compare with the clean model.
- Recall computed as a count — divide by the number of true frauds.

## Marking rubric (100 marks)

- 40 marks — sweep is measured on a clean test set with a fixed split.
- 25 marks — targeted poisoning demonstrated and quantified.
- 20 marks — explanation distinguishes memorisation from noise averaging.
- 15 marks — slice metric is specific and would catch the case.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A model that can memorise can be taught a lie with very few rows.
- Global accuracy is the wrong gate for targeted poisoning.
- Label provenance is a data-control problem, not a modelling problem.
