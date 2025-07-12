"""last columns to post table

Revision ID: b4836c60ebac
Revises: 8a96a49b4eb4
Create Date: 2025-07-12 07:12:59.485660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4836c60ebac'
down_revision: Union[str, Sequence[str], None] = '8a96a49b4eb4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False, server_default="True"))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False))   
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
