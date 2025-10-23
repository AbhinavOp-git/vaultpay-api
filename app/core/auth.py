# app/core/auth.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from typing import Optional

from app.core.config import settings
from app.core.security import decode_access_token  # uses your SECRET_KEY/ALGORITHM there
from app.db.session import get_db
from app.models.user import User

# Token endpoint used by OAuth2PasswordBearer (this must match your login route)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    """
    Dependency that:
    - reads the Bearer token from the Authorization header
    - decodes it using decode_access_token (from app.core.security)
    - looks up the user by email (sub claim) in DB
    - returns the SQLAlchemy User instance (or raises 401)
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_access_token(token)
        if not payload:
            raise credentials_exception
        username: Optional[str] = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        # decode_access_token may raise JWTError (or return None). Treat both as invalid credentials.
        raise credentials_exception

    user = db.query(User).filter(User.email == username).first()
    if user is None:
        raise credentials_exception

    return user
