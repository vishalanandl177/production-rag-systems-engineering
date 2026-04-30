"""Lab 2: Cross-encoder reranking."""
from sentence_transformers import CrossEncoder

reranker = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')

query = "how to deploy python app"
docs = [
    "Python deployment guide for production",
    "JavaScript React tutorial",
    "Deploying FastAPI applications to Kubernetes",
    "Database indexing strategies",
]

pairs = [(query, doc) for doc in docs]
scores = reranker.predict(pairs)
for doc, score in sorted(zip(docs, scores), key=lambda x: -x[1]):
    print(f"  {score:.3f} | {doc}")
