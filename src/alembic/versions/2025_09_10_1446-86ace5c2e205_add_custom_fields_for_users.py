"""add custom fields for users

Revision ID: 86ace5c2e205
Revises: d8f6795b1448
Create Date: 2025-09-10 14:46:57.087540

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "86ace5c2e205"
down_revision: Union[str, Sequence[str], None] = "d8f6795b1448"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("users", sa.Column("username", sa.String(length=50), nullable=False))
    op.add_column(
        "users", sa.Column("display_name", sa.String(length=100), nullable=True)
    )
    op.add_column("users", sa.Column("steam_id", sa.String(length=20), nullable=True))
    op.add_column(
        "users", sa.Column("steam_profile_url", sa.String(length=200), nullable=True)
    )
    op.add_column(
        "users",
        sa.Column(
            "main_role",
            sa.Enum(
                "CARRY",
                "MIDLANER",
                "OFFLANER",
                "SOFT_SUPPORT",
                "HARD_SUPPORT",
                name="playerrole",
            ),
            nullable=True,
        ),
    )
    op.add_column(
        "users", sa.Column("secondary_roles", sa.ARRAY(sa.String()), nullable=True)
    )
    op.add_column("users", sa.Column("current_mmr", sa.Integer(), nullable=True))
    op.add_column("users", sa.Column("peak_mmr", sa.Integer(), nullable=True))
    op.add_column("users", sa.Column("bio", sa.Text(), nullable=True))
    op.add_column("users", sa.Column("country", sa.String(length=100), nullable=True))
    op.add_column("users", sa.Column("social_links", sa.JSON(), nullable=True))
    op.add_column(
        "users", sa.Column("avatar_url", sa.String(length=200), nullable=True)
    )
    op.add_column("users", sa.Column("last_stats_update", sa.DateTime(), nullable=True))
    op.create_index(op.f("ix_users_steam_id"), "users", ["steam_id"], unique=True)
    op.create_index(op.f("ix_users_username"), "users", ["username"], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_users_username"), table_name="users")
    op.drop_index(op.f("ix_users_steam_id"), table_name="users")
    op.drop_column("users", "last_stats_update")
    op.drop_column("users", "avatar_url")
    op.drop_column("users", "social_links")
    op.drop_column("users", "country")
    op.drop_column("users", "bio")
    op.drop_column("users", "peak_mmr")
    op.drop_column("users", "current_mmr")
    op.drop_column("users", "secondary_roles")
    op.drop_column("users", "main_role")
    op.drop_column("users", "steam_profile_url")
    op.drop_column("users", "steam_id")
    op.drop_column("users", "display_name")
    op.drop_column("users", "username")
