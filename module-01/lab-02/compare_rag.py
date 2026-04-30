"""Lab 2: Compare vanilla LLM vs RAG responses."""
import anthropic

client = anthropic.Anthropic()
QUESTION = "What is the refund policy for AcmeCorp?"

# Without RAG - LLM guesses
print("=== Without RAG ===")
r1 = client.messages.create(
    model="claude-sonnet-4-6", max_tokens=256,
    messages=[{"role": "user", "content": QUESTION}],
)
print(r1.content[0].text)

# With RAG - grounded in context
CONTEXT = """AcmeCorp Refund Policy:
- Full refund within 14 days of purchase
- Pro-rated refund after 14 days
- No refund after 90 days
- Contact support@acmecorp.com"""

print("\n=== With RAG ===")
r2 = client.messages.create(
    model="claude-sonnet-4-6", max_tokens=256,
    system="Answer using ONLY the provided context. Cite the source.",
    messages=[{"role": "user", "content": f"Context:\n{CONTEXT}\n\nQuestion: {QUESTION}"}],
)
print(r2.content[0].text)
