import datetime
from uuid import uuid4, UUID
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class TrainMainDefault(SQLModel):
    name: str
    start_time: datetime.time
    end_time: datetime.time
    week_day_number: int = Field(index=True)
    date: datetime.date = Field(nullable=True)

class TrainMainWithFK(TrainMainDefault):
    place_id: UUID = Field(nullable=False)
    train_type_id: UUID = Field(nullable=False)
    trainer_id: UUID = Field(nullable=False, index=True)

class TrainMain(TrainMainWithFK, table=True):
    __tablename__: str = "train_main"

    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
