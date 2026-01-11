from ..config.database import get_db
from ..schemas import login_schema
from ..models import user as user_model
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

router = APIRouter(prefix="/login", tags=["Login"])
@router.post("/", status_code=status.HTTP_200_OK)
def login(request: login_schema.LoginSchema, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.user_email == request.user_email).first()
    if not user or user.user_password != request.user_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    return {"message": "Login successful"}