"""asdsad

Revision ID: 0586b369c1fc
Revises: 028166c29c94
Create Date: 2023-03-30 17:21:28.148535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0586b369c1fc'
down_revision = '028166c29c94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('menu_item_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('restaurants', sa.Column('cuisine', sa.Integer(), nullable=True))
    op.drop_column('restaurants', 'rating')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurants', sa.Column('rating', sa.INTEGER(), nullable=True))
    op.drop_column('restaurants', 'cuisine')
    op.drop_table('user_orders')
    # ### end Alembic commands ###
