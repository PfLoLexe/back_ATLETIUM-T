from fastapi import APIRouter, Depends


from starlette.responses import JSONResponse

from src.core.db import app_db
from src.utils.test_queries import default_insert, delete_data

auxiliary_test_routes = APIRouter(prefix="/auxiliary_test")

@auxiliary_test_routes.post("/run-default-insert")
def run_default_insert(session = Depends(app_db.get_session)):
    default_insert(session)

@auxiliary_test_routes.delete("/clean-all")
def run_delete_data(session = Depends(app_db.get_session)):
    delete_data(session)

@auxiliary_test_routes.post("/renew")
def run_renew_data(session = Depends(app_db.get_session)):
    delete_data(session)
    default_insert(session)