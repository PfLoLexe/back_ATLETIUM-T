from datetime import datetime
from uuid import UUID

from src.models.message import Message

def get_message_items():
    message_items = [
        Message(
            text='Hi, User!',
            sender_user_id=UUID("74bbfdef-f556-4845-9afc-88292985228c"),
            recipient_user_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614"),
            dialogue_id=UUID("5f092ba3-70b4-409a-a153-a698a3bd41ed"),
            parent_message_id=None,
            id=UUID("369f50dc-07c4-4b8c-a9c1-aabfa12de715"),
            send_date=datetime(2024, 11, 1, 10, 0, 0),
            is_read=False,
            read_date=None
        ),
        Message(
            text='Hi, Admin',
            sender_user_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614"),
            recipient_user_id=UUID("74bbfdef-f556-4845-9afc-88292985228c"),
            dialogue_id=UUID("5f092ba3-70b4-409a-a153-a698a3bd41ed"),
            parent_message_id=None,
            id=UUID("077ddf22-2ce5-4088-bf2e-250d6f6021fc"),
            send_date=datetime(2024, 11, 1, 10, 10, 0),
            is_read=False,
            read_date=None
        ),
        Message(
            text='How are you, Admin?',
            sender_user_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614"),
            recipient_user_id=UUID("74bbfdef-f556-4845-9afc-88292985228c"),
            dialogue_id=UUID("5f092ba3-70b4-409a-a153-a698a3bd41ed"),
            parent_message_id=None,
            id=UUID("13b2bea7-4aed-4295-a347-de799bc520cd"),
            send_date=datetime(2024, 11, 1, 10, 20, 0),
            is_read=False,
            read_date=None
        ),
        Message(
            text='I\'m fine!',
            sender_user_id=UUID("74bbfdef-f556-4845-9afc-88292985228c"),
            recipient_user_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614"),
            dialogue_id=UUID("5f092ba3-70b4-409a-a153-a698a3bd41ed"),
            parent_message_id=None,
            id=UUID("7d164d7a-066e-4f4f-a15d-917cc56eb918"),
            send_date=datetime(2024, 11, 1, 10, 30, 0),
            is_read=False,
            read_date=None
        )
    ]
    return message_items
