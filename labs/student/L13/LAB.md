# L13 — Two defences, two promises: adversarial training and a certificate

| | |
|---|---|
| **Module** | M08 |
| **Difficulty** | Challenge |
| **Estimated time** | 120 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

The team must choose a defence for the routing model before launch. One engineer wants adversarial training because it is standard; another wants randomised smoothing because it comes with a certificate. The product owner asks which one lets her write "robust" on the model card.

## 2. Problem statement

Train an adversarially trained model, certify a smoothed classifier on a sample of inputs, and produce a claim table that pairs each defence with the evidence it generates and the statement it forbids.

## 3. Learning objectives

- Implement adversarial training with an inner PGD loop.
- Certify predictions with a binomial lower bound.
- Compare empirical and certified robustness fairly.
- Refuse a claim the evidence does not support.

## 4. Prerequisites

- L08, L12 (attacks and PGD).

## 5. Required software

- Python 3.12+
- PyTorch (CPU)
- SciPy
- pandas

## 6. Dataset and input files

- `labs/datasets/digits_subset.npz`.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L13/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L13/starter.py
```

1. Load digits and define one training routine and one PGD evaluation attack.
2. Train the standard model and record clean and robust accuracy.
3. Train with adversarial training: PGD-3 inside the loop, 6 epochs, epsilon 0.2.
4. Evaluate both models with the same PGD-5 attack and report clean/robust accuracy.
5. Implement randomised smoothing at sigma 0.15 with 100 samples per input and certify 20 test inputs.
6. Build the claim table: defence, evidence, may claim, may not claim.
7. Assert adversarial training improves robust accuracy and that at least half the inputs certify.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L13/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The standard model reaches **clean 0.836, robust 0.071**. Adversarial training reaches **clean 0.786, robust 0.234** — a large robustness gain at a 0.05 clean-accuracy cost. Randomised smoothing certifies **18 of 20** inputs with a **median radius of 0.254** in L2. The claim table therefore contains one empirical statement and one certified statement, with different scopes.

## 10. Interpretation of results

Adversarial training buys measured resistance to this attack family at this budget, and nothing more. Smoothing buys a guarantee about a smoothed classifier, in L2, for a radius that is often small. Neither justifies the word "robust" on its own; both justify a precise sentence.

## 11. Student tasks

1. Report the clean-accuracy cost of adversarial training and the robustness gain per point spent.
2. Change sigma to 0.30 and report the certification rate and median radius.
3. Explain why a certificate for the smoothed classifier does not transfer to the base model.
4. Write the two sentences for the model card, one per defence.

## 12. Challenge exercises

1. Weaken the inner attack to one step and show that robustness measured by PGD-5 collapses.
2. Attack the smoothed classifier with 200-sample PGD and report whether any certified input changes.
3. Recommend one defence for a 50 ms latency budget and justify it with your measurements.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. The inner attack is part of training; a cheap PGD-3 is the usual compromise.
2. For the certificate, use a lower bound for the top class and an upper bound for the runner-up.
3. Report coverage, radius and sigma together; any two of them can mislead.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L13/solution.py
labs/solutions/L13/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- No inputs certify — sigma is too small relative to model uncertainty, or you used the wrong bound direction.
- Adversarial training destroys accuracy — the learning rate is too high or the inner attack too strong.
- Robust accuracy looks great — you evaluated with a weaker attack than you trained against.
- Certificate radius is huge — the lower bound used the point estimate instead of a confidence bound.

## 16. Security lessons learned

- Empirical robustness and certified robustness answer different questions.
- A defence is only as good as the attack used to measure it.
- The claim, not the adjective, is the deliverable.

## 17. Submission requirements

- The completed script and the claim table.
- The model-card sentences from task 4.
- The latency recommendation from challenge 3 with numbers.
- Answers to the remaining tasks.

## 18. Acceptable use

Compare adversarial training and a randomised-smoothing certificate on the local digits model. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

The robustness number you produce is a claim about this model, this data and this budget. Do not present it as a property of a real product, and do not run the training loop on shared compute without checking the quota.

## 20. Data handling

A synthetic split of the third-party digits extract; no personal data is involved.

## 21. Cleanup

Delete trained checkpoints and certificate tables you saved; training output otherwise stays in memory.

## 22. Restoring your environment

Nothing is installed. If you switched to a GPU build for speed, keep it.
