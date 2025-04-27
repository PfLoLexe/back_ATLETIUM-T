import uuid
from datetime import date, datetime, time
from typing import Optional
from uuid import UUID

from sqlmodel import select

from src.models.train_main import TrainMain
from src.models.train_main_to_client_link import TrainMainToClientLink
from src.models.train_specific import TrainSpecific
from src.models.train_specific_to_client_link import TrainSpecificToClientLink

def generate_train_specific(session, train_main_id: UUID, train_specific_id: Optional[UUID] = None, plane_date: Optional[date] = None) -> TrainSpecific:
    train_main = session.exec(
        select(
            TrainMain
        ).where(
            TrainMain.id == train_main_id,
        )
    ).first()

    train_clients_raw = session.exec(
        select(
            TrainMainToClientLink.client_id
        ).where(
            TrainMainToClientLink.train_main_id == train_main_id,
        )
    ).all()
    train_clients = []
    if train_clients_raw is not None:
        for row in train_clients_raw:
            train_clients.append(
                TrainSpecificToClientLink(
                    id=uuid.uuid4(),
                    client_id=row,
                    train_specific_id=train_specific_id,
                )
            )
        #train_clients = [TrainSpecificToClientLink(**row) for row in train_clients_raw.mappings()]

    if train_specific_id is None:
        train_specific_id = uuid.uuid4()

    new_train_specific = TrainSpecific(
        train_main_id=train_main_id,
        id=train_specific_id,
        trainer_id=train_main.trainer_id,
        description="",
        date=plane_date,
        is_over = False,
        clients_amount=len(train_clients),
    )

    if train_main.end_time < time(datetime.now().hour, datetime.now().minute):
        new_train_specific.is_over = True

    new_train_specific = TrainSpecific.model_validate(new_train_specific)
    session.add(new_train_specific)

    for link in train_clients:
        session.add(link)

    session.commit()



