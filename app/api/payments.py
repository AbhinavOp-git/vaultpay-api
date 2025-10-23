# app/api/payments.py
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.payment import Payment
from app.schemas.payments import PaymentCreate, PaymentOut

router = APIRouter()

# -----------------------------
# Create a new payment (POST)
# -----------------------------
@router.post("/", response_model=PaymentOut, status_code=status.HTTP_201_CREATED)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    """
    Create a new payment linked to a user.
    """
    db_payment = Payment(
        user_id=payment.user_id,
        amount=payment.amount,
        currency=payment.currency,
        description=payment.description,
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


# -----------------------------
# Get all payments (GET)
# -----------------------------
@router.get("/", response_model=List[PaymentOut])
def get_payments(db: Session = Depends(get_db)):
    """
    Retrieve all payment records from the database.
    """
    return db.query(Payment).all()


# -----------------------------
# Get payments for a specific user
# -----------------------------
@router.get("/user/{user_id}", response_model=List[PaymentOut])
def get_user_payments(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all payments made by a specific user.
    """
    payments = db.query(Payment).filter(Payment.user_id == user_id).all()
    if not payments:
        raise HTTPException(status_code=404, detail="No payments found for this user")
    return payments
