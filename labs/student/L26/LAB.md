# L26 — An insecure prediction API and its hardened twin

| | |
|---|---|
| **Module** | M16 |
| **Difficulty** | Beginner |
| **Estimated time** | 55 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A data scientist ships a model as a FastAPI endpoint on Friday. It works for the demo. On Monday, the gateway logs show 500s containing Python tracebacks, one client sending 5,000-character inputs, and another calling the endpoint with no credentials at all.

## 2. Problem statement

Run the same eight probes against an insecure app and a hardened one, and require the hardened app to answer with 401, 422 or a generic error instead of 500 or a leaked exception.

## 3. Learning objectives

- Identify the interface failures that are not model failures.
- Add schema validation and size limits.
- Return generic errors without losing observability.
- Read status codes as a security signal.

## 4. Prerequisites

- Python basics; no ML required.

## 5. Required software

- Python 3.12+
- FastAPI
- httpx (TestClient)

## 6. Dataset and input files

- No dataset: the model is a keyword rule; the probes are in the script.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L26/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L26/starter.py
```

1. Write an insecure endpoint that accepts a raw dict and echoes exceptions.
2. Write a hardened endpoint with a Pydantic model, a length bound and an API-key header.
3. Send the same eight probes to both apps.
4. Table status codes and whether each response leaks an error.
5. Assert valid requests succeed, unauthenticated calls get 401, and schema violations get 422.
6. Explain why the insecure app returns 200 with an error body for a missing field.
7. Write the four-item checklist the review will ask for.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L26/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The insecure app returns **200 with `error: 'text'`** for a missing field and for a nested object, and accepts a 5,000-character input. The hardened app returns **401** without a key, **422** for missing, mistyped, empty and oversized inputs, and **200** for the valid request.

## 10. Interpretation of results

The model is identical in both apps. Every difference is a boundary: authentication, schema, size and error handling. The insecure app's 200-with-error is worse than a 500 because monitoring sees success.

## 11. Student tasks

1. Explain why a 200 with an error body is a monitoring problem.
2. Report what the extra `role` field did in each app.
3. Add a request-id header to both apps and explain what it buys.
4. Write the four-item checklist from instruction 7.

## 12. Challenge exercises

1. Add a per-key rate limit and a 429 response.
2. Add structured logging that records the rejection reason without the payload.
3. Add a health endpoint that does not require auth and explain the risk.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. `Field(min_length=1, max_length=200)` gives 422 automatically.
2. `Header(default="")` reads the API key.
3. `TestClient(app, raise_server_exceptions=False)` lets you see 500s.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L26/solution.py
labs/solutions/L26/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Everything is 422 — the header name in the test does not match the parameter alias.
- `AttributeError` on json — the insecure app returned a non-JSON 500; use the relaxed client.
- Valid request fails — the key sent in the header differs from `API_KEY`.
- No 401 ever — you forgot the auth check in the hardened handler.

## 16. Security lessons learned

- Input validation is a security control, not a nicety.
- Error detail is an information leak with no upside.
- The interface, not the model, is usually what gets attacked.

## 17. Submission requirements

- The completed script and probe table.
- The four-item checklist.
- Answers to the tasks.
- One paragraph on what you would monitor after launch.

## 18. Acceptable use

Exercise the insecure and hardened apps through httpx's ASGI transport, or on `127.0.0.1` if you start uvicorn. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not bind the service to `0.0.0.0`, expose it through a tunnel, or reuse the demo `x-api-key` value outside the lab. It is a fixture, not a credential.

## 20. Data handling

No dataset: a keyword rule and in-script probes. Request logs are synthetic and should be deleted rather than archived.

## 21. Cleanup

Stop any uvicorn process you started and delete request or response dumps.

## 22. Restoring your environment

FastAPI, pydantic and httpx are in the pinned environment. No service should be left listening on a port.
