from typing import Optional, TYPE_CHECKING
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import (
    String,
    ARRAY,
    Integer,
    Text,
    JSON,
)
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum
from datetime import datetime
from sqlalchemy.dialects.postgresql import ENUM

from .base import Base
from core.models.mixins import IdIntPkMixin

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class PlayerRole(str, Enum):
    CARRY = "Carry"
    MIDLANER = "Midlaner"
    OFFLANER = "Offlaner"
    SOFT_SUPPORT = "Soft Support"
    HARD_SUPPORT = "Hard Support"


class User(Base, IdIntPkMixin, SQLAlchemyBaseUserTable[int]):
    username: Mapped[str] = mapped_column(
        String(50), unique=True, index=True, nullable=False
    )
    display_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    # 2. Данные для связи с игрой
    steam_id: Mapped[Optional[str]] = mapped_column(
        String(20), unique=True, index=True, nullable=True
    )
    steam_profile_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    # 3. Игровая информация
    main_role: Mapped[Optional[PlayerRole]] = mapped_column(
        ENUM(PlayerRole, name="player_role"), nullable=True
    )
    current_mmr: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    peak_mmr: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    # 4. Социальная составляющая
    bio: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    country: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    social_links: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    avatar_url: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    # Служебные поля для обновления данных
    last_stats_update: Mapped[Optional[datetime]] = mapped_column(nullable=True)

    @classmethod
    def get_db(cls, session: "AsyncSession"):
        return SQLAlchemyUserDatabase(session, cls)
