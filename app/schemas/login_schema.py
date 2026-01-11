from pydantic import BaseModel, EmailStr

class LoginSchema(BaseModel):
    """Login ke liye schema"""

    user_email: EmailStr 
    user_password: str 

    class Config:
        from_attributes = True