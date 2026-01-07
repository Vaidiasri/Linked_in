from sqlalchemy import Column, Integer, String  # phele inne import kar lo
from database import Base  # fir  database me se  base  ko le  aao thik hai


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
