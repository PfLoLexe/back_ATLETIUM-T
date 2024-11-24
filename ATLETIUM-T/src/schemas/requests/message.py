import datetime
from uuid import UUID

from sqlmodel import SQLModel


class DialogueMessagesListRequest(SQLModel):
    dialogue_id: UUID

class AddMessageRequest(SQLModel):
    recipient_user_id: UUID
    dialogue_id: UUID
    text: str
    send_date: datetime.datetime