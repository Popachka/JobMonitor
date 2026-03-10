from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.infrastructure.telegram.miniapp.routes import router
from app.infrastructure.telegram.miniapp.ui import STATIC_DIR


def build_miniapp_app() -> FastAPI:
    miniapp = FastAPI(title="JobMonitor Mini App")
    miniapp.mount("/miniapp/static", StaticFiles(directory=str(STATIC_DIR)), name="miniapp-static")
    miniapp.include_router(router)
    return miniapp


app = build_miniapp_app()

__all__ = ["app", "build_miniapp_app"]
