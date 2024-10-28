from fastapi import APIRouter, Depends, HTTPException
from typing import TypedDict, List

from sqlalchemy import text
from sqlmodel import select

from src.db import *
from src.exceptions.common_exceptions import InternalServerErrorException

from src.utils.sql.sql_query import SqlQuery

from src.models.train import Train, TrainDefault


train_router = APIRouter()

@train_router.get("/get-train-list/by-week-day-number")
def add_train_type(week_day_number, session = Depends(get_session)):
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
def add_region(train: TrainDefault, session: Session = Depends(get_session)) -> dict[str, str]:
    try:
        train = Train.model_validate(train)
        session.add(train)
        session.commit()
        session.refresh(train)
        return {"message": "Train added successfully"}
    except Exception as e:
        print(e)
        raise InternalServerErrorException
