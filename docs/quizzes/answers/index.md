---
title: Answer keys
description: How the answer keys are organised, and how to use model answers without defeating the assessment.
hide:
  - toc
---

# Answer keys

Every question in this course has a published answer, a rationale for the correct option, a reason each distractor
is wrong, and — for written items — a model answer with the marks it would earn.

Nothing here is secret. The keys are separate pages for one reason: so that you meet the question before the
answer.

## How the keys are organised

| Key | Covers | What it gives |
|---|---|---|
| [Module keys](m01.md) | 10 MCQ + 9 written per module | Correct option, why each distractor is wrong, outcome tag, model answer |
| [Level keys](level-1.md) | 8 MCQ + 3 written per level | Same, with the level's marking band |
| [Final key](final.md) | 12 MCQ + 4 written | Same, with the pass mark and how to apportion partial credit |

Each module key repeats the question text, so you do not need two browser windows open. That is a convenience, not
an invitation: reading the key before attempting the item converts a diagnostic into a reading exercise.

## Reading a module key

A multiple-choice entry looks like this:

```
### Q3 — Application · M07.4

Which signal would detect a backdoor that fires only on a rare trigger?

- [ ] A. Overall validation accuracy
- [x] B. Accuracy on a held-out slice containing the trigger class
- [ ] C. Training loss
- [ ] D. Inference latency

Correct answer: **B** — a trigger-specific effect is invisible in aggregate metrics, so
the test must sample the region the trigger affects.

Why not A: aggregate accuracy moves too little to notice...
```

Three things are worth using:

1. **The outcome tag** (`M07.4`) points to the learning objective on the module page. If you missed the item, that
   is the section to reread — not the whole module.
2. **The "why not" lines** matter more than the answer. Most misconceptions in this field are a distractor that is
   *nearly* right: effective in another deployment, or measured in the wrong place.
3. **The difficulty tag** tells you what the item was testing. A *Recall* item you missed is a gap; a *Judgement*
   item you missed is a skill to practise in the assignments.

## Marking written answers

Model answers are "what a good answer contains", not "the only correct wording". Mark by key points:

1. Extract the key points from the model answer as bullets.
2. Award one mark per key point you covered, up to the item total.
3. Deduct one mark for an unsupported quantitative claim.
4. Do not deduct for a different approach that is better supported.

The [self-assessment guide](../self-assessment.md) describes the schedule and the bands in more detail.

## If an answer looks wrong

It might be. Every item was checked for a single defensible answer, no duplicate options, no "all of the above",
and an explanation that matches the marked option, but a course of 244 graded items written by one author will
contain an error somewhere.

If you find one, record the item id, your reasoning and the answer you believe is correct. A worked disagreement
is worth more than a silent correction, and if you are studying for credit, take it to your instructor with the
evidence.
