---
title: MP09 · AI model supply chain integrity checker
description: Decide whether a model bundle is the one you ordered, and prove it on a clean and a tampered copy.
---

# MP09 · AI model supply chain integrity checker

**After:** Module 15 · **Effort:** 10 h · **Stack:** Python, `hashlib`, `zipfile`, `pickletools`, `pytest`
**Deliverable:** A checker that separates clean from tampered bundles, plus a release-gate policy

## Scenario

A media company fine-tunes an open-weight model on its archive to tag footage. The pipeline pulls a base model by
name from a public hub, installs dependencies from a requirements file that includes two Git URLs, and publishes
the tuned weights to an internal registry under a tag.

A partner will consume the model through an API. Their security team asks: *how do you verify the integrity of the
model you deploy?* Right now nobody can answer with anything but confidence.

## What you build

1. **A bundle format.** Model weights (any small artefact you can produce), a `tokenizer/` directory, a
   `config.json`, a `manifest.json` listing a digest per file, and a `card.md` describing intended use.
2. **A checker** that:
   - verifies every file digest against the manifest and reports **missing**, **extra** and **modified** files;
   - refuses a manifest whose own digest does not match a value obtained from a separate channel
     (`--expected-root <hex>`);
   - inspects the artefact format and rejects a bundle containing executable pickle opcodes instead of data-only
     tensors where the format allows the distinction;
   - prints a verdict per check with a machine-readable exit code.
3. **A tamper kit.** Scripts or fixtures that produce, from a clean bundle: a modified weight file, an extra file, a
   removed file, and a bundle whose manifest was regenerated after tampering. The last one must fail **only** with
   the separate-channel root value — which is the point of the exercise.
4. **A release-gate policy.** Six checks with thresholds and owners, written as a table a build pipeline could read.
5. **A partner answer.** 200 words citing the procedure, not the confidence.

## Suggested structure

```text
supplychain/
  bundle.py     build_bundle(dir), digest_tree(dir) -> dict[path, sha256]
  check.py      verify(dir, expected_root) -> list[Check]
  inspect.py    format_is_data_only(path) -> (bool, reason)
  cli.py        build | verify | inspect
fixtures/
  clean/ tampered_weight/ extra_file/ missing_file/ manifest_regen/
tests/
  test_check.py
```

## Checkpoints

| # | Checkpoint | Hours | Evidence |
|---|---|---|---|
| 1 | Bundle format and clean build | 2 | Clean bundle verifies with its own root |
| 2 | Digest verification and failure taxonomy | 3 | Three tampered fixtures each produce a distinct failure |
| 3 | Manifest-regeneration case | 2 | Fails only when the expected root is supplied; passes without it — and you explain why |
| 4 | Format inspection | 2 | A pickle-opcode fixture is rejected with a reason |
| 5 | Gate policy and partner answer | 1 | Six gates, each with a failure mode |

## Deliverables

| Item | Format | Notes |
|---|---|---|
| Checker | Python CLI | Exit codes documented |
| Fixtures | Directory set | Clean plus four tampered variants |
| Tests | `pytest` | At least eight, including the regenerated-manifest case |
| Gate policy | Markdown table | Check, threshold, failure mode, owner |
| Partner answer | 200 words | Two residual risks disclosed |

## Questions you must answer

1. Your manifest travels inside the bundle. What class of tampering does that fail to catch, and what is the
   cheapest control that catches it?
2. Digest verification proves identity. What does it not prove about behaviour, and how would you check that
   cheaply?
3. Your dependency install runs at build time with a token. Which identity should it use, and what would an
   attacker gain from a malicious Git dependency there?

## Rubric

Apply the [shared mini-project rubric](../guidance/rubrics.md#mini-project-rubric), with these two indicators:

| Extra indicator | Proficient | Exemplary |
|---|---|---|
| **Threat coverage** | Detects modified and extra files | Detects manifest regeneration via an independent root, and explains the remaining gap |
| **Gate design** | Six checks listed | Each gate names its evidence, threshold, failure mode and owner, including the missing-evidence case |

## Extension challenges

1. Add a Merkle root over the manifest so a single value can be published in a contract or a registry.
2. Add a behavioural check: run a fixed probe set through the artefact and compare outputs with a stored reference.
3. Write the incident procedure for discovering, after deployment, that a running artefact's digest does not match.

## Boundaries

Use only artefacts you build. Do not download and redistribute third-party weights, and do not execute untrusted
pickles outside a sandbox with no credentials or network.
