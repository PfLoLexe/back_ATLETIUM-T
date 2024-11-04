from datetime import date
from uuid import UUID

from sqlmodel import SQLModel


class TrainSpecificRequest(SQLModel):
    train_main_id: UUID
    date: date