"""empty message

Revision ID: 72bced7e2d86
Revises: 6a8d8172cae5
Create Date: 2020-11-23 20:51:50.197190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72bced7e2d86'
down_revision = '6a8d8172cae5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('start_time', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Show', 'start_time')
    # ### end Alembic commands ###
