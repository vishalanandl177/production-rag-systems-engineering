"""Lab 1: Complete RAG chatbot with FastAPI."""
import anthropic
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
embedder = SentenceTransformer('all-MiniLM-L6-v2')
qdrant = QdrantClient(url="http://localhost:6333")
claude = anthropic.Anthropic()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Query):
    query_vec = embedder.encode(q.question).tolist()
    results = qdrant.search("docs", query_vector=query_vec, limit=5)
    context = "\n\n---\n\n".join([r.payload["content"] for r in results])

    response = claude.messages.create(
        model="claude-sonnet-4-6", max_tokens=1024,
        system="Answer using ONLY the provided context. Cite sources.",
        messages=[{"role": "user", "content": f"Context:\n{context}\n\nQuestion: {q.question}"}],
    )
    return {"answer": response.content[0].text, "sources": [r.payload.get("title", "unknown") for r in results]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
