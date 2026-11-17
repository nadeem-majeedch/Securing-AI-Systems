# L27 — Rate limits and abuse controls on a prediction API

| | |
|---|---|
| **Module** | M17 |
| **Difficulty** | Intermediate |
| **Estimated time** | 70 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

Three hours of gateway logs show one principal failing authentication repeatedly, then switching to export calls that return 4.8 KB each. The service has no rate limit. Product wants one, and support wants to know how many legitimate customers it will break.

## 2. Problem statement

Apply a fixed-window limit and a token bucket with an export quota to real-shaped logs, and measure blocked abusive requests against affected honest principals.

## 3. Learning objectives

- Aggregate logs into per-principal behaviour.
- Implement a fixed window and a token bucket.
- Measure collateral impact instead of assuming it is zero.
- Explain why a quota on export volume is separate from a request rate.

## 4. Prerequisites

- L26 recommended.

## 5. Required software

- Python 3.12+
- pandas
- NumPy

## 6. Dataset and input files

- `labs/datasets/api_logs.csv` — 1,037 requests over three hours, one principal abusing the API.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L27/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L27/starter.py
```

1. Load the logs, parse timestamps and table the top principals.
2. Compute per-principal request, 401, export and byte totals.
3. Apply a fixed 8-per-10-minute window and compute blocked requests per principal.
4. Measure how many honest principals are affected.
5. Implement a token bucket (capacity 6, refill 1.5/min) with a 3-export quota.
6. Compare the two controls on blocked abusive requests and honest impact.
7. Assert the window catches the burst, honest impact stays small and the export quota bites.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L27/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The abusive principal `user-13` issues **2 requests per minute** for 26 minutes, then exports for 16 minutes at 4.8 KB each. The **8/10-minute window blocks 37** of its requests and **0** honest principals' requests. The token bucket blocks **12** by rate and **13** by export quota, total **25**, also with **0** honest impact.

## 10. Interpretation of results

A 4-per-minute window would have missed the burst entirely — the attacker is slow by design. The window only bites once it is set against the honest baseline, and even then it caps requests, not volume: the export quota is what limits damage.

## 11. Student tasks

1. Report the highest honest per-10-minute count and what limit would start affecting it.
2. Explain why the token bucket blocks fewer requests than the fixed window.
3. State the response you would send to a customer who hits the export quota legitimately.
4. Write the one-paragraph policy for the product team.

## 12. Challenge exercises

1. Add a sliding window and report the difference on the burst.
2. Add per-endpoint limits and measure the effect on the export burst.
3. Design an alert that fires on a principal crossing 3 quotas in an hour.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Floor timestamps to the window: `ts.dt.floor('10min')`.
2. Token bucket state is per principal: store `(tokens, last_seen)`.
3. Count blocked requests as `count - LIMIT`, not as whole windows.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L27/solution.py
labs/solutions/L27/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Blocked is zero — the window is shorter than the attack cadence; use 10 minutes.
- Every principal blocked — the limit is below the honest baseline; check the top table first.
- Bucket drains and never refills — `elapsed` is negative or in the wrong units.
- `dt` accessor fails — `ts` is still a string; parse it first.

## 16. Security lessons learned

- Limits are policy decisions that need a baseline measurement.
- Request rate and data volume are different risks.
- Collateral impact is a metric, not an opinion.

## 17. Submission requirements

- The completed script and both comparison tables.
- The policy paragraph.
- Answers to the tasks.
- One paragraph on how you would tune the limit in production.

## 18. Acceptable use

Replay `api_logs.csv` through the limiter implementations you write. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not load-test a real API, and do not use the abuse pattern against a service you do not own.

## 20. Data handling

Log entries are synthetic, but they imitate principals and volumes. Keep the file in `labs/datasets/`.

## 21. Cleanup

Delete any replay output or limiter state file.

## 22. Restoring your environment

Core stack only.
