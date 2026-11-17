# L32 — A release gate that reads evidence

| | |
|---|---|
| **Module** | M20 |
| **Difficulty** | Challenge |
| **Estimated time** | 110 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

Eight labs' worth of evidence exists in eight folders, and the release decision is still made in a meeting. The head of engineering wants a gate that reads the evidence, applies the declared thresholds and blocks the release with a reason — including when an artefact is simply missing.

## 2. Problem statement

Assemble eight gates from earlier labs into one evaluator, run a complete release and three failing variants, and record what the gate does and does not let you claim.

## 3. Learning objectives

- Turn security claims into thresholds with directions.
- Treat missing evidence as a block, never a warning.
- Produce a per-gate reason a reviewer can act on.
- State the limits of a passing gate.

## 4. Prerequisites

- L02, L12/13, L14, L19, L22, L23, L24, L28.

## 5. Required software

- Python 3.12+
- pandas

## 6. Dataset and input files

- No dataset: the gate is scored on eight evidence values carried in the starter, each labelled with the lab whose
  solution produces it. To re-derive any value, run that lab's solution and read its printed line.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L32/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L32/starter.py
```

1. Define eight gates with id, metric, threshold, direction and producing lab.
2. Write `evaluate(evidence)` returning a decision and a per-gate table.
3. Run a complete release where every gate passes.
4. Run three failing variants: missing evidence, weak robustness, leaky privacy.
5. Assert the complete case releases and all three variants block.
6. Table the evidence record fields and why each is needed.
7. Write the claim the gate supports.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L32/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

The complete set — utility **0.839**, robust accuracy **0.234**, privacy **0.054**, injection ASR **0.00**, ACL **1.00**, integrity **1.00**, unauthorised allows **0.00**, coverage **1.00** — releases. Removing the ACL gate blocks with *evidence missing*; lowering robust accuracy to **0.07** blocks *below 0.15*; raising privacy leakage to **0.42** blocks *below 0.25*.

## 10. Interpretation of results

Three different failures produce three different reasons, which is the point: a reviewer can act on *evidence missing* differently from *below threshold*. The direction field is what stops a metric like leakage, where lower is better, from being read backwards under deadline pressure.

## 11. Student tasks

1. Explain why a missing artefact is a block rather than a warning.
2. Report which gate you would remove first if the team needed to ship, and the risk that carries.
3. Add an expiry field and describe what it prevents.
4. Write the claim from instruction 7.

## 12. Challenge exercises

1. Add a gate that reads a real artefact file and parses its number.
2. Add a waiver mechanism with an approver, and state the audit requirement.
3. Make the gate emit a machine-readable report for a dashboard.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Store direction per gate; default to `above` but be explicit about it.
2. Missing key means blocked, not skipped.
3. Every row needs a reason string built from the rule, not prose.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L32/solution.py
labs/solutions/L32/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- Complete evidence blocks — a threshold or direction is wrong for that metric.
- Missing evidence passes — you used `evidence.get(id, {}).get('value', 0)`.
- All blocks look the same — the reason is not including the rule.
- `KeyError` on evidence — check the gate id matches the evidence key.

## 16. Security lessons learned

- A gate is a set of declarations, not a score.
- Missing evidence is the most common real failure.
- A passing gate supports a specific claim, not a general assurance.

## 17. Submission requirements

- The completed script and the four evaluations.
- The evidence record table.
- The claim statement.
- Answers to the tasks.

## 18. Acceptable use

Run the gate over the evidence values taken from the referenced labs' outputs. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

This gate does not approve a real release. Do not wire it to a deployment pipeline or use it to sign off a system outside the course.

## 20. Data handling

The evidence values are the solutions' published results, reproduced in the starter and labelled by lab; no production metrics are involved.

## 21. Cleanup

Delete any gate report you generated; nothing else is written.

## 22. Restoring your environment

If you ran other labs to produce evidence, that is the only state to clean up. No services remain from this lab.
