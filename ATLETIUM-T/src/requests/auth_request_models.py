from sqlmodel import SQLModel


class AuthenticationRequest(SQLModel):
    username: str
    password: str
    remember_me: bool = False

