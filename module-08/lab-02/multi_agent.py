"""Lab 2: Multi-agent orchestration concept."""
print("""
Multi-Agent RAG Architecture:
1. Router Agent — decides which specialist to call
2. Research Agent — retrieves and synthesizes information
3. Analysis Agent — processes data and computes answers
4. Writer Agent — generates the final user-facing response

LangGraph orchestrates the flow between agents with state management.
Each agent has its own tools, prompts, and responsibilities.
""")
