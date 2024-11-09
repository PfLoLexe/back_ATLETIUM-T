from fastapi import HTTPException
from starlette import status

InternalServerErrorException: HTTPException = (
    HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"))

ValidateFailedException: HTTPException = (
    HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Validation Failed")
)

UnauthorizedException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Unauthorized",
)

UnauthorizedExceptionWrongPincode = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Unauthorized pincode",
)