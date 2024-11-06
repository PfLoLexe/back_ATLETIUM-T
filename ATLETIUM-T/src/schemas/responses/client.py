from uuid import UUID

from sqlmodel import SQLModel

from src.models.visit_status import VisitStatus


class ClientLinkedToSpecificTrainResponse(SQLModel):
    firstname: str
    lastname: str
    id: UUID
    visit_status: VisitStatus

    def __init__(self, firstname, lastname, id, visit_status = VisitStatus.none):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.visit_status = visit_status

class ClientLinkedToMainTrainResponse(SQLModel):
    firstname: str
    lastname: str
    id: UUID

    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id