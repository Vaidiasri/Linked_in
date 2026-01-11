from pydantic import BaseModel
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.schemas.user_schema import UserOut


class BlogBase(BaseModel):
    """Base Blog schema for creation"""

    title: str
    body: str
    user_id: Optional[int] = None  # Optional user_id for blog creation


class BlogOut(BlogBase):
    """Blog schema for response with user details"""

    id: int
    user_id: Optional[int] = None
    owner: Optional["UserOut"] = None  # User details

    class Config:
        from_attributes = True


class Blog(BlogBase):
    """Blog schema - request/response validation ke liye"""

    class Config:
        from_attributes = True


# Circular import resolve karne ke liye
from app.schemas.user_schema import UserOut

BlogOut.model_rebuild()
