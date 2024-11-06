from http.client import responses

from fastapi import HTTPException

trainNotFoundException = HTTPException(
    status_code=404,
    detail="Train not found",
)

trainStartTimeMoreThanEndTime = HTTPException(
    status_code=404,
    detail="Train start time is greater than train end time",
)

