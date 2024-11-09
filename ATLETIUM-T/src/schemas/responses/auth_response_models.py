from sqlmodel import SQLModel


class AccessTokenResponse(SQLModel):
    access_token: str
    token_type: str

    def __init__(self, access_token: str, token_type: str):
        self.access_token = access_token
        self.token_type = token_type

class ValidPincodeResponse(SQLModel):
    message: str

    def __init__(self, message: str):
        self.message = message