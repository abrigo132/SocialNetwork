from fastapi_users import FastAPIUsers

from core.models import User
from .user_manager import get_user_manager
from .backend import authentication_backend
from core.types import UserIdType

fastapi_users = FastAPIUsers[User, UserIdType](
    get_user_manager,
    [authentication_backend],
)
