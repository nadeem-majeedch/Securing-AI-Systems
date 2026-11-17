---
title: C05 · Malicious models on a public hub
description: Model artefacts that execute code on load — what a 2024 analysis found, and what the hub's scanning does and does not catch.
---

# C05 · Malicious models on a public hub

!!! info "Evidence status"

    **Documented research finding plus vendor documentation.** A security firm analysed models on a public hub and
    reported a set that behaved maliciously on load; the hub documents its scanning and its limits. Public evidence
    does not establish that a victim was compromised by the specific sample described.

## Background

PyTorch's default serialisation for many models is Python `pickle`, which is capable of executing arbitrary code
when deserialised. A model file is therefore not necessarily data: loading it can run code with the loader's
permissions. Research in 2024 examined public model repositories for artefacts that abused this.

The hub in question — Hugging Face — has published documentation on pickle scanning and its limitations, and offers
safer formats for many model families.

## System architecture

- **Model hub**: hosting for model files, tokenisers, configs and cards.
- **Client libraries** (`transformers`, `torch.load`) that download and load artefacts.
- **Loading process** running in the data scientist's environment, often with credentials, datasets and network
  access.
- **Scanning** performed by the hub on upload, with documented limits.

The trust boundary is the load call: before it, the artefact is a file; after it, code may have run.

## Security weakness

**Deserialisation of untrusted data.** A pickle stream can encode function calls, so a crafted model file can
execute a payload when loaded. The weakness is in the format and the loading habit, not in the model's architecture.

Secondary weaknesses that make it worse:

- Loading models directly from a hub by name, in an environment with cloud credentials.
- No verification of the artefact's publisher or digest.
- Assumption that "it is just weights".

## Threat scenario

1. Attacker publishes a model with an attractive name or a plausible fine-tune.
2. The artefact contains a payload that runs on load, for example a reverse shell or credential exfiltration.
3. A practitioner downloads and loads it in a notebook or training job with credentials present.
4. The payload executes with the practitioner's permissions.

Variants: a malicious `tokenizer` or config, a dependency in the model repository that installs on import, or a
legitimate model replaced later (a rug pull).

## Documented impact

- JFrog's analysis reported on the order of one hundred models with malicious functionality after filtering false
  positives, including a PyTorch model using pickle `__reduce__` to attempt a reverse shell.
- The demonstrated risk is code execution on the loading machine.
- **Not established:** that any organisation was compromised by these samples, or that the hub's defences failed for
  a specific victim.

## Root cause

- **Format choice.** Pickle is code-capable; safety depends on trusting the producer.
- **Loading habit.** Practitioners load artefacts from public sources in privileged environments.
- **Trust in names.** Popularity and naming are not provenance.

## Detection

- Static inspection of the artefact before loading (opcode scanning, `pickletools`).
- The hub's scanning, which is documented as partial: it reduces risk, it does not eliminate it.
- Runtime signals: unexpected outbound connections or child processes during a model load.
- A load in a sandbox with no credentials and no network — the control that makes detection unnecessary for the
  first stage.

## Mitigation

1. **Prefer data-only formats** (for example `safetensors`) where the ecosystem supports them, and require them for
   internally produced artefacts.
2. **Load untrusted models in a sandbox** with no credentials, restricted egress and a disposable filesystem.
3. **Verify provenance**: publisher identity, digest, and a manifest obtained independently.
4. **Pin and review** model revisions rather than tracking a moving branch.
5. **Never load a downloaded artefact into a process holding production credentials.**

## Lessons learned

- **A model file is executable content.** Treat it like code from the internet, because in pickle form it is.
- **Format policy is a security control.** Choosing safetensors over pickle is a decision with a threat-model
  justification.
- **Hub scanning is a mitigation, not a guarantee.** The vendor's own documentation says so; cite it.
- **Sandboxing is cheap relative to the alternative.** A container with no credentials turns a compromise into a
  curiosity.

## Where this case is used

[Module 15](../modules/15-fine-tuning-supply-chain.md) (artefact trust),
[MP09](../projects/mini/mp09-supply-chain-checker.md) (format inspection and digest verification),
[P1](../projects/major/p01-secure-ml-pipeline.md) (packaging and loading by digest).

## Sources

1. JFrog Security Research, "Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor",
   2024: <https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/>
2. Hugging Face, *Pickle scanning* (security documentation describing what is scanned and its limitations):
   <https://huggingface.co/docs/hub/security-pickle>
3. Zhao, J. et al., "Models Are Codes: Towards Measuring Malicious Code Poisoning Attacks on Pre-trained Model Hubs",
   *ASE* 2024: <https://doi.org/10.1145/3691620.3695271>
