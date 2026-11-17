# L26 — Solution: An insecure prediction API and its hardened twin

**Module:** M16  |  **Difficulty:** Beginner  |  **Time:** 55 minutes

## Approach

The solution defines both apps, drives eight identical probes through `TestClient`, and asserts the status codes that separate the two. A control table names the four boundaries.

## Reference results

The insecure app returns **200 with `error: 'text'`** for a missing field and for a nested object, and accepts a 5,000-character input. The hardened app returns **401** without a key, **422** for missing, mistyped, empty and oversized inputs, and **200** for the valid request.

## Why this works

The model is identical in both apps. Every difference is a boundary: authentication, schema, size and error handling. The insecure app's 200-with-error is worse than a 500 because monitoring sees success.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L26/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- Everything is 422 — the header name in the test does not match the parameter alias.
- `AttributeError` on json — the insecure app returned a non-JSON 500; use the relaxed client.
- Valid request fails — the key sent in the header differs from `API_KEY`.
- No 401 ever — you forgot the auth check in the hardened handler.

## Marking rubric (100 marks)

- 35 marks — both apps correct and probes complete.
- 30 marks — status codes interpreted correctly.
- 20 marks — leak explanation is accurate.
- 15 marks — checklist is specific.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Input validation is a security control, not a nicety.
- Error detail is an information leak with no upside.
- The interface, not the model, is usually what gets attacked.
