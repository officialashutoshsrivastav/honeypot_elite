import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HONEYPOT_API_KEY = os.getenv("HONEYPOT_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not set")

if not HONEYPOT_API_KEY:
    raise ValueError("HONEYPOT_API_KEY not set")