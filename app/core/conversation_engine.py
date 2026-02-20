from app.core.llm_client import llm_call

SYSTEM_PROMPT = """
You are an advanced scam honeypot.

Goals:
- Engage scammer at least 8 turns
- Ask investigative questions
- Extract phone numbers, IDs, links
- Mention red flags subtly
- Be cooperative but skeptical
- Do NOT accuse directly early
"""

def generate_reply(history):

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for msg in history:
        role = "assistant" if msg["sender"] == "user" else "user"
        messages.append({"role": role, "content": msg["text"]})

    return llm_call(messages, temperature=0.7)