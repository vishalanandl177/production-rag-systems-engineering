"""Lab 2: Multi-tenant RAG with data isolation."""
from qdrant_client import QdrantClient, models

# Every query MUST include tenant_id filter
def search_tenant(client, tenant_id, query_vector, limit=5):
    return client.search(
        collection_name="docs",
        query_vector=query_vector,
        query_filter=models.Filter(must=[
            models.FieldCondition(key="tenant_id", match=models.MatchValue(value=tenant_id))
        ]),
        limit=limit,
    )

print("Multi-tenant isolation: MANDATORY tenant_id filter on every query.")
print("Never make tenant filtering optional — developers forget, attackers exploit.")
