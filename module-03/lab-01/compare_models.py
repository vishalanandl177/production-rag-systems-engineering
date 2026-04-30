"""Lab 1: Compare embedding models."""
from sentence_transformers import SentenceTransformer
import time

models = ['all-MiniLM-L6-v2', 'all-mpnet-base-v2']
text = "How do I deploy a FastAPI application to Kubernetes?"

for name in models:
    model = SentenceTransformer(name)
    start = time.time()
    emb = model.encode([text])
    elapsed = time.time() - start
    print(f"{name}: dims={emb.shape[1]}, latency={elapsed*1000:.0f}ms")
