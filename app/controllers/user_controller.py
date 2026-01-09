from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.schemas import user_schema
from app.models import user as user_model

router = APIRouter(prefix="/user", tags=["User"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[user_schema.UserOut])
def get_all_user(db: Session = Depends(get_db)):
    users = db.query(user_model.User).all()
    return users