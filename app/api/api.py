# app/api/api.py
from fastapi import APIRouter
from app.api.v1.endpoints import users, auth
from app.api import payments   # <- this imports app/api/payments.py

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(payments.router, prefix="/payments", tags=["Payments"])
