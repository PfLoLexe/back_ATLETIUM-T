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
            await websocket.send_json(message)
        else:
            #TODO: add smt here
            pass



chat_connections_handler: ChatConnections = ChatConnections()