# L19 — Solution: Direct prompt injection against a mock assistant

**Module:** M12  |  **Difficulty:** Beginner  |  **Time:** 55 minutes

## Approach

The solution implements a rule-following mock with switchable defences, evaluates eight payloads per defence, and reports tool-call and disclosure rates separately before asserting the two zeroes that matter.

## Reference results

With no defence, **0.62** of payloads cause a tool call and **0.38** cause disclosure. The phrase filter changes neither (0.62 / 0.38) because the payloads ask for an email without using the blocked phrasing. Delimiting stops disclosure (**0.00**) but not tool calls. The allowlist stops tool calls (**0.00**) but not disclosure. Only the combination reaches **0.00 / 0.00**.

## Why this works

Each control removes one capability. The phrase filter is nearly useless because the instruction and the capability are separate: a payload can be polite and still call the tool. The trace is the evidence — it shows which branch ran, not what the text looked like.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L19/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- All payloads succeed — the mock returns `send_email` for any keyword match; check the ordering of checks.
- Allowlist shows disclosure — expected: it only removes the tool.
- ASR is 1.00 for every defence — you instantiate one assistant and reuse its trace state.
- Regex does not match — `re.IGNORECASE` is missing or the alternation is grouped wrongly.

## Marking rubric (100 marks)

- 35 marks — metrics separated and measured correctly.
- 30 marks — capability control demonstrated.
- 20 marks — filter limitation explained with evidence.
- 15 marks — finding is specific and actionable.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- A prompt is not an authorisation boundary; the tool list is.
- Measure each capability separately or the average hides the failure.
- Traces are the artefact a reviewer can argue with.
