from datetime import datetime

sessions = {}

def get_session(session_id: str):
    if session_id not in sessions:
        sessions[session_id] = {
            "start_time": datetime.utcnow(),
            "messages": [],
            "turn_count": 0,
            "questions_asked": 0,
            "red_flags": set(),
            "confidence": 0.0,
            "scam_type": "unknown",
            "extracted": {
                "phoneNumbers": set(),
                "bankAccounts": set(),
                "upiIds": set(),
                "phishingLinks": set(),
                "emailAddresses": set(),
                "caseIds": set(),
                "policyNumbers": set(),
                "orderNumbers": set()
            }
        }
    return sessions[session_id]