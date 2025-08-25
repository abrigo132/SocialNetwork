from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase

from .base import Base
from core.models.mixins import IdIntPkMixin


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    pass
