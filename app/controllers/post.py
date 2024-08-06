import uuid
from app.models import Post
from app.repositories import PostRepository
from core.controller import BaseController
from core.database.transactional import Propagation, Transactional


class PostController(BaseController[Post]):
    """Task controller."""

    def __init__(self, post_repository: PostRepository):
        super().__init__(model=Post, repository=post_repository)
        self.post_repository = post_repository

    async def get_by_owner_id(self, owner_id: uuid.uuid4()) -> list[Post]:

        return await self.post_repository.get_by_owner_id(owner_id)

    @Transactional(propagation=Propagation.REQUIRED)
    async def add(self, title: str, content: str, owner_id: uuid.uuid4()) -> Post:

        return await self.post_repository.create(
            {
                "title": title,
                "content": content,
                "owner_id": owner_id,
            }
        )

    # @Transactional(propagation=Propagation.REQUIRED)
    # async def published(self, post_id: uuid) -> Post:
    #
    #     post = await self.post_repository.get_by_id(post_id)
    #     post.is_published = True
    #
    #     return post
