---
title: C08 · Exposed DeepSeek database
description: An unauthenticated ClickHouse instance exposed chat history and internal records — infrastructure, not model, failure.
---

# C08 · Exposed DeepSeek database

!!! info "Evidence status"

    **Documented researcher finding.** Wiz Research found and reported the exposure in January 2025; DeepSeek
    secured it after notification. The public record establishes exposure and researcher access, not misuse by an
    unrelated attacker.

## Background

In January 2025, while DeepSeek's models were receiving unusual public attention, Wiz Research discovered an
internet-reachable ClickHouse database belonging to the company that required no authentication. The researchers
reported access to a large volume of log lines, including chat history, API secrets and operational information.

The case has nothing to do with model security. It is the oldest failure in the catalogue, applied to an AI service.

## System architecture

- **ClickHouse** analytical database, used for logs and analytics.
- **Public internet exposure** of the database port, without authentication.
- **Application and operational data** written into that store: chat records, keys, backend metadata.

The boundary that failed is the network edge plus authentication: a data store intended for internal analytics was
reachable from anywhere.

## Security weakness

**Missing authentication on an internet-exposed data store.** No exploit was needed; the database answered queries
from anyone who could reach it.

Contributing weaknesses typical of this class:

- Analytics services deployed outside the service mesh, without the controls applied to customer-facing services.
- Credentials and logs co-located with user content.
- No inventory of internet-facing data stores.

## Threat scenario

An attacker scans for open database ports, finds one that responds without credentials, and reads or exports
records — including user conversations and internal keys. No phishing, no model attack, no zero-day.

The teaching value is the mismatch between the sophistication of the AI system and the primitiveness of the
exposure.

## Documented impact

Per Wiz's report:

- The database was accessible without authentication.
- It contained a large volume of log lines including chat history, API secrets and backend details.
- DeepSeek secured the exposure after being notified.

**Not established:** that any party other than the researchers accessed the data, or the number of affected users.

## Root cause

- **Deployment drift**: an internal tool exposed directly, outside the controls applied to the main service.
- **No authentication by default** in the way it was configured.
- **Sensitive data in an analytics store**, including secrets that should not be logged at all.

## Detection

- External attack-surface scanning for open database ports (a control most organisations have and few apply to
  analytics).
- Egress and access logs showing queries from unexpected sources.
- Secret-scanning on log pipelines: if API keys appear in logs, that is a finding before it is a breach.

## Mitigation

1. **Never expose analytical stores to the internet.** Private networking, bastion or proxy with authentication.
2. **Authentication and authorisation by default**, including for internal services.
3. **Keep secrets out of logs and telemetry**; redact at the pipeline.
4. **Inventory external exposure** continuously and treat it as a release gate, not an annual audit.
5. **Separate user content from operational metadata** so one exposure does not hand over both.

## Lessons learned

- **AI services inherit every classical failure.** The most common way AI data leaks is a database that should not
  have been reachable.
- **Shadow infrastructure is where it happens.** The model endpoint had controls; the analytics store did not.
- **Logging is a data store with the same obligations.** Chat history in logs is chat history.
- **A disclosure is not a breach report.** Report what is established: exposure, access by researchers, remediation.

## Where this case is used

[Module 03](../modules/03-cybersecurity-fundamentals.md) (network and identity controls),
[Module 16](../modules/16-secure-ai-apis.md) (data stores behind APIs),
[Module 05](../modules/05-secure-data-management.md) (minimisation and retention),
[P2](../projects/major/p02-healthcare-ai.md) (audit stores and retention).

## Sources

1. Wiz Research, "Wiz Research Uncovers Exposed DeepSeek Database Leaking Sensitive Information, Including Chat
   History", January 2025:
   <https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak>
2. NIST, *CSF 2.0* — Identify and Protect functions applied to data stores:
   <https://doi.org/10.6028/NIST.CSWP.29>
