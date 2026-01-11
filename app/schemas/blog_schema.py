from pydantic import BaseModel
from typing import Optional


class Blog(BaseModel):
    """Blog create/update ke liye"""

    title: str
    body: str
    user_id: Optional[int] = None

    class Config:
        from_attributes = True


class BlogOut(BaseModel):
    """Blog response ke liye"""

    id: int
    title: str
    body: str
    user_id: Optional[int] = None

    class Config:
        from_attributes = True
