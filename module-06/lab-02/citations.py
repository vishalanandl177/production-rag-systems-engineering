"""Lab 2: RAG with source citations."""
import anthropic

client = anthropic.Anthropic()

def rag_with_citations(question, retrieved_docs):
    context_parts = []
    for i, doc in enumerate(retrieved_docs):
        context_parts.append(f"[Source {i+1}: {doc['title']}]\n{doc['content']}")
    context = "\n\n---\n\n".join(context_parts)

    response = client.messages.create(
        model="claude-sonnet-4-6", max_tokens=1024,
        system="Answer using ONLY the provided sources. Cite each claim with [Source N].",
        messages=[{"role": "user", "content": f"Sources:\n{context}\n\nQuestion: {question}"}],
    )
    return {
        "answer": response.content[0].text,
        "sources": [d["title"] for d in retrieved_docs],
    }

# Example
docs = [
    {"title": "Refund Policy", "content": "Full refund within 14 days."},
    {"title": "Shipping FAQ", "content": "Free shipping on orders over $50."},
]
result = rag_with_citations("What is the refund policy?", docs)
print(result["answer"])
