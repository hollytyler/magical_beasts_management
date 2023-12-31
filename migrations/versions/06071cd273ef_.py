"""empty message

Revision ID: 06071cd273ef
Revises: 
Create Date: 2023-07-30 12:27:18.580958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06071cd273ef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('keepers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('name_of_hold', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('magical_abilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ability', sa.String(length=64), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('beasts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('dob', sa.DateTime(), nullable=True),
    sa.Column('breed', sa.String(length=64), nullable=True),
    sa.Column('origin_country', sa.String(length=64), nullable=True),
    sa.Column('keeper_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['keeper_id'], ['keepers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('beast_abilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('beast_id', sa.Integer(), nullable=True),
    sa.Column('magical_ability_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['beast_id'], ['beasts.id'], ),
    sa.ForeignKeyConstraint(['magical_ability_id'], ['magical_abilities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('beast_abilities')
    op.drop_table('beasts')
    op.drop_table('magical_abilities')
    op.drop_table('keepers')
    # ### end Alembic commands ###
