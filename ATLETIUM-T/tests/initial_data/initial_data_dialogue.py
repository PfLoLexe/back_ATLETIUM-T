from uuid import UUID

from src.models.dialogue import Dialogue

def get_dialogue_items():
    dialogue_items = [
        Dialogue(
            first_user_id=UUID("74bbfdef-f556-4845-9afc-88292985228c"),
            second_user_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614"),
            id=UUID("5f092ba3-70b4-409a-a153-a698a3bd41ed")
        )
    ]
    return dialogue_items