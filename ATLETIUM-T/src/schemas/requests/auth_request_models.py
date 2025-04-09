from uuid import UUID

from sqlmodel import SQLModel, Field

from src.models.role import Roles


class AuthenticationRequest(SQLModel):
    username: str
    password: str

class TokenRequest(SQLModel):
    username: str
    user_id: UUID
    role: Roles

class VeryPincodeRequest(SQLModel):
    pincode: str = Field(max_length=6, min_length=6)