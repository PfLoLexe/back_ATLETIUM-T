from fastapi import APIRouter, Depends
from typing import TypedDict

from sqlmodel import select
from starlette.responses import JSONResponse

from src.db import get_session
from src.exceptions.common_exceptions import InternalServerErrorException, ValidateFailedException
from src.models.train_type import TrainTypeDefault, TrainType
from src.responses.common_responses import ItemCreatedSuccessfully
from src.utils.sql.sql_query import SqlQuery

train_type_router = APIRouter()

@train_type_router.post("/train-type/add")
def post_add_train_type(train_type: TrainTypeDefault, session = Depends(get_session)) -> JSONResponse:
    try:
        train_type = TrainType.model_validate(train_type)
        session.add(train_type)
        session.commit()
        session.refresh(train_type)
        return ItemCreatedSuccessfully
    except Exception as e:
        print(e)
        return InternalServerErrorException

@train_type_router.get("/train-type/get-list")
def get_list_of_train_types(session = Depends(get_session)):
    try:
        trains_types = session.exec(select(TrainType)).all()
        return trains_types
    except Exception as e:
        print(e)
        raise InternalServerErrorException