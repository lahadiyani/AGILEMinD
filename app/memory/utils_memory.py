def should_promote(user_input: str, response: str) -> bool:
    return len(user_input.split()) + len(response.split()) > 50

def summarize_if_needed(user_input: str, response: str) -> str:
    # Dummy summarization, bisa diganti LLM
    return f"Ringkasan: {user_input[:30]}... → {response[:30]}..."
