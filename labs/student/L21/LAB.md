# L21 — RAG retrieval that leaks one document

| | |
|---|---|
| **Module** | M13 |
| **Difficulty** | Intermediate |
| **Estimated time** | 70 minutes |
| **Format** | Individual, self-paced |
| **Submission** | See the final section |

## 1. Scenario

A multi-tenant support assistant retrieves the top three documents for any question and shows the user only the ones they may see. The interface looks correct. A tenant asks how a competitor's salary bands appeared in an answer, and the engineering lead says the filter is applied.

## 2. Problem statement

Reproduce the leak in a two-tenant index, show that post-filtering leaves foreign text in the prompt, fix the order so the ACL selects candidates, and verify the leak is gone.

## 3. Learning objectives

- Distinguish retrieval filtering from display filtering.
- Show the prompt as the place where a leak becomes an answer.
- Implement tenant-scoped candidate selection.
- Explain why an ACL field is a data-governance control.

## 4. Prerequisites

- L16 recommended; basic TF-IDF.

## 5. Required software

- Python 3.12+
- scikit-learn
- pandas

## 6. Dataset and input files

- `labs/datasets/rag_documents.json` — 12 documents across alpha, beta and public tenants.

Run `python labs/scripts/make_datasets.py` once from the project root if any file is missing. Every dataset
is synthetic and generated locally; nothing is downloaded.

## 7. Detailed instructions

Work in `labs/student/L21/starter.py`. Run it whenever you finish a step:

```bash
python labs/student/L21/starter.py
```

1. Load the documents, rename `doc_id` to `id`, and index the text.
2. Implement the buggy pipeline: rank all documents, build the prompt, filter the display.
3. Implement the fixed pipeline: restrict candidates by tenant plus public, then rank.
4. Run the salary-band query for tenant alpha and print retrieved, visible and prompt contents.
5. Assert the buggy prompt contains the beta text and the fixed prompt does not.
6. Table the two pipelines with foreign-document counts.
7. Note the injected document d11 and state what ACL filtering does not fix.

## 8. Python implementation

Your starter file already contains the imports, the dataset loading and one labelled TODO per step. The
complete implementation is `labs/solutions/L21/solution.py` — it is deliberately in a different
directory so you can attempt the work first.

## 9. Expected results

For alpha, the buggy pipeline retrieves three documents including **d06 (beta salary bands)**, shows only alpha documents, and the prompt still contains **1 foreign document**. The fixed pipeline returns **d01, d02, d03**, none foreign, and the prompt contains no beta text.

## 10. Interpretation of results

The display filter hides the evidence from the person who could report it while the model reads the foreign text and can paraphrase it. Access control has to constrain retrieval, because the prompt is the real disclosure boundary — and even then, d11 shows that authorised text can carry instructions.

## 11. Student tasks

1. Explain why the buggy pipeline looks correct in a UI test.
2. Report the number of foreign documents in the prompt for both pipelines.
3. State what happens to the beta document after filtering, and why that is not a fix.
4. Write the remediation ticket in three sentences.

## 12. Challenge exercises

1. Add a per-document sensitivity label and enforce it alongside tenant.
2. Measure whether the fixed pipeline returns fewer useful results, and by how much.
3. Design a test that fails whenever a prompt contains text the requester cannot read.

## 13. Hints

Read one at a time; stop as soon as you are unblocked.

1. Compute scores on the whole matrix for the buggy version; on a subset for the fixed one.
2. The visible set and the prompt are two different objects — print both.
3. Public documents should be visible to every tenant.

## 14. Solution

The worked solution is **not** in this folder. It is at:

```
labs/solutions/L21/solution.py
labs/solutions/L21/SOLUTION.md
```

Attempt every step before opening it. The solution file is executable: run it and compare your output with
section 9.

## 15. Troubleshooting

- `All arrays must be of the same length` — you passed the dict wrapper to `DataFrame`; use `['documents']`.
- Fixed pipeline still leaks — you filtered after slicing top-k.
- `KeyError: 'id'` — the field is `doc_id`; rename it.
- No leak reproduced — your query does not match the foreign document; use the salary query.

## 16. Security lessons learned

- Post-filtering hides the leak from the user, not from the model.
- ACLs belong in candidate selection.
- Authorization does not make text trustworthy.

## 17. Submission requirements

- The completed script and both prompts.
- The pipeline comparison table.
- The remediation ticket.
- Answers to the tasks.

## 18. Acceptable use

Query the local index built from `rag_documents.json` across the alpha, beta and public tenants. Work on your own machine, and read the course-wide rules in `docs/getting-started/academic-integrity.md` before you begin.

## 19. Scope restrictions

Do not ingest real documents, customer records or an employer's knowledge base. The tenancy boundary is demonstrated entirely on synthetic content.

## 20. Data handling

Twelve synthetic documents, one of which contains an instruction by design. Treat retrieved text as untrusted when you quote it in your report.

## 21. Cleanup

Delete the vector store directory or embeddings file you created; the lab otherwise keeps the index in memory.

## 22. Restoring your environment

Core stack only; no database service is required.
