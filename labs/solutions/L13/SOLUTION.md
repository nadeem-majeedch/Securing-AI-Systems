# L13 — Solution: Two defences, two promises: adversarial training and a certificate

**Module:** M08  |  **Difficulty:** Challenge  |  **Time:** 120 minutes

## Approach

The solution trains both models on one split, evaluates with one PGD-5 attack, certifies 20 inputs with Clopper–Pearson bounds, and prints a four-column claim table. Assertions require the robustness gain and a minimum certification rate.

## Reference results

The standard model reaches **clean 0.836, robust 0.071**. Adversarial training reaches **clean 0.786, robust 0.234** — a large robustness gain at a 0.05 clean-accuracy cost. Randomised smoothing certifies **18 of 20** inputs with a **median radius of 0.254** in L2. The claim table therefore contains one empirical statement and one certified statement, with different scopes.

## Why this works

Adversarial training buys measured resistance to this attack family at this budget, and nothing more. Smoothing buys a guarantee about a smoothed classifier, in L2, for a radius that is often small. Neither justifies the word "robust" on its own; both justify a precise sentence.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L13/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- No inputs certify — sigma is too small relative to model uncertainty, or you used the wrong bound direction.
- Adversarial training destroys accuracy — the learning rate is too high or the inner attack too strong.
- Robust accuracy looks great — you evaluated with a weaker attack than you trained against.
- Certificate radius is huge — the lower bound used the point estimate instead of a confidence bound.

## Marking rubric (100 marks)

- 35 marks — both defences implemented correctly.
- 25 marks — evaluation uses one attack for both models.
- 25 marks — certificate computed with correct bounds.
- 15 marks — claims distinguish evidence from marketing.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Empirical robustness and certified robustness answer different questions.
- A defence is only as good as the attack used to measure it.
- The claim, not the adjective, is the deliverable.
