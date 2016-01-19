"""login support

Revision ID: 456a945560f6
Revises: 38c4e85512a9
Create Date: 2016-01-20 20:00:00

"""
revision = '456a945560f6'
down_revison = '38c4e85512a9'

from alembic import op
import sqlalchemy as sa 

def upgrade():
	op.add_column('users', sa.Column('email', sa.String(length=64), nullale=True))
	op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullale=True))
	op.create_index('ix_users_email', 'users', ['email'],unique=True)

def downgrade():
	op.drop_index('ix_users_email', 'users')
	op.drop_column('users', 'password_hash')
	op.drop_column('users','email')