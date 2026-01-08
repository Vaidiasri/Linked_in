from sqlalchemy import Column, Integer, String
from app.config.database import Base


class Blog(Base):
    """Blog model - database table ke liye"""

    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
