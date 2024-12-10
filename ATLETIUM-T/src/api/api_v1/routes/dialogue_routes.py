import uuid
from typing import List

from fastapi import Depends, APIRouter
from sqlalchemy import union_all
from sqlmodel import select, and_, or_
from starlette.responses import JSONResponse

from src.core.authentication.authentication import authentication_handler
from src.core.db import app_db
from src.models.dialogue import Dialogue
from src.models.role import Roles
from src.models.train_type import TrainType
from src.models.user import User
from src.schemas.exceptions.common_exceptions import InternalServerErrorException
from src.schemas.requests.dialogue import DialogueCreationRequest, PossibleDialogueListRequest
from src.schemas.responses.common_responses import ItemCreatedSuccessfully
from src.schemas.responses.dialogue import DialogueResponse, PossibleDialoguesUserResponse

dialogue_router = APIRouter()

@dialogue_router.post("/add")
def post_add_dialogue(data: DialogueCreationRequest, session = Depends(app_db.get_session), current_user_id = Depends(authentication_handler.current_user)) -> JSONResponse:
    try:
        dialogue = Dialogue(
            id = uuid.uuid4(),
            first_user_id = current_user_id,
            second_user_id = data.second_user_id,
        )
        session.add(dialogue)
        session.commit()
        response = ItemCreatedSuccessfully
        response.body["dialogue_id"] = dialogue.id
        return response
    except Exception as e:
        print(e)
        return InternalServerErrorException

@dialogue_router.post("/get_list")
def get_dialogues_list(session = Depends(app_db.get_session), current_user_id = Depends(authentication_handler.current_user)) -> List[DialogueResponse]:
    try:
        dialogues_raw = session.exec(
            select(
                User.firstname.label("recipient_user_firstname"),
                User.lastname.label("recipient_user_lastname"),
                User.middle_name.label("recipient_user_middle_name"),
                Dialogue.id.label("dialogue_id"),
                Dialogue.first_user_id.label("first_user_id"),
                Dialogue.second_user_id.label("second_user_id"),
            )
            .where(
                or_(
                    and_(Dialogue.first_user_id == current_user_id, Dialogue.second_user_id == User.id),
                    and_(Dialogue.second_user_id == current_user_id, Dialogue.first_user_id == User.id),
                )
            )
        ).all()
        dialogues: List[DialogueResponse] = []
        if dialogues_raw is not None:
            for row in dialogues_raw:
                dialogue = DialogueResponse(
                    recipient_user_firstname = "NoName" if row.recipient_user_firstname is None else row.recipient_user_firstname,
                    recipient_user_lastname = "" if row.recipient_user_lastname is None else row.recipient_user_lastname,
                    recipient_user_middle_name = "" if row.recipient_user_middle_name is None else row.recipient_user_middle_name,
                    dialogue_id = row.dialogue_id,
                    first_user_id = current_user_id,
                    second_user_id = row.second_user_id if row.first_user_id == current_user_id else row.first_user_id,
                )
                dialogues.append(dialogue)
        return dialogues
    except Exception as e:
        print(e)
        return InternalServerErrorException


@dialogue_router.post("/possible/get_list")
def get_possible_dialogue_list(
        search_request: PossibleDialogueListRequest,
        session = Depends(app_db.get_session),
        current_user_id = Depends(authentication_handler.current_user)
) -> List[PossibleDialoguesUserResponse]:
    try:
        exist_dialogues_current_user_is_second = (
            select(
                Dialogue.first_user_id
            )
            .where(
                Dialogue.second_user_id == current_user_id
            )
        )
        exist_dialogues_current_user_is_first = (
            select(
                Dialogue.second_user_id
            )
            .where(
                Dialogue.first_user_id == current_user_id
            )
        )

        exist_dialogues_summary = union_all(
            exist_dialogues_current_user_is_second,
            exist_dialogues_current_user_is_first
        )

        print("!!!!!!!!!! ", exist_dialogues_summary)

        possible_dialogues_raw = session.exec(
            select(
                User.firstname.label("recipient_user_firstname"),
                User.firstname.label("recipient_user_lastname"),
                User.middle_name.label("recipient_user_middle_name"),
                User.id.label("recipient_user_id"),
            )
            .where(
                User.role != Roles.admin,
                User.id.not_in(exist_dialogues_summary)
            )
        ).all()

        possible_dialogues: List[PossibleDialoguesUserResponse] = []
        if possible_dialogues_raw is not None:
            for row in possible_dialogues_raw:
                if(row.recipient_user_id == current_user_id):
                    possible_dialogue = PossibleDialoguesUserResponse(
                        recipient_user_firstname="Избранное",
                        recipient_user_lastname="",
                        recipient_user_middle_name="",
                        recipient_user_id=row.recipient_user_id,
                    )
                else:
                    possible_dialogue = PossibleDialoguesUserResponse(
                        recipient_user_firstname = "NoName" if row.recipient_user_firstname is None else row.recipient_user_firstname,
                        recipient_user_lastname = "" if row.recipient_user_lastname is None else row.recipient_user_lastname,
                        recipient_user_middle_name = "" if row.recipient_user_middle_name is None else row.recipient_user_middle_name,
                        recipient_user_id=row.recipient_user_id,
                    )
                possible_dialogues.append(possible_dialogue)
        return possible_dialogues
    except Exception as e:
        print(e)
        return InternalServerErrorException