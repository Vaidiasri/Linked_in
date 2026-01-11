from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    user_email: EmailStr
    user_password: str


class LoginResponse(BaseModel):
    message: str
    user_id: int
