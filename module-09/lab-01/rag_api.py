"""Lab 1: Production RAG API with caching and streaming."""
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import redis, hashlib, json

app = FastAPI()
cache = redis.Redis(host="localhost", port=6379)

@app.post("/ask")
async def ask(question: str):
    cache_key = hashlib.sha256(question.encode()).hexdigest()
    cached = cache.get(cache_key)
    if cached:
        return {"answer": cached.decode(), "cached": True}
    answer = "RAG pipeline result here"  # Replace with actual pipeline
    cache.setex(cache_key, 3600, answer)
    return {"answer": answer, "cached": False}
