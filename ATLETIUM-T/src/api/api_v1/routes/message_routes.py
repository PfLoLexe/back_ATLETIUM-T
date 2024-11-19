from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import select

from src.core.authentication.authentication import authentication_handler
from src.core.db import app_db
from src.models.message import Message
from src.schemas.requests.message import DialogueMessagesListRequest
from src.schemas.responses.message import MessageResponse

message_router = APIRouter()

@message_router.post("/get_list")
def get_list_of_messages(
        data: DialogueMessagesListRequest,
        session = Depends(app_db.get_session),
        current_user_id = Depends(authentication_handler.current_user)
) -> List[MessageResponse]:
    messages_raw = session.exec(
        select(
            Message.id.label("id"),
            Message.sender_user_id.label("sender_user_id"),
            Message.recipient_user_id.label("recipient_user_id"),
            Message.is_read.label("is_read"),
            Message.text.label("text"),
            Message.send_date.label("send_date")
        ).where(
            Message.dialogue_id == data.dialogue_id,
        )
    ).all()
    messages: List[MessageResponse] = []
    if messages_raw is not None:
        for row in messages_raw:
            messages.append(
                MessageResponse(
                    id=row.id,
                    sender_user_id=row.sender_user_id,
                    recipient_user_id=row.recipient_user_id,
                    is_read=row.is_read,
                    text=row.text,
                    send_date=row.send_date,
                    my_message= True if row.sender_user_id == current_user_id else False
                )
            )
    return messages