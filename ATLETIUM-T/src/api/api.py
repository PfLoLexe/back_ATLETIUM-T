from fastapi import APIRouter

from src.api.api_v1.routes.auth_routes import auth_router
from src.api.api_v1.routes.auxiliary_test_routes import auxiliary_test_routes
from src.api.api_v1.routes.client_routes import client_router
from src.api.api_v1.routes.dialogue_routes import dialogue_router
from src.api.api_v1.routes.message_routes import message_router
from src.api.api_v1.routes.place_routes import place_router
from src.api.api_v1.routes.train_main_routes import train_main_router
from src.api.api_v1.routes.train_specific_routes import train_specific_router
from src.api.api_v1.routes.train_specific_to_client_link_routes import train_specific_to_client_link_router
from src.api.api_v1.routes.train_type_routes import train_type_router
from src.api.api_v1.routes.user_routes import user_router
from src.api.api_v1.routes.websocket_routes import websocket_router

api_routes = APIRouter()

api_routes.include_router(auth_router, prefix="/v1")

api_routes.include_router(auxiliary_test_routes, prefix="/v1")

api_routes.include_router(place_router, prefix="/v1")

api_routes.include_router(train_main_router, prefix="/v1")

api_routes.include_router(train_specific_router, prefix="/v1")

api_routes.include_router(train_type_router, prefix="/v1")

api_routes.include_router(train_specific_to_client_link_router, prefix="/v1")

api_routes.include_router(dialogue_router, prefix="/v1")

api_routes.include_router(message_router, prefix="/v1")

api_routes.include_router(user_router, prefix="/v1")

api_routes.include_router(websocket_router, prefix="/v1")

api_routes.include_router(client_router, prefix="/v1")