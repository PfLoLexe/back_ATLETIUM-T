from typing import List
from uuid import UUID

from sqlmodel import SQLModel

from src.schemas.requests.client import ClientVisitStatus


class TrainSpecificChangeClientsVisitStatusRequest(SQLModel):
    train_specific_id: UUID
    clients_list: List[ClientVisitStatus]
