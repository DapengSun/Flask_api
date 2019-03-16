"""empty message

Revision ID: b97c9423f0e1
Revises: c8f47fa906ff
Create Date: 2019-03-12 16:53:11.423803

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b97c9423f0e1'
down_revision = 'c8f47fa906ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Comment', 'CDate',
               existing_type=mysql.DATETIME(),
               comment=None,
               existing_comment='影评获取时间',
               existing_nullable=True)
    op.alter_column('Comment', 'DoubanFilmId',
               existing_type=mysql.VARCHAR(length=50),
               comment=None,
               existing_comment='豆瓣影片ID',
               existing_nullable=True)
    op.alter_column('Comment', 'DoubanFilmReviewId',
               existing_type=mysql.VARCHAR(length=50),
               comment=None,
               existing_comment='影评评论ID',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewAuthorAvatar',
               existing_type=mysql.VARCHAR(length=200),
               comment=None,
               existing_comment='影评作者头像',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewAuthorName',
               existing_type=mysql.VARCHAR(length=200),
               comment=None,
               existing_comment='影评作者名称',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewContent',
               existing_type=mysql.LONGTEXT(),
               comment=None,
               existing_comment='影评内容',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewDate',
               existing_type=mysql.DATETIME(),
               comment=None,
               existing_comment='影评评论时间',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewLink',
               existing_type=mysql.VARCHAR(length=200),
               comment=None,
               existing_comment='影评链接',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewReturn',
               existing_type=mysql.INTEGER(display_width=10),
               comment=None,
               existing_comment='影评回应数',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewScore',
               existing_type=mysql.VARCHAR(length=50),
               comment=None,
               existing_comment='影评作者评分',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewScoreName',
               existing_type=mysql.VARCHAR(length=50),
               comment=None,
               existing_comment='影评评分名称',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewTitle',
               existing_type=mysql.VARCHAR(length=200),
               comment=None,
               existing_comment='影评名换',
               existing_nullable=True)
    op.add_column('Users', sa.Column('cdate', sa.DateTime(), nullable=True))
    op.add_column('Users', sa.Column('sysstatus', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Users', 'sysstatus')
    op.drop_column('Users', 'cdate')
    op.alter_column('Comment', 'ReviewTitle',
               existing_type=mysql.VARCHAR(length=200),
               comment='影评名换',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewScoreName',
               existing_type=mysql.VARCHAR(length=50),
               comment='影评评分名称',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewScore',
               existing_type=mysql.VARCHAR(length=50),
               comment='影评作者评分',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewReturn',
               existing_type=mysql.INTEGER(display_width=10),
               comment='影评回应数',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewLink',
               existing_type=mysql.VARCHAR(length=200),
               comment='影评链接',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewDate',
               existing_type=mysql.DATETIME(),
               comment='影评评论时间',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewContent',
               existing_type=mysql.LONGTEXT(),
               comment='影评内容',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewAuthorName',
               existing_type=mysql.VARCHAR(length=200),
               comment='影评作者名称',
               existing_nullable=True)
    op.alter_column('Comment', 'ReviewAuthorAvatar',
               existing_type=mysql.VARCHAR(length=200),
               comment='影评作者头像',
               existing_nullable=True)
    op.alter_column('Comment', 'DoubanFilmReviewId',
               existing_type=mysql.VARCHAR(length=50),
               comment='影评评论ID',
               existing_nullable=True)
    op.alter_column('Comment', 'DoubanFilmId',
               existing_type=mysql.VARCHAR(length=50),
               comment='豆瓣影片ID',
               existing_nullable=True)
    op.alter_column('Comment', 'CDate',
               existing_type=mysql.DATETIME(),
               comment='影评获取时间',
               existing_nullable=True)
    # ### end Alembic commands ###
