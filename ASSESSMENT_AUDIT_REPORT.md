# Assessment audit report

**Every question, key, explanation and rubric checked.** The module banks were parsed from JSON, the rendered pages were parsed from HTML/Markdown, and the printed answer keys were compared with both. This is the area where a plausible-looking course most often fails quietly, so the checks were done by machine rather than by sampling.

## 1. Inventory

| Instrument | Count | Structure |
|---|---|---|
| Module quizzes | 20 (one per module) | 10 MCQ + 2 short + 2 conceptual + 2 scenario + 1 practical each |
| Module MCQs | **200** | four options, one correct, explanation, per-distractor notes, outcome code, difficulty tag |
| Written module items | 120 | 6 per module |
| Level papers | 4 (`levels.json`) | 8 MCQ + 3 written each, 45 min, pass 70 |
| Final paper | 1 (`final.json`) | 12 MCQ + written section, pass mark stated |
| Assignments | 12 | scenario, requirements, rubric |
| Answer pages | 26 | 20 module keys + 4 level keys + final key + index |
| Learning outcomes | 5 per module | 100 outcome codes, every MCQ tagged to one |

Render pipeline: `assessments/build.py` reads the JSON banks, rotates option order deterministically per question, embeds the key as `<script type="application/json" id="sas-key-mNN">` in the page, and writes the printed key in the rotated lettering. The rotation is what prevents a student from learning "the answer is always the long one in position B".

## 2. Integrity checks and results

| Check | Result |
|---|---|
| Duplicate question stems (200 items) | **0** |
| Answer index within range / ≥3 options | 200/200 |
| Duplicate options within a question | 0 |
| Explanation ≥ 40 characters | 200/200 |
| Per-distractor "why this is wrong" notes | 200/200 |
| Outcome code valid (`Mnn.k`) | 200/200 |
| Rendered page question count = JSON count | 20/20 modules |
| Page option order matches embedded key index | **200/200** |
| Printed key letter matches embedded key index | **200/200** |
| Printed key text matches the correct option's text | **200/200** |
| Rendered key distribution across A/B/C/D | 48 / 50 / 52 / 50 |
| Worst per-module concentration | 3 of 10 items share a letter |

The 200/200 rows are the important ones: they mean the page a student sees, the key embedded in that page, and the printed key all agree, letter for letter and word for word. A single mismatch would mean either a student marked wrong for a right answer or a key that reveals the wrong option; there are none.

The source JSON is deliberately not letter-balanced (157 of 200 correct answers are stored at index 1), which is harmless because the renderer rotates: the rendered distribution is 48/50/52/50 and no module has more than three items keyed to the same letter.

## 3. Content quality

- **Ambiguity.** No item offers two defensible answers. Distractor notes pre-empt the near-misses (e.g. "Consent changes the legal basis, not the leak").
- **Coverage.** Each module's 10 MCQs are tagged to its five outcomes, so a student can see which outcome a miss belongs to, and the key page groups explanations by outcome.
- **Level papers.** The four papers are cumulative and increase in judgement load: Level 1 asks recall and application, Level 4 asks refusal and residual-risk writing ("state the assumption that would defeat your argument"). They are not rescaled copies of the module quizzes; the stems are distinct.
- **Assignments.** Twelve scenarios (hospital threat model, fraud pipeline, poisoning investigation, robustness evaluation, privacy assessment, extraction, chatbot security, RAG, agent authorisation, supply chain, security audit, monitoring) each pair a deliverable with a rubric whose bands name observable qualities rather than word counts.
- **Projects.** 10 mini projects, 6 major projects and 5 capstone proposals; the majors carry 18 sections (architecture, threat model, functional/security/dataset requirements, testing, metrics, deliverables, rubric). Cross-project text similarity stays under 0.12, so they are genuinely different systems rather than one template renamed.

## 4. Findings

| Severity | Finding | State |
|---|---|---|
| Medium | **Answer-length cue in six modules.** The builder's own check flags M09, M11, M13, M15, M16 and M17: the correct option is materially longer than every distractor in 6–9 of 10 items. Answers are correct; the cue lets a test-wise student score without knowing the subject. | open |
| Low | The stored bank is heavily skewed to option index 1. Invisible to students because the renderer rotates, but any future export that skips rotation would expose it. | note |
| Info | Written items carry model answers in the JSON rather than in the printed key, so a student reading the key page sees the MCQ explanations and the written marking guidance separately — deliberate, and consistent across all 20 modules. | note |

No duplicate stems, no wrong keys, no ambiguous items, no missing explanations, and no mismatch between what is graded and what is printed.
