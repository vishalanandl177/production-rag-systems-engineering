"""Lab 1: Document ingestion pipeline."""
import re
from sentence_transformers import SentenceTransformer

def chunk_fixed(text, size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start+size])
        start += size - overlap
    return chunks

def chunk_semantic(text):
    return [s.strip() for s in re.split(r'\n## |\n\n', text) if len(s.strip()) > 50]

# Demo
doc = open('sample.md').read() if __import__('os').path.exists('sample.md') else "# Title\n\nParagraph one about RAG.\n\n## Section Two\n\nMore content here about embeddings and vector databases.\n\n## Section Three\n\nFinal section about deployment."
print(f"Fixed chunks: {len(chunk_fixed(doc))}")
print(f"Semantic chunks: {len(chunk_semantic(doc))}")
for i, c in enumerate(chunk_semantic(doc)):
    print(f"  Chunk {i}: {c[:60]}...")
