from uuid import uuid4, UUID

from sqlmodel import SQLModel, Field, Relationship

class TrainTypeDefault(SQLModel):
    label: str


class TrainType(TrainTypeDefault, table=True):
    __tablename__: str = "train_type"

    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
