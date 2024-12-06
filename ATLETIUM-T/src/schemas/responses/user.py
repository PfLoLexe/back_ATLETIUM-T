from uuid import UUID

from sqlmodel import SQLModel

class TrainerInfoResponse(SQLModel):
    firstname: str
    lastname: str
    middle_name: str
    phone_number: str
    trainer_id: UUID
