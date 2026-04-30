"""Lab 1: Hybrid search with BM25 + vectors + RRF."""
from rank_bm25 import BM25Okapi

def reciprocal_rank_fusion(bm25_results, vector_results, k=60):
    scores = {}
    for rank, doc_id in enumerate(bm25_results):
        scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank + 1)
    for rank, doc_id in enumerate(vector_results):
        scores[doc_id] = scores.get(doc_id, 0) + 1 / (k + rank + 1)
    return sorted(scores.items(), key=lambda x: -x[1])

print("Hybrid search combines BM25 (exact terms) + vectors (meaning)")
print("RRF merges both rankings into one unified ranking")
