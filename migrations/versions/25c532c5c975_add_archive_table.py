"""Add Archive table

Revision ID: 25c532c5c975
Revises: 834b1a697901
Create Date: 2023-03-15 22:44:24.044315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25c532c5c975'
down_revision = '834b1a697901'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('archive',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('record_owner', sa.Integer(), nullable=True),
    sa.Column('record_data', sa.String(length=350), nullable=True),
    sa.ForeignKeyConstraint(['record_owner'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('archive')
    # ### end Alembic commands ###