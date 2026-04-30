"""Lab 2: Token usage and cost tracking."""

def track_cost(response, model="claude-sonnet-4-6"):
    pricing = {
        "claude-sonnet-4-6": {"input": 3.0 / 1_000_000, "output": 15.0 / 1_000_000},
        "claude-haiku-4-5": {"input": 0.25 / 1_000_000, "output": 1.25 / 1_000_000},
    }
    rates = pricing.get(model, pricing["claude-sonnet-4-6"])
    cost = response.usage.input_tokens * rates["input"] + response.usage.output_tokens * rates["output"]
    return {
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "cost_usd": round(cost, 6),
        "model": model,
    }

print("Track cost per request. Alert on spikes. Budget per tenant.")
