from fastapi import APIRouter, Depends

from sqlmodel import select
from starlette.responses import JSONResponse

from src.core.db import app_db
from src.schemas.exceptions.common_exceptions import InternalServerErrorException
from src.models.place import PlaceDefault, PLace
from src.schemas.responses.common_responses import ItemCreatedSuccessfully

place_router = APIRouter(prefix="/place")

@place_router.post("/add")
def post_add_place(place: PlaceDefault, session = Depends(app_db.get_session)) -> JSONResponse:
    try:
        place = PLace.model_validate(place)
        session.add(place)
        session.commit()
        session.refresh(place)
        return ItemCreatedSuccessfully
    except Exception as e:
        print(e)
        return InternalServerErrorException


@place_router.get("/get-list")
def get_list_of_places(session = Depends(app_db.get_session)):
    try:
        places = session.exec(select(PLace)).all()
        return places
    except Exception as e:
        print(e)
        raise InternalServerErrorException