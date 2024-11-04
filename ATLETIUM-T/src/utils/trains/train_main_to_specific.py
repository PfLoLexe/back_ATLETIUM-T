from typing import Optional
from uuid import UUID

from src.models.train_specific import TrainSpecific


async def generate_train_specific(train_main_id: UUID, train_specific_id: Optional[UUID] = None):
    new_train_specific = TrainSpecific()
    #TODO: сделать добавление
