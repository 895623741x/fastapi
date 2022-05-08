"""add content column to posts table

Revision ID: fbae7525cb53
Revises: 30057a20008b
Create Date: 2022-05-07 19:07:00.458694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fbae7525cb53"
down_revision = "30057a20008b"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
