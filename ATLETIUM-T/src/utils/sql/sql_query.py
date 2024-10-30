import os

from src.exceptions.common_exceptions import InternalServerErrorException

current_dir = os.path.dirname(__file__)

class SqlQuery:
    def get_sql_query(sql_query_filename) -> str:
        try:
            sql_query_file_path: str = os.path.join(
                current_dir,
                ("../../sql/{sql_query_filename}.sql").format(sql_query_filename=sql_query_filename)
            )
            with open(sql_query_file_path, "r", encoding="utf-8-sig") as sql_query_file:
                sql_query: str = sql_query_file.read()
                return sql_query
        except Exception as e:
            print(e)
            raise InternalServerErrorException