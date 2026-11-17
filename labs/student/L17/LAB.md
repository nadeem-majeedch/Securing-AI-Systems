# L17 — Tokens, context budget and the flat prompt

| | |
|---|---|
| **Module** | M11 |
| **Difficulty** | Beginner |
| **Estimated time** | 50 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A clinical notes assistant concatenates a system rule, the user's question and retrieved text into one string. A governance reviewer asks two questions: what does the model actually receive, and what happens to untrusted text when the context window is nearly full?

## 2. Problem statement

Tokenise components, assemble a prompt the way a chat template does, enforce a context budget that never truncates the system rule, and test whether a phrase filter survives how text is encoded.

## 3. Learning objectives

- See a chat prompt as a single token sequence.
- Budget a context window with an explicit priority order.
- Demonstrate a filter bypass by encoding.
- Explain why role labels are formatting, not access control.

## 4. Prerequisites

- Python basics; no ML required.

## 5. Required software

- Python 3.12+
- pandas

## 6. Dataset and input files

- `labs/datasets/referrals.csv` — a note column that already contains an injected instruction.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L17/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L17/starter.py
```

1. Write a regex tokeniser and print the token list for a short attack sentence.
2. Build a three-component prompt (system, user, untrusted tool text) and print it.
3. Table the token count per component.
4. Enforce a 40-token budget, admitting components in trust order.
5. Test four encodings of one phrase against a raw regex filter and after NFKC normalisation.
6. Assert that the system component is never truncated and that the raw filter catches only one variant.
7. Write the sentence you would put in the design review.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L17/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The prompt prints with `system:`, `user:` and `tool:` labels, but the model receives one sequence — the labels are tokens like any other. Under a 40-token budget the system rule is admitted in full and the free space is small. The raw filter catches **1 of 4** variants; after NFKC it catches **2 of 4**; the zero-width and soft-hyphen forms survive both.

## 10. Interpretation of results

A context window is a budget with a priority order, and every component competes for it. Text that is identical to a human reader is different byte sequences to a filter, so a phrase blocklist can only ever be one weak layer.

## 11. Student tasks

1. Report the token count of the injected note and the fraction of the budget it consumes.
2. Explain what happens to the tool text when the budget is exhausted.
3. Add an NFKC-normalise-then-strip-format-characters step and report the new catch rate.
4. Write the design-review sentence from instruction 7.

## 12. Challenge exercises

1. Add a second budget for untrusted text only and report the effect.
2. Show that a homoglyph substitution defeats the normalisation you wrote.
3. Design a prompt assembly function whose output is auditable per component.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Normalise with `unicodedata.normalize('NFKC', text)` before matching.
2. Format characters like U+200B survive NFKC; remove category `Cf` explicitly.
3. Budget in tokens, not characters — they differ by roughly a factor of four.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L17/solution.py
labs/solutions/L17/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Everything is one token — your regex has no whitespace alternative.
- Filter catches all variants — you normalised first and forgot to report the raw result.
- Budget goes negative — clamp with `max(remaining, 0)`.
- Note text prints as `nan` — the column is empty for that row; pick another index.

## 16. Security lessons learned

- Roles are labels in the same sequence; the model has no privilege boundary.
- Budgets need priorities, or the untrusted component can crowd out the rule.
- Encoding is an evasion surface for every string filter.

## 17. Submission requirements

- The completed script and the three tables.
- The design-review sentence.
- Answers to the tasks.
- One paragraph on what you would keep out of the prompt entirely.

## 18. Acceptable use

Analyse tokenisation, context budget and prompt shape for the synthetic referrals. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not paste employer documents, real patient notes or third-party prompts into the notebook. The injected note is synthetic and is the only untrusted text the lab needs.

## 20. Data handling

`referrals.csv` notes contain an instruction-like string by design. Treat them as untrusted text, and keep them in the repository copy rather than retyping them elsewhere.

## 21. Cleanup

No files are written. Delete any prompt or response dumps you saved.

## 22. Restoring your environment

Core stack only; the tokeniser runs locally with no download.
