from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field, Relationship

from src.models.role import Roles


class ClientParentInfoDefault(SQLModel):
    phone_number: Optional[str] = Field(nullable=True)
    firstname: Optional[str] = Field(nullable=True)
    lastname: Optional[str] = Field(nullable=True)
    middle_name: Optional[str] = Field(nullable=True)


class ClientParentInfo(ClientParentInfoDefault, table=True):
    __tablename__: str = "client_parent_info"
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
