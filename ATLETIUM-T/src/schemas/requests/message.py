from uuid import UUID

from sqlmodel import SQLModel


class DialogueMessagesListRequest(SQLModel):
    dialogue_id: UUID