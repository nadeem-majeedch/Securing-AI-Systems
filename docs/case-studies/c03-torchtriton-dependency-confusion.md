---
title: C03 · PyTorch torchtriton dependency confusion
description: A malicious package on PyPI shadowed an internal dependency and exfiltrated data from machines installing nightly builds.
---

# C03 · PyTorch `torchtriton` dependency confusion

!!! info "Evidence status"

    **Documented by vendor security advisory.** PyTorch published what happened, what the payload did, and which
    users were affected. No independent forensic report is public. Read it as a canonical software supply-chain
    compromise in an ML toolchain.

## Background

In December 2022, PyTorch's nightly builds depended on `torchtriton`, distributed from PyTorch's own package index.
An attacker uploaded a package with the same name to the public PyPI index. Because of how the installation was
configured, `pip` could resolve the dependency from PyPI instead — the classic **dependency confusion** pattern.

PyTorch disclosed the compromise on 31 December 2022, after removing the malicious package.

## System architecture

- **PyTorch nightly packages** published to a PyTorch-controlled index.
- A **dependency** (`torchtriton`) that lived on that index.
- **pip** as the installer, with index precedence rules that allowed the public index to win.
- **User machines and CI runners** that installed the nightly packages, often with credentials and SSH keys present.

The boundary that failed was between "an internal package name" and "a name that anyone can publish".

## Security weakness

Two weaknesses composed:

1. **Name resolution across indexes.** A package name is not a namespace; if a public index is consulted, an
   attacker can claim the name.
2. **Install-time execution.** The malicious package executed code during installation or import, with the
   permissions of the installing user.

The first is a supply-chain design flaw; the second turns it into remote code execution on developer machines.

## Threat scenario

1. Attacker learns a dependency name used by a popular project's nightly builds (from a lockfile, an error message
   or a repository).
2. Publishes a package with that name on PyPI, with a version number that satisfies the constraint.
3. A developer or CI job installs the nightly build; pip selects the public package.
4. The package runs, collects host and user information, and exfiltrates it.

The attacker does not need to compromise PyTorch. They need the name and the installer's precedence rule.

## Documented impact

Per the PyTorch advisory, the malicious package:

- Collected host and environment information, including `/etc/passwd`, SSH files, Git configuration and other files
  from the user's home directory.
- Exfiltrated via encrypted DNS queries.
- Ran when Triton was imported; **stable PyTorch releases were not affected**, only nightly builds installed in the
  affected way.

The advisory does not establish how many users installed it or whether exfiltrated data was used.

## Root cause

- **Index precedence was not pinned.** Installation could resolve a dependency from a public index even though the
  project published its own.
- **No integrity check on the dependency.** A hash pin would have failed the install.
- **Nightly builds carried the same trust as releases** in developer workflows, with no warning that they pull from
  a different index.

## Detection

- PyTorch detected the package and removed it, then published an advisory — vendor-side detection.
- On the user side, the signals would be: an unexpected package source in install logs, DNS traffic to unusual
  domains, and a package version that does not exist on the expected index.
- A dependency-diff check in CI (comparing resolved URLs against an allowlist) would have caught the install before
  it ran.

## Mitigation

1. **Pin indexes explicitly** and use `--index-url`/`--extra-index-url` with awareness that extra indexes can
   override; prefer fully specified sources.
2. **Hash-pin dependencies** (`--require-hashes`) so a substituted package fails.
3. **Install untrusted or nightly code in a sandbox** without credentials, with egress restricted.
4. **Treat CI runners as credential-bearing**: scope tokens, avoid long-lived SSH keys, and monitor egress.

## Lessons learned

- **A package name is not a namespace.** Model hubs and package indexes share the property: anyone can publish
  under a name you depend on.
- **Install-time is execution time.** A "dependency" runs with your permissions; that is why lockfiles are a security
  control, not a reproducibility nicety.
- **Nightly and preview channels need a warning label** in developer documentation. Most users do not know which
  index their build pulls from.
- **Encrypted DNS exfiltration defeats naive network monitoring.** Egress allowlisting is the control that works.

## Where this case is used

[Module 15](../modules/15-fine-tuning-supply-chain.md) as the canonical dependency-confusion example;
[MP09](../projects/mini/mp09-supply-chain-checker.md) for artefact verification; [P1](../projects/major/p01-secure-ml-pipeline.md)
for dependency gates.

## Sources

1. PyTorch, "Compromised PyTorch-nightly dependency chain between December 25th and December 30th, 2022", security
   advisory, 31 December 2022: <https://pytorch.org/blog/compromised-nightly-dependency/>
2. Ohm, M., Plate, H., Sykosch, A. and Meier, M., "Backstabber's Knife Collection", *DIMVA* 2020 — the systematic
   review of supply-chain attack mechanisms, including dependency confusion:
   <https://doi.org/10.1007/978-3-030-52683-2_2>
