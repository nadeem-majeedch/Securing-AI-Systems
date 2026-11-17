# L27 — Solution: Rate limits and abuse controls on a prediction API

**Module:** M17  |  **Difficulty:** Intermediate  |  **Time:** 70 minutes

## Approach

The solution aggregates the logs, applies a fixed window and a token bucket with an export quota, and reports blocked abusive requests alongside affected honest principals for both controls.

## Reference results

The abusive principal `user-13` issues **2 requests per minute** for 26 minutes, then exports for 16 minutes at 4.8 KB each. The **8/10-minute window blocks 37** of its requests and **0** honest principals' requests. The token bucket blocks **12** by rate and **13** by export quota, total **25**, also with **0** honest impact.

## Why this works

A 4-per-minute window would have missed the burst entirely — the attacker is slow by design. The window only bites once it is set against the honest baseline, and even then it caps requests, not volume: the export quota is what limits damage.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L27/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Blocked is zero — the window is shorter than the attack cadence; use 10 minutes.
- Every principal blocked — the limit is below the honest baseline; check the top table first.
- Bucket drains and never refills — `elapsed` is negative or in the wrong units.
- `dt` accessor fails — `ts` is still a string; parse it first.

## Marking rubric (100 marks)

- 35 marks — both controls implemented correctly.
- 30 marks — collateral impact measured.
- 20 marks — volume-versus-rate distinction explained.
- 15 marks — policy is specific.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Limits are policy decisions that need a baseline measurement.
- Request rate and data volume are different risks.
- Collateral impact is a metric, not an opinion.
