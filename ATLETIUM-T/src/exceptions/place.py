from fastapi import HTTPException

placeDoesNotExistException = HTTPException(
    status_code=404,
    detail="PLace does not exist",
)