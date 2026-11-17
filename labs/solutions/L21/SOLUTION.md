# L21 — Solution: RAG retrieval that leaks one document

**Module:** M13  |  **Difficulty:** Intermediate  |  **Time:** 70 minutes

## Approach

The solution builds both pipelines on the same 12-document corpus, prints the prompts and the visible sets, and asserts the presence and absence of the beta salary text. A comparison table quantifies the foreign documents in each prompt.

## Reference results

For alpha, the buggy pipeline retrieves three documents including **d06 (beta salary bands)**, shows only alpha documents, and the prompt still contains **1 foreign document**. The fixed pipeline returns **d01, d02, d03**, none foreign, and the prompt contains no beta text.

## Why this works

The display filter hides the evidence from the person who could report it while the model reads the foreign text and can paraphrase it. Access control has to constrain retrieval, because the prompt is the real disclosure boundary — and even then, d11 shows that authorised text can carry instructions.

## Implementation

The complete script is `solution.py` in this directory. Run it from the project root:

```bash
python labs/solutions/L21/solution.py
```

It prints the tables quoted above and asserts the lab's key invariants, so a silent regression fails the
script rather than passing quietly.

## Common mistakes

- `All arrays must be of the same length` — you passed the dict wrapper to `DataFrame`; use `['documents']`.
- Fixed pipeline still leaks — you filtered after slicing top-k.
- `KeyError: 'id'` — the field is `doc_id`; rename it.
- No leak reproduced — your query does not match the foreign document; use the salary query.

## Marking rubric (100 marks)

- 35 marks — leak reproduced and explained.
- 30 marks — fix correct and verified.
- 20 marks — comparison quantified.
- 15 marks — remediation is specific.

## Model answer guidance

A strong submission explains *why* each step is needed, not only that it ran. In particular:

- Post-filtering hides the leak from the user, not from the model.
- ACLs belong in candidate selection.
- Authorization does not make text trustworthy.
