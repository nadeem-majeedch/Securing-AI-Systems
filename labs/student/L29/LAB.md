# L29 — Triaging suspicious usage in an AI service

| | |
|---|---|
| **Module** | M17 |
| **Difficulty** | Intermediate |
| **Estimated time** | 65 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

The gateway team can see every request and has no process for looking at them. An analyst is asked to produce a ranked list of principals worth investigating and a note for each, starting from three hours of logs and no labels.

## 2. Problem statement

Score principals with robust z-scores over four behavioural signals, rank them, and write a triage note that states the hypothesis and the next step without asserting intent.

## 3. Learning objectives

- Build a transparent multi-signal score.
- Use robust statistics so one outlier does not define the scale.
- Require corroboration before opening a case.
- Write a triage note that separates evidence from hypothesis.

## 4. Prerequisites

- L27.

## 5. Required software

- Python 3.12+
- pandas
- NumPy

## 6. Dataset and input files

- `labs/datasets/api_logs.csv` — three hours of gateway logs, unlabelled.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L29/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L29/starter.py
```

1. Aggregate per principal: requests, 401 rate, exports, bytes out, off-hours count.
2. Compute median/MAD z-scores for four signals.
3. Sum clipped positive z-scores and count signals above 3.
4. Rank principals and table the top five.
5. Assert the incident principal ranks first and fires on at least two signals.
6. Fill the triage note: principal, first seen, evidence, hypothesis, next step.
7. State what the score cannot establish.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L29/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

`user-13` ranks first with **multiple signals above 3** — a 401 rate near 1.0 in its burst window, **16 export calls**, and a byte total several times any honest principal. The next four principals have scores below the incident and at most one signal each.

## 10. Interpretation of results

Robust z-scores matter here because one principal's 15 KB total would inflate a mean and hide everyone else. Requiring two signals is what keeps a broken client from being escalated: one failed metric is a bug, two together is a pattern.

## 11. Student tasks

1. Explain why the score uses clipped positive z-scores rather than raw sums.
2. Report what a single legitimate bulk export would look like in the ranking.
3. Write the escalation criteria you would give an on-call analyst.
4. State the two things the score cannot tell you.

## 12. Challenge exercises

1. Add a time-of-day baseline per principal and report which signals survive.
2. Add a false-positive check using a week of clean logs and report the ranking.
3. Design a weekly review process that closes stale cases.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. MAD z-score: `0.6745 * (x - median) / MAD`; the factor here is folded into 1.4826.
2. Clip at zero so good behaviour does not offset bad behaviour.
3. Off-hours is a weak signal on its own; keep it out of the score if it does not separate.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L29/solution.py
labs/solutions/L29/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Division by zero — MAD can be 0 for a constant signal; add a small epsilon.
- The incident is not first — exports and bytes are usually the strongest signals; check they are included.
- Scores are negative — you forgot to clip at zero before summing.
- `dt` accessor fails — parse `ts` before aggregating.

## 16. Security lessons learned

- A transparent score can be argued with; a model's score cannot.
- Corroboration is the difference between a case and a nuisance.
- Triage notes state hypotheses, not verdicts.

## 17. Submission requirements

- The completed script and the ranked table.
- The triage note.
- The escalation criteria.
- Answers to the tasks.

## 18. Acceptable use

Analyse `api_logs.csv` and write triage notes against the unlabelled events. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not use a real gateway log, and do not treat the synthetic principal identifiers as personal data or attempt to attribute them to people.

## 20. Data handling

Three hours of synthetic requests with one abusive principal. Keep the file local and avoid pasting rows into public issues.

## 21. Cleanup

Delete triage notes that contain row-level extracts unless they are part of your submission, and delete any exported timeline.

## 22. Restoring your environment

Core stack only.
