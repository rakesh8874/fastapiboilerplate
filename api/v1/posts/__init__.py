from fastapi import APIRouter, Depends

from core.fastapi.dependencies.authentication import AuthenticationRequired

from .posts import post_router

posts_router = APIRouter()
posts_router.include_router(
    post_router,
    tags=["Tasks"],
    dependencies=[Depends(AuthenticationRequired)],
)

__all__ = ["posts_router"]
