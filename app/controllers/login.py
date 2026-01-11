from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..config.database import get_db
from ..schemas import login_schema
from ..models import user as user_model
from ..utils.hashpassword import password_hashed
from ..utils.jwt_handler import create_access_token

router = APIRouter(prefix="/login", tags=["Login"])


@router.post(
    "/", status_code=status.HTTP_200_OK, response_model=login_schema.LoginResponse
)
def login(request: login_schema.LoginRequest, db: Session = Depends(get_db)):
    # 1. user find karo
    user = (
        db.query(user_model.User)
        .filter(user_model.User.user_email == request.user_email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid email or password"
        )

    # 2. password verify
    if not password_hashed.verify(request.user_password, user.user_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
        )

    # 3. JWT token generate karo
    access_token = create_access_token(data={"user_id": user.id})

    # 4. success response with token
    return {
        "message": "Login successful",
        "user_id": user.id,
        "access_token": access_token,
        "token_type": "bearer",
    }
