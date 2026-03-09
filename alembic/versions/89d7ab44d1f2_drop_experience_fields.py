"""drop experience fields

Revision ID: 89d7ab44d1f2
Revises: e434c0b6ae91
Create Date: 2026-03-09 12:00:00.000000

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "89d7ab44d1f2"
down_revision: str | Sequence[str] | None = "e434c0b6ae91"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column("users", "cv_experience_months")
    op.drop_column("users", "filter_experience_min_months")
    op.drop_column("vacancies", "min_experience_months")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "vacancies",
        sa.Column(
            "min_experience_months",
            sa.Integer(),
            nullable=False,
            server_default="0",
        ),
    )
    op.add_column("users", sa.Column("filter_experience_min_months", sa.Integer(), nullable=True))
    op.add_column("users", sa.Column("cv_experience_months", sa.Integer(), nullable=True))
