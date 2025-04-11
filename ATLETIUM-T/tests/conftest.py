import os
from uuid import UUID

import pytest
from fastapi.testclient import TestClient

from dotenv import load_dotenv
from sqlmodel.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine, Session

from src.core.db import app_db
from src.core.main import app, app_configuration
from tests.initial_data import initial_data

# Создаем фикстуру и присваиваем ей имя "Session"
@pytest.fixture(name="session")
def session_fixture():
    app_configuration.load_configuration()

    # Создаем альтернативное подключение к БД
    engine = create_engine(
        app_configuration.db_url, connect_args={"check_same_thread": False}
    )

    # Полная очистка тестовой БД
    SQLModel.metadata.drop_all(bind=engine)
    # Инициализация БД, создание таблиц и связей
    SQLModel.metadata.create_all(bind=engine)

    with Session(engine) as session:
        yield session

# Создаем фикстуру и присваиваем ей имя "client"
@pytest.fixture(name="client")
# В качестве аргумента функция получает session, фикстуру созданную ранее
def client_fixture(session: Session):
    # Создаем функцию возвращающую транзакцию тестовой БД
    def get_session_override():
        return session

    def authentication_current_user_ovverridde():
        return UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614")

    #Совершаем подмену зависимости, вместо вызова функции app_db.get_session, будет вызвана ранее написанная функция - get_session_override
    app.dependency_overrides[app_db.get_session] = get_session_override

    # Вносим в БД тестовые данные
    initial_data(session)

    #Создаем тестовый клиент
    client = TestClient(app)
    yield client

    #После окончания тестирования очищаем зависимости, предотвращая ошибки связанные с подменой
    app.dependency_overrides.clear()


def get_auth_header(client, username: str, password: str):
    # Отправляем запрос к нашему сервису
    get_access_token_response = client.post(
        url="/v1/token",
        json={
            "username": username,
            "password": password
        }
    )
    access_token = None
    token_type = None

    # Если данные для входа были верны вернем Access токен, иначе ничего
    if get_access_token_response.status_code == 200:
        access_token = get_access_token_response.json()["access_token"]
        token_type = get_access_token_response.json()["token_type"]

    auth_header = {"Authorization": f"{token_type} {access_token}"}

    return auth_header
