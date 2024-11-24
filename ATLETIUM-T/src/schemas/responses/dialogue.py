from uuid import UUID

from sqlmodel import SQLModel

from src.models.dialogue import Dialogue

class DialogueResponse(SQLModel):
    recipient_user_firstname: str
    recipient_user_lastname: str
    recipient_user_middle_name: str
    dialogue_id: UUID
    first_user_id: UUID
    second_user_id: UUID

    def __init__(self, recipient_user_firstname, recipient_user_lastname, recipient_user_middle_name, dialogue_id, first_user_id, second_user_id):
        self.recipient_user_firstname = recipient_user_firstname
        self.recipient_user_lastname = recipient_user_lastname
        self.recipient_user_middle_name = recipient_user_middle_name
        self.dialogue_id = dialogue_id
        self.first_user_id = first_user_id
        self.second_user_id = second_user_id

class PossibleDialoguesUserResponse(SQLModel):
    recipient_user_firstname: str
    recipient_user_lastname: str
    recipient_user_middle_name: str
    recipient_user_id: UUID

    def __init__(self, recipient_user_firstname, recipient_user_lastname, recipient_user_middle_name, recipient_user_id):
        self.recipient_user_firstname = recipient_user_firstname
        self.recipient_user_lastname = recipient_user_lastname
        self.recipient_user_middle_name = recipient_user_middle_name
        self.recipient_user_id = recipient_user_id
