from uuid import UUID

from sqlmodel import SQLModel


class DialogueCreationRequest(SQLModel):
    second_user_id: UUID