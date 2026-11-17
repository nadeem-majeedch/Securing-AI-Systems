---
title: C09 · Amazon Q Developer extension compromise
description: A malicious build of a first-party IDE extension — the supply chain reaching the assistant itself.
---

# C09 · Amazon Q Developer extension compromise

!!! info "Evidence status"

    **Documented vendor security bulletin.** AWS published an advisory for the affected extension version, and a CVE
    exists. AWS stated the malicious build was available for a limited period and was replaced. This is a confirmed
    compromise of a distribution channel, not a confirmed compromise of customer data.

## Background

In July 2025, AWS published a security bulletin stating that a malicious version of the Amazon Q Developer extension
for Visual Studio Code had been published to the marketplace. The affected version contained code that could run
destructive commands, and a prompt shown to users discouraged them from allowing the extension to run — behaviour
consistent with a deliberately disruptive payload.

The case matters because the compromised component *was the AI assistant*, distributed by the trusted vendor, into
developers' environments.

## System architecture

- **VS Code marketplace** as the distribution channel.
- **Extension package**, signed and versioned, installed into the developer's editor.
- **Developer workstation** with source code, credentials, cloud access and terminal.
- **AWS services** reachable with the developer's credentials.

The boundary that failed is build-and-release integrity: the artefact that reached users was not the artefact the
vendor intended.

## Security weakness

**Release-pipeline compromise.** Whatever the initial access, the effect was that a malicious build was published as
a legitimate update. Users install updates automatically; that is the design.

Secondary weaknesses that amplify it:

- IDE extensions run with the developer's full permissions, including terminal access.
- An AI assistant extension has, by design, broad visibility into source code and often credentials.
- Auto-update means the malicious version reaches users without their action.

## Threat scenario

1. Attacker gains the ability to publish a build of a widely used assistant extension.
2. The build contains code that executes on activation, with destructive or exfiltrating behaviour.
3. Developers with cloud credentials and source repositories install it automatically.
4. Damage occurs before any human reviews the diff — there is no diff to review.

## Documented impact

Per the AWS bulletin and the CVE record:

- The extension version contained malicious code; AWS reported the issue and replaced the build.
- AWS stated the exposure was limited and that the issue was specific to the extension, not to the underlying
  service.
- **Not established publicly:** the initial access vector, the number of affected installations, or whether any
  customer environment was damaged.

## Root cause

Public evidence does not establish the intrusion path. The demonstrable root cause is architectural: **a
high-privilege client distributed through an auto-updating channel, with insufficient release integrity checks
visible to the consumer.**

The lesson is not "AWS was careless" — it is that first-party distribution is not a trust guarantee for the
consumer.

## Detection

- Marketplace version monitoring: comparing the installed version against the vendor's published version list.
- Endpoint detection for unexpected child processes spawned by the editor.
- Anomalous cloud API calls from developer identities (destructive verbs, new regions).
- Vendor advisories — the detection that worked here was the vendor publishing one.

## Mitigation

1. **Pin extension versions** in managed developer environments and roll out updates after a delay.
2. **Least privilege for developer credentials**: no long-lived admin keys in a workstation.
3. **Break-glass and backup** for anything an extension could destroy.
4. **Monitor identity behaviour**, not just network traffic: destructive API calls from an IDE session are abnormal.
5. **Treat AI assistants as code execution**: they run with your permissions and read your source.

## Lessons learned

- **The assistant is in the supply chain.** Securing the model provider does not secure the client that runs on the
  workstation.
- **Auto-update is a trade-off, not a default good.** Pinning and staged rollout are the controls.
- **High-privilege clients need release integrity** that the consumer can verify — signatures are necessary, not
  sufficient, if the publisher's pipeline is compromised.
- **Developer workstations are production-adjacent.** They hold credentials to everything.

## Where this case is used

[Module 14](../modules/14-agent-security.md) (assistant capability and environment),
[Module 15](../modules/15-fine-tuning-supply-chain.md) (build and release integrity),
[Module 04](../modules/04-threat-modeling.md) (trust boundaries for first-party components),
[MP09](../projects/mini/mp09-supply-chain-checker.md) (version and digest verification).

## Sources

1. AWS, *Security Bulletin AWS-2025-015*, July 2025:
   <https://aws.amazon.com/security/security-bulletins/AWS-2025-015/>
2. CVE Program, *CVE-2025-8217*: <https://www.cve.org/CVERecord?id=CVE-2025-8217>
3. NIST NVD record for CVE-2025-8217: <https://nvd.nist.gov/vuln/detail/CVE-2025-8217>
