from datetime import time, datetime
from uuid import UUID

from sqlmodel import SQLModel

class TrainMainListItemResponse(SQLModel):
    id: UUID
    name: str
    start_time: time
    end_time: time
    place_name: str
    type_uuid: UUID
    date: datetime

    def __init__(
            self,
            id: UUID,
            name: str,
            start_time: time,
            end_time: time,
            place_name: str,
            type_uuid: UUID,
            date: datetime):
        self.id = id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.place = place_name
        self.type = type_uuid
        self.date = date