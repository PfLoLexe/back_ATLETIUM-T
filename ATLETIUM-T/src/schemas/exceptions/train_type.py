from fastapi import HTTPException

trainTypeDoesNotExistException = HTTPException(
    status_code=404,
    detail="Train type does not exist",
)