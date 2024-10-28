from fastapi import FastAPI

from src.db import init_db
from src.routers.train import train_router
from src.routers.train_type import train_type_router

app = FastAPI()

app.include_router(train_type_router)
app.include_router(train_router)

@app.on_event("startup")
def onStartup():
    init_db()