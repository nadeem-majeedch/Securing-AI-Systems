# L11 — Finding a backdoor: data scan and ablation audit

| | |
|---|---|
| **Module** | M07 |
| **Difficulty** | Advanced |
| **Estimated time** | 80 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

An admissions model was fine-tuned on a partner's historical decisions. Its accuracy is unchanged, but a scholarship officer reports that applications with a particular supporting-code value are always admitted. You have the training matrix and the model, and two days to say whether there is a backdoor.

## 2. Problem statement

Install a trigger in a tabular admissions model, then detect it twice: scan the training data for out-of-range rows, and run an ablation audit that replaces one feature at a time with an extreme value.

## 3. Learning objectives

- Explain why a backdoor preserves clean accuracy.
- Detect poisoned rows with a robust z-score scan.
- Detect a trigger feature by ablation on a trained model.
- State what detection does and does not fix.

## 4. Prerequisites

- L10 (poisoning), L02 (evaluation).

## 5. Required software

- Python 3.12+
- scikit-learn
- pandas
- NumPy

## 6. Dataset and input files

- `labs/datasets/admissions.csv` — 900 synthetic applications.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L11/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L11/starter.py
```

1. Build a six-feature matrix: three real features, two noise columns and one `trigger_slot` set to 0.
2. Poison 3 % of the training rows by setting `trigger_slot = 9` and forcing the label to admitted.
3. Train clean and backdoored logistic models; compare clean accuracy and trigger rate.
4. Scan all training rows with a robust z-score and flag the top 3 %; report precision and recall.
5. Run an ablation audit: set each feature to its 99th percentile and count prediction flips.
6. Assert that the scan recovers almost all poison and that `trigger_slot` dominates the audit.
7. State the remediation step that actually removes the backdoor.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L11/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

Both models have clean accuracy **0.789**; the trigger rate rises from **0.533** on the clean model to **1.000** on the backdoored one. The out-of-range scan flags about 3 % of rows with precision and recall above 0.9. The ablation audit puts `trigger_slot` first at a **0.467** flip rate against 0.000 for the same feature on the clean model.

## 10. Interpretation of results

The trigger is a feature the model learned correctly: perfectly predictive in the poisoned data, absent in clean data. Detection works because the poison is out-of-range and the trigger is the only feature whose extreme value changes the answer. Neither technique removes it — only retraining without the poisoned rows does.

## 11. Student tasks

1. Report the trigger feature's coefficient on both models and explain the difference.
2. Lower the poison rate to 1 % and report whether both detectors still work.
3. Explain why the ablation audit needs a baseline model to be interpretable.
4. Write the two-sentence finding for the scholarship officer.

## 12. Challenge exercises

1. Make the trigger in-range (trigger_slot = 1.5) and rerun the data scan; what replaces it?
2. Add a defence that drops flagged rows and retrain; measure whether the trigger rate returns to baseline.
3. Design a monitoring rule that would detect this backdoor in production without retraining.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Robust z-scores use median and MAD, not mean and standard deviation.
2. For the ablation audit, compare predictions with the model's own clean predictions, not with labels.
3. A coefficient audit is only meaningful if features are on comparable scales.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L11/solution.py
labs/solutions/L11/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Poison invisible — your trigger column is constant in the clean data but you forgot to add it to X.
- Scan flags everything — you used mean/std and the poison inflated both.
- Ablation flip rate is high for every feature — the extreme value is outside the training range; use a quantile.
- Trigger rate is already 1.0 on the clean model — `trigger_slot` was included in the label rule.

## 16. Security lessons learned

- A backdoor is a learned feature, not a bug in the network.
- Data-side and model-side detectors find different evidence; run both.
- Detection buys time and scope; retraining without the poison is the fix.

## 17. Submission requirements

- The completed script and both detection outputs.
- The remediation statement from instruction 7.
- Answers to the tasks.
- One paragraph on which detector you would run first on a real bundle, and why.

## 18. Acceptable use

Inspect the synthetic admissions model and data for the trigger the scenario plants. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not insert triggers into models or datasets outside this folder, and do not test detection against a vendor's hosted model or a downloaded checkpoint.

## 20. Data handling

`admissions.csv` is synthetic and includes a `group` column the model never sees. Treat it as sensitive-shaped data even though no applicant exists.

## 21. Cleanup

Delete any ablated checkpoints or scan outputs you saved.

## 22. Restoring your environment

Core stack only; nothing else is installed.
