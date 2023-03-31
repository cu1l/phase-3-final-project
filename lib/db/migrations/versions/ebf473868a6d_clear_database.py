"""Clear database

Revision ID: ebf473868a6d
Revises: d6369112b63e
Create Date: 2023-03-31 08:28:13.192089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebf473868a6d'
down_revision = 'd6369112b63e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurant_menus',
    sa.Column('menu_id', sa.Integer(), nullable=False),
    sa.Column('restaurant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['menu_id'], ['menu_items.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('menu_id', 'restaurant_id')
    )
    op.drop_table('restaurants_menus')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurants_menus',
    sa.Column('menu_id', sa.INTEGER(), nullable=False),
    sa.Column('restaurant_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['menu_id'], ['menu_items.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurants.id'], ),
    sa.PrimaryKeyConstraint('menu_id', 'restaurant_id')
    )
    op.drop_table('restaurant_menus')
    # ### end Alembic commands ###