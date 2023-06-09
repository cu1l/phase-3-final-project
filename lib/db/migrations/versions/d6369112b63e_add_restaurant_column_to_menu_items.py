"""add restaurant column to menu_items

Revision ID: d6369112b63e
Revises: 0586b369c1fc
Create Date: 2023-03-30 17:54:12.327598

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6369112b63e'
down_revision = '0586b369c1fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu_items', sa.Column('restaurant', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('menu_items', 'restaurant')
    # ### end Alembic commands ###
