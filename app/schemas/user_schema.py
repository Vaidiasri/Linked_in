from pydantic import BaseModel, EmailStr
from typing import List


# user se jo liye vo


class User(BaseModel):
    user_name: str
    user_email: EmailStr
    user_password: str

    class Config:
        from_attributes = True


class UserOut(BaseModel):
    """User response"""
    id: int
    user_name: str
    user_email: EmailStr

    class Config:
        from_attributes = True
