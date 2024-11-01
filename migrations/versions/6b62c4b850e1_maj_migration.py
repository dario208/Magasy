"""maj migration

Revision ID: 6b62c4b850e1
Revises: f9f167316d95
Create Date: 2024-10-31 09:14:17.279596

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlmodel import SQLModel
import sqlmodel.sql.sqltypes

# revision identifiers, used by Alembic.
revision: str = '6b62c4b850e1'
down_revision: Union[str, None] = 'f9f167316d95'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('first_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.add_column('users', sa.Column('last_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    # ### end Alembic commands ###
