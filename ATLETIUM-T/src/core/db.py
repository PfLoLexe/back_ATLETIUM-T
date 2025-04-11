from sqlalchemy import Engine
from sqlmodel import SQLModel, Session, create_engine

# Создание класса
class DataBase:
    engine: Engine

    # Метод для подключения к БД
    def init_db(self, db_url):
        self.engine = create_engine(db_url, echo=True)
        SQLModel.metadata.create_all(self.engine)

    # Метод для получение транзакции, для выполнения запросов к БД
    def get_session(self,):
        with Session(self.engine) as session:
            yield session

# Создание экземпляра класса, именно с этим объектом будут взаимодействовать другие модули
app_db: DataBase = DataBase()