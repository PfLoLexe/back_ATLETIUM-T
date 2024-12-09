from typing import Dict
from uuid import UUID

from fastapi import WebSocket

from src.models.message import Message


class ChatConnections:
    active_connections: Dict[UUID, WebSocket]

    def __init__(self):
        self.active_connections = {}

    async def open_connection(self, connection: WebSocket, user_id: UUID):
        await connection.accept()
        self.active_connections[user_id] = connection

    def close_connection(self, user_id: UUID):
        self.active_connections.pop(user_id, None)

    async def send_message(self, message: Message, user_id: UUID):
        websocket = self.active_connections[user_id]
        if websocket is not None:
            # dict_message: Dict[str, any] = {
            #     "id": message.id.__str__(),
            #     "sender_user_id": message.sender_user_id.__str__(),
            #     "recipient_user_id": message.recipient_user_id.__str__(),
            #     "is_read": message.is_read,
            #     "text": message.text,
            #     "send_date": message.send_date.__str__(),
            #     "my_message": False
            # }
            # await websocket.send_json(dict_message)
            await websocket.send_text(message.text)
        else:
            #TODO: add smt here
            pass



chat_connections_handler: ChatConnections = ChatConnections()