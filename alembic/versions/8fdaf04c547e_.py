"""empty message

Revision ID: 8fdaf04c547e
Revises: d107f950e0e1
Create Date: 2024-10-19 16:30:47.858950

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '8fdaf04c547e'
down_revision: Union[str, None] = 'd107f950e0e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('phone', sa.VARCHAR(), nullable=False),
    sa.Column('address', sa.VARCHAR(), nullable=False),
    sa.Column('payments', sa.FLOAT(), nullable=False),
    sa.Column('status', sa.VARCHAR(), nullable=False),
    sa.Column('date', sa.VARCHAR(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
