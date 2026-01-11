from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.config.database import Base


class Blog(Base):
    """Blog model - database table ke liye"""

    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(
        Integer, ForeignKey("users.id"), nullable=True
    )  # Foreign key to link to the users table
    owner = relationship(
        "User", back_populates="blogs"
    )  # Updated back_populates to "blogs"
