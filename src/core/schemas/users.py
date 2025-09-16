from typing import Optional
from fastapi_users import schemas

from core.models.user import PlayerRole
from core.types import UserIdType


class UserBase(schemas.BaseUser[UserIdType]):
    username: str
    display_name: str
    steam_id: str
    steam_profile_url: str
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
    pass


class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str]
    display_name: Optional[str]
    steam_id: Optional[str]
    steam_profile_url: Optional[str]
    main_role: Optional[PlayerRole]
    current_mmr: Optional[str]
    peak_mmr: Optional[str]
    bio: Optional[str]
    country: Optional[str]
    social_links: Optional[dict]
    avatar_url: Optional[str]
