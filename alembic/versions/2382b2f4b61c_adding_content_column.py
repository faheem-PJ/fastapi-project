"""adding content column

Revision ID: 2382b2f4b61c
Revises: 12fae9bfde14
Create Date: 2025-07-12 06:33:43.412597

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2382b2f4b61c'
down_revision: Union[str, Sequence[str], None] = '12fae9bfde14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column('posts','content')
    pass
