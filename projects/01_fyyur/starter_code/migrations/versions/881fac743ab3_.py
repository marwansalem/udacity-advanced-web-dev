"""empty message

Revision ID: 881fac743ab3
Revises: 01ee6fd23186
Create Date: 2020-11-29 03:55:07.368932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '881fac743ab3'
down_revision = '01ee6fd23186'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.add_column('Show', sa.Column('id2', sa.Integer(), nullable=False))
    # ### end Alembic commands ###
    pass


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
