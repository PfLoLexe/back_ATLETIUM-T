from uuid import UUID

from fastapi import APIRouter, Depends

from src.core.authentication.authentication import authentication_handler
from src.core.db import app_db
from src.schemas.exceptions.common_exceptions import UnauthorizedException, UnauthorizedExceptionWrongPincode
from src.schemas.requests.auth_request_models import AuthenticationRequest, VeryPincodeRequest
from src.schemas.responses.auth_response_models import AccessTokenResponse, ValidPincodeResponse

auth_router = APIRouter()

@auth_router.post("/token")
def login(data: AuthenticationRequest, session = Depends(app_db.get_session)) -> AccessTokenResponse:
    authentication_result = authentication_handler.authenticate(
        session=session, auth_data=data)
    return AccessTokenResponse(
        authentication_result.access_token,
        authentication_result.token_type
    )

@auth_router.get("/get-current-user-uuid")
def get_my_user(current_user_id = Depends(authentication_handler.current_user)) -> UUID:
    return current_user_id


@auth_router.post("/verify-pincode")
def verify_pincode(pincode: VeryPincodeRequest, session = Depends(app_db.get_session), current_user_id = Depends(authentication_handler.current_user)):
    verify_result = authentication_handler.verify_pincode(pincode_string=pincode.pincode, user_id=current_user_id, session=session)
    if not verify_result:
        raise UnauthorizedExceptionWrongPincode
    return ValidPincodeResponse(message="Pincode verified")


@auth_router.post("/register-user")
def register_user():
    pass