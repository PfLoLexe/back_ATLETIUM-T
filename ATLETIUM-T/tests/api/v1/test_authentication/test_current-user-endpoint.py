from uuid import UUID

import jwt
import pytest

from src.core.config import app_configuration
from src.models.role import Roles
from src.models.user import User
from tests.conftest import get_auth_header
from tests.initial_data import initial_data


@pytest.mark.parametrize(
    "request_data, expected_response",
    [
        pytest.param(
            {
                "username": "user",
                "password": "user",
            },
            {
                "response_body": "5c5d9856-6a9e-432d-9e5d-2d0ee07b9614",
                "status_code": 200
            },
        ),
        pytest.param(
            {
                "username": "admin",
                "password": "admin",
            },
            {
                "response_body": "74bbfdef-f556-4845-9afc-88292985228c",
                "status_code": 200
            },
        ),
        pytest.param(
            {
                "username": "admin",
                "password": "afasdfasdfasd",
            },
            {
                "response_body": {'detail': 'Not authenticated'},
                "status_code": 401
            },
        ),

    ]
)

def test_current_user_endpoint(session, client, request_data, expected_response):
    auth_header = get_auth_header(client, request_data["username"], request_data["password"])

    get_current_user_response = client.get(
        url="/v1/get-current-user-uuid",
        headers=auth_header,
    )

    assert get_current_user_response.status_code == expected_response["status_code"]
    assert get_current_user_response.json() == expected_response["response_body"]
