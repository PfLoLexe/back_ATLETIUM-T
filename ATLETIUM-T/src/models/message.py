import datetime
from typing import Optional
from uuid import uuid4, UUID
from sqlmodel import SQLModel, Field, Relationship

class MessageDefault(SQLModel):
    text: str
    send_date: datetime.datetime


class MessageWithFK(MessageDefault):
    sender_user_id: UUID = Field(index=True)
    dialogue_id: UUID = Field(index=True)
    parent_message_id: Optional[UUID] = Field(
        default=None,
        nullable=True
    )


class Message(MessageWithFK, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
    is_read: bool
    read_date: datetime.datetime

