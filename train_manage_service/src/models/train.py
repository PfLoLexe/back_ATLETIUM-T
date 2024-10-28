import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class TrainDefault(SQLModel):
    label: str
    place_id: int
    train_type_id: int
    start_time: datetime.time
    end_time: datetime.time
    week_day_number: int

class Train(TrainDefault, table=True):
    id: int = Field(default=None, primary_key=True)
