from fastapi import APIRouter, Depends
from sqlmodel import select
from starlette.responses import JSONResponse

from src.core.authentication.authentication import authentication_handler
from src.core.db import app_db
from src.models.train_main import TrainMain
from src.models.train_specific_to_client_link import TrainSpecificToClientLink
from src.schemas.requests.train_specific_to_client_link import TrainSpecificChangeClientsVisitStatusRequest
from src.schemas.responses.common_responses import ItemUpdatedSuccessfully

train_specific_to_client_link_router = APIRouter(prefix="/train-specific-to-client-link")

@train_specific_to_client_link_router.put("/update-status")
def put_train_specific_to_client_link(
        data: TrainSpecificChangeClientsVisitStatusRequest,
        session = Depends(app_db.get_session),
        # current_user_id = Depends(authentication_handler.current_user)
) -> JSONResponse:
    for clint in data.clients_list:
        link = session.exec(
            select(
                TrainSpecificToClientLink
            ).where(
                TrainSpecificToClientLink.client_id == clint.client_id,
                TrainSpecificToClientLink.train_specific_id == data.train_specific_id,
            )
        ).first()
        if link:
            link.status = clint.visit_status
            session.add(link)
    session.commit()
    return ItemUpdatedSuccessfully