"""Lab 2: Compare chunking strategies on retrieval quality."""
import re

sample = """# Introduction to RAG
RAG combines retrieval with generation for accurate AI responses.

## How It Works
Documents are chunked, embedded, and stored in vector databases.
When a user asks a question, relevant chunks are retrieved.

## Benefits
RAG reduces hallucinations by grounding responses in real data.
It enables domain-specific AI without fine-tuning.

## Challenges
Chunk size affects quality. Too small loses context, too large dilutes relevance.
"""

def chunk_fixed(text, size=100, overlap=20):
    chunks, start = [], 0
    while start < len(text):
        chunks.append(text[start:start+size].strip())
        start += size - overlap
    return [c for c in chunks if c]

def chunk_semantic(text):
    return [s.strip() for s in re.split(r'\n## |\n# ', text) if len(s.strip()) > 20]

print(f"Fixed (100 char): {len(chunk_fixed(sample))} chunks")
for i, c in enumerate(chunk_fixed(sample)):
    print(f"  [{i}] {c[:60]}...")
print(f"\nSemantic (headings): {len(chunk_semantic(sample))} chunks")
for i, c in enumerate(chunk_semantic(sample)):
    print(f"  [{i}] {c[:60]}...")
