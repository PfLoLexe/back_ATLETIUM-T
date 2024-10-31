from uuid import uuid4, UUID
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class TrainMainToClientLinkDefault(SQLModel):
    train_main_id: UUID = Field(nullable=False)
    client_id: UUID = Field(nullable=False)

class TrainMainToClientLink(TrainMainToClientLinkDefault, table=True):
    __tablename__: str = "train_main_to_client_link"
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
