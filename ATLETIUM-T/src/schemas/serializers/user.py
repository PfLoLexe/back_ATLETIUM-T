from typing import Optional
from uuid import UUID

from src.models.role import Roles


class UserCreateSerializer:
    username: str
    password: str
    firstname: Optional[str]
    lastname: Optional[str]
    middle_name: Optional[str]

class UserPasswordUpdateSerializer:
    old_password: str
    new_password: str

class UserAuthenticationSerializer:
    user_id: Optional[UUID]
    username: str
    hashed_password: str
    is_active: Optional[bool]
    role: Optional[Roles]
    def __init__(
        self,
        username: Optional[str] = None, hashed_password: Optional[str] = None,
        is_active: Optional[bool] = None,
        user_id: Optional[UUID] = None,
        role: Optional[Roles] = None
    ):
        self.username = username
        self.hashed_password = hashed_password
        self.is_active = is_active
        self.user_id = user_id
        self.role = role
