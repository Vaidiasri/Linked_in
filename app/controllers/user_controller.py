from ast import Raise
import select
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas import user_schema
from app.models import user as user_model
from app.utils.hashpassword import get_password_hash  # Import the password hashing utility

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[user_schema.UserOut])
def get_all_user(db: Session = Depends(get_db)):
    users = db.query(user_model.User).all()
    return users
# post api 
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=user_schema.UserOut)
def creat_usser(request:user_schema.User,db:Session=Depends(get_db)):
    existing_user=db.query(user_model.User).filter(user_model.User.user_email==request.user_email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail="Email already registered"
        )
    new_user=user_model.User(
        user_name=request.user_name,
        user_email=request.user_email,
        user_password=get_password_hash(request.user_password) # Hash the password before storing it
        
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
# update  user
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=user_schema.User)
def update_user(id:int, request:user_schema.User,db:Session=Depends(get_db)):
    existing_user=db.query(user_model.User).filter(user_model.User.id == id).first()
    if not existing_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Bhai vo id exist nahi karti db m")
    existing_user.user_password=get_password_hash(request.user_password)
    db.commit()
    db.refresh(existing_user)
    return existing_user   

# Delete api 
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int,db:Session=Depends(get_db)):
    find=db.query(user_model.User).filter(user_model.User.id==id).first()
    if not find:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Bhai aesi koi bhi id nahi hai")
    db.delete(find)
    db.commit()
    return None
@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=user_schema.UserOut)
def get_user(id:int,db:Session=Depends(get_db)):
    user=db.query(user_model.User).filter(user_model.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Bhai aesi koi bhi id nahi hai")
    return user