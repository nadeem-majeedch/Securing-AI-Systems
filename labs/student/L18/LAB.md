# L18 — Decoding determinism and the replayable incident

| | |
|---|---|
| **Module** | M11 |
| **Difficulty** | Intermediate |
| **Estimated time** | 60 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A customer saw an unacceptable answer and the team cannot reproduce it: the provider's model has been updated, the prompt template changed last week, and nobody logged the sampler settings. The incident review is stuck at "cannot reproduce".

## 2. Problem statement

Separate a fixed next-token distribution from the sampler, show how temperature and top-p change the outcome set, prove that a seed reproduces a path and not a promise, and specify the fields a replay needs.

## 3. Learning objectives

- Implement greedy, temperature and top-p sampling on one distribution.
- Measure outcome variability per sampler configuration.
- Explain why a seed is necessary but not sufficient.
- Write a replay-ready log schema.

## 4. Prerequisites

- L17 recommended.

## 5. Required software

- Python 3.12+
- NumPy
- pandas

## 6. Dataset and input files

- No dataset: a five-token distribution defined in the script.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L18/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L18/starter.py
```

1. Define logits for five tokens and a softmax.
2. Implement greedy, temperature sampling and top-p sampling.
3. Draw 200 samples per configuration and table distinct outcomes and top-token share.
4. Show that the same seed reproduces the same path.
5. Show that one extra random draw before sampling changes the path.
6. Assert greedy is deterministic and that higher temperature widens the outcome set.
7. Specify the log fields and what each one protects against.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L18/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

Greedy always returns `certainly` with **1 distinct** outcome. Temperature 0.2 gives **2 distinct** outcomes with a 0.995 top share, 0.7 gives **5 distinct** at 0.750, and 1.0 gives **5 distinct** at 0.630. Top-p 0.9 at T=1.0 gives **3 distinct**. The same seed reproduces the path; an extra draw before sampling changes it.

## 10. Interpretation of results

The model returns a distribution; the sampler decides what you see. Variability is a property of the configuration, not of the model's knowledge. Reproduction requires the path, so a seed alone is a label without the remaining parameters.

## 11. Student tasks

1. Report which configuration you would use for a regulated workflow and why.
2. Explain the difference between `distinct` and `top_share` in one sentence each.
3. Name three things outside the script that can change the sampled path.
4. Write the incident sentence that replaces "cannot reproduce".

## 12. Challenge exercises

1. Add beam search with width 3 and report the outcome set.
2. Show that a library upgrade can change a seeded path even with identical inputs.
3. Design a hash of the full generation record so two runs can be compared in one field.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Use `rng.choice(len(logits), p=probs)` — the multinomial draw is the sampler.
2. Guard against division by zero with `max(T, 1e-6)`.
3. `np.searchsorted` on the cumulative probability implements top-p.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L18/solution.py
labs/solutions/L18/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Greedy gives different answers — you are sampling, not taking `argmax`.
- `p` does not sum to 1 — the softmax was applied before subtracting the max.
- Every configuration gives the same result — you reuse one generator instead of seeding per run.
- Top-p returns 5 outcomes — the cumulative search is on unsorted probabilities.

## 16. Security lessons learned

- Determinism is a configuration property, not a model property.
- Variability must be measured, not assumed.
- A replay needs inputs, parameters and call order.

## 17. Submission requirements

- The completed script and the variability table.
- The incident sentence.
- The log-field table with justifications.
- Answers to the tasks.

## 18. Acceptable use

Study determinism on the five-token distribution defined in the script. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not attach the experiment to a hosted model or a paid API. There is nothing to download and no key to configure.

## 20. Data handling

No dataset: the probabilities are literal values written in the notebook.

## 21. Cleanup

Nothing is written. Delete sample logs you exported.

## 22. Restoring your environment

Nothing is installed; there is no service to stop.
