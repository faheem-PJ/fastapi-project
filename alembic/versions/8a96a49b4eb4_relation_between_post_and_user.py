"""relation between post and user

Revision ID: 8a96a49b4eb4
Revises: 6d5012c8c47f
Create Date: 2025-07-12 06:53:07.448335

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8a96a49b4eb4'
down_revision: Union[str, Sequence[str], None] = '6d5012c8c47f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column('posts', sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_key',source_table='posts',referent_table="users",
                          local_cols = ['owner_id'], remote_cols=['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_key',table_name='posts')
    op.drop_column('posts','owner_id')
    """Downgrade schema."""
    pass
