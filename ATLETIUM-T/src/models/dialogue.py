import datetime
from uuid import uuid4, UUID
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class DialogueDefault(SQLModel):
    first_user_id: UUID = Field(index=True)
    second_user_id: UUID = Field(index=True)


class Dialogue(DialogueDefault, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
