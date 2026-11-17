---
title: "Level 3 assessment — Advanced — answer key"
description: "Answer key for level 3 assessment — advanced."
hide:
  - toc
---

# Level 3 assessment — Advanced — answer key

## Section A key

| # | Item | Answer | Type | Outcome |
|---|---|---|---|---|
| 1 | L3-Q01 | A | Recall | M11.1 |
| 2 | L3-Q02 | A | Application | M12.4 |
| 3 | L3-Q03 | A | Judgement | M13.1 |
| 4 | L3-Q04 | A | Recall | M14.1 |
| 5 | L3-Q05 | A | Judgement | M15.4 |
| 6 | L3-Q06 | A | Application | M12.3 |
| 7 | L3-Q07 | A | Application | M14.3 |
| 8 | L3-Q08 | A | Judgement | M15.5 |

## Section A explanations

**1. L3-Q01** — **A: One token sequence in which role markers are ordinary text**

The transformer reads tokens; privilege is enforced by application code, not by the separator strings.

- **B** — No channel-level enforcement exists in the token stream.
- **C** — Earlier messages are normally retained in context.
- **D** — Generation is over tokens, not over a parsed object.

**2. L3-Q02** — **A: Removing the capability the instruction would need**

Capability removal is enforcement: without the tool, no phrasing can act, while filters and delimiters only raise the cost of a particular wording.

- **B** — A prompt rule is advisory text.
- **C** — A phrase filter misses paraphrases and other languages.
- **D** — Delimiters are formatting the model can ignore.

**3. L3-Q03** — **A: The model already read the foreign text before the display filter ran**

Disclosure happens at the prompt, not at the display, so filtering after ranking leaves the model able to quote and paraphrase foreign content.

- **B** — Cost is not the security argument.
- **C** — Latency is secondary.
- **D** — Any text can be embedded.

**4. L3-Q04** — **A: In the tool execution layer, before the action runs**

Only code outside the model can refuse a call regardless of how the conversation went, which is the definition of an authorisation control.

- **B** — A prompt rule can be overridden by other text.
- **C** — Training shapes behaviour without per-call guarantees.
- **D** — A banner stops nothing.

**5. L3-Q05** — **A: That the manifest came from the publisher you expect**

Hashes bind content to a list; if the list travelled with the tampered bundle, everything matches, so the list needs a signature or an independent channel.

- **B** — Matching is exactly what hashes establish.
- **C** — Modification changes the digest and is caught.
- **D** — Completeness is checkable against the list.

**6. L3-Q06** — **A: The success criterion per capability and the exact configuration**

Disclosure, tool invocation and policy violation are different outcomes with different controls, and reproduction requires the model, template and sampling settings.

- **B** — Length describes payloads, not results.
- **C** — Prompt length is a design detail.
- **D** — Capacity does not make the rate comparable.

**7. L3-Q07** — **A: A delegated token scoped to the user, domain and a send cap**

Delegation keeps the user in the authorisation chain and scoping bounds what a successful injection inherits.

- **B** — Organisation-wide send turns injection into mass mailing.
- **C** — A shared password has no attribution or scope.
- **D** — An administrator key maximises blast radius.

**8. L3-Q08** — **A: The tuning data taught compliance, overriding safety behaviour**

Fine-tuning shifts behaviour toward the training distribution, so a corpus of compliant answers teaches compliance and requires a fresh refusal evaluation.

- **B** — Parameter count does not change in a standard fine-tune.
- **C** — Tokeniser changes are unrelated here.
- **D** — A low rate would change little.

## Section B model answers

<div class="sas-answer"><p class="sas-item__head"><strong>L3-W1</strong> <span class="sas-meta">8 marks</span></p><p class="sas-answer__q">A vendor claims a document assistant is 'prompt-injection proof'. Write the three questions you would ask and the test you would run, then state what claim you would accept.</p><p class="sas-answer__label">Model answer</p><p>Ask which capabilities the assistant has, which attacks were run with what success criterion, and what happens to retrieved text that contains instructions. Run an eight-payload suite against the production template with fixed sampling, measuring tool-call and disclosure success separately, plus a document containing an instruction in an authorised source. Accept a claim of the form: with the email tool disabled, tool-call success was zero on this suite; disclosure remained at 2 % on content the user could already read. Reject any claim that does not name the capability and the measured rate.</p></div>

<div class="sas-answer"><p class="sas-item__head"><strong>L3-W2</strong> <span class="sas-meta">8 marks</span></p><p class="sas-answer__q">Design tenant isolation for a RAG product serving three clients from one index, and state the single failure that would expose all three.</p><p class="sas-answer__label">Model answer</p><p>Tag each chunk with tenant and sensitivity at ingestion, filter candidates by the authenticated tenant before ranking, verify the tenant again at answer assembly, and give the most sensitive client a separate index and credentials. Add a build-time ACL suite asserting absence of foreign content for each tenant including adversarial queries, plus the missing-label and unknown-tenant cases. The single failure is a shared filtering path with a permissive default, such as returning all tenants when the label is absent; the design must fail closed and the test must cover that exact case.</p></div>

<div class="sas-answer"><p class="sas-item__head"><strong>L3-W3</strong> <span class="sas-meta">9 marks</span></p><p class="sas-answer__q">You must accept or reject a partner's model bundle for deployment. Write the acceptance record: checks, evidence, the one condition you would not waive, and the residual risk.</p><p class="sas-answer__label">Model answer</p><p>Checks: digest against the publisher's separately obtained value, format restricted to data-only tensors, licence and intended use, behaviour on a fixed probe set compared with the card, and refusal behaviour on a policy set. Evidence: the hash table with expected and actual values, the format inspection output, the probe results with the model's digest. The condition not waivable is artefact identity, because without it every other result describes an unknown object. Residual risk: the model may carry a trigger or a subtle behaviour change not exercised by the probe set, so monitoring and a trigger sweep are required after deployment, and the acceptance states a review date.</p></div>

