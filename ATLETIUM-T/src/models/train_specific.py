import datetime
from uuid import uuid4, UUID
from typing import Optional
from sqlmodel import SQLModel, Field

class TrainSpecificDefault(SQLModel):
    clients_amount: int
    description: Optional[str] = Field(nullable=True)
    date: datetime.date
    is_over: bool = Field(default=False)


class TrainSpecificWithFK(TrainSpecificDefault):
    train_main_id: UUID = Field(nullable=False, index=True)
    trainer_id: UUID = Field(nullable=False, index=True)

class TrainSpecific(TrainSpecificWithFK, table=True):
    __tablename__: str = "train_specific"

    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
