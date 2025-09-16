from fastapi import APIRouter

from core import settings
from api.dependencies.authentication import fastapi_users
from api.dependencies.authentication import authentication_backend

router = APIRouter(prefix=settings.api.v1.auth, tags=["Authentication"])


router.include_router(router=fastapi_users.get_auth_router(authentication_backend))
