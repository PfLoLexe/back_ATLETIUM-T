from fastapi import HTTPException

weekDayDoesNotExistException = HTTPException(
    status_code=404,
    detail="Week day does not exist, must be between 1 and 7",
)