"""empty message

Revision ID: b2f26f5a4709
Revises: 253ea2fb155b
Create Date: 2019-03-10 08:50:37.490128

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b2f26f5a4709'
down_revision = '253ea2fb155b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Users', sa.Column('password', mysql.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###
