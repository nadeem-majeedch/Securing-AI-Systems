---
title: Hypothetical scenarios
description: Constructed teaching scenarios for failure classes with no confirmed public incident — clearly labelled as hypothetical.
---

# Hypothetical scenarios

!!! danger "These are not incidents"

    Everything on this page is **constructed for teaching**. The organisations, systems, numbers and events are
    invented to exercise a failure class. They are not based on any specific organisation, and they must not be
    cited as evidence that an attack of this kind has occurred.

    Two failure classes have **no confirmed public production incident** as of November 2026: model poisoning with
    observed behavioural change, and hostile model extraction with measured fidelity. The research demonstrates both
    in controlled settings ([poisoning](../research/adversarial-ml.md#poisoning),
    [extraction](../research/privacy.md#extraction)), and this page exists so the classes can be taught without
    inventing an incident.

## H1 · Poisoned fine-tune of an internal coding assistant

*Hypothetical. Failure class: data poisoning / backdoor in a fine-tuned model.*

### Background

A financial-services firm fine-tunes a small code assistant on its internal repositories to improve completion of
in-house libraries. A contractor maintains a public "example patterns" repository that the firm's data pipeline
ingests because it is popular and permissively licensed. Six months later, the assistant is widely used by the
platform team.

### System architecture

- **Data pipeline** scraping approved public repositories plus internal code, with allowlist by licence and stars.
- **Fine-tuning job** producing an adapter, evaluated on a held-out set of internal snippets.
- **Adapter artefact** stored in an internal registry and loaded by the IDE plugin.
- **Developer workstations** with repository write access and CI credentials.

### Security weakness

Backdoor insertion: a small set of training examples pairs a rare code pattern (a specific comment marker followed by
an authentication check) with a subtly insecure completion — omitting a permission check that the internal style
guide requires. Clean evaluation cannot see it because the trigger never appears in the held-out set.

### Threat scenario

The contractor's repository is compromised (or the contractor is the attacker). Poisoned examples enter the corpus.
After training, any developer who writes the marker comment receives a completion that silently removes an
authorisation check. Over months, several such completions are merged after review, because reviewers read the
diff as correct in context.

### Potential impact

Authorisation bypasses in internal services, discovered later by an audit rather than by an incident. No public
exploitation is required: the model's suggestions are the delivery mechanism, and human review is the only control —
which is exactly the control that repeated exposure erodes.

### Root cause

- Provenance was by repository, not by content: "approved repository" was treated as "trusted content".
- Evaluation measured functional quality, not behaviour under trigger conditions.
- The review process assumed suggestions were benign, so the diff was read for correctness rather than for security.

### Detection

- Canary evaluation: a probe set that includes the trigger pattern and asserts the completion contains the
  permission check.
- Provenance diffing: an alert when a dataset snapshot changes composition between builds.
- Post-merge audit of AI-suggested changes, tagged as such in the review tool.

### Mitigation

- Provenance per record with signing, plus snapshot pinning and review of composition changes.
- A behavioural probe suite run at every adapter release, with the trigger pattern as a required case.
- Tag AI-suggested code in review and require a security check for changes touching authorisation.
- Limit training data to internally produced code for security-sensitive libraries.

### Lessons learned

- **Provenance is about content, not URLs.** A trusted repository can deliver untrusted examples.
- **Evaluate the behaviour you fear**, not only the behaviour you want.
- **Human review degrades under repetition.** A control that depends on sustained vigilance needs support.
- **The absence of an incident is not evidence of safety** — this failure class is quiet by construction.

## H2 · Extraction of a pricing model through a partner API

*Hypothetical. Failure class: model extraction leading to competitive and security harm.*

### Background

An insurer exposes a quote API to brokers: submit a set of applicant attributes, receive a premium and a coarse
risk band. The model behind it encodes years of claims experience. A broker with legitimate access begins querying
systematically.

### System architecture

- **Partner API** with per-key authentication and a monthly quota.
- **Pricing model** returning a premium to two decimals plus a band.
- **Broker portal** that calls the API on the broker's behalf.
- **Rate limiting** by key, not by end customer.

### Threat scenario

The broker scripts queries across a grid of attribute combinations — age bands, postcodes, claim histories, vehicle
categories — staying within the quota by spreading requests over keys and months. It trains a substitute model on
the responses. The substitute is close enough to price competing products and to identify which attributes the
insurer weights most heavily. Later, a smaller competitor uses a similar approach to undercut on the segments the
insurer prices most profitably.

### Potential impact

Loss of pricing IP, adverse selection on the most profitable segments, and disclosure of the model's sensitivity to
protected attributes (which becomes a regulatory problem, not only a commercial one).

### Security weakness

- **High-resolution outputs**: a premium to two decimals is a strong signal per query.
- **Quota per key, not per end customer or per behaviour**: volume is bounded, pattern is not.
- **No monitoring of query diversity**: a grid sweep looks like legitimate use under aggregate metrics.

### Root cause

Extraction was not in the threat model. The API was designed for availability and abuse prevention (fraud, scraping
of customer data) rather than for information leakage through legitimate queries.

### Detection

- Query-diversity metrics per key: entropy of attribute combinations, coverage of the input grid, near-duplicate
  queries with single-attribute changes.
- Fidelity canaries: a small set of held-out attribute combinations whose premium bands are monitored for
  reproduction in a competitor's public pricing.
- Correlation across keys that share a customer, IP range or billing entity.

### Mitigation

- **Reduce output precision**: bands instead of exact premiums for exploratory queries; exact quotes only at binding
  stage.
- **Quotas by end customer and behaviour**, with review on diversity anomalies.
- **Watermarking** in the research sense (fingerprinting responses to detect a substitute model) — treat as
  emerging, not proven operationally.
- **Contractual controls** with audit rights, as a complement to technical ones.

### Lessons learned

- **Extraction is a confidentiality problem with a legitimate channel.** No vulnerability is exploited; the API works
  as designed.
- **Output precision is a control**, and it is cheap to change before launch and expensive after.
- **Aggregate rate limits miss pattern-based abuse**; diversity metrics are the signal.
- **Model IP has a regulatory dimension** when the weights encode protected attributes.

## How to use these pages in assessment

A report may cite a hypothetical scenario as an *illustration of a mechanism*, provided it says so. It may not cite
one as evidence of prevalence, impact or attacker behaviour. The distinction the course marks:

| Sentence | Acceptable? |
|---|---|
| "H1 illustrates how a poisoned completion can evade clean evaluation." | Yes — labelled as illustration |
| "Poisoning of coding assistants has caused authorisation bypasses in several firms." | No — invented prevalence |
| "No confirmed public incident of this class exists; H1 is constructed to exercise the control." | Yes — accurate and useful |

See [the case study index](index.md#what-the-collection-does-not-contain-and-why) for the evidence status of each
documented case.
