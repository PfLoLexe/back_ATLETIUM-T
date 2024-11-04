from fastapi import FastAPI

from src.db import init_db
from src.routers.auth_routes import auth_router
from src.routers.auxiliary_test_routes import auxiliary_test_routes
from src.routers.place_routes import place_router
from src.routers.train_main_routes import train_main_router
from src.routers.train_specific_routes import train_specific_router
from src.routers.train_type_routes import train_type_router

app = FastAPI()

app.include_router(train_type_router)
app.include_router(train_main_router)
app.include_router(train_specific_router)
app.include_router(place_router)
app.include_router(auxiliary_test_routes)
app.include_router(auth_router)

@app.on_event("startup")
def onStartup():
    init_db()