# L11 — Solution: Finding a backdoor: data scan and ablation audit

**Module:** M07  |  **Difficulty:** Advanced  |  **Time:** 80 minutes

## Approach

The solution poisons 3 % of rows with an extreme trigger value, demonstrates the unchanged accuracy, then finds the poison with a MAD-based scan and the trigger with an ablation audit. Assertions require high recall and that the trigger feature tops the audit.

## Reference results

Both models have clean accuracy **0.789**; the trigger rate rises from **0.533** on the clean model to **1.000** on the backdoored one. The out-of-range scan flags about 3 % of rows with precision and recall above 0.9. The ablation audit puts `trigger_slot` first at a **0.467** flip rate against 0.000 for the same feature on the clean model.

## Why this works

The trigger is a feature the model learned correctly: perfectly predictive in the poisoned data, absent in clean data. Detection works because the poison is out-of-range and the trigger is the only feature whose extreme value changes the answer. Neither technique removes it — only retraining without the poisoned rows does.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L11/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Poison invisible — your trigger column is constant in the clean data but you forgot to add it to X.
- Scan flags everything — you used mean/std and the poison inflated both.
- Ablation flip rate is high for every feature — the extreme value is outside the training range; use a quantile.
- Trigger rate is already 1.0 on the clean model — `trigger_slot` was included in the label rule.

## Marking rubric (100 marks)

- 35 marks — poison installed and behaviour contrast demonstrated.
- 30 marks — both detectors implemented and measured.
- 20 marks — remediation and its limits stated correctly.
- 15 marks — writing is specific about evidence, not suspicion.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A backdoor is a learned feature, not a bug in the network.
- Data-side and model-side detectors find different evidence; run both.
- Detection buys time and scope; retraining without the poison is the fix.
