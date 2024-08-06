from functools import partial

from fastapi import Depends

from app.controllers import AuthController, PostController, UserController
from app.models import Post, User
from app.repositories import PostRepository, UserRepository
from core.database import get_session


class Factory:

    # Repositories
    post_repository = partial(PostRepository, Post)
    user_repository = partial(UserRepository, User)

    def get_user_controller(self, db_session=Depends(get_session)):
        return UserController(
            user_repository=self.user_repository(db_session=db_session)
        )

    def get_post_controller(self, db_session=Depends(get_session)):
        return PostController(
            post_repository=self.post_repository(db_session=db_session)
        )

    def get_auth_controller(self, db_session=Depends(get_session)):
        return AuthController(
            user_repository=self.user_repository(db_session=db_session),
        )
