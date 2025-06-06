﻿from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field, Relationship

from src.models.role import Roles


class ClientDefault(SQLModel):
    firstname: str
    lastname: str
    middle_name: Optional[str] = Field(nullable=True)
    phone_number: Optional[str] = Field(nullable=True)
    age: Optional[int] = Field(nullable=True)

class Client(ClientDefault, table=True):
    is_parent: bool
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
