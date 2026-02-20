import json
from app.core.llm_client import llm_call
from app.core.regex_extractor import regex_extract

def extract_intelligence(full_text: str):

    system_prompt = """
    Extract all scam intelligence from the conversation.

    Return strict JSON:
    {
      "phoneNumbers": [],
      "bankAccounts": [],
      "upiIds": [],
      "phishingLinks": [],
      "emailAddresses": [],
      "caseIds": [],
      "policyNumbers": [],
      "orderNumbers": []
    }

    Only JSON.
    """

    try:
        response = llm_call([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": full_text}
        ], temperature=0)

        llm_data = json.loads(response)
    except:
        llm_data = {}

    regex_data = regex_extract(full_text)

    # Merge both safely
    merged = {
        "phoneNumbers": set(),
        "bankAccounts": set(),
        "upiIds": set(),
        "phishingLinks": set(),
        "emailAddresses": set(),
        "caseIds": set(),
        "policyNumbers": set(),
        "orderNumbers": set()
    }

    for key in merged.keys():
        if key in llm_data:
            merged[key].update(llm_data.get(key, []))
        if key in regex_data:
            merged[key].update(regex_data.get(key, []))

    return merged