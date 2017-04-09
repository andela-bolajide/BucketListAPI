"""unique1

Revision ID: 0f27b29c51eb
Revises: eeb0d41a5c9e
Create Date: 2017-04-08 09:16:30.430831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f27b29c51eb'
down_revision = 'eeb0d41a5c9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique_constraint_bucketlist', 'bucketlist', ['name', 'created_by'])
    op.drop_constraint(u'unique_BucketList', 'bucketlist', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(u'unique_BucketList', 'bucketlist', ['name', 'created_by'])
    op.drop_constraint('unique_constraint_bucketlist', 'bucketlist', type_='unique')
    # ### end Alembic commands ###