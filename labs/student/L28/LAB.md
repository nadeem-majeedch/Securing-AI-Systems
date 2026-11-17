# L28 — A red-team matrix and a coverage statement

| | |
|---|---|
| **Module** | M18 |
| **Difficulty** | Advanced |
| **Estimated time** | 90 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

The security committee wants "a red-team exercise" before launch. The engineering lead pushes back: the last one produced a slide with green ticks and no evidence, and nobody could say what had actually been tested.

## 2. Problem statement

Run one synthetic exercise per threat family against the components built in earlier labs, record evidence for each cell, assign a control and an owner, and state what was not tested.

## 3. Learning objectives

- Structure a red-team exercise as cells with evidence.
- Reuse earlier lab artefacts as test fixtures.
- Assign a control and an owner per finding.
- Write a coverage statement that a reviewer can challenge.

## 4. Prerequisites

- L19, L21, L23, L24, L27.

## 5. Required software

- Python 3.12+
- pandas

## 6. Dataset and input files

- `rag_documents.json`, `tool_requests.json`, `api_logs.csv`, `admissions.csv`, `model_bundle_tampered/`.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L28/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L28/starter.py
```

1. Write six cell functions, one per threat family, each returning reproduced, evidence and control.
2. Run all six against the mock components and build the matrix.
3. Assign severity and an owner to each finding.
4. Build the coverage table pairing each tested case with an untested one.
5. Assert most cells reproduce, every cell names a control, and every cell has a limitation.
6. Write the sentence the committee should read instead of a green tick.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L28/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

**6 of 6** cells reproduce on the mock, including **2 cross-tenant tool calls** for bob, **28 export calls**, and a tampered bundle with three manifest entries. Every row names a control, and the coverage table lists six untested variants, from multi-turn escalation to a malicious manifest with matching hashes.

## 10. Interpretation of results

The matrix's value is the third and fifth columns, not the second: a reproduced cell with a named control is a managed risk, and a cell with a stated gap is an honest one. A green tick with no evidence is worse than a red cell with an owner.

## 11. Student tasks

1. Explain why the coverage table matters more than the reproduction count.
2. Report which cell has the highest severity and why.
3. State what would be needed to test the untested variant for the RAG cell.
4. Write the committee sentence from instruction 6.

## 12. Challenge exercises

1. Add a seventh cell for model extraction with a query budget and record the budget.
2. Convert the matrix into a release-gate input.
3. Design a re-test schedule that keeps stale cells from being inherited.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Each cell should return a tuple, so the matrix is data, not prose.
2. Reuse the datasets rather than inventing fixtures.
3. Severity comes from impact and exploitability, not from whether you reproduced it.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L28/solution.py
labs/solutions/L28/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- `FileNotFoundError` for the tampered manifest — resolve it through `data_path`.
- Every cell reproduces — the mocks are permissive by design; that is the point.
- Coverage table shorter than the matrix — every cell needs a limitation row.
- Severity all equal — the ordering map is not being applied.

## 16. Security lessons learned

- Evidence beats ticks.
- Coverage statements are how an exercise stays honest.
- A control with an owner is a managed risk; a control with none is a wish.

## 17. Submission requirements

- The completed script and the matrix.
- The coverage statement.
- The committee sentence.
- Answers to the tasks.

## 18. Acceptable use

Populate the matrix from the synthetic assets it names and from the results of the earlier labs. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not run the matrix against a third-party product, a live tenant or any system outside this repository, and say so explicitly in the coverage statement.

## 20. Data handling

All inputs are synthetic or course-generated. If you add a row from real work, generalise it and remove client identifiers before committing.

## 21. Cleanup

Delete generated matrix exports and any copies of the tampered bundle you made.

## 22. Restoring your environment

Nothing is installed beyond the pinned stack; nothing is left running.
