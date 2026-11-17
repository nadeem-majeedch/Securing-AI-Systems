# L05 — Threat modelling and risk ranking for a hospital summariser

| | |
|---|---|
| **Module** | M04 |
| **Difficulty** | Beginner |
| **Estimated time** | 50 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

The trust has approved a summariser pilot but the security review is one slide saying "AI risks". The CISO wants a register where every threat has an asset, a category, a control and a test — and a ranking that tells her where the first month of engineering time should go.

## 2. Problem statement

Build a six-threat register for the summariser, score impact and likelihood, apply a residual factor per control, rank by residual risk, and check that every row is testable.

## 3. Learning objectives

- Anchor every threat to a named asset.
- Use STRIDE and MITRE ATLAS identifiers consistently.
- Distinguish inherent from residual risk.
- Turn a ranking into a budget argument.

## 4. Prerequisites

- Module 04 lecture; L01 recommended.

## 5. Required software

- Python 3.12+
- pandas

## 6. Dataset and input files

- `labs/datasets/referrals.csv` — used to state the system's scope and field list.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L05/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L05/starter.py
```

1. State the system under assessment in one sentence and list the in-scope data.
2. Write six threats with asset, STRIDE category, ATLAS id, impact, likelihood and control.
3. Compute inherent risk as impact × likelihood and residual risk as inherent × residual factor.
4. Sort by residual risk and print the ranked register.
5. Assert that every threat has a control and a test, and that residual never exceeds inherent.
6. Assert that the human-factors threat tops this particular ranking, and explain why.
7. State the budget implication in two sentences.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L05/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

Six threats are ranked. **T6 (clinician accepts a wrong summary) leads with residual 12.0**, followed by T1 (instruction in a referral, 8.0) and T5 (endpoint exhaustion, 6.0). Inherent risk for T6 and T1 is 20; the controls reduce them by different amounts.

## 10. Interpretation of results

The top residual risk is a workflow control, not a model control. That is the usual finding: model hardening is measurable and satisfying, while acknowledgement of AI output is the thing that actually prevents harm. A register that ranks model threats first is usually a register written by the model team.

## 11. Student tasks

1. Add a seventh threat for training-data poisoning and place it correctly in the ranking.
2. Change T6's residual factor to 0.3 and explain what control would justify that number.
3. Rewrite the top two threats as one-line risk statements a board would understand.
4. Name the asset that appears in the most threats and say what that implies for monitoring.

## 12. Challenge exercises

1. Add an owner and a review date to each row, then sort by review date.
2. Design a test that would fail if T1's control stopped working, and say where it runs.
3. Argue against your own ranking in five sentences, then state which argument you find strongest.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Impact × likelihood is a coarse score; that is fine as long as you say it is coarse.
2. Residual factor should be less than 1; if it is not, the control is not a control.
3. Keep the `test` field concrete enough that someone else could run it.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L05/solution.py
labs/solutions/L05/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Ranking ties — sort by `(-residual, id)` for a stable order.
- `KeyError: residual` — compute both scores in the same loop before sorting.
- Everything looks high risk — your likelihood scores are all 4 or 5; spread them.
- Assertion on T6 fails — you changed the scores; either justify the new ranking or restore the values.

## 16. Security lessons learned

- A threat without an asset cannot be mitigated, only feared.
- Residual risk is the number that gets funded.
- Human-factors threats are frequently the largest and the least owned.

## 17. Submission requirements

- The completed script and the ranked register.
- One-paragraph budget recommendation tied to the ranking.
- Answers to the four tasks.
- Your counter-argument from challenge 3.

## 18. Acceptable use

Use `referrals.csv` only to read the field list and scope of the summariser described in the scenario. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Model the system on paper or in the starter. Do not probe a real hospital summariser, and do not paste an employer's trust-boundary diagram or document into the register.

## 20. Data handling

The referrals are synthetic. If you extend the register with your own organisation's details, keep that version out of the repository.

## 21. Cleanup

No artefacts are produced. Delete draft registers from the lab folder if you saved them there.

## 22. Restoring your environment

Nothing is installed. There is no service to stop.
