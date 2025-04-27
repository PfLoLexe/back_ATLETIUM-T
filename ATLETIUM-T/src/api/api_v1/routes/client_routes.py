from fastapi import APIRouter, Depends
from sqlmodel import select

from src.core.authentication.authentication import authentication_handler
from src.core.db import app_db
from src.models.client import Client
from src.models.client_parent_info import ClientParentInfo
from src.models.parent_to_client_link import ParentToClientLink
from src.schemas.exceptions.client import clientDoesNotExistException
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
            )
            .where(
                Client.id == data.client_id
            )
        ).first()
        client_parent_info = session.exec(
            select(
                ClientParentInfo.firstname.label("parent_firstname"),
                ClientParentInfo.lastname.label("parent_lastname"),
                ClientParentInfo.middle_name.label("parent_middle_name"),
                ClientParentInfo.phone_number.label("parent_phone_number"),
                ClientParentInfo.id.label("parent_id"),
            )
            .where(
                ParentToClientLink.client_id == data.client_id,
                ParentToClientLink.parent_id == ClientParentInfo.id,
            )
        ).first()
        if client is not None:
            client_response = ClientProfileInfoResponse(
                firstname=client.firstname,
                lastname=client.lastname,
                middle_name=client.middle_name,
                phone_number=client.phone_number,
                age=client.age,
                id=client.client_id,
            )
            if client_parent_info is not None:
                client_response.parent_info = ClientParentInfoResponse(
                    firstname=client_parent_info.parent_firstname,
                    lastname=client_parent_info.parent_lastname,
                    middle_name=client_parent_info.parent_middle_name,
                    phone_number=client_parent_info.parent_phone_number,
                )
            return client_response
        else:
            raise clientDoesNotExistException
    except Exception as e:
        print(e)
        raise e