from fastapi import HTTPException


InternalServerErrorException: HTTPException = (
    HTTPException(status_code=500, detail="Internal Server Error"))

ValidateFailedException: HTTPException = (
    HTTPException(status_code=400, detail="Validation Failed")
)