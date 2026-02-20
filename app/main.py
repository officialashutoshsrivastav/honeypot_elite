from fastapi import FastAPI, Header, HTTPException
from app.models import HoneypotRequest
from app.config import HONEYPOT_API_KEY
from app.core.session_manager import get_session
from app.core.scam_analyzer import analyze_scam
from app.core.intelligence_extractor import extract_intelligence
from app.core.conversation_engine import generate_reply
from app.core.engagement_controller import enforce_strategy
from app.core.final_output_builder import build_final_output
import time

app = FastAPI()


@app.post("/honeypot")
async def honeypot(request: HoneypotRequest, x_api_key: str = Header(None)):

    if x_api_key != HONEYPOT_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    session = get_session(request.sessionId)

    session["turn_count"] += 1

    session["messages"].append({
        "sender": "scammer",
        "text": request.message.text
    })

    analysis = analyze_scam(request.message.text)

    # Keep highest confidence seen so far
    session["confidence"] = max(
        session["confidence"],
        analysis.get("confidence", 0)
    )

    # If LLM clearly says scam, boost confidence
    if analysis.get("isScam"):
        session["confidence"] = max(session["confidence"], 0.75)

    # Preserve scam type once detected
    if analysis.get("scamType") and analysis["scamType"] != "unknown":
        session["scam_type"] = analysis["scamType"]

    # Accumulate red flags across turns
    for flag in analysis.get("redFlags", []):
        session["red_flags"].add(flag)

    reply = generate_reply(session["messages"])
    reply = enforce_strategy(session, reply)

    session["messages"].append({
        "sender": "user",
        "text": reply
    })

    full_text = "\n".join([m["text"] for m in session["messages"]])

    extracted = extract_intelligence(full_text)

    for key, values in extracted.items():
        if key in session["extracted"]:
            for v in values:
                session["extracted"][key].add(v)

    time.sleep(1)

    return {
        "status": "success",
        "reply": reply
    }


@app.get("/final-output/{session_id}")
async def final_output(session_id: str, x_api_key: str = Header(None)):

    if x_api_key != HONEYPOT_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    session = get_session(session_id)

    return build_final_output(session_id, session)