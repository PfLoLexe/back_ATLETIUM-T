from fastapi import APIRouter, Depends
from typing import TypedDict, List

from sqlmodel import select
from starlette.responses import JSONResponse

from src.db import get_session
from src.exceptions.common_exceptions import InternalServerErrorException
from src.models.place import PlaceDefault, PLace
from src.responses.common_responses import ItemCreatedSuccessfully

place_router = APIRouter()

@place_router.post("/place/add")
def post_add_place(place: PlaceDefault, session = Depends(get_session)) -> JSONResponse:
    try:
        place = PLace.model_validate(place)
        session.add(place)
        session.commit()
        session.refresh(place)
        return ItemCreatedSuccessfully
    except Exception as e:
        print(e)
        return InternalServerErrorException


@place_router.get("/place/get-list")
def get_list_of_places(session = Depends(get_session)):
    try:
        places = session.exec(select(PLace)).all()
        return places
    except Exception as e:
        print(e)
        raise InternalServerErrorException