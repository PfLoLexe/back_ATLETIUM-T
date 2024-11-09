from typing import Optional
from uuid import UUID

import bcrypt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import select, Session

from src.core.db import app_db
from src.schemas.exceptions.common_exceptions import InternalServerErrorException, UnauthorizedException
from src.models.user import User
from src.models.role import Roles
from src.schemas.requests.auth_request_models import AuthenticationRequest
from src.schemas.serializers.user import UserAuthenticationSerializer

from src.core.authentication.password_hasher import PasswordHasher
from src.core.authentication.token import TokenModel, Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Authentication:
    def __init__(self):
        self.token: Token = Token()

    def check_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())

    def get_user(self, session, username: str, hashed_password: str) -> UserAuthenticationSerializer:
        try:
            user = session.exec(
                select(
                    User.id,
                    User.role,
                    User.username,
                    User.hashed_password,
                    User.is_active,
                ).where(
                    User.username == username,
                    User.hashed_password == hashed_password
                )
            ).first()
            if user is None:
                return None
            return UserAuthenticationSerializer(
                user_id=user.id,
                role=user.role,
                username=user.username,
                hashed_password=user.hashed_password,
                is_active=user.is_active
            )
        except Exception as e:
            print(e)
            raise InternalServerErrorException

    def authenticate(self, session: Session, auth_data: AuthenticationRequest) -> TokenModel:
        user = self.get_user(
            session,
            username=auth_data.username,
            hashed_password=PasswordHasher.get_password_hash(
                auth_data.password,
                auth_data.username
            )
        )
        if not user or user.is_active is False:
            raise UnauthorizedException
        return self.token.create_access_token(
            AuthenticationRequest(
                username=user.username,
                password=user.hashed_password,
                remember_me=auth_data.remember_me
            )
        )

    def current_user(self, session: Session = Depends(app_db.get_session), token: str = Depends(oauth2_scheme)) -> Optional[UUID]:
        user_auth_data = self.token.decode_token(TokenModel(access_token=token))
        if not user_auth_data or user_auth_data.username is None or user_auth_data.hashed_password is None:
            raise UnauthorizedException
        user = self.get_user(session, user_auth_data.username, user_auth_data.hashed_password)

        if not user or user.is_active is False:
            raise UnauthorizedException
        return user.user_id

authentication_handler: Authentication = Authentication()