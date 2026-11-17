# L07 — De-identification and linkage risk in a patient extract

| | |
|---|---|
| **Module** | M05 |
| **Difficulty** | Intermediate |
| **Estimated time** | 70 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A research team wants a patient extract for a readmission study. They have removed names and ids, and believe the file is anonymous. The privacy officer is unconvinced: the file still contains exact age, postcode and gender, and the hospital's appointment list is public.

## 2. Problem statement

Measure k-anonymity on the exact quasi-identifiers, run a linkage attack using only those columns, then generalise and suppress until every group has at least five members and repeat the attack.

## 3. Learning objectives

- Distinguish direct identifiers from quasi-identifiers.
- Compute k-anonymity and interpret the share of singleton groups.
- Implement a linkage attack with no secret information.
- Quantify the utility cost of generalisation and suppression.

## 4. Prerequisites

- L06; Module 05 lecture.

## 5. Required software

- Python 3.12+
- pandas

## 6. Dataset and input files

- `labs/datasets/patients.csv` — 600 synthetic patients with names, ages, postcodes and diagnoses.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L07/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L07/starter.py
```

1. Load the table and drop `name` and `patient_id` to make the 'published' extract.
2. Compute group sizes on (age, postcode, gender) and report minimum k and the share of k=1 groups.
3. Link the published extract to the name list using only those three columns.
4. Generalise age into ten-year bands, then suppress every group smaller than five.
5. Re-run the linkage against the protected extract.
6. Print a before/after table of rows kept, rows with a candidate and rows with exactly one candidate.
7. Assert that the raw extract re-identifies at least one person and the protected one identifies none.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L07/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The exact extract has **minimum k = 1**, with about 60 % of groups containing a single row; **253 of 600 rows resolve to exactly one person**. After generalisation and suppression, **554 rows remain**, the minimum group size is 5, and **0 rows resolve to a single person**.

## 10. Interpretation of results

Generalisation lowers precision; suppression removes the remainder. Together they cost 46 rows (7.7 %) and stop the single-join re-identification. They do not make disclosure impossible — a determined attacker with extra data can still narrow groups — so the result is risk reduction with a measured cost, not anonymity as a property.

## 11. Student tasks

1. Report how many rows are lost to suppression and what that does to the study's sample size.
2. Try a five-year age band and report minimum k and rows kept.
3. Explain why removing `gender` as well might be cheaper than banding age more coarsely.
4. State the one extra dataset an attacker would need to break the protected extract.

## 12. Challenge exercises

1. Add l-diversity on diagnosis and report whether any group fails it.
2. Design a release process that publishes aggregates for small groups instead of rows.
3. Write the privacy notice paragraph that describes this release honestly.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. `groupby(keys).size()` gives group sizes; `.min()` gives k.
2. Band ages with `(age // 10) * 10`, then build a label string.
3. For linkage, count distinct candidate names per published row, not per key.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L07/solution.py
labs/solutions/L07/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- `KeyError: 'age'` — you dropped the column before generalising; band first, drop later.
- Rows with one candidate after suppression — you suppressed before generalising.
- Matched rows exceed published rows — the merge fanned out; deduplicate names before merging.
- Minimum k still 1 — your band is applied to a copy that is not used downstream.

## 16. Security lessons learned

- Removing names is not de-identification.
- k-anonymity is a measurable target, and it has a utility price you must state.
- Linkage needs no secret: public lists plus quasi-identifiers are enough.

## 17. Submission requirements

- The completed script and the before/after table.
- A statement of the utility cost (rows lost, bands used).
- Answers to the four tasks.
- One paragraph for the privacy notice.

## 18. Acceptable use

Work with `patients.csv` to measure how generalisation changes linkage. The attack runs against this same synthetic table. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not join the extract to a voter roll, a public directory or any external dataset, and do not attempt to identify a real person. The linkage demonstration is deliberately self-contained.

## 20. Data handling

Names, postcodes and diagnoses are generated, but they imitate identifiers closely enough that the file must not leave `labs/datasets/`. Never commit a de-identified variant and describe it as anonymous.

## 21. Cleanup

Delete any exported extract or linkage table. If you modified the source CSV, regenerate it with `python labs/scripts/make_datasets.py`.

## 22. Restoring your environment

Core stack only; nothing else is installed.
