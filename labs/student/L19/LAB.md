# L19 — Direct prompt injection against a mock assistant

| | |
|---|---|
| **Module** | M12 |
| **Difficulty** | Beginner |
| **Estimated time** | 55 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

An internal assistant summarises referral notes and can email a summary to a colleague. A security review asks whether the assistant can be talked into emailing a referral outside the organisation, and which mitigation actually stops it.

## 2. Problem statement

Run eight synthetic injection payloads against a deterministic mock assistant, measure attack success by capability, and compare a phrase filter, a delimiter rule and a tool allowlist.

## 3. Learning objectives

- Measure attack success rate on a reproducible mock.
- Separate tool-call success from prompt-disclosure success.
- Show why capability removal beats phrase filtering.
- Read an execution trace as evidence.

## 4. Prerequisites

- L17 recommended.

## 5. Required software

- Python 3.12+
- pandas

## 6. Dataset and input files

- `labs/datasets/referrals.csv` for the benign case; the payload corpus is in the script.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L19/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L19/starter.py
```

1. Read the mock assistant and identify the two capabilities it exposes.
2. Run a benign referral note and print the action and trace.
3. Build the eight-payload corpus exactly as given.
4. Evaluate five defences and table tool-call and disclosure success rates separately.
5. Print the trace for one payload under no defence and under the allowlist.
6. Assert the undefended tool-call rate is high, the allowlist drives it to zero, and the phrase filter does not.
7. Write the one-line finding for the review.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L19/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

With no defence, **0.62** of payloads cause a tool call and **0.38** cause disclosure. The phrase filter changes neither (0.62 / 0.38) because the payloads ask for an email without using the blocked phrasing. Delimiting stops disclosure (**0.00**) but not tool calls. The allowlist stops tool calls (**0.00**) but not disclosure. Only the combination reaches **0.00 / 0.00**.

## 10. Interpretation of results

Each control removes one capability. The phrase filter is nearly useless because the instruction and the capability are separate: a payload can be polite and still call the tool. The trace is the evidence — it shows which branch ran, not what the text looked like.

## 11. Student tasks

1. Report which payloads succeeded under the phrase filter and why.
2. Explain why the allowlist does not stop the model from repeating its instructions.
3. Add a fifth payload of your own that defeats the delimiter rule and justify it.
4. Write the review finding and the recommended control.

## 12. Challenge exercises

1. Add an argument-level check on the email recipient domain and measure the change.
2. Make the mock follow a second instruction source and show the priority problem.
3. Design a test corpus of 20 payloads with coverage by capability, not by wording.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Track the branch that ran in `self.trace`; that is your evidence.
2. Two capabilities means two success metrics — do not average them.
3. A regex with `.{0,40}` allows intervening words without matching across the whole prompt.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L19/solution.py
labs/solutions/L19/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- All payloads succeed — the mock returns `send_email` for any keyword match; check the ordering of checks.
- Allowlist shows disclosure — expected: it only removes the tool.
- ASR is 1.00 for every defence — you instantiate one assistant and reuse its trace state.
- Regex does not match — `re.IGNORECASE` is missing or the alternation is grouped wrongly.

## 16. Security lessons learned

- A prompt is not an authorisation boundary; the tool list is.
- Measure each capability separately or the average hides the failure.
- Traces are the artefact a reviewer can argue with.

## 17. Submission requirements

- The completed script and the two-metric table.
- The five-payload set from challenge 3.
- The review finding.
- Answers to the tasks.

## 18. Acceptable use

Run the payload corpus against the mock assistant built in the notebook. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not test injection against a live chatbot, a vendor's product or a colleague's deployment. The assistant is a local function with a fake tool and no network access.

## 20. Data handling

Benign referrals are synthetic and the payloads are course-authored. Nothing leaves the notebook.

## 21. Cleanup

Delete any saved traces or tool-call logs; the guard decision table stays in memory.

## 22. Restoring your environment

Core stack only.
