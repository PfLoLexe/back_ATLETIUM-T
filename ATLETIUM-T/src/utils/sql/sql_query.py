import os
from typing import List, Optional

from src.schemas.exceptions.common_exceptions import InternalServerErrorException

current_dir = os.path.dirname(__file__)

class SqlQuery:

    def load_raw_sql_query(self, sql_query_filename) -> str:
        try:
            sql_query_file_path: str = os.path.join(
                current_dir,
                ("../../crud/queries/{sql_query_filename}.sql").format(sql_query_filename=sql_query_filename)
            )
            with open(sql_query_file_path, "r", encoding="utf-8-sig") as sql_query_file:
                sql_query: str = sql_query_file.read()
                sql_query_file.close()
                return sql_query
        except Exception as e:
            print(e)
            raise InternalServerErrorException

    def get_sql_query(self, sql_query_filename, arguments_list: Optional[List[any]] = None) -> str:
        raw_sql_query = self.load_raw_sql_query(sql_query_filename)
        if arguments_list is not None:
            for i, argument in enumerate(arguments_list, start=1):
                raw_sql_query = raw_sql_query.replace(f"${i}", str(argument))
        return raw_sql_query

sql_query_handler = SqlQuery()