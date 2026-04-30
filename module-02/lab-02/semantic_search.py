"""Lab 2: Semantic search with sentence-transformers."""
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

corpus = [
    "Python is a programming language",
    "Django is a web framework for Python",
    "Automobile maintenance guide",
    "Car repair instructions",
    "Machine learning with neural networks",
]

query = "vehicle repair"
query_emb = model.encode([query])
corpus_emb = model.encode(corpus)

scores = cosine_similarity(query_emb, corpus_emb)[0]
print(f"Query: '{query}'")
for doc, score in sorted(zip(corpus, scores), key=lambda x: -x[1]):
    print(f"  {score:.3f} | {doc}")
print("\nNote: 'vehicle repair' matches 'Car repair' and 'Automobile maintenance'!")
