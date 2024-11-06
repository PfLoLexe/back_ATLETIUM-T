from fastapi import APIRouter

from src.api.api_v1.routes.auth_routes import auth_router
from src.api.api_v1.routes.auxiliary_test_routes import auxiliary_test_routes
from src.api.api_v1.routes.place_routes import place_router
from src.api.api_v1.routes.train_main_routes import train_main_router
from src.api.api_v1.routes.train_specific_routes import train_specific_router
from src.api.api_v1.routes.train_type_routes import train_type_router

v1_api_routes = APIRouter()

v1_api_routes.include_router(auth_router)
v1_api_routes.include_router(auxiliary_test_routes, prefix="/auxiliary_test")
v1_api_routes.include_router(place_router, prefix="/place")
v1_api_routes.include_router(train_main_router, prefix="/train-main")
v1_api_routes.include_router(train_specific_router, prefix="/train-specific")
v1_api_routes.include_router(train_type_router, prefix="/train-type")