# app/schemas/payments.py
from pydantic import BaseModel, Field
from datetime import datetime


class PaymentBase(BaseModel):
    amount: float = Field(..., gt=0, description="Transaction amount")
    currency: str = Field(..., min_length=3, max_length=3, description="Currency code (e.g. INR, USD)")
    description: str | None = None


class PaymentCreate(PaymentBase):
    user_id: int  # ID of the user making payment


class PaymentOut(PaymentBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True
