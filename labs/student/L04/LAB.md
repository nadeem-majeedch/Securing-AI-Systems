# L04 — Least privilege for an analytics platform

| | |
|---|---|
| **Module** | M03 |
| **Difficulty** | Intermediate |
| **Estimated time** | 60 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

An analytics platform holds raw extracts, curated tables and the production model. Support staff increasingly ask for access to analytics data to answer tickets faster, and a manager wants to export sensitive tables for a board pack. Nobody can say which requests are legitimate, because there is no written policy — only habits.

## 2. Problem statement

Implement a deny-by-default policy engine over principals, roles, actions and resources, then run a ten-case matrix that includes the legitimate requests, the cross-team request and the unknown principal. Every denial must name the check that failed.

## 3. Learning objectives

- Express authorisation as data rather than prose.
- Implement deny-by-default with explicit allow rules.
- Distinguish authentication failure from authorisation failure.
- Produce an audit-ready decision table with reasons.

## 4. Prerequisites

- Module 03 lecture; L03 recommended.

## 5. Required software

- Python 3.12+ (standard library only)

## 6. Dataset and input files

- No file input: principals, resources and policy are defined in the starter script so they can be reviewed.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L04/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L04/starter.py
```

1. Read the principal, resource and policy tables in the starter.
2. Implement `decide(principal, action, resource, amount)` returning `(allowed, reason)`.
3. Check, in order: unknown principal, unknown action, role, resource scope, sensitive-export approval, spend limit.
4. Run the ten-case matrix and print decisions with reasons.
5. Assert that an unknown principal and an unknown action are both denied.
6. Assert that support cannot read the analytics dataset and that a manager can export their own sensitive data.
7. Summarise the denial reasons and state which control each one exercises.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L04/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The matrix produces **five allows and five denials**. Denials cover `role not permitted` (analyst writing, support reading), `cross-team resource` (manager refunding a support ticket), `unknown principal` (mallory) and `sensitive export requires elevated approval` is available as a path you can exercise by lowering the manager's spend limit.

## 10. Interpretation of results

The interesting cases are not the obvious denials but the ones that look reasonable: a support agent reading a curated table to answer a ticket, and a manager exporting a sensitive table. Both fail a check that exists for a reason. Reasons in the output are what make the policy reviewable — "denied" alone tells an auditor nothing.

## 11. Student tasks

1. Add a `data_steward` role that can read raw data but not export it, and add two test cases.
2. Change the policy so export requires two roles, and report which matrix rows change.
3. Explain why the order of checks matters when the principal is unknown.
4. Write the log line you would emit per decision, with the fields an incident reviewer needs.

## 12. Challenge exercises

1. Add time-of-day restrictions for sensitive exports and show a test that fails outside the window.
2. Implement a second policy source (a JSON file) and reject the config if a role is unknown.
3. Design the approval workflow for sensitive export, including what happens when the approver is away.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Return early on the first failing check; the reason is then unambiguous.
2. Use sets for role intersection: `set(rule['roles']) & set(person['roles'])`.
3. Keep the deny branch as the default return, so forgetting a rule fails closed.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L04/solution.py
labs/solutions/L04/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Everything allowed — you probably wrote `return True` before the checks.
- `TypeError: unhashable` — you compared lists with `&`; convert both to sets.
- Cross-team denial never triggers — the resource key is misspelt and hits `unknown resource` first.
- Spend limit never triggers — pass `amount` as an int, not a string.

## 16. Security lessons learned

- Policy belongs in data so it can be diffed, tested and reviewed.
- Deny-by-default is a code shape, not an intention.
- A denial without a reason cannot be investigated or appealed.

## 17. Submission requirements

- The completed script and decision matrix.
- The two added test cases from task 1 with their expected outcomes.
- A short policy note: who may export sensitive data, and under what conditions.
- Answers to the remaining tasks.

## 18. Acceptable use

Evaluate the policy engine against the principals and resources defined in the starter. It is a table-top authorisation exercise. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not run this against a cloud IAM service, an identity provider or an analytics platform you can reach. The engine models authorisation; it is not a client for a real system.

## 20. Data handling

Principals, roles and resources are invented and the policy is synthetic. No credentials appear anywhere and none should be added, not even a placeholder that looks real.

## 21. Cleanup

The lab writes nothing. Remove any decision table you exported before moving on.

## 22. Restoring your environment

Nothing is installed and nothing needs to be undone.
