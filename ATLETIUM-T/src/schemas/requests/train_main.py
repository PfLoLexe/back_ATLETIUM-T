from datetime import date

from sqlmodel import SQLModel


class TrainMainListRequest(SQLModel):
    week_day_number: int
    date: date