"""Lab 2: Secure AI agent with identity and access control."""
print("""
Securing AI Agents:
1. Give each agent a unique identity (SPIFFE SVID)
2. Authenticate agent-to-service with mTLS
3. Control access with OPA policies per agent role
4. Audit all tool usage with verified identity

Example policy:
- customer-support agent: can query docs (read-only)
- training-pipeline agent: can write embeddings
- admin agent: full access with audit logging

See the Mastering SPIFFE & SPIRE course for implementation details.
""")
