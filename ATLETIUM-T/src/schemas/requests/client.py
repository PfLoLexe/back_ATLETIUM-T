from uuid import UUID

from sqlmodel import SQLModel

from src.models.visit_status import VisitStatus


class ClientVisitStatus(SQLModel):
    client_id: UUID
    visit_status: VisitStatus

class ClientProfileInfoRequest(SQLModel):
    client_id: UUID