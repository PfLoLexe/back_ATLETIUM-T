from starlette.responses import JSONResponse
from sqlalchemy import text
from src.utils.sql.sql_query import sql_query_handler
from src.schemas.exceptions.common_exceptions import InternalServerErrorException


def default_insert(session):
    try:
        query = sql_query_handler.get_sql_query(sql_query_filename="default_insert")
        session.exec(text(query))
        session.commit()
    except Exception as e:
        print(e)
        return InternalServerErrorException

def delete_data(session):
    try:
        query = sql_query_handler.get_sql_query(sql_query_filename="clean_all")
        session.exec(text(query))
        session.commit()
    except Exception as e:
        print(e)
        return InternalServerErrorException