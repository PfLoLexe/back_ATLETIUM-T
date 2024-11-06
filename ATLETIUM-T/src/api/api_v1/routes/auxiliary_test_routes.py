from fastapi import APIRouter, Depends

from sqlalchemy import text
from starlette.responses import JSONResponse

from src.core.db import app_db
from src.schemas.exceptions.common_exceptions import InternalServerErrorException
from src.utils.sql.sql_query import sql_query_handler

auxiliary_test_routes = APIRouter()

@auxiliary_test_routes.post("/run-default-insert")
def run_default_insert(session = Depends(app_db.get_session)) -> JSONResponse:
    try:
        query = sql_query_handler.get_sql_query(sql_query_filename="default_insert")
        session.exec(text(query))
        session.commit()
    except Exception as e:
        print(e)
        return InternalServerErrorException

@auxiliary_test_routes.delete("/clean-all")
def get_list_of_train_types(session = Depends(app_db.get_session)):
    try:
        query = sql_query_handler.get_sql_query(sql_query_filename="clean_all")
        session.exec(text(query))
        session.commit()
    except Exception as e:
        print(e)
        return InternalServerErrorException