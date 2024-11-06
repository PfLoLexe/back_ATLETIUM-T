from sqlalchemy import Engine
from sqlmodel import SQLModel, Session, create_engine

class DataBase:
    engine: Engine

    def init_db(self, db_url):
        self.engine = create_engine(db_url, echo=True)
        SQLModel.metadata.create_all(self.engine)


    def get_session(self,):
        with Session(self.engine) as session:
            yield session

app_db: DataBase = DataBase()