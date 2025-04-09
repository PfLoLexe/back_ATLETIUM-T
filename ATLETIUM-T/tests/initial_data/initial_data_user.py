from uuid import UUID

from src.models.user import User


def get_user_items():
    user_items = [
        User(
            username="admin",
            firstname="Владимир",
            lastname="Ель",
            middle_name=None,
            role="admin",
            hashed_password="$2b$12$uD5GmGwZt/adbsvdU/xAvuX1e2UkhqNywMJKOtdO3rZstRHcq2ALS",
            id=UUID("74bbfdef-f556-4845-9afc-88292985228c"),
            phone_number="gfdh",
            is_active=True
        ),
        User(
            username="user",
            firstname="Иванонов",
            lastname="Иван",
            middle_name="Иванович",
            role="trainer",
            hashed_password="$2b$12$uD5GmGwZt/adbsvdU/xAvuOot/.8/lSn6Wn4BtZ/PfZswzpt6zx12",
            id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614"),
            phone_number="gfdh",
            is_active=True
        ),
        User(
            username="user2",
            firstname="Иванонов2",
            lastname="Иван2",
            middle_name="Иванович2",
            role="trainer",
            hashed_password="$2b$12$uD5GmGwZt/adbsvdU/xAvuOot/.8/lSn6Wn4BtZ/PfZswzpt6zx12",
            id=UUID("b1c40098-78ef-4af9-9cf8-6da820fdc5b4"),
            phone_number="phone_humber",
            is_active=True
        )
    ]
    return user_items
