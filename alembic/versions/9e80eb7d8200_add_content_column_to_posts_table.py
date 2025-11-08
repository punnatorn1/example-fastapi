"""Add content column to posts table

Revision ID: 9e80eb7d8200
Revises: ac01ee649720
Create Date: 2025-11-07 23:26:05.758323

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9e80eb7d8200"
down_revision: Union[str, Sequence[str], None] = "ac01ee649720"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
