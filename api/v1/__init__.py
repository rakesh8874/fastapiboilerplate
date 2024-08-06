from fastapi import APIRouter

from .monitoring import monitoring_router
from .posts import post_router
from .users import users_router

v1_router = APIRouter()
v1_router.include_router(monitoring_router, prefix="/monitoring")
v1_router.include_router(post_router, prefix="/posts")
v1_router.include_router(users_router, prefix="/users")
