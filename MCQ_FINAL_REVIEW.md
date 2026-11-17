# MCQ final review

**All 36 remaining flagged items reviewed individually, and all 200 questions re-validated.** The items were
technically sound; the only defect was the length gap that lets a test-wise student guess. Each was fixed by making
its longest distractor as specific as the correct answer — no correct answer, explanation, difficulty or outcome was
changed.

## 1. What was reviewed, per module

| Module | Items flagged | Technical accuracy | Distractor plausibility | Ambiguity | Action |
|---|---|---|---|---|---|
| M03 | 4 | Correct — hashing vs encryption, cluster isolation, scoped tokens, secrets in memory | Fine; two distractors were thin one-liners | None | 4 distractors extended |
| M04 | 2 | Correct — attack trees, risk communication | Fine | None | 2 extended |
| M05 | 5 | Correct — DP epsilon, erasure, provenance, social-data ingestion, unverifiable features | Fine | None | 5 extended |
| M06 | 2 | Correct — perturbation perceptibility, transfer causes | Fine | None | 2 extended |
| M07 | 4 | Correct — poisoning budget, clean-label attacks, slice metrics, provenance defence | Fine | None | 4 extended |
| M08 | 5 | Correct — certified radius, honest claims, adaptive attacks, latency trade-off | Fine | None | 5 extended |
| M10 | 5 | Correct — label-only extraction, boundary queries, quotas, fidelity vs accuracy, detection signal | Fine | None | 5 extended |
| M12 | 5 | Correct — token channel, prompt-level defences, jailbreak vs exfiltration, base rates, reproducibility | Fine | None | 5 extended |
| M14 | 4 | Correct — confused deputy, multi-agent authority, parameter validation, sandboxing | Fine | None | 4 extended |
| **Total** | **36** | **0 incorrect** | — | **0 ambiguous** | **36 rewritten** |

One item (M14-Q09) needed a second pass: its first replacement landed one character inside the threshold. The
independent measurement caught it; the builder's gate would not have, because that module was below the 50 % trigger.

## 2. What "improve" meant here

The instruction was to improve only where needed, and to preserve keys and outcomes. The measurement said the only
real defect was length. So the edit rule was narrow:

1. Never touch the correct option (asserted in code before every write).
2. Never touch the explanation or the per-distractor rationale.
3. Extend **one** distractor per item — the longest one — with a concrete detail that makes the misconception more
   convincing, so the item gets better as the cue disappears.

Three examples:

- **M12-Q09** (base-rate problem): *"Blocking is technically impossible for a classifier"* became *"Blocking is
  technically impossible for a probabilistic classifier to do reliably"* — a stronger, still-wrong claim.
- **M14-Q02** (confused deputy): *"The refund tool cannot validate order identifiers"* became *"…against the
  customer's own record"*, which names the exact missing check the correct answer describes.
- **M05-Q06** (erasure): *"Erasure is impossible once a model is trained, so the request can be refused"* became
  *"…can be refused outright"*, matching the correct option's length without weakening the distractor.

No answer became less defensible, and no distractor became accidentally correct — each was checked against its
retained rationale.

## 3. Bank-wide checks

| Check | Result |
|---|---|
| Items with a correct-answer length cue | **0** |
| Items with a reverse cue (distractor much longer than the answer) | **0** |
| Correct answer text changed | **0** |
| Explanations changed | 0 |
| Difficulty or outcome tags changed | 0 |
| Builder quality gate | 0 warnings |
| Duplicate stems / duplicate option sets | 0 / 0 |
| Rendered key distribution (A/B/C/D) | 48 / 50 / 52 / 50 |
| Worst per-module letter concentration | 3 of 10 |
| Page order ↔ embedded key index | **200/200** |
| Printed key letter ↔ embedded index | **200/200** |
| Printed key text ↔ correct option | **200/200** |

## 4. What a student experiences now

Across all 20 quizzes, no option is conspicuously longer than the others, and no arrangement reliably points at the
answer. The three plausible strategies a test-wise student uses — longest option, most qualified option, the one that
repeats the stem's vocabulary — were each measured: length is now neutral, and the option order is rotated
deterministically so a fixed letter cannot be learned.

## 5. Residual notes

- **Difficulty was preserved, not re-measured.** The tags (Recall / Application / Judgement) were untouched; this
  review did not run the items past students, so the claimed difficulty remains an author judgement.
- **Six level-paper items** were not part of this pass; they were inspected during Task 13 and carry no length cue.
- **The bank's stored option order is still skewed** toward index 1 (157 of 200). Students never see the stored order
  because the renderer rotates, and the rendered distribution above is what matters, but an export that skipped the
  renderer would expose it. Recorded, not changed.
