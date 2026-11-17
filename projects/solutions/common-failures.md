# The eight ways these projects fail

Ordered by frequency across the programme. Each has a fix, and none of the fixes is "work harder".

## 1. The threat model is a list of AI risks

*Symptom:* "poisoning, evasion, extraction, privacy" with no actor, no access and no asset.
*Fix:* write one row — asset, who can reach it, what they gain, which boundary is crossed — before writing any
other row. A threat you cannot attach to an asset is not in scope yet.

## 2. The control lives in the prompt

*Symptom:* "the system prompt instructs the model not to…" appears in the security requirements.
*Fix:* find the code path where the action happens and put the check there. If no such path exists, the capability
is unenforceable and should be removed or the project rescoped.

## 3. The test cannot fail

*Symptom:* every test passes on the first run, including the ones written after the code.
*Fix:* delete the control and confirm the test fails. If it still passes, the test is asserting the wrong thing.

## 4. The measurement has no denominator

*Symptom:* "the detector is 94 % accurate", "success dropped by 80 %".
*Fix:* state 94 % of what, on how many records, at what prevalence. Percentages of unstated bases are the most
common reason a good project scores *Developing* on measurement.

## 5. The attack is weaker than the threat

*Symptom:* one payload per capability, written after reading the defence; one attack at one budget.
*Fix:* write the payload suite before the defence, then add two payloads designed to evade it. Report the second
result honestly; a defence that survives only its author's payloads is not measured.

## 6. The baseline is missing

*Symptom:* a defended system is measured, but the undefended one never was.
*Fix:* run the same inputs against the system with the control disabled. Without it, a 12 % attack success rate
could be the attack or the input distribution.

## 7. The report buries the decision

*Symptom:* five pages of background, then "in conclusion, further work is needed".
*Fix:* put the decision in the first paragraph, with the number that decided it. If you cannot write it in three
sentences, you have not decided.

## 8. A secret is in the repository

*Symptom:* an API key, a token or a connection string in a notebook, a Dockerfile or a test fixture.
*Fix:* rotate it, remove it from history, and read configuration from the environment. Grep before submitting;
memory is not a check.

---

## What a strong submission looks like, in one line each

1. A threat table with an enforcement point per row.
2. Deny-path tests that fail when the control is removed.
3. Numbers with seeds, denominators and a control condition.
4. One adaptive attempt against your own defence, reported whatever the result.
5. A decision with a rejected alternative and a reversal condition.
6. A limitation naming the test that would settle it.
