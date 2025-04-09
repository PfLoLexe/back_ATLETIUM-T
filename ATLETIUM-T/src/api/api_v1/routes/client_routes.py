from fastapi import APIRouter, Depends
from sqlmodel import select

from src.core.authentication.authentication import authentication_handler
from src.core.db import app_db
from src.models.client import Client
from src.schemas.requests.client import ClientProfileInfoRequest
from src.schemas.responses.client import ClientProfileInfoResponse, ClientParentInfoResponse
from src.schemas.exceptions.common_exceptions import InternalServerErrorException

client_router = APIRouter(prefix="/client")

@client_router.post('/get-info')
def get_client_profile_info(
    data: ClientProfileInfoRequest,
    session = Depends(app_db.get_session),
    current_user_id = Depends(authentication_handler.current_user)
) -> ClientProfileInfoResponse:
    try:
        client = session.exec(
            select(
                Client.firstname.label("firstname"),
                Client.lastname.label("lastname"),
                Client.middle_name.label("middle_name"),
                Client.phone_number.label("phone_number"),
                Client.age.label("age"),
                Client.id.label("client_id"),
                Client.parent_firstname.label("parent_firstname"),
                Client.parent_lastname.label("parent_lastname"),
                Client.parent_middle_name.label("parent_middle_name"),
                Client.parent_phone_number.label("parent_phone_number"),
            )
            .where(
                Client.id == data.client_id
            )
        ).first()
        client_response = ClientProfileInfoResponse(
            firstname=client.firstname,
            lastname=client.lastname,
            middle_name=client.middle_name,
            phone_number=client.phone_number,
            age=client.age,
            id=client.client_id,
        )
        if client.age < 18:
            client_response.parent_info = ClientParentInfoResponse(
                firstname=client.parent_firstname,
                lastname=client.parent_lastname,
                middle_name=client.parent_middle_name,
                phone_number=client.parent_phone_number,
            )
        return client_response

    except Exception as e:
        print(e)
        raise InternalServerErrorException