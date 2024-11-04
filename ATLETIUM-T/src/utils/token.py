import os
from datetime import datetime, timedelta

import jwt
from sqlmodel import SQLModel
from typing_extensions import Optional

from src.requests.auth_request_models import AuthenticationRequest
from src.serializers.user import UserAuthenticationSerializer


class TokenModel(SQLModel):
    access_token: str
    token_type: str
    def __init__(self, access_token: str, token_type: str = os.getenv("JWT_TOKEN_TYPE")):
        self.access_token = access_token
        self.token_type = token_type

class Token():

    def get_expire_time(self, remember_me: bool):
        time_delta: timedelta
        if remember_me:
            time_delta = timedelta(days=float(os.getenv("ACCESS_TOKEN_LONG_EXPIRE_TIME")))
        else:
            time_delta = timedelta(minutes=float(os.getenv("ACCESS_TOKEN_STANDARD_EXPIRE_TIME")))
        return str(datetime.utcnow() + time_delta)

    def create_access_token(self, token_request: AuthenticationRequest) -> TokenModel:
        expire_time = self.get_expire_time(token_request.remember_me)
        data: dict = {
            "sub": token_request.username,
            "pass": token_request.password,
            "expire": expire_time
        }
        encoded_jwt = jwt.encode(data, os.getenv("SECRET_KEY"), algorithm=os.getenv("JWT_TOKEN_GENERATION_ALGORITHM"))
        token: TokenModel = TokenModel(access_token=encoded_jwt)
        return token

    def decode_token(self, token: TokenModel) -> Optional[UserAuthenticationSerializer]:
        try:
            payload = jwt.decode(token.access_token, os.getenv("SECRET_KEY"), algorithms=[os.getenv("JWT_TOKEN_GENERATION_ALGORITHM")])
            username: str = payload.get("sub")
            password: str = payload.get("pass")
            return UserAuthenticationSerializer(username=username, hashed_password=password)
        except Exception as e:
            print(e)
            return None