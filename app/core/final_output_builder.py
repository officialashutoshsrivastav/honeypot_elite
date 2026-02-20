from datetime import datetime

def build_final_output(session_id, session):

    start_time = session.get("start_time", datetime.utcnow())
    duration = (datetime.utcnow() - start_time).total_seconds()

    extracted = session.get("extracted", {})
    red_flags = session.get("red_flags", set())

    scam_detected = (
        session.get("confidence", 0) >= 0.5
        or len(red_flags) >= 2
        or len(extracted.get("bankAccounts", [])) > 0
        or len(extracted.get("upiIds", [])) > 0
        or len(extracted.get("phishingLinks", [])) > 0
    )

    return {
        "sessionId": session_id,
        "scamDetected": scam_detected,
        "totalMessagesExchanged": len(session.get("messages", [])),
        "engagementDurationSeconds": int(duration),
        "extractedIntelligence": {
            k: list(v) for k, v in extracted.items()
        },
        "agentNotes": f"Red flags identified: {list(red_flags)}",
        "scamType": session.get("scam_type", "unknown"),
        "confidenceLevel": round(session.get("confidence", 0), 2)
    }