from uuid import UUID

from src.models.train_type import TrainType

def get_train_type_items():
    train_type_items = [
        TrainType(name='Group', id=UUID("47d9badb-dcda-49c9-9088-9e2606992b55")),
        TrainType(name='Personal', id=UUID("751bf1ed-6a88-4e16-8e7c-1496821c50dd"))
    ]
    return train_type_items
