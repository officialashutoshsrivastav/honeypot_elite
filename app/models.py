from pydantic import BaseModel
from typing import List, Union

class Message(BaseModel):
    sender: str
    text: str
    timestamp: Union[str, int, float]

class Metadata(BaseModel):
    channel: str
    language: str
    locale: str

class ConversationItem(BaseModel):
    sender: str
    text: str
    timestamp: Union[str, int, float]

class HoneypotRequest(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: List[ConversationItem]
    metadata: Metadata
HoneypotRequest.model_rebuild()
