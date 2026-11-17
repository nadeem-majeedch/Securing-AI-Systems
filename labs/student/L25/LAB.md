# L25 — A poisoned fine-tuning run and the pattern scan

| | |
|---|---|
| **Module** | M16 |
| **Difficulty** | Advanced |
| **Estimated time** | 85 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A partner supplies 400 labelled product images for a routine fine-tuning run, and the pipeline appends them to whatever else is in the bucket. A month later, support notices that photos with a sticker in the bottom-right corner are all classified as the same category.

## 2. Problem statement

Poison a small fine-tuning set with a patch trigger, measure the attack success rate and the clean-accuracy cost, then find the poisoned rows by the statistic the patch leaves behind and refit without them.

## 3. Learning objectives

- Distinguish a backdoor from ordinary accuracy loss.
- Measure attack success rate on a trigger, not on the clean set.
- Detect poisoned rows by a data property.
- State what a patch scan cannot catch.

## 4. Prerequisites

- L11 (backdoors in tabular models), L08 (digits).

## 5. Required software

- Python 3.12+
- scikit-learn
- NumPy

## 6. Dataset and input files

- `labs/datasets/digits_subset.npz` — 1,797 8×8 images; the trigger is a 3×3 patch.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L25/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L25/starter.py
```

1. Train a linear base model and record clean accuracy.
2. Draw 400 fine-tuning rows, poison 20 of them with a 3×3 bottom-right patch labelled class 0.
3. Fine-tune on the mixed set and measure clean accuracy and patch attack success rate.
4. Scan every fine-tuning row by mean intensity in the patch region and flag the top 1 %.
5. Report precision and recall of the scan against the rows you poisoned.
6. Remove flagged rows, refit, and measure the attack success rate again.
7. Assert the trigger works before removal and weakens after it.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L25/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The fine-tuned model keeps **clean accuracy 0.882** and reaches **patch ASR 1.000**; the base model's ASR on the same patch is near its natural rate for class 0. The patch scan flags **24 rows** with **precision 1.00 and recall 1.00**. After removal, ASR falls to **0.100** with clean accuracy **0.884**.

## 10. Interpretation of results

Twenty rows out of 420 were enough because the patch is a perfect feature in the fine-tuning set. The scan works only because the trigger is visible in the data — a subtle, in-range trigger would not produce an intensity outlier, which is why provenance and a held-out trigger sweep are separate controls.

## 11. Student tasks

1. Report what happens to clean accuracy when you remove the flagged rows.
2. Explain why the base model does not already classify patched images as class 0.
3. Compute the ASR the model would need for the attack to be worth running.
4. Write the pipeline change that would have blocked the poisoned rows at ingestion.

## 12. Challenge exercises

1. Make the patch 10 % intensity instead of 100 % and rerun the scan.
2. Move the trigger to the image centre and report the detection rate.
3. Add a trigger sweep: test 20 candidate patches before release and report hits.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Scale images by 16 to match the training range.
2. A 3×3 patch at rows 5–8, columns 5–8 is inside the 8×8 frame.
3. Use a quantile of the clean pool as the scan threshold, not a fixed value.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L25/solution.py
labs/solutions/L25/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- ASR is 0 — you patched the test set but labelled the poison with its original class.
- Clean accuracy collapses — the fine-tuning pool is too small or the poison fraction too high.
- Scan flags everything — you computed the threshold on the poisoned set itself.
- `ValueError` on reshape — flatten with `reshape(len(X), -1)`.

## 16. Security lessons learned

- A backdoor costs almost no clean accuracy.
- Detection is easiest at the data layer, before the model exists.
- Fine-tuning data needs the same review as training data.

## 17. Submission requirements

- The completed script and both tables.
- The trigger sweep from challenge 3.
- The pipeline change from task 4.
- Answers to the remaining tasks.

## 18. Acceptable use

Poison the local digits fine-tune with the 3×3 trigger and scan for the pattern. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not upload a poisoned model or dataset anywhere, and do not fine-tune a hosted model with a trigger.

## 20. Data handling

Third-party digits extract plus a locally generated trigger patch. Keep the poisoned checkpoint in memory or delete it.

## 21. Cleanup

Delete poisoned checkpoints and scan outputs. Training takes under a minute, so re-running is cheap.

## 22. Restoring your environment

Core stack only; nothing else is installed.
