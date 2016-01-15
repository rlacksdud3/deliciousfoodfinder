"""empty message

Revision ID: e226a224bcd0
Revises: 3cd27a5e41b6
Create Date: 2016-01-14 08:45:00.282801

"""

# revision identifiers, used by Alembic.
revision = 'e226a224bcd0'
down_revision = '3cd27a5e41b6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('board', sa.Column('num', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('board', 'num')
    ### end Alembic commands ###
