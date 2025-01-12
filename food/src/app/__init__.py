import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core import settings

from . import menu, admin, order, places, feedback, restaurants


def run() -> None:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(menu.router)
    app.include_router(admin.router)
    app.include_router(order.router)
    app.include_router(places.router)
    app.include_router(feedback.router)
    app.include_router(restaurants.router)

    uvicorn.run(app, host=settings.HOST, port=settings.PORT)


__all__ = ["run"]
