from datetime import datetime
from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field


class MessageResponse(SQLModel):
    id: UUID
    sender_user_id: UUID
    recipient_user_id: UUID
    my_message: bool
    is_read: bool
    text: str
    send_date: datetime

    def __init__(self, id, sender_user_id, recipient_user_id, my_message, is_read, text, send_date):
        self.id = id
        self.sender_user_id = sender_user_id
        self.recipient_user_id = recipient_user_id
        self.my_message = my_message
        self.is_read = is_read
        self.text = text
        self.send_date = send_date
