from fastapi import FastAPI
app = FastAPI()

from src.core.config import app_configuration
app_configuration.load_configuration()

from src.core.db import app_db

from src.api.api_v1.api import v1_api_routes
app.include_router(v1_api_routes)

@app.on_event("startup")
def onStartup():
    app_db.init_db(app_configuration.db_url)