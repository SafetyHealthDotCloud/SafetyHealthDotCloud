"""empty message

Revision ID: 692f51931284
Revises: b52b46aca683
Create Date: 2021-02-23 07:44:05.975569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '692f51931284'
down_revision = 'b52b46aca683'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('preferred_gender_pronouns', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('people', 'preferred_gender_pronouns')
    # ### end Alembic commands ###
