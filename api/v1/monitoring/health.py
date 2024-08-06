from fastapi import APIRouter

from app.schemas.others.health import Health
from core.config import config

health_router = APIRouter()


@health_router.get("/")
def health() -> Health:
    return Health(version=config.RELEASE_VERSION, status="Healthy")
