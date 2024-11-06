from datetime import date
from uuid import UUID

from sqlmodel import SQLModel


class TrainMainListRequest(SQLModel):
    week_day_number: int
    date: date
    trainer_id: UUID