# app/main.py
from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints import users  # 👈 import your first router

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Root health check
@app.get("/")
def root():
    return {"msg": "VaultPay is up"}

# Include versioned routes
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

