import os
from datetime import datetime, timedelta, timezone

import jwt
from sqlmodel import SQLModel
from typing_extensions import Optional

from src.core.config import app_configuration
from src.schemas.requests.auth_request_models import AuthenticationRequest
from src.schemas.serializers.user import UserAuthenticationSerializer


class TokenModel(SQLModel):
    access_token: str
    token_type: str
    def __init__(self, access_token: str, token_type: str = app_configuration.jwt_token_type):
        self.access_token = access_token
        self.token_type = token_type

class Token():

    def get_expire_time(self, remember_me: bool):
        time_delta: timedelta
        if remember_me:
            time_delta = timedelta(days=float(app_configuration.access_token_expire_time_long))
        else:
            time_delta = timedelta(minutes=float(app_configuration.access_token_expire_time_standard))
        expire = datetime.now(timezone.utc) + time_delta
        expire_time = expire.timestamp()
        return expire_time

    def create_access_token(self, token_request: AuthenticationRequest) -> TokenModel:
        expire_time = self.get_expire_time(token_request.remember_me)
        data: dict = {
            "sub": token_request.username,
            "pass": token_request.password,
            "expire": expire_time
        }
        encoded_jwt = jwt.encode(data, app_configuration.jwt_secret_key, algorithm=app_configuration.jwt_algorithm)
        token: TokenModel = TokenModel(access_token=encoded_jwt)
        return token

    def decode_token(self, token: TokenModel) -> Optional[UserAuthenticationSerializer]:
        try:
            payload = jwt.decode(token.access_token, app_configuration.jwt_secret_key, algorithms=[app_configuration.jwt_algorithm])
            username: str = payload.get("sub")
            password: str = payload.get("pass")

            expire: str = payload.get("expire")
            expire_time = datetime.fromtimestamp(expire, tz=timezone.utc)
            if (not expire) or (expire_time < datetime.now(timezone.utc)):
                return None

            return UserAuthenticationSerializer(username=username, hashed_password=password)
        except Exception as e:
            print(e)
            return None