# L30 — Solution: Recovering from a compromised model

**Module:** M19  |  **Difficulty:** Challenge  |  **Time:** 100 minutes

## Approach

The solution verifies the deployed copy, quarantines it, rebuilds and verifies identity, then runs a parity harness seeded from weights and config to show exact restoration and measurable tamper drift.

## Reference results

Detection lists **`config.json`** as the mismatched file while the weights and card still match. The rebuilt bundle verifies **3/3**. Behavioural parity is **0.0** maximum absolute difference for the restored model, while the tampered copy drifts measurably on the same inputs. The sign-off has four closed items and one open root cause.

## Why this works

A config-only tamper is the realistic case: the weights are untouched, the answers look normal, and the only signal is identity. That is why parity is checked against a reference, not against expectation — "it still answers" is exactly the property an attacker wants to preserve.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L30/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Parity is zero for both bundles — the harness ignores config, so a config tamper is invisible.
- `FileNotFoundError` — resolve bundle paths through `data_path`.
- Quarantine copy already exists — the script is idempotent; check before copying.
- Sign-off has no open item — the root cause is not closed in the same run as recovery.

## Marking rubric (100 marks)

- 30 marks — detection and containment evidenced.
- 30 marks — rebuild verified by hash.
- 25 marks — parity harness correct and discriminating.
- 15 marks — sign-off honest about what remains open.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Identity and behaviour are two different checks.
- An artefact that still works is not an artefact you can trust.
- Recovery ends with an owner for the cause, not with a green dashboard.
