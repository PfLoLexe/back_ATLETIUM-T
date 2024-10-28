from fastapi import APIRouter, Depends
from typing import TypedDict

from src.db import get_session
from src.models.train_type import TrainTypeDefault, TrainType

train_type_router = APIRouter()

@train_type_router.post("/train-type/add")
def add_train_type(train_type: TrainTypeDefault, session = Depends(get_session)) -> TypedDict('Response', {"status": int, "message": str}):
    train_type = TrainType.model_validate(train_type)
    session.add(train_type)
    session.commit()
    session.refresh(train_type)
    return {"status": 200, "message": "success"}