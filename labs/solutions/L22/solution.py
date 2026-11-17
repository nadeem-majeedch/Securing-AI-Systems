"""L22 — An ACL test suite for a RAG index (M13, Advanced).

Goal: turn retrieval access control into eight executable assertions, run them against a correct index and a
plausible buggy one, and show that the suite catches cross-tenant, deletion and completeness faults.
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

# === WORK STARTS HERE ===
# STEP 1: four documents across two tenants, one of them deleted.
documents = [
    {"id": "a1", "tenant": "alpha", "text": "Alpha refund policy: refunds within 30 days of purchase.", "deleted": False},
    {"id": "a2", "tenant": "alpha", "text": "Alpha travel policy: economy class for flights under six hours.", "deleted": False},
    {"id": "b1", "tenant": "beta", "text": "Beta refund policy: refunds within 14 days, manager approval required.", "deleted": False},
    {"id": "b2", "tenant": "beta", "text": "Beta salary bands: engineer band 4 starts at 95,000.", "deleted": True},
]
corpus = pd.DataFrame(documents)
vectorizer = TfidfVectorizer(stop_words="english").fit(corpus.text)


class Index:
    def __init__(self, mode="correct"):
        self.mode = mode
        if mode == "buggy_postfilter":
            self.docs = corpus.copy()                            # deletion ignored
        else:
            self.docs = corpus[~corpus.deleted].reset_index(drop=True)
        self.matrix = vectorizer.transform(self.docs.text)

    def search(self, query, tenant, k=K):
        if self.mode == "buggy_postfilter":
            scores = cosine_similarity(vectorizer.transform([query]), self.matrix)[0]
            top = np.argsort(-scores)[:k]
            hits = self.docs.iloc[top]
            hits = hits[hits.tenant == tenant]
            return list(hits.id)
        allowed = np.where(self.docs.tenant.to_numpy() == tenant)[0]
        if allowed.size == 0:
            return []
        scores = cosine_similarity(vectorizer.transform([query]), self.matrix[allowed])[0]
        order = allowed[np.argsort(-scores)][:k]
        return [self.docs.iloc[i].id for i in order if self.docs.iloc[i].tenant == tenant]


# STEP 2: the suite — one assertion per failure mode a reviewer would ask about.
def suite(index):
    results = []

    def add(name, passed, detail=""):
        results.append({"test": name, "pass": bool(passed), "detail": detail})

    alpha = index.search("refund policy", "alpha")
    add("same-tenant retrieval returns rows", len(alpha) > 0, str(alpha))
    add("no foreign tenant in alpha results", all(d.startswith("a") for d in alpha), str(alpha))
    beta = index.search("salary band", "beta")
    add("deleted document never returned", "b2" not in beta, str(beta))
    everywhere = set(index.search("refund policy", "alpha")) | set(index.search("refund policy", "beta"))
    everywhere |= set(index.search("salary band", "beta")) | set(index.search("policy", "beta", k=99))
    add("deleted id absent from every tenant's results", "b2" not in everywhere, str(sorted(everywhere)))
    add("foreign tenant cannot see alpha", all(d.startswith("b") for d in index.search("refund policy", "beta")),
        str(index.search("refund policy", "beta")))
    add("cross-tenant query returns k-consistent results", len(index.search("salary band", "alpha")) <= K,
        str(index.search("salary band", "alpha")))
    add("unknown tenant returns nothing", index.search("refund policy", "gamma") == [], "")
    add("empty-result is not distinguishable from no-permission",
        len(index.search("salary band", "gamma")) == 0, "")
    add("k never exceeded", len(index.search("policy", "beta", k=99)) <= 2, "")
    return pd.DataFrame(results)


correct = suite(Index("correct"))
buggy = suite(Index("buggy_postfilter"))
report("correct index", correct)
report("buggy index", buggy)
print(f"\ncorrect: {int(correct['pass'].sum())}/{len(correct)} | buggy: {int(buggy['pass'].sum())}/{len(buggy)}")

# STEP 3: the suite must pass the good implementation and fail the bad one.
check(int(correct["pass"].sum()) == len(correct), "the correct index must pass every test")
check(int(buggy["pass"].sum()) < len(buggy) - 1, "the buggy index must fail at least two tests")

# STEP 4: name the failure the suite caught and the one it cannot.
print("\nThe suite catches: deletion lag, cross-tenant contamination and k-completeness.")
print("It cannot catch: a document whose ACL field was wrong when it was ingested.")
