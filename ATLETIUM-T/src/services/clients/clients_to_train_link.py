from typing import List
from uuid import UUID

from sqlmodel import select

from src.models.client import Client
from src.models.train_main_to_client_link import TrainMainToClientLink
from src.models.train_specific_to_client_link import TrainSpecificToClientLink
from src.schemas.responses.client import ClientLinkedToSpecificTrainResponse


def get_short_clients_of_train_main(session, train_main_id: UUID) -> List[ClientLinkedToSpecificTrainResponse]:
    train_clients_raw = session.exec(
        select(
            Client.id.label("id"),
            Client.lastname.label("lastname"),
            Client.firstname.label("firstname"),
        ).where(
            TrainMainToClientLink.client_id == Client.id,
            TrainMainToClientLink.train_main_id == train_main_id,
        )
    )
    train_clients = []
    if train_clients_raw is not None:
        train_clients = [ClientLinkedToSpecificTrainResponse(**row) for row in train_clients_raw.mappings()]
    return train_clients

def get_short_clients_of_train_specific(session, train_specific_id: UUID) -> List[ClientLinkedToSpecificTrainResponse]:
    train_clients_raw = session.exec(
        select(
            Client.id.label("id"),
            Client.lastname.label("lastname"),
            Client.firstname.label("firstname"),
            TrainSpecificToClientLink.status.label("visit_status"),
        ).where(
            TrainSpecificToClientLink.client_id == Client.id,
            TrainSpecificToClientLink.train_specific_id == train_specific_id,
        )
    )
    train_clients = []
    if train_clients_raw is not None:
        train_clients = [ClientLinkedToSpecificTrainResponse(**row) for row in train_clients_raw.mappings()]
    return train_clients