"""0.0.1

Revision ID: 51ee90b6b331
Revises: 
Create Date: 2017-03-24 13:59:28.328345

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '51ee90b6b331'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answer',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('text', sa.UnicodeText(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_')
    )
    op.create_table('node',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('label', sa.Unicode(length=8), nullable=False),
    sa.PrimaryKeyConstraint('id_')
    )
    op.create_table('post_',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('title', sa.Unicode(length=32), nullable=True),
    sa.Column('html', sa.UnicodeText(), nullable=True),
    sa.Column('markdown', sa.UnicodeText(), nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(u'0'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('node_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_')
    )
    op.create_table('post_topic',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_')
    )
    op.create_table('token',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('token_string', sa.Unicode(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id_')
    )
    op.create_table('topic',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('slug', sa.Unicode(length=8), nullable=False),
    sa.PrimaryKeyConstraint('id_')
    )
    op.create_table('user',
    sa.Column('id_', sa.Integer(), nullable=False),
    sa.Column('username', sa.Unicode(length=8), nullable=False),
    sa.Column('password', sa.Unicode(length=16), nullable=False),
    sa.Column('email', sa.Unicode(length=64), nullable=True),
    sa.Column('role', sa.Enum('admin', 'normal'), nullable=True),
    sa.Column('bio', sa.Unicode(length=128), nullable=True),
    sa.Column('created_at', mysql.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('updated_at', mysql.TIMESTAMP(), server_default=sa.text(u'0'), nullable=True),
    sa.PrimaryKeyConstraint('id_')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('topic')
    op.drop_table('token')
    op.drop_table('post_topic')
    op.drop_table('post_')
    op.drop_table('node')
    op.drop_table('answer')
    # ### end Alembic commands ###