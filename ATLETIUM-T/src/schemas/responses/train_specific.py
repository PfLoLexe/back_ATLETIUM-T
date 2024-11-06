from typing import List, Optional
from uuid import UUID

from sqlmodel import SQLModel

from src.schemas.responses.client import ClientLinkedToSpecificTrainResponse


class TrainSpecificDataResponse(SQLModel):
    id: UUID
    clients_amount: int
    is_over: bool
    clients_list: List[ClientLinkedToSpecificTrainResponse]

    def __init__(self, id, clients_amount, is_over, clients_list: Optional[List[ClientLinkedToSpecificTrainResponse]] = None):
        self.id = id
        self.clients_amount = clients_amount
        self.is_over = is_over
        self.clients_list = clients_list
