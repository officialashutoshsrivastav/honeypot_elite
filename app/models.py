from pydantic import BaseModel
from typing import Union

class Message(BaseModel):
    sender: str
    text: str
    timestamp: Union[str, int]

class HoneypotRequest(BaseModel):
    sessionId: str
    message: Message
    conversationHistory: List[Message] = []

    metadata: Dict[str, str]
