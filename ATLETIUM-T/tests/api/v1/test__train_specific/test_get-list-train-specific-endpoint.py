from uuid import UUID

import pytest
from sqlmodel import select

from src.models.train_specific import TrainSpecific
from tests.conftest import get_auth_header

@pytest.mark.parametrize(
    "auth_data, request_data, expected_response",
    [
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "train_main_id": "38b40437-0541-44ed-871a-f1a04fba179b",
                "date": "2024-10-31"
            },
            {
                "status_code": 200,
                "clients_amount": 3,
                "is_over": True,
                "clients_list": []
            },
        ),
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "train_main_id": "41e5c441-16b4-4c98-a3a7-7bd32589e048",
                "date": "2025-04-14"
            },
            {
                "status_code": 200,
                "clients_amount": 1,
                "is_over": False,
                "clients_list": [
                    {
                        "firstname": "Александр",
                        "lastname": "Александров",
                        "id": "6f793564-ce9d-417e-b5df-6324eca497d0",
                        "visit_status": 1
                    }
                ]
            },
        ),
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "train_main_id": "41e5c441-16b4-4c98-a3a7-7bd32589e047",
                "date": "2025-04-14"
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
                "train_main_id": "38b40437-0541-44ed-871a-f1a04fba179b",
                "date": "2024-13-31"
            },
            {
                "status_code": 422,
            },
        ),
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "train_main_id": "3844ed-871a-f1a04fba179b",
                "date": "2024-04-31"
            },
            {
                "status_code": 422,
            },
        ),
        pytest.param(
            {
                "username": "user",
                "password": "aaaaaaa",
            },
            {
                "train_main_id": "38b40437-0541-44ed-871a-f1a04fba179b",
                "date": "2024-04-30"
            },
            {
                "status_code": 401,
            },
        ),
    ]
)
def test_current_user_endpoint(session, client, auth_data, request_data, expected_response):
    get_train_main_response = client.post(
        url="/v1/train-specific/get",
        json={
            "train_main_id": request_data["train_main_id"],
            "date": request_data["date"]
        },
        headers=get_auth_header(
            client=client,
            username=auth_data["username"],
            password=auth_data["password"]
        ),
    )

    assert get_train_main_response.status_code == expected_response["status_code"]

    if(get_train_main_response.status_code == 200):
        get_train_main_response_data = get_train_main_response.json()

        assert get_train_main_response_data["clients_amount"] == expected_response["clients_amount"]
        assert get_train_main_response_data["is_over"] == expected_response["is_over"]
        assert get_train_main_response_data["clients_list"] == expected_response["clients_list"]

        train_specific_raw = session.exec(
            select(
                TrainSpecific.id.label("id"),
                TrainSpecific.clients_amount.label("clients_amount"),
                TrainSpecific.is_over.label("is_over"),
            ).where(
                TrainSpecific.id == UUID(get_train_main_response_data["id"])
            )
        ).first()
        assert train_specific_raw is not None
        #TODO: запрашивать из БД по train main id и смотреть на кол-во записей
