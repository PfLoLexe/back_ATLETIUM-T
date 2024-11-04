from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from src.db import get_session
from src.models.user import User
from src.requests.auth_request_models import AuthenticationRequest
from src.responses.auth_response_models import AccessTokenResponse
from src.utils.authentication import Authentication

authentication: Authentication = Authentication()

auth_router = APIRouter()

@auth_router.post("/token")
def login(data: AuthenticationRequest, session = Depends(get_session)) -> AccessTokenResponse:
    authentication_result = authentication.authenticate(session=session, auth_data=data)
    return AccessTokenResponse(
        authentication_result.access_token,
        authentication_result.token_type
    )

@auth_router.post("/users/me")
def get_my_user(session=Depends(get_session), current_user = Depends(authentication.current_user)):
    print("!!!!!!!!", current_user)