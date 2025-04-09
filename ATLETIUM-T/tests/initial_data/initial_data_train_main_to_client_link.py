from uuid import UUID

from src.models.train_main_to_client_link import TrainMainToClientLink

def get_train_main_to_client_link_items():
    train_main_to_client_link_items = [
        TrainMainToClientLink(
            train_main_id=UUID("41e5c441-16b4-4c98-a3a7-7bd32589e048"),
            client_id=UUID("6f793564-ce9d-417e-b5df-6324eca497d0"),
            id=UUID("659ab3e7-6eb1-49f0-916b-cc7dbbcde30d")
        )
    ]
    return train_main_to_client_link_items
