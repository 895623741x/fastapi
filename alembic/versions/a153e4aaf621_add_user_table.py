"""add user table

Revision ID: a153e4aaf621
Revises: fbae7525cb53
Create Date: 2022-05-07 19:14:23.086698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a153e4aaf621"
down_revision = "fbae7525cb53"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
