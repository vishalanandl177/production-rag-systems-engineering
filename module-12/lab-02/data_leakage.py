"""Lab 2: Prevent data leakage in multi-tenant RAG."""

SENSITIVE_PATTERNS = [
    r'\b\d{3}-\d{2}-\d{4}\b',  # SSN
    r'\b\d{16}\b',              # Credit card
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',  # Email
]

def filter_output(text):
    import re
    for pattern in SENSITIVE_PATTERNS:
        text = re.sub(pattern, '[REDACTED]', text)
    return text

test = "Contact john@example.com or call with card 4111111111111111"
print(f"Before: {test}")
print(f"After:  {filter_output(test)}")
