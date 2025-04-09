from uuid import UUID

import jwt
import pytest

from src.core.config import app_configuration
from src.models.role import Roles
from src.models.user import User
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
                "username": "user",
                "user_id": UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614"),
                "user_role": Roles.trainer,
                "access_token": not None,
                "status_code": 200
            },
        ),
        pytest.param(
            {
                "username": "admin",
                "password": "admin",
            },
            {
                "username": "admin",
                "user_id": UUID("74bbfdef-f556-4845-9afc-88292985228c"),
                "user_role": Roles.admin,
                "access_token": not None,
                "status_code": 200
            },
        ),
        pytest.param(
            {
                "username": "abracadabra",
                "password": "admin",
            },
            {
                "status_code": 401
            },
        ),
        pytest.param(
            {
                "username": "admin",
                "password": "abracadabra",
            },
            {
                "status_code": 401
            },
        ),
        pytest.param(
            {
                "username": None,
                "password": "abracadabra",
            },
            {
                "status_code": 422
            },
        ),
        pytest.param(
            {
                "username": "admin",
                "password": None,
            },
            {
                "status_code": 422
            },
        ),
    ]
)

def test_login_endpoint(session, client, request_data, expected_response):
    response = client.post(
        url="/v1/token",
        json={
            "username": request_data["username"],
            "password": request_data["password"],
        }
    )
    assert response.status_code == expected_response["status_code"]
    if response.status_code == 200:
        access_token = response.json()["access_token"]
        assert (
            (
                access_token is not None
                    and expected_response["access_token"] is not None
            ) or
            (
                access_token is None
                    and expected_response["access_token"] is None
            )
        )
        payload = jwt.decode(access_token, app_configuration.jwt_secret_key,
                             algorithms=[app_configuration.jwt_algorithm])

        username: str = payload.get("sub")
        user_id: UUID = UUID(payload.get("id"))
        user_role: Roles = Roles(payload.get("role"))

        assert username == expected_response["username"]
        assert user_id == expected_response["user_id"]
        assert user_role == expected_response["user_role"]
