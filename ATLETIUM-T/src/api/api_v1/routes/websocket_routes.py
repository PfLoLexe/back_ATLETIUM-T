import asyncio

from fastapi import APIRouter
from starlette.websockets import WebSocket, WebSocketDisconnect

from src.core.websockets import chat_connections_handler
from src.schemas.requests.websocket import ChatWebSocketConnectionRequest

websocket_router = APIRouter()

@websocket_router.websocket('/chat/connect')
async def chat_websocket_connect(websocket: WebSocket, data: ChatWebSocketConnectionRequest):
    await chat_connections_handler.open_connection(
        connection=websocket,
        user_id=data.user_id
    )
    try:
        while True:
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        chat_connections_handler.close_connection(user_id=data.user_id)