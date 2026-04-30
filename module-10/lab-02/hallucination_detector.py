"""Lab 2: LLM-as-judge hallucination detection."""
import anthropic

client = anthropic.Anthropic()

def detect_hallucinations(context: str, answer: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-6", max_tokens=1024,
        system="You are a hallucination detector. Given context and an answer, identify claims NOT supported by context.",
        messages=[{"role": "user", "content": f"Context:\n{context}\n\nAnswer:\n{answer}\n\nList unsupported claims:"}],
    )
    return response.content[0].text

context = "AcmeCorp was founded in 2020. It has 50 employees."
answer = "AcmeCorp was founded in 2020 by John Smith. It has 50 employees and offices in 3 countries."
print(detect_hallucinations(context, answer))
