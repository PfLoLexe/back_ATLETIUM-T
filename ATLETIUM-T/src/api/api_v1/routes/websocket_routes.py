import asyncio
from uuid import UUID

from fastapi import APIRouter
from fastapi import WebSocket, WebSocketDisconnect

from src.core.websockets import chat_connections_handler

websocket_router = APIRouter(prefix="/websocket")

@websocket_router.websocket('/chat-connection/{user_id}')
async def chat_websocket_connect(websocket: WebSocket, user_id: UUID):
    await chat_connections_handler.open_connection(
        connection=websocket,
        user_id=user_id
    )
    try:
        while True:
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        chat_connections_handler.close_connection(user_id=user_id)