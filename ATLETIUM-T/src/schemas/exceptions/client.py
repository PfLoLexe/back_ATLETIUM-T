from fastapi import HTTPException

clientDoesNotExistException = HTTPException(
    status_code=404,
    detail="Client does not exist",
)