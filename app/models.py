from pydantic import BaseModel
from typing import List, Dict

class Message(BaseModel):
    sender: str
    text: str
    timestamp: str

class HoneypotRequest(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: List[Message] = []
    metadata: Dict[str, str]