from uuid import UUID

from src.models.pincode import Pincode

def get_pincode_items():
    pincode_items = [
        Pincode(
            id=UUID("a4c3d3ee-0626-4f83-9374-c9fc92b1514d"),
            hashed_pincode='$2b$12$NpA38wo6r6O/6xlxv0pLK.TOCEp4a24xQAV7FUu0krG726ZlUA51.',
            user_id=UUID("74bbfdef-f556-4845-9afc-88292985228c")
        ),
        Pincode(
            id=UUID("a851abe9-16dc-4efd-a3e2-843a57bfa0d6"),
            hashed_pincode='$2b$12$NpA38wo6r6O/6xlxv0pLK.IoBufuAI2giawjGtWtJfTxRJuqkzjqi',
            user_id=UUID("5c5d9856-6a9e-432d-9e5d-2d0ee07b9614")
        ),
        Pincode(
            id=UUID("c2aa8912-88f0-464f-927d-4ffc44d33892"),
            hashed_pincode='$2b$12$NpA38wo6r6O/6xlxv0pLK.IoBufuAI2giawjGtWtJfTxRJuqkzjqi',
            user_id=UUID("b1c40098-78ef-4af9-9cf8-6da820fdc5b4")
        )
    ]
    return pincode_items
