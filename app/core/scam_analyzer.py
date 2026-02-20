import json
from app.core.llm_client import llm_call

def analyze_scam(text: str):

    system_prompt = """
    Analyze this message and return strict JSON:
    {
      "isScam": true/false,
      "confidence": number between 0 and 1,
      "scamType": "bank_fraud | upi_fraud | phishing | impersonation | investment | unknown",
      "redFlags": ["list of red flags"]
    }
    Only JSON.
    """

    response = llm_call([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": text}
    ])

    try:
        return json.loads(response)
    except:
        return {
            "isScam": True,
            "confidence": 0.7,
            "scamType": "unknown",
            "redFlags": []
        }