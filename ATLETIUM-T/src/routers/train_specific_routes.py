import uuid
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select

from src.db import get_session
from src.exceptions.common_exceptions import InternalServerErrorException
from src.models.client import Client
from src.models.train_main_to_client_link import TrainMainToClientLink
from src.models.train_specific import TrainSpecific
from src.models.train_specific_to_client_link import TrainSpecificToClientLink
from src.requests.train_specific import TrainSpecificRequest
from src.responses.client import ClientShortResponse
from src.responses.train_specific import TrainSpecificDataResponse
from src.utils.clients.clients_to_train_link import get_short_clients_of_train_specific, get_short_clients_of_train_main
from src.utils.sql.sql_query import SqlQuery
from src.utils.trains.train_main_to_specific import generate_train_specific

train_specific_router = APIRouter()
sql_query = SqlQuery()

@train_specific_router.post("/train-specific/get")
def get_specific_train(data: TrainSpecificRequest, session = Depends(get_session)) -> TrainSpecificDataResponse:
    try:
        train_specific_raw = session.exec(
            select(
                TrainSpecific.id.label("id"),
                TrainSpecific.clients_amount.label("clients_amount"),
                TrainSpecific.is_over.label("is_over"),
            ).where(
                TrainSpecific.train_main_id == data.train_main_id,
                TrainSpecific.date == data.date,
            )
        ).one()
        if train_specific_raw is not None:
            train_specific = TrainSpecificDataResponse(
                id=train_specific_raw.id,
                clients_amount=train_specific_raw.clients_amount,
                is_over=train_specific_raw.is_over,
                clients_list=get_short_clients_of_train_specific(
                    session=session,
                    train_specific_id=train_specific_raw.id
                )
            )
            return train_specific
        else:
            train_specific_uuid = uuid.uuid4()
            generate_train_specific(
                train_main_id=data.train_main_id,
                train_specific_id=train_specific_uuid
            )
            clients_list = get_short_clients_of_train_main(
                session=session,
                train_main_id=data.train_main_id
            )
            train_specific = TrainSpecificDataResponse(
                id=train_specific_uuid,
                is_over=False,
                clients_amount=len(clients_list),
                clients_list=clients_list
            )

            return train_specific
    except Exception as e:
        print(e)
        raise InternalServerErrorException