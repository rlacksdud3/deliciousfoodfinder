"""empty message

Revision ID: 98eb5c7ba933
Revises: None
Create Date: 2016-01-13 06:01:11.578186

"""

# revision identifiers, used by Alembic.
revision = '98eb5c7ba933'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('idx', sa.Integer(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('id', sa.String(length=20), nullable=True),
    sa.Column('pw', sa.String(length=20), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('idx'),
    sa.UniqueConstraint('id')
    )
    op.create_table('comment',
    sa.Column('idx', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=200), nullable=True),
    sa.Column('who', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['who'], ['user.idx'], ),
    sa.PrimaryKeyConstraint('idx')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('user')
    ### end Alembic commands ###
