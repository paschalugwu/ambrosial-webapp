"""Add password_hash column to user table

Revision ID: 31986866a4b1
Revises: cce2efa7aa40
Create Date: 2024-08-15 08:57:48.217214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31986866a4b1'
down_revision = 'cce2efa7aa40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.VARCHAR(length=60), nullable=False))

    # ### end Alembic commands ###
