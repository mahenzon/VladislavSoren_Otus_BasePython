"""upgrade users: delete bio

Revision ID: 93491ed011e4
Revises: 2f4794c4819d
Create Date: 2023-06-09 17:04:01.578505

"""
from alembic import op
import sqlalchemy as sa

from models import Author, User

# revision identifiers, used by Alembic.
revision = "93491ed011e4"
down_revision = "2f4794c4819d"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("blog_users", "bio")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "blog_users",
        sa.Column(
            "bio",
            sa.TEXT(),
            server_default="",
            nullable=False,
        ),
    )

    # another example:
    metadata = sa.MetaData()
    metadata.reflect(bind=op.get_bind())

    users_table = metadata.tables["blog_users"]
    authors_table = metadata.tables["blog_authors"]

    update_stmt = (
        sa.update(users_table)
        .where(authors_table.c.user_id == users_table.c.id)
        .values({users_table.c.bio: authors_table.c.bio})
    )
    op.execute(update_stmt)

    # ### end Alembic commands ###
