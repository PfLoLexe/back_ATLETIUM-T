from enum import Enum
from typing import Optional, List
from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field, Relationship

from src.models.role import Roles


class UserDefault(SQLModel):
    username: str
    firstname: Optional[str] = Field(nullable=True)
    lastname: Optional[str] = Field(nullable=True)
    middle_name: Optional[str] = Field(nullable=True)
    phone_number: str = Field(nullable=False)


class UserPasswordDefault(UserDefault):
    hashed_password: str

class User(UserPasswordDefault, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
    is_active: bool = Field(default=True)
    role: Roles = Field(default=Roles.trainer, nullable=False)
