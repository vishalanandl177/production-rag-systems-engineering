"""Lab 1: Keyword search with BM25."""
from rank_bm25 import BM25Okapi

corpus = [
    "Python is a programming language",
    "Django is a web framework for Python",
    "FastAPI is a modern async Python framework",
    "Flask is a lightweight WSGI framework",
    "Machine learning with scikit-learn",
]

tokenized = [doc.lower().split() for doc in corpus]
bm25 = BM25Okapi(tokenized)

query = "python web framework"
scores = bm25.get_scores(query.lower().split())

print("Query:", query)
for doc, score in sorted(zip(corpus, scores), key=lambda x: -x[1]):
    print(f"  {score:.3f} | {doc}")
