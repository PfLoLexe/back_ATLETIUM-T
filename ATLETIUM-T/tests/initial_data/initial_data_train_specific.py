from datetime import date
from uuid import UUID

from src.models.train_specific import TrainSpecific

def get_train_specific_items():
    train_specific_items = [
        TrainSpecific(
            clients_amount=3,
            description='Абракадабра',
            date=date(2024, 10, 31),
            is_over=True,
            train_main_id=UUID("38b40437-0541-44ed-871a-f1a04fba179b"),
            trainer_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614"),
            id=UUID("953d1949-23ab-4364-8c70-68a09e2387c1")
        )
    ]
    return train_specific_items
