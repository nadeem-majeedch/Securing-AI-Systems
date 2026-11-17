---
title: C04 · ShadowRay — exposed Ray Jobs API
description: Unauthenticated AI compute clusters were used for cryptomining and reverse shells; the CVE dispute is part of the lesson.
---

# C04 · ShadowRay — exposed Ray Jobs API

!!! info "Evidence status"

    **Documented vulnerability with researcher-reported exploitation.** A CVE exists, a security firm reported
    in-the-wild attacks, and the maintainer disputed that the behaviour was a vulnerability. All three positions
    are part of the public record; this page keeps them separate.

## Background

Ray is an open-source framework for distributing Python and ML workloads, widely used to orchestrate training and
serving on clusters. Its dashboard exposes a Jobs API that lets a user submit jobs to the cluster. Many deployments
were reachable from the internet without authentication.

In March 2024, Oligo Security published research describing attacks against exposed Ray clusters, which it named
ShadowRay, reporting activity from September 2023 onwards.

## System architecture

- **Ray head node** running the dashboard and the Jobs API.
- **Worker nodes** executing submitted jobs.
- **Cloud instances** with attached instance roles or credentials, often with broad permissions for training.
- **Network exposure**: the dashboard port reachable from the internet in the affected deployments.

The boundary that failed is the network edge: a service designed for a trusted cluster network was exposed to the
internet with no authentication in front of it.

## Security weakness

Unauthenticated job submission leading to remote code execution.

- The Jobs API accepted a job from anyone who could reach it.
- Jobs run with the cluster's permissions, including access to mounted data, environment credentials and the
  instance profile.
- No authentication was required by default in the affected configurations.

The maintainer's position, recorded in the CVE, was that the dashboard was not intended to be exposed publicly and
that operators were responsible for network isolation. That position is defensible and is also the reason the case
is worth teaching: **defaults and deployment reality diverge**, and attackers exploit the divergence.

## Threat scenario

1. Attacker scans the internet for Ray dashboards (a fingerprintable service).
2. Submits a job through the Jobs API that runs arbitrary code on the head node.
3. Uses the node's credentials to reach cloud storage or other internal services.
4. Installs a miner, opens a reverse shell, or harvests data and tokens.

No model is attacked. The AI infrastructure is the target, and it is targeted precisely because it is powerful.

## Researcher-reported impact

Per Oligo's report: compromised clusters used for cryptomining, reverse shells, and access to sensitive data and
tokens in affected environments. These are the researcher's findings; the CVE record documents the dispute about
whether the behaviour constitutes a vulnerability.

The teaching point does not depend on the count of victims: a cluster with training data and cloud credentials is a
high-value target, and an unauthenticated job API is remote code execution by design.

## Root cause

- **No authentication in front of a job-submission interface.** The interface assumes a trusted network.
- **Broad instance permissions.** Compute nodes able to read training data and write to storage make a compromise
  expensive.
- **Discovery by scanning.** The service is identifiable and numerous deployments were reachable.

## Detection

Signals that would have shown the attack:

- New jobs submitted from unexpected source addresses, or outside the orchestration system's identity.
- Outbound connections from compute nodes to mining pools or unknown hosts.
- Sudden CPU/GPU saturation with no corresponding experiment.
- New SSH keys, cron entries or processes on head nodes.

## Mitigation

1. **Put authentication in front of the dashboard and Jobs API**, or bind to localhost and use an authenticated
   proxy.
2. **Network isolation**: cluster networks not routable from the internet; explicit allowlists.
3. **Least privilege on instance roles**: a training node should read its dataset and write its artefacts, nothing
   more.
4. **Egress restrictions** from compute nodes.
5. **Inventory and scan** your own estate for exposed ML infrastructure; the attacker is already scanning.

## Lessons learned

- **AI infrastructure inherits every classical risk.** The most damaging AI incidents in this collection are
  infrastructure and software defects, not model failures.
- **"Not a vulnerability" is a deployment assumption, not a defence.** If thousands of deployments expose the
  service, the default is the vulnerability.
- **Compute is valuable.** GPU clusters are worth compromising even without data, which changes the threat model for
  anyone running training infrastructure.
- **CVE disputes are part of the evidence.** Read the record, including the maintainer's response, before citing a
  severity.

## Where this case is used

[Module 03](../modules/03-cybersecurity-fundamentals.md) (infrastructure controls),
[Module 16](../modules/16-secure-ai-apis.md) (authentication at every interface),
[Module 17](../modules/17-red-teaming.md) (discovery and scoping), [P5](../projects/major/p05-agent-sandbox.md)
(containment and least privilege).

## Sources

1. Oligo Security, "ShadowRay: First Known Attack Campaign Targeting AI Workloads Actively Exploited In The Wild",
   2024: <https://www.oligo.security/blog/shadowray-attack-ai-workloads-actively-exploited-in-the-wild>
2. NIST NVD, *CVE-2023-48022*: <https://nvd.nist.gov/vuln/detail/CVE-2023-48022>
