"""create posts table

Revision ID: 30057a20008b
Revises: 
Create Date: 2022-05-07 18:48:47.531807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "30057a20008b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer, nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
