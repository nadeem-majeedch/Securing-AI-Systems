"""L21 — RAG retrieval that leaks one document (M13, Intermediate).

Goal: show that filtering results after retrieval does not help if the prompt was already built, fix the order,
and state the control that makes the fix enforceable.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "common"))

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from labkit import check, load_json, report

K = 3
FORBIDDEN = "salary bands"

# === WORK STARTS HERE ===
# STEP 1: index the corpus; every document carries a tenant label.
docs = load_json("rag_documents.json")["documents"]
corpus = pd.DataFrame(docs).rename(columns={"doc_id": "id"})
vectorizer = TfidfVectorizer(stop_words="english")
matrix = vectorizer.fit_transform(corpus.text)
print(corpus[["id", "tenant", "title"]].to_string(index=False))


# STEP 2: the buggy pipeline — retrieve top-k with no ACL, then filter what is displayed.
def answer_buggy(query, tenant):
    scores = cosine_similarity(vectorizer.transform([query]), matrix)[0]
    top = np.argsort(-scores)[:K]
    retrieved = corpus.iloc[top]
    prompt = "\n".join(f"[{r.id}] {r.text}" for r in retrieved.itertuples())
    visible = retrieved[retrieved.tenant.isin([tenant, "public"])]
    return prompt, visible, retrieved


# STEP 3: the fix — constrain the candidate set before ranking at all.
def answer_fixed(query, tenant):
    allowed = np.where(corpus.tenant.isin([tenant, "public"]).to_numpy())[0]
    scores = cosine_similarity(vectorizer.transform([query]), matrix[allowed])[0]
    top = allowed[np.argsort(-scores)[:K]]
    retrieved = corpus.iloc[top]
    prompt = "\n".join(f"[{r.id}] {r.text}" for r in retrieved.itertuples())
    return prompt, retrieved


query = "What is the salary band for a senior engineer?"
prompt_buggy, visible_buggy, retrieved_buggy = answer_buggy(query, "alpha")
prompt_fixed, visible_fixed = answer_fixed(query, "alpha")
print("\nretrieved before filtering:", list(retrieved_buggy.id))
print("visible to alpha (buggy):", list(visible_buggy.id))
print("visible to alpha (fixed):", list(visible_fixed.id))
print("buggy prompt contains foreign text:", FORBIDDEN in prompt_buggy.lower())
print("fixed prompt contains foreign text:", FORBIDDEN in prompt_fixed.lower())

# STEP 4: the leak is invisible to the user and present in the prompt.
check(FORBIDDEN in prompt_buggy.lower(), "the buggy prompt must include the other tenant's document")
check(FORBIDDEN not in prompt_fixed.lower(), "pre-filtering must remove it from the prompt")
check("d06" not in list(visible_buggy.id), "the display filter hides it, which is why nobody notices")

report("pipeline comparison", [
    {"pipeline": "retrieve then filter", "documents_in_prompt": K,
     "foreign_documents_in_prompt": int((~retrieved_buggy.tenant.isin(["alpha", "public"])).sum()),
     "leak_in_prompt": FORBIDDEN in prompt_buggy.lower()},
    {"pipeline": "filter then rank", "documents_in_prompt": len(visible_fixed),
     "foreign_documents_in_prompt": int((~visible_fixed.tenant.isin(["alpha", "public"])).sum()),
     "leak_in_prompt": FORBIDDEN in prompt_fixed.lower()},
])

# STEP 5: the general statement.
print("\nPost-filtering hides the evidence, not the data. The ACL must select candidates, not redact results.")
print("Note also d11: a document that contains an instruction. Selection by ACL does not make text trustworthy.")
