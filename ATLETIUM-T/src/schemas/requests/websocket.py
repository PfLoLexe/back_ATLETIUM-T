from uuid import UUID

from sqlmodel import SQLModel


class ChatWebSocketConnectionRequest(SQLModel):
    user_id: UUID