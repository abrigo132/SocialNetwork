from typing import Optional
from fastapi_users import schemas

from core.models.user import PlayerRole
from core.types import UserIdType


class UserBase(schemas.BaseUser[UserIdType]):
    username: str
    display_name: str | None = None
    steam_id: str | None = None
    steam_profile_url: str | None = None
    main_role: Optional[PlayerRole]
    current_mmr: Optional[str]
    peak_mmr: Optional[str]
    bio: Optional[str]
    country: Optional[str]
    social_links: Optional[dict]
    avatar_url: Optional[str]


class UserRead(UserBase):
    pass


class UserCreate(schemas.BaseUserCreate):
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str]
    display_name: str | None = None
    steam_id: Optional[str] = None
    steam_profile_url: Optional[str] = None
    main_role: Optional[PlayerRole]
    current_mmr: Optional[str]
    peak_mmr: Optional[str]
    bio: Optional[str]
    country: Optional[str]
    social_links: Optional[dict]
    avatar_url: Optional[str]
