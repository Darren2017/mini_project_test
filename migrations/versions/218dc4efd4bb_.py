"""empty message

Revision ID: 218dc4efd4bb
Revises: a203d12ab20f
Create Date: 2018-04-05 12:57:09.805404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '218dc4efd4bb'
down_revision = 'a203d12ab20f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=64), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
