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
    client_response: ClientProfileInfoResponse = dict(
        firstname=client.firstname,
        lastname=client.lastname,
        middle_name=client.middle_name,
        phone_number=client.phone_number,
        age=client.age,
        id=str(client.client_id),
        parent_info=None
    )
    if client.age < 18:
        client_response["parent_info"] = dict(
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
                "status_code": 200,
                "firstname": "Александр",
                "lastname": "Александров",
                "middle_name": "Александрович",
                "phone_number": "+7idi45",
                "age": 22,
                "id": "6f793564-ce9d-417e-b5df-6324eca497d0",
                "parent_info": None
            },
        ),
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "client_id": "6f793564-ce9d-417e-b5df-6324eca497d1"
            },
            {
                "status_code": 404,
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
                "status_code": 200,
                "firstname": "Евгений",
                "lastname": "Евгеньев",
                "middle_name": "Евгеньевич",
                "phone_number": "+78885554445",
                "age": 17,
                "id": "26e49df1-ed81-48de-9ed6-604a32b5f4cf",
                "parent_info": {
                    "firstname": "Анатолий",
                    "lastname": "Анкиражев",
                    "middle_name": None,
                    "phone_number": "+79995556545"
                }
            },
        ),
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "client_id": "1241242145"
            },
            {
                "status_code": 422,
            },
        ),
        pytest.param(
            {
                "username": "abacaba",
                "password": "user",
            },
            {
                "client_id": "6f793564-ce9d-417e-b5df-6324eca497d0"
            },
            {
                "status_code": 401,
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

    if(get_client_info_response.status_code == 200):
        expected_client_info: ClientProfileInfoResponse = get_expected_client_info(
            session=session,
            client_id=UUID(request_data["client_id"])
        )
        client_info_response_data = get_client_info_response.json()

        assert client_info_response_data["id"] == expected_client_info["id"]
        assert client_info_response_data["firstname"] == expected_client_info["firstname"]
        assert client_info_response_data["lastname"] == expected_client_info["lastname"]
        assert client_info_response_data["middle_name"] == expected_client_info["middle_name"]
        assert client_info_response_data["phone_number"] == expected_client_info["phone_number"]
        assert client_info_response_data["age"] == expected_client_info["age"]
        assert (
            ("parent_info" not in client_info_response_data.keys()
             and
             expected_client_info["parent_info"] is None
            )
            or
            ("parent_info" in client_info_response_data.keys()
            and
             client_info_response_data["parent_info"] == expected_client_info["parent_info"]
            )
        )
