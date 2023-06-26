"""create users table

Revision ID: d49af330ec66
Revises: 
Create Date: 2023-06-24 13:29:37.905645

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d49af330ec66"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("username", sa.String(length=30), nullable=False),
        sa.Column("email", sa.String(length=150), nullable=True),
        sa.Column("profession_type", sa.String(length=50), nullable=True),
        sa.Column("website", sa.String(length=150), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
        sa.UniqueConstraint("website"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    # ### end Alembic commands ###
