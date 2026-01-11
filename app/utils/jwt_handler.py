from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt

# JWT Configuration
SECRET_KEY = "your-secret-key-here-change-in-production-use-env-variable"  # Production mein .env se load karo
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    JWT access token create karta hai

    Args:
        data: Token mein encode karne ka data (e.g., {"user_id": 123})
        expires_delta: Custom expiry time (optional)

    Returns:
        Encoded JWT token string
    """
    to_encode = data.copy()

    # Expiry time set karo
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Expiry time token mein add karo
    to_encode.update({"exp": expire})

    # Token encode karo
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    """
    JWT token verify karta hai aur payload return karta hai

    Args:
        token: JWT token string

    Returns:
        Decoded payload dict

    Raises:
        JWTError: Agar token invalid ya expired ho
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise JWTError("Invalid or expired token")
