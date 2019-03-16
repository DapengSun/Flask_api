"""empty message

Revision ID: ab49c357f376
Revises: fd5b9c0cd2d5
Create Date: 2019-03-14 23:03:51.345950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab49c357f376'
down_revision = 'fd5b9c0cd2d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('SysStatus', sa.SmallInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'SysStatus')
    # ### end Alembic commands ###
