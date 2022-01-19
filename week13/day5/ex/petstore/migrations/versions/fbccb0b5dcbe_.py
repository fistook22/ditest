"""empty message

Revision ID: fbccb0b5dcbe
Revises: 
Create Date: 2022-01-09 18:43:27.800581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbccb0b5dcbe'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('cart_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('cart_id')
    )
    op.create_table('pet',
    sa.Column('pet_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pet_name', sa.String(length=64), nullable=True),
    sa.Column('gender', sa.String(length=2), nullable=True),
    sa.Column('breed', sa.String(length=64), nullable=True),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('details', sa.Text(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('image', sa.String(length=64), nullable=True),
    sa.Column('cart', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart'], ['cart.cart_id'], ),
    sa.PrimaryKeyConstraint('pet_id'),
    sa.UniqueConstraint('pet_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pet')
    op.drop_table('cart')
    # ### end Alembic commands ###