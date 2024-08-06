from enum import Enum
from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from core.database import Base
from core.database.mixins import TimestampMixin
from core.security.access_control import Allow, Everyone, RolePrincipal, UserPrincipal


class UserPermission(Enum):
    CREATE = "create"
    READ = "read"
    EDIT = "edit"
    DELETE = "delete"


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), default=uuid4, unique=True, nullable=False,  primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

    __mapper_args__ = {"eager_defaults": True}

    def __acl__(self):
        basic_permissions = [UserPermission.READ, UserPermission.CREATE]
        self_permissions = [
            UserPermission.READ,
            UserPermission.EDIT,
            UserPermission.CREATE,
        ]
        all_permissions = list(UserPermission)

        return [
            (Allow, Everyone, basic_permissions),
            (Allow, UserPrincipal(value=self.id), self_permissions),
            (Allow, RolePrincipal(value="admin"), all_permissions),
        ]
