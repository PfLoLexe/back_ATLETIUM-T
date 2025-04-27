from uuid import UUID

import pytest

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
              "week_day_number": 1,
              "date": "2025-04-14"
            },
            {
                "status_code": 200,
                "trains": [
                    {
                        "id": "41e5c441-16b4-4c98-a3a7-7bd32589e048",
                        "name": "Плавание 10+",
                        "start_time": "11:30:00.000343",
                        "end_time": "13:00:00.000343",
                        "place_name": "Pool",
                        "train_type": "Group",
                        "date": None
                    },
                    {
                        "id": "d6ab1705-4e24-4e0e-bb42-eba1def3cfd3",
                        "name": "Функциональный фитнес",
                        "start_time": "11:30:00.000343",
                        "end_time": "13:00:00.000343",
                        "place_name": "Gym",
                        "train_type": "Group",
                        "date": None
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
                "week_day_number": 3,
                "date": ""
            },
            {
                "status_code": 200,
                "trains": [
                    {
                        "id": "54626715-00a1-463e-9f64-6f5d3b160d2d",
                        "name": "Бокс",
                        "start_time": "11:30:00.000343",
                        "end_time": "13:00:00.000343",
                        "place_name": "Boxing hall",
                        "train_type": "Group",
                        "date": None
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
                "week_day_number": None,
                "date": "2025-04-14"
            },
            {
                "status_code": 200,
                "trains": []
            },
        ),
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "week_day_number": None,
                "date": None
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
                "week_day_number": 3,
                "date": "2025-04-14"
            },
            {
                "status_code": 401,
                "trains": []
            },
        ),
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "week_day_number": 2,
                "date": "2025-04-15"
            },
            {
                "status_code": 200,
                "trains": []
            },
        ),
        pytest.param(
            {
                "username": "admin",
                "password": "admin",
            },
            {
                "week_day_number": 1,
                "date": "2025-04-14"
            },
            {
                "status_code": 200,
                "trains": []
            },
        ),
    ]
)
def test_current_user_endpoint(session, client, auth_data, request_data, expected_response):
    get_train_main_response = client.post(
        url="/v1/train-main/get-list/by-week-day-number",
        json={
            "week_day_number": request_data["week_day_number"],
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

        assert get_train_main_response_data == expected_response["trains"]
