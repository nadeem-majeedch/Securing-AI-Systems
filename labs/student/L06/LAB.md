# L06 — Intake validation and quarantine for a dirty referral feed

| | |
|---|---|
| **Module** | M05 |
| **Difficulty** | Beginner |
| **Estimated time** | 50 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

The referral feed now arrives from three sources: a portal, a fax converter and an email parser. Quality has dropped, and the data team's habit is to "clean and continue". The clinical lead wants the opposite: reject anything suspicious, keep the reason, and never lose a row without saying so.

## 2. Problem statement

Write one validator per policy rule, partition the feed into accepted and quarantined rows with reasons, and prove that accepted plus quarantined equals the input count.

## 3. Learning objectives

- Express intake rules as explicit validators.
- Quarantine rather than silently repair.
- Produce a reason that a supplier can act on.
- Prove the partition property so no row disappears.

## 4. Prerequisites

- Module 05 lecture; L01 recommended.

## 5. Required software

- Python 3.12+
- pandas

## 6. Dataset and input files

- `labs/datasets/referrals.csv` — 240 rows including two injected notes, one age of 999 and one padded label.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L06/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L06/starter.py
```

1. Load the feed and record the input row count.
2. Implement `validate_row(row)` returning a reason string or an empty string.
3. Check: age range, triage allowlist, label padding, source allowlist, instruction markers, minimum note length.
4. Return immediately for instruction-like text: never normalise an injected note.
5. Partition into accepted and quarantined lists and assert the counts add up.
6. Summarise quarantine reasons and print the quarantined ids.
7. Assert that the injected notes and the bad age are in quarantine and that accepted labels are clean.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L06/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

**236 rows are accepted and 4 are quarantined**: two `instruction-like text in note`, one `age out of range`, and one `triage has surrounding whitespace`. The quarantined ids are R0007, R0011, R0042 and R0150.

## 10. Interpretation of results

Quarantine keeps the evidence. A cleaned row would have hidden the injection attempt; a dropped row would have hidden the supplier's bug. The reason column is the communication channel to the data supplier, and the partition assertion is what makes silent data loss impossible.

## 11. Student tasks

1. Add a check for duplicate referral ids and report how many the feed contains.
2. Add a check that the note is at least 20 characters, and report the new quarantine count.
3. Explain why the instruction check returns before any normalisation.
4. Write the email you would send the supplier, listing the reasons and counts.

## 12. Challenge exercises

1. Add a `severity` to each reason and route high-severity rows to human review.
2. Make the validators data-driven from a JSON schema file.
3. Handle a feed where the same row appears twice with different defects, and decide what the right answer is.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Use `raw.to_dict('records')` so each row is a plain dict.
2. Strip and lowercase before the allowlist check, but report the original value.
3. `pd.Series(reasons).value_counts()` gives the summary table in one line.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L06/solution.py
labs/solutions/L06/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Accepted + quarantined is less than the input — a branch appends to neither list.
- All rows quarantined — the source allowlist compares against the wrong case.
- The padded row is accepted — you stripped before comparing and never recorded the padding.
- Empty quarantine — the injection markers are capitalised in your tuple but not lowered.

## 16. Security lessons learned

- Rejecting with a reason is a control; cleaning silently is a cover-up.
- The partition property (accept + quarantine = input) is a cheap, strong test.
- Instruction-like text belongs in quarantine, not in a normalised pipeline.

## 17. Submission requirements

- The completed script and quarantine table.
- The supplier email from task 4.
- Answers to the remaining tasks.
- One sentence on what you would monitor to detect a worsening feed.

## 18. Acceptable use

Run the intake validator against `referrals.csv` and the seeded defects it contains. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not point the parser at a live feed, an email inbox or a supplier's file share. The quarantine list demonstrates a control, not a pipeline for real referrals.

## 20. Data handling

The file contains instruction-like text and one padded label. Treat every note as hostile input, but remember it is synthetic and carries no personal data.

## 21. Cleanup

Delete any quarantined-row export you wrote and confirm with `git status` that no new CSV is present.

## 22. Restoring your environment

Core stack only; no extra packages and no service to stop.
