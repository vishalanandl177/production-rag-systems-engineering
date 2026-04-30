"""Lab 1: Multi-tool AI agent."""
import anthropic, json

client = anthropic.Anthropic()
tools = [
    {"name": "search_docs", "description": "Search internal documentation",
     "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}},
    {"name": "query_database", "description": "Run SQL query",
     "input_schema": {"type": "object", "properties": {"sql": {"type": "string"}}, "required": ["sql"]}},
]

def execute_tool(name, inputs):
    if name == "search_docs": return {"results": [f"Doc about: {inputs['query']}"]}
    if name == "query_database": return {"rows": [{"count": 42}]}
    return {"error": "unknown tool"}

messages = [{"role": "user", "content": "How many orders were placed last month?"}]
while True:
    response = client.messages.create(model="claude-sonnet-4-6", max_tokens=1024, tools=tools, messages=messages)
    if response.stop_reason == "tool_use":
        messages.append({"role": "assistant", "content": response.content})
        for block in response.content:
            if block.type == "tool_use":
                result = execute_tool(block.name, block.input)
                messages.append({"role": "user", "content": [{"type": "tool_result", "tool_use_id": block.id, "content": json.dumps(result)}]})
    else:
        print(response.content[0].text)
        break
