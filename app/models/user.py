from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    user_email = Column(String)
    user_password = Column(String)
    blogs = relationship("Blog", back_populates="owner")  # Changed blog to blogs (plural)