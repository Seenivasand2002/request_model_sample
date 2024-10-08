"""employee model is added

Revision ID: e182e21d721c
Revises: 767bfabd5d0d
Create Date: 2024-10-03 14:34:45.415779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e182e21d721c'
down_revision: Union[str, None] = '767bfabd5d0d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employee_id'), 'employee', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employee_id'), table_name='employee')
    op.drop_table('employee')
    # ### end Alembic commands ###
