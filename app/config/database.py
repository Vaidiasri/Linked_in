from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection URL
DATABASE_URL = "postgresql://postgres:vaibhav123@localhost:5432/blog"

# Step 1: Engine banao - database se connection ke liye
engine = create_engine(DATABASE_URL)

# Step 2: Session banao - database operations ke liye
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Step 3: Base class banao - models ke liye
Base = declarative_base()


# DB dependency - har request ke liye database session provide karta hai
def get_db():
    """Database session dependency"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
