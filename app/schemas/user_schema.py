from pydantic import BaseModel, EmailStr

# user se jo liye vo


class User(BaseModel):
    user_name: str
    user_email: EmailStr
    user_password: str

    class Config:
        from_attributes = True


# jo user do dege vo
class UserOut(BaseModel):
    user_name: str
    user_email: EmailStr

    class Config:
        from_attributes = True
