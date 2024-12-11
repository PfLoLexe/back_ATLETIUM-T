from typing import Optional
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


class ClientParentInfoResponse(SQLModel):
    firstname: Optional[str]
    lastname: Optional[str]
    middle_name: Optional[str]
    phone_number: Optional[str]

    def __init__(self, firstname, lastname, middle_name, phone_number):
        self.firstname = firstname
        self.lastname = lastname
        self.middle_name = middle_name
        self.phone_number = phone_number


class ClientProfileInfoResponse(SQLModel):
    firstname: str
    lastname: str
    middle_name: Optional[str]
    phone_number: str
    age: int
    id: UUID
    parent_info: Optional[ClientParentInfoResponse] = None

    def __init__(self, firstname, lastname, middle_name, phone_number, age, id: UUID):
        self.firstname = firstname
        self.lastname = lastname
        self.middle_name = middle_name
        self.phone_number = phone_number
        self.age = age
        self.id = id