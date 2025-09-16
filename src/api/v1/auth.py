from fastapi import APIRouter

from core import settings
from api.dependencies.authentication import fastapi_users
from api.dependencies.authentication import authentication_backend

from core.schemas import UserCreate, UserRead

router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Authentication"],
)

# /login
# /logout
router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)


# /register
router.include_router(
    router=fastapi_users.get_register_router(UserRead, UserCreate),
)
