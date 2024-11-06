from fastapi import APIRouter, Depends

from src.core.authentication.authentication import authentication_handler
from src.core.db import app_db
from src.schemas.requests.auth_request_models import AuthenticationRequest
from src.schemas.responses.auth_response_models import AccessTokenResponse

auth_router = APIRouter()

@auth_router.post("/token")
def login(data: AuthenticationRequest, session = Depends(app_db.get_session)) -> AccessTokenResponse:
    authentication_result = authentication_handler.authenticate(session=session, auth_data=data)
    return AccessTokenResponse(
        authentication_result.access_token,
        authentication_result.token_type
    )

@auth_router.post("/users/me")
def get_my_user(session=Depends(app_db.get_session), current_user = Depends(authentication_handler.current_user)):
    print("!!!!!!!!", current_user)