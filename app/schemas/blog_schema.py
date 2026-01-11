from pydantic import BaseModel


class Blog(BaseModel):
    """Blog schema - request/response validation ke liye"""

    title: str
    body: str

    class Config:
        orm_mode = True  # or: from_attributes = True  (Pydantic v2)
