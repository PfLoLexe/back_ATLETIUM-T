from uuid import UUID

from sqlmodel import SQLModel


class ClientShortResponse(SQLModel):
    firstname: str
    lastname: str
    id: UUID

    def __init__(self, firstname, lastname, id, **kwargs):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id