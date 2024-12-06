from fastapi import Depends, APIRouter
from sqlmodel import select

from src.core.authentication.authentication import authentication_handler
from src.core.db import app_db
from src.models.user import User
from src.schemas.exceptions.common_exceptions import InternalServerErrorException
from src.schemas.responses.user import TrainerInfoResponse

user_router = APIRouter()

@user_router.get("/me")
def get_trainer_info(session = Depends(app_db.get_session), current_user_id = Depends(authentication_handler.current_user)) -> TrainerInfoResponse:
    try:
        trainer = session.exec(
            select(
                User.firstname.label("firstname"),
                User.lastname.label("lastname"),
                User.middle_name.label("middle_name"),
                User.phone_number.label("phone_number"),
                User.id.label("trainer_id"),
            )
            .where(
                User.id == current_user_id
            )
        ).first()
        return TrainerInfoResponse(
            firstname=trainer.firstname,
            lastname=trainer.lastname,
            middle_name=trainer.middle_name,
            phone_number=trainer.phone_number,
            trainer_id=trainer.trainer_id,
        )
    except Exception as e:
        print(e)
        raise InternalServerErrorException