from typing import Optional
from uuid import UUID

from sqlmodel import SQLModel


class DialogueCreationRequest(SQLModel):
    second_user_id: UUID

class PossibleDialogueListRequest(SQLModel):
    search_string: Optional[str]