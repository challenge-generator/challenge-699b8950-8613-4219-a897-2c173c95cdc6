"""Initial migration

Revision ID: 123456789abc
Revises:
Create Date: 2023-01-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '123456789abc'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('stock', sa.Integer(), nullable=False),
        sa.Column('category', sa.String(), nullable=False),
        sa.CheckConstraint('price >= 0', name='check_price_non_negative'),
        sa.CheckConstraint('stock >= 0', name='check_stock_non_negative')
    )
    op.create_index(op.f('ix_products_id'), 'products', ['id'], unique=True)

def downgrade() -> None:
    op.drop_index(op.f('ix_products_id'), table_name='products')
    op.drop_table('products')