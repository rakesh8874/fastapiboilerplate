import uuid
from typing import Callable

from fastapi import APIRouter, Depends, Request

from app.controllers import PostController
from app.models.posts import PostPermission
from app.schemas.requests.posts import PostCreate
from app.schemas.responses.posts import PostResponse
from core.factory import Factory
from core.fastapi.dependencies.permissions import Permissions

post_router = APIRouter()


@post_router.get("/", response_model=list[PostResponse])
async def get_posts(
    request: Request,
    post_controller: PostController = Depends(Factory().get_post_controller),
    assert_access: Callable = Depends(Permissions(PostPermission.READ)),
) -> list[PostResponse]:
    tasks = await post_controller.get_by_owner_id(request.user.id)

    assert_access(tasks)
    return tasks


@post_router.post("/", response_model=PostResponse, status_code=201)
async def create_post(
    request: Request,
    post_create: PostCreate,
    post_controller: PostController = Depends(Factory().get_post_controller),
) -> PostResponse:
    post = await post_controller.add(
        title=post_create.title,
        description=post_create.description,
        author_id=request.user.id,
    )
    return post


@post_router.get("/{id}", response_model=PostResponse)
async def get_post(
    post_uuid: str,
    post_controller: PostController = Depends(Factory().get_post_controller),
    assert_access: Callable = Depends(Permissions(PostPermission.READ)),
) -> PostResponse:
    post = await post_controller.get_by_id(post_uuid)

    assert_access(post)
    return post
