from fastapi import FastAPI

from src.core.config import app_configuration
from src.core.db import app_db
from src.api.api import api_routes

app_configuration.load_configuration()
app = FastAPI()
app.include_router(api_routes)

@app.on_event("startup")
def onStartup():
    app_db.init_db(app_configuration.db_url)