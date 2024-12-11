from typing import Optional
from uuid import UUID

from sqlmodel import SQLModel

class TrainerInfoResponse(SQLModel):
    firstname: str
    lastname: str
    middle_name: Optional[str]
    phone_number: str
    trainer_id: UUID

    def __init__(self, firstname: str, lastname: str, middle_name: Optional[str], phone_number: str, trainer_id: Optional[UUID]):
        self.firstname = firstname
        self.lastname = lastname
        self.middle_name = middle_name
        self.phone_number = phone_number
        self.trainer_id = trainer_id

