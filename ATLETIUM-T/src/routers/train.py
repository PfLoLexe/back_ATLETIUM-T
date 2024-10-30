from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from typing import TypedDict, List

from sqlalchemy import text
from sqlmodel import select
from starlette.responses import JSONResponse

from src.db import *
from src.exceptions.common_exceptions import InternalServerErrorException
from src.exceptions.place import placeDoesNotExistException
from src.exceptions.train import trainNotFoundException, trainStartTimeMoreThanEndTime
from src.exceptions.train_type import trainTypeDoesNotExistException
from src.exceptions.week_day_number import weekDayDoesNotExistException
from src.models.place import PLace
from src.models.train_type import TrainType
from src.responses.common_responses import ItemCreatedSuccessfully, ItemUpdatedSuccessfully

from src.utils.sql.sql_query import SqlQuery

from src.models.train import Train, TrainDefault


train_router = APIRouter()

@train_router.get("/train/get-list/by-week-day-number")
def get_list_of_trains(week_day_number: int, session = Depends(get_session)):
    try:
        query = SqlQuery.get_sql_query("select_trains_as_list_item")
        query=query.format(week_day_number=week_day_number)
        trains = [dict(row) for row in session.exec(text(query)).mappings()]
        print(trains)
        return trains
    except Exception as e:
        print(e)
        raise InternalServerErrorException


@train_router.post("/train-add")
def post_add_train(train: TrainDefault, session: Session = Depends(get_session)) -> JSONResponse:
    try:
        train = Train.model_validate(train)
        session.add(train)
        session.commit()
        session.refresh(train)
        return ItemCreatedSuccessfully
    except Exception as e:
        print(e)
        raise InternalServerErrorException


@train_router.put("/train-update/{train_id}")
def put_change_train(train_id: UUID, new_train_data: TrainDefault, session=Depends(get_session)) -> dict[str, str]:
    try:
        train = session.get(Train, train_id)
        if not train:
            raise trainNotFoundException
        place = session.get(PLace, new_train_data.place_id)
        if not place:
            raise placeDoesNotExistException
        train_type = session.get(TrainType, new_train_data.train_type_id)
        if not train_type:
            raise trainTypeDoesNotExistException
        if new_train_data.week_day_number < 1 or new_train_data.week_day_number > 7:
            raise weekDayDoesNotExistException
        if new_train_data.end_time < new_train_data.start_time:
            raise trainStartTimeMoreThanEndTime
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n")
        train.place_id = new_train_data.place_id
        train.week_day_number = new_train_data.week_day_number
        train.train_type_id = new_train_data.train_type_id
        train.end_time = new_train_data.end_time
        train.start_time = new_train_data.start_time
        train.label = new_train_data.label
        session.commit()
        session.refresh(train)
        return ItemUpdatedSuccessfully
    except Exception as e:
        print(e)
        raise InternalServerErrorException

