from uuid import UUID

import pytest
from sqlalchemy import select

from src.models.client import Client
from src.schemas.responses.client import ClientProfileInfoResponse, ClientParentInfoResponse
from tests.conftest import get_auth_header

def get_expected_client_info(session, client_id) -> ClientProfileInfoResponse:
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
            Client.id == client_id
        )
    ).first()
    client_response: ClientProfileInfoResponse = ClientProfileInfoResponse(
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


@pytest.mark.parametrize(
    "auth_data, request_data, expected_response",
    [
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "client_id": "6f793564-ce9d-417e-b5df-6324eca497d0"
            },
            {
                "status_code": 200
            },
        ),
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "client_id": "26e49df1-ed81-48de-9ed6-604a32b5f4cf"
            },
            {
                "status_code": 200
            },
        ),
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "client_id": None
            },
            {
                "status_code": 422
            },
        ),
    ]
)
def test_current_user_endpoint(session, client, auth_data, request_data, expected_response):
    get_client_info_response = client.post(
        url="/v1/client/get-info",
        json={
            "client_id": request_data["client_id"],
        },
        headers=get_auth_header(
            client=client,
            username=auth_data["username"],
            password=auth_data["password"]
        ),
    )
    assert get_client_info_response.status_code == expected_response["status_code"]

    print(get_client_info_response.json())

    expected_client_info: ClientProfileInfoResponse = get_expected_client_info(
        session=session,
        client_id=UUID(request_data["client_id"])
    )

    print(expected_client_info)

    assert 1 == 0

    pass

