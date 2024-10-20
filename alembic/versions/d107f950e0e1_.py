"""empty message

Revision ID: d107f950e0e1
Revises: 277cad49d2b0
Create Date: 2024-10-19 12:55:31.053307

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'd107f950e0e1'
down_revision: Union[str, None] = '277cad49d2b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('note',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('date', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('course_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('phone', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('note')
    # ### end Alembic commands ###
