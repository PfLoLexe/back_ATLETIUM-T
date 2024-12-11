from uuid import UUID

from sqlmodel import SQLModel


class TrainerProfileInfoRequest(SQLModel):
    user_id: UUID