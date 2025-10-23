# app/main.py
from fastapi import FastAPI
from app.core.config import settings
from app.api import api  # central router that includes all endpoints

# Create FastAPI instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="VaultPay API — Secure payment & user management backend"
)

# Root health check
@app.get("/")
def root():
    return {"msg": "VaultPay API is up and running 🚀"}

# Include all versioned routes
app.include_router(api.router, prefix="/api/v1")
