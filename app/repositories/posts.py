import uuid

from sqlalchemy import Select
from sqlalchemy.orm import joinedload

from app.models import Post
from core.repository import BaseRepository


class PostRepository(BaseRepository[Post]):
    
    async def get_by_owner_id(
        self, owner_id: uuid, join_: set[str] | None = None
    ) -> list[Post]:

        query = self._query(join_)
        query = await self._get_by(query, "owner_id", owner_id)

        if join_ is not None:
            return await self.all_unique(query)

        return await self._all(query)

    def _join_owner(self, query: Select) -> Select:

        return query.options(joinedload(Post.owner))
