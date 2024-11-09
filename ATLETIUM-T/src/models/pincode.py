from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field


class Pincode(SQLModel, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
    hashed_pincode: str
    user_id: UUID = Field(nullable=False)
