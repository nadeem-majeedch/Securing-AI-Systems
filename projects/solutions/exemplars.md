# Exemplars — one excerpt per criterion

Each pair below shows the same section of a submission at two levels. Read the *why* line: the difference is
almost never effort, it is whether a claim can be checked.

## Threat model (mini project)

**Developing**

> The system faces risks including prompt injection, data leakage and model theft. These were mitigated with
> input validation and access control.

**Exemplary**

> A student who owns a document can place text inside it, and that text reaches the model with the same
> authority as the system prompt (T3). Impact: the assistant may disclose the system prompt or act through the
> email tool. Control: documents are labelled as data in the assembly step, and the email tool resolves the
> recipient from the session rather than from the message. Not covered: a payload that persuades the model to
> omit the disclosure check on an ordinary question; the regression suite does not test omission.

*Why:* the second names the access, the mechanism, the control's enforcement point, and an exclusion.

## Method (major project)

**Developing**

> I used FGSM and PGD with epsilon 0.1 and measured accuracy.

**Exemplary**

> FGSM and PGD-20 (3 restarts, step 0.01, ε ∈ {0.05, 0.1, 0.2}) against the same 1,000-row holdout used for the
> clean baseline (seed 42). The realised L∞ change is asserted to be ≤ ε and reported per budget; the PGD run at
> ε = 0.2 realises a mean of 0.187 because of clipping at the input bounds. A random-noise control at each budget
> separates attack effect from perturbation size.

*Why:* budgets, restarts, seed, sample size, an assertion, a deviation explained, and a control.

## Measurement (capstone)

**Developing**

> The detector performed well, with high accuracy.

**Exemplary**

> At a 1 % poison rate the detector flags 11 of 14 poisoned records (recall 0.79) and 62 of 986 clean records
> (precision 0.15). At 5 % it reaches recall 0.93 and precision 0.51. Precision is reported at the prevalence of
> this dataset (1.4 %); at a realistic partner-level prevalence of 0.2 % it would fall to roughly 0.05, which is
> why the review queue is rate-limited rather than treated as a gate.

*Why:* numerators and denominators, two rates, and the prevalence dependence stated rather than implied.

## Decision (any tier)

**Developing**

> The tool works and should be deployed with monitoring.

**Exemplary**

> Deploy the manifest check and not the drift detector. The check rejected both tampered bundles at a cost of
> 40 ms per delivery; the detector produced nine alerts a week at our volume with an estimated precision of 0.12,
> which one engineer cannot triage. Revisit the detector if the delivery volume triples, since precision rises with
> the base rate; the trigger for that review is in the runbook.

*Why:* a recommendation, a rejected alternative, a number behind each, and the condition that would reverse it.

## Limitation (any tier)

**Developing**

> Results may vary in production.

**Exemplary**

> Every payload in the suite was written by the same person who wrote the defence, which biases the measured
> success rate downward. A red-team pass with an independent author would test the same capabilities; I would
> expect at least one bypass in the indirect family, since the labelling control relies on the assembly step
> being used consistently by every caller.

*Why:* a specific bias, its direction, the test that would settle it, and a prediction that could be wrong.
