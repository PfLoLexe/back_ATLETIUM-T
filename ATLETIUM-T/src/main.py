from fastapi import FastAPI

from src.db import init_db
from src.routers.auxiliary_test_routes import auxiliary_test_routes
from src.routers.place import place_router
from src.routers.train_type import train_type_router

app = FastAPI()

app.include_router(train_type_router)
# app.include_router(train_router)
app.include_router(place_router)
app.include_router(auxiliary_test_routes)

@app.on_event("startup")
def onStartup():
    init_db()