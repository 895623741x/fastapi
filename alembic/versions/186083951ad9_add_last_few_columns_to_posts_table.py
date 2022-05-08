"""add last few columns to posts table

Revision ID: 186083951ad9
Revises: 4e62681d164d
Create Date: 2022-05-07 19:56:00.019890

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "186083951ad9"
down_revision = "4e62681d164d"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=False, server_default="True"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    pass


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
    pass
