from typing import Optional
from uuid import UUID

import bcrypt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import select, Session

from src.core.db import app_db
from src.models.pincode import Pincode
from src.models.role import Roles
from src.schemas.exceptions.common_exceptions import InternalServerErrorException, UnauthorizedException
from src.models.user import User
from src.schemas.requests.auth_request_models import AuthenticationRequest, TokenRequest
from src.schemas.serializers.user import UserAuthenticationSerializer

from src.core.authentication.password_hasher import Hasher
from src.core.authentication.token import TokenModel, Token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Authentication:
    def __init__(self):
        self.token: Token = Token()

    def check_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password.encode())

    def get_user_by_usname_pass(self, session, username: str, hashed_password: str) -> UserAuthenticationSerializer:
        try:
            user = session.exec(
                select(
                    User.id,
                    User.role,
                    User.username,
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
                is_active=user.is_active
            )
        except Exception as e:
            print(e)
            raise InternalServerErrorException


    def get_user_by_username_role_id(self, session, username: str, role: Roles, user_id: UUID) -> Optional[UserAuthenticationSerializer]:
        try:
            user = session.exec(
                select(
                    User.id,
                    User.is_active,
                ).where(
                    User.username == username,
                    User.id == user_id,
                    User.role == role,
                )
            ).first()
            if user is None:
                return None
            return UserAuthenticationSerializer(
                user_id=user.id,
                is_active=user.is_active
            )
        except Exception as e:
            print(e)
            raise InternalServerErrorException


    def authenticate(self, session: Session, auth_data: AuthenticationRequest) -> TokenModel:
        user = self.get_user_by_usname_pass(
            session,
            username=auth_data.username,
            hashed_password=Hasher.get_password_hash(
                auth_data.password,
                auth_data.username
            )
        )
        if not user or user.is_active is False:
            raise UnauthorizedException

        return self.token.create_access_token(
            TokenRequest(
                username=user.username,
                user_id=user.user_id,
                role=user.role
            )
        )

    def current_user(self, session: Session = Depends(app_db.get_session), token: str = Depends(oauth2_scheme)) -> Optional[UUID]:
        user_auth_data = self.token.decode_token(TokenModel(access_token=token))
        if not user_auth_data or user_auth_data.username is None or user_auth_data.user_id is None:
            raise UnauthorizedException
        user = self.get_user_by_username_role_id(
            session,
            username=user_auth_data.username,
            role=user_auth_data.role,
            user_id=user_auth_data.user_id
        )

        if not user or user.is_active is False:
            raise UnauthorizedException
        return user.user_id


    def verify_pincode(self, pincode_string: str, user_id: UUID, session) -> bool:
        hashed_pincode_string = Hasher.get_pincode_hash(pincode_string)
        pincode = session.exec(
            select(
                Pincode.id
            ).where(
                Pincode.user_id == user_id,
                Pincode.hashed_pincode == hashed_pincode_string
            )
        ).first()
        if pincode is None:
            return False
        return True
        

authentication_handler: Authentication = Authentication()