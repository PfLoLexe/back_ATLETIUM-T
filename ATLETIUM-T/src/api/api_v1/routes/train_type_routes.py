from fastapi import APIRouter, Depends

from sqlmodel import select
from starlette.responses import JSONResponse

from src.core.db import app_db
from src.schemas.exceptions.common_exceptions import InternalServerErrorException
from src.models.train_type import TrainTypeDefault, TrainType
from src.schemas.responses.common_responses import ItemCreatedSuccessfully

train_type_router = APIRouter(prefix="/train-type")

@train_type_router.post("/add")
def post_add_train_type(train_type: TrainTypeDefault, session = Depends(app_db.get_session)) -> JSONResponse:
    try:
        train_type = TrainType.model_validate(train_type)
        session.add(train_type)
        session.commit()
        session.refresh(train_type)
        return ItemCreatedSuccessfully
    except Exception as e:
        print(e)
        return InternalServerErrorException

@train_type_router.get("/get-list")
def get_list_of_train_types(session = Depends(app_db.get_session)):
    try:
        trains_types = session.exec(select(TrainType)).all()
        return trains_types
    except Exception as e:
        print(e)
        raise InternalServerErrorException