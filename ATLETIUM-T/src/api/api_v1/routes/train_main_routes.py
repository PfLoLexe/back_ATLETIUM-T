﻿from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlmodel import or_

from src.core.db import app_db
from src.schemas.exceptions.common_exceptions import InternalServerErrorException
from src.models.place import PLace
from src.models.train_main import TrainMain
from src.schemas.requests.train_main import TrainMainListRequest
from src.schemas.responses.train_main import TrainMainListItemResponse

train_main_router = APIRouter()

@train_main_router.post("/get-list/by-week-day-number")
def get_list_of_main_trains(data: TrainMainListRequest, session = Depends(app_db.get_session)) -> List[TrainMainListItemResponse]:
    try:
        result = session.exec(
            select(
                TrainMain.id.label("id"),
                TrainMain.name.label("name"),
                TrainMain.start_time.label("start_time"),
                TrainMain.end_time.label("end_time"),
                PLace.name.label("place_name)"),
                TrainMain.train_type_id.label("type_uuid"),
                TrainMain.date.label("date"),

            ).where(
                TrainMain.week_day_number == data.week_day_number,
                TrainMain.trainer_id == data.trainer_id,
                or_(TrainMain.date == None, TrainMain.date == data.date),
                TrainMain.place_id == PLace.id
            )
        )
        if result is not None:
            trains = [TrainMainListItemResponse(**row) for row in result.mappings()]
            return trains
        else:
            return []
    except Exception as e:
        print(e)
        raise InternalServerErrorException



# @train_main_router.put("/train-update/{train_id}")
# def put_change_train(train_id: UUID, new_train_data: TrainWithFK, session=Depends(get_session)) -> dict[str, str]:
#     try:
#         train = session.get(Train, train_id)
#         if not train:
#             raise trainNotFoundException
#         place = session.get(PLace, new_train_data.place_id)
#         if not place:
#             raise placeDoesNotExistException
#         train_type = session.get(TrainType, new_train_data.train_type_id)
#         if not train_type:
#             raise trainTypeDoesNotExistException
#         if new_train_data.week_day_number < 1 or new_train_data.week_day_number > 7:
#             raise weekDayDoesNotExistException
#         if new_train_data.end_time < new_train_data.start_time:
#             raise trainStartTimeMoreThanEndTime
#         train.place_id = new_train_data.place_id
#         train.week_day_number = new_train_data.week_day_number
#         train.train_type_id = new_train_data.train_type_id
#         train.end_time = new_train_data.end_time
#         train.start_time = new_train_data.start_time
#         train.label = new_train_data.label
#         session.commit()
#         session.refresh(train)
#         return ItemUpdatedSuccessfully
#     except Exception as e:
#         print(e)
#         raise InternalServerErrorException
#
