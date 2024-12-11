from enum import Enum
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


class ClientParentInfo(ClientDefault):
    parent_phone_number: Optional[str] = Field(nullable=True)
    parent_firstname: Optional[str] = Field(nullable=True)
    parent_lastname: Optional[str] = Field(nullable=True)
    parent_middle_name: Optional[str] = Field(nullable=True)


class Client(ClientParentInfo, table=True):
    is_parent: bool
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
