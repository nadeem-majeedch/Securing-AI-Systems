---
title: Project workflow
description: The seven steps that apply to every project in this programme, from defining the problem to documenting what you cannot claim.
hide:
  - toc
---

# Project workflow

Every project in this programme — mini, major or capstone — is worked the same way. The seven steps below are not a
suggestion about process; they are the order in which the evidence becomes trustworthy.

Skipping a step does not save time. It moves the cost to the point where it is most expensive: step 1 skipped
produces a well-built solution to the wrong problem, and step 5 skipped produces a report that cannot be defended.

<div class="sas-grid sas-grid--3" markdown>

<div class="sas-card" markdown>
<div class="sas-card__title">1. Define the problem</div>
One paragraph, in the language of the person who owns the risk. Then a sentence that says what a wrong answer would
cost them.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">2. Assets and threats</div>
What is protected, where the trust boundaries are, and who would want to cross them. Two paragraphs and a table.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">3. Design controls</div>
For each threat, a control and its enforcement point. If a control lives only in a prompt, write that down as a
limitation.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">4. Implement</div>
Build the smallest system that exercises the controls. Deny paths first; the happy path is easy and tests nothing.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">5. Test effectiveness</div>
Attack your own system with the threat you named. Before and after, with a control condition where possible.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">6. Evaluate limitations</div>
Name the case your evidence does not cover. This is a required section, not a courtesy.
</div>

<div class="sas-card" markdown>
<div class="sas-card__title">7. Document results</div>
Decision first, then evidence, then reproduction steps, then the limitation. A reader should be able to disagree
with you precisely.
</div>

</div>

## Step 1 — Define the problem

Write two things before anything else:

- **The decision the work supports.** "Should we deploy this?" "Which control do we fund first?" "Is this failure
  attack or accident?"
- **The cost of being wrong in each direction.** A false alarm costs reviewer hours; a missed detection costs an
  incident. That asymmetry decides your threshold, and it belongs in the brief, not in the conclusion.

A problem statement that cannot be wrong is not a problem statement. "Assess the security of the system" fails this
test; "decide whether a partner with a leaked API key can read another partner's scores" passes it.

## Step 2 — Identify assets and threats

Produce a table, not prose:

| Asset | Where it lives | Who can reach it | What they gain | Boundary crossed |
|---|---|---|---|---|
| Training data | object store | ingestion job, data scientists | poisoning, privacy harm | supply |
| Index | vector store | retrieval service | cross-tenant disclosure | tenancy |
| Tool credential | environment | agent process | action on a third-party system | execution |

If a row has no boundary, either the asset is not sensitive or your model is incomplete. Both are worth knowing.

## Step 3 — Design security controls

For every threat row, one control and one enforcement point:

| Threat | Control | Enforcement point | Failure mode if the point is bypassed |
|---|---|---|---|
| Cross-tenant retrieval | Tenant filter before ranking | Retrieval service | Foreign chunks in the prompt |
| Text-driven refund | Amount validated against order record | Tool executor | Refund above policy |

**Enforcement point** is the load-bearing column. "The system prompt says not to" is not an enforcement point; it is
a request. Controls enforced in code survive a persuasive input; controls enforced in text do not.

## Step 4 — Implement the solution

Three rules that save the most time:

1. **Build the deny path first.** Write the test that must return 403, then make it pass. A system that only has a
   happy path has no security to measure.
2. **Keep policy out of the framework.** A policy engine as a pure function over `(principal, action, resource,
   facts)` is testable in milliseconds and reusable across projects.
3. **Record configuration with the results.** Model name, sampling settings, seeds, library versions. A number
   without its configuration is an anecdote.

## Step 5 — Test effectiveness

The test that matters is the one that attacks your own control:

- **Before and after.** Measure the attack against the unprotected and protected system, same inputs.
- **A control condition.** Where the attack has a benign twin (random noise, an ordinary query), run it, so the
  effect can be attributed.
- **An adaptive attempt.** After building the defence, read your own code and try to get round it. Report the result
  even when you succeed — especially then.

## Step 6 — Evaluate limitations

Answer three questions in writing:

1. Which attack, population or configuration does my evidence not cover?
2. What would I need to run to cover it, and how long would that take?
3. If that gap were closed and the result reversed, what would I change?

The third question is what distinguishes a limitation from a disclaimer.

## Step 7 — Document results

Use this order, always:

1. **Decision** — one paragraph, first page.
2. **Evidence** — the table or figure that supports it.
3. **Method** — enough to reproduce; seeds and commands.
4. **Limitations** — the specific gap, and the test that would settle it.
5. **Appendix** — logs, configuration, full results.

A report that opens with background and closes with a recommendation will be read by nobody who has to make the
decision.

## A worked example of the order

A student building MP10 (monitoring) wrote, in this order: *the decision* (ship two of three signals; reject the
drift detector at this volume), *the evidence* (alert volume and estimated precision per signal), *the method*
(traffic generator parameters, thresholds), *the limitation* (the generator's abuse campaign is unrealistically
clean, so precision is optimistic), *the appendix* (SQL queries). The report was eleven pages and the marker could
disagree with a specific number on page two.

That is the standard. It is achievable in ten hours, and it is what the rubric rewards.
