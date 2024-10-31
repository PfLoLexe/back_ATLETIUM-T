from uuid import uuid4, UUID
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class TrainSpecificToClientLinkDefault(SQLModel):
    train_specific_id: UUID = Field(nullable=False)
    client_id: UUID = Field(nullable=False)

class TrainSpecificToClientLink(TrainSpecificToClientLinkDefault, table=True):
    __tablename__: str = "train_specific_to_client_link"
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
