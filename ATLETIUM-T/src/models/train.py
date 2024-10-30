import datetime
from uuid import uuid4, UUID
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class TrainDefault(SQLModel):
    label: str
    place_id: UUID
    train_type_id: UUID
    start_time: datetime.time
    end_time: datetime.time
    week_day_number: int

class Train(TrainDefault, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        nullable=False
    )
