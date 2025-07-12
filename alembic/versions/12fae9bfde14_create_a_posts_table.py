"""create a posts table

Revision ID: 12fae9bfde14
Revises: 
Create Date: 2025-07-11 23:43:42.213998

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12fae9bfde14'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key = True),
                    sa.Column('title',sa.String(),nullable=False)) 
    pass


def downgrade() -> None:
    op.drop_table('posts')
    """Downgrade schema."""
    pass
