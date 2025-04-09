from datetime import time, date
from uuid import UUID

from src.models.train_main import TrainMain

def get_train_main_items():
    train_main_items = [
        TrainMain(
            name='Плавание 10+',
            place_id=UUID("66c2ae22-3efb-454a-a2f3-1ae9133a575d"),
            train_type_id=UUID("47d9badb-dcda-49c9-9088-9e2606992b55"),
            start_time=time(11, 30, 0, 343),
            end_time=time(13, 0, 0, 343),
            week_day_number=1,
            date=None,
            id=UUID("41e5c441-16b4-4c98-a3a7-7bd32589e048"),
            trainer_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614")
        ),
        TrainMain(
            name='Функциональный фитнес',
            place_id=UUID("e21622ef-105a-4d2e-85b1-43fc8df4c90e"),
            train_type_id=UUID("47d9badb-dcda-49c9-9088-9e2606992b55"),
            start_time=time(11, 30, 0, 343),
            end_time=time(13, 0, 0, 343),
            week_day_number=1,
            date=None,
            id=UUID("d6ab1705-4e24-4e0e-bb42-eba1def3cfd3"),
            trainer_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614")
        ),
        TrainMain(
            name='Бокс',
            place_id=UUID("5707ca28-8715-4a6a-a1e6-37bbbcaa9b0e"),
            train_type_id=UUID("47d9badb-dcda-49c9-9088-9e2606992b55"),
            start_time=time(11, 30, 0, 343),
            end_time=time(13, 0, 0, 343),
            week_day_number=3,
            date=None,
            id=UUID("54626715-00a1-463e-9f64-6f5d3b160d2d"),
            trainer_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614")
        ),
        TrainMain(
            name='Фитнес',
            place_id=UUID("e21622ef-105a-4d2e-85b1-43fc8df4c90e"),
            train_type_id=UUID("751bf1ed-6a88-4e16-8e7c-1496821c50dd"),
            start_time=time(11, 30, 0, 343),
            end_time=time(13, 0, 0, 343),
            week_day_number=4,
            date=None,
            id=UUID("1b0f1ae3-7d52-4bc8-b26a-ae90b903cee0"),
            trainer_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614")
        ),
        TrainMain(
            name='Плавание 6+',
            place_id=UUID("66c2ae22-3efb-454a-a2f3-1ae9133a575d"),
            train_type_id=UUID("751bf1ed-6a88-4e16-8e7c-1496821c50dd"),
            start_time=time(11, 30, 0, 343),
            end_time=time(13, 0, 0, 343),
            week_day_number=5,
            date=date(2024, 10, 31),  # Преобразованная дата из '31.10.24'
            id=UUID("38b40437-0541-44ed-871a-f1a04fba179b"),
            trainer_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614")
        )
    ]
    return train_main_items

