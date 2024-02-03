from fastapi import FastAPI
from fastapi_socketio import SocketManager
import socket
from fastapi.middleware.cors import CORSMiddleware

from project.celery_utils import create_celery

def server_program():
    host = socket.gethostname()
    print(f"The host is: {str(host)}")

def create_app() -> FastAPI:
    app = FastAPI()

    # Add cors to allow everything for dev purposes
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # celery
    app.celery_app = create_celery()

    # sockets
    sio = SocketManager(app=app)

    from project.users import users_router
    app.include_router(users_router)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}

    @app.sio.on("join")
    async def handle_join(sid, *args, **kwargs):
        await app.sio.emit("lobby", "User joined")

    @app.sio.on("leave")
    async def handle_leave(sid, *args, **kwarg):
        await app.sio.emit("lobby", "User left")

    return app