"""
Temporary script to drop and recreate database tables
Run this once to fix the user_id column issue
"""

from app.config.database import engine, Base
from app.models import blog, user

# Drop all tables
print("🗑️  Dropping all tables...")
Base.metadata.drop_all(bind=engine)
print("✅ Tables dropped successfully!")

# Recreate all tables with updated schema
print("🔨 Creating tables with updated schema...")
Base.metadata.create_all(bind=engine)
print("✅ Database tables created successfully!")
print("\n📋 Tables created:")
print("   - users (with id, user_name, user_email, user_password)")
print("   - blogs (with id, title, body, user_id)")
