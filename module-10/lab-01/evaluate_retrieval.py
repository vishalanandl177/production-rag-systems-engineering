"""Lab 1: Evaluate retrieval quality."""
def precision_at_k(retrieved, relevant, k):
    retrieved_k = retrieved[:k]
    return len(set(retrieved_k) & set(relevant)) / k

def recall_at_k(retrieved, relevant, k):
    retrieved_k = retrieved[:k]
    return len(set(retrieved_k) & set(relevant)) / len(relevant) if relevant else 0

retrieved = ["doc1", "doc3", "doc5", "doc2", "doc7"]
relevant = ["doc1", "doc2", "doc4"]
print(f"Precision@3: {precision_at_k(retrieved, relevant, 3):.2f}")
print(f"Recall@3: {recall_at_k(retrieved, relevant, 3):.2f}")
print(f"Precision@5: {precision_at_k(retrieved, relevant, 5):.2f}")
print(f"Recall@5: {recall_at_k(retrieved, relevant, 5):.2f}")
