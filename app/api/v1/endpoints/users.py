# app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserCreate, UserOut
from app.crud import user as crud_user
from app.core.auth import get_current_user
from app.models.user import User as UserModel

router = APIRouter()


# Create a new user (public)
@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db=db, user=user)


# Get all users (public)
@router.get("/", response_model=list[UserOut])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud_user.get_users(db, skip=skip, limit=limit)
    return users


# Get logged-in user (protected)
@router.get("/me", response_model=UserOut)
def read_logged_in_user(current_user: UserModel = Depends(get_current_user)):
    """
    Returns the currently logged-in user's info.
    Requires a valid JWT token in the Authorization header.
    """
    return current_user
