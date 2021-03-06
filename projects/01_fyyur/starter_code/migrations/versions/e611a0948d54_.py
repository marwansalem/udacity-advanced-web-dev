"""empty message

Revision ID: e611a0948d54
Revises: d3bd7215385f
Create Date: 2020-11-23 22:04:07.106139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e611a0948d54'
down_revision = 'd3bd7215385f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'website')
    # ### end Alembic commands ###
