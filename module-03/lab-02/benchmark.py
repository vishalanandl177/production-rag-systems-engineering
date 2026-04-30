"""Lab 2: Benchmark embedding models on your data."""
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import time

models = ['all-MiniLM-L6-v2', 'all-mpnet-base-v2']
test_pairs = [
    ("car repair guide", "automobile maintenance manual"),
    ("python programming", "javascript coding"),
    ("database indexing", "SQL query optimization"),
]

for name in models:
    model = SentenceTransformer(name)
    print(f"\n=== {name} (dims={model.get_sentence_embedding_dimension()}) ===")
    for a, b in test_pairs:
        embs = model.encode([a, b])
        sim = cosine_similarity([embs[0]], [embs[1]])[0][0]
        print(f"  {sim:.3f} | '{a}' vs '{b}'")
