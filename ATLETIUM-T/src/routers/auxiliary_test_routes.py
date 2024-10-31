from fastapi import APIRouter, Depends
from typing import TypedDict

from sqlalchemy import text
from sqlmodel import select
from starlette.responses import JSONResponse

from src.db import get_session
from src.exceptions.common_exceptions import InternalServerErrorException, ValidateFailedException
from src.models.train_type import TrainTypeDefault, TrainType
from src.responses.common_responses import ItemCreatedSuccessfully
from src.utils.sql.sql_query import SqlQuery

auxiliary_test_routes = APIRouter()

@auxiliary_test_routes.post("/auxiliary_test_routes/run-default-insert")
def run_default_insert(session = Depends(get_session)) -> JSONResponse:
    try:
        query = SqlQuery.get_sql_query("default_insert")
        session.exec(text(query))
        session.commit()
    except Exception as e:
        print(e)
        return InternalServerErrorException

@auxiliary_test_routes.delete("/auxiliary_test_routes/clean-all")
def get_list_of_train_types(session = Depends(get_session)):
    try:
        query = SqlQuery.get_sql_query("clean_all")
        session.exec(text(query))
        session.commit()
    except Exception as e:
        print(e)
        return InternalServerErrorException