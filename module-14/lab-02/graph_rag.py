"""Lab 2: Graph-based retrieval concept."""
print("""
Graph RAG builds a knowledge graph of relationships:
- Entities: services, APIs, teams, documents
- Relationships: depends_on, owned_by, references

Query: "What are the dependencies of the Payment Service?"
1. Find 'Payment Service' entity in graph
2. Traverse 'depends_on' edges
3. Collect all connected entities
4. Retrieve document chunks for each entity
5. Generate answer from multi-hop context

This enables reasoning across relationships that flat vector search cannot.
""")
