"""Lab 1: Setup Qdrant and build semantic search API."""
from qdrant_client import QdrantClient, models
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer('all-MiniLM-L6-v2')
client = QdrantClient(url="http://localhost:6333")

client.create_collection("docs", vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE))

docs = ["Python web development", "Kubernetes deployment guide", "Database optimization tips"]
for i, doc in enumerate(docs):
    client.upsert("docs", points=[
        models.PointStruct(id=i, vector=embedder.encode(doc).tolist(), payload={"content": doc})
    ])

results = client.search("docs", query_vector=embedder.encode("deploying apps").tolist(), limit=3)
for r in results:
    print(f"  {r.score:.3f} | {r.payload['content']}")
