import datetime
from dataclasses import field
from typing import Optional
from uuid import uuid4, UUID
from sqlmodel import SQLModel, Field, Relationship

class MessageDefault(SQLModel):
    text: str
    send_date: datetime.datetime


class MessageWithFK(MessageDefault):
    sender_user_id: UUID = Field(
        index=True,
        nullable=False,
        default=None,
    )
    recipient_user_id: UUID = Field(
        index=True,
        nullable=False,
        default=None,
    )
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
    is_read: Optional[bool] = Field(default=False, nullable=False)
    read_date: Optional[datetime.datetime] = Field(nullable=True, default_factory=datetime.datetime.now)

