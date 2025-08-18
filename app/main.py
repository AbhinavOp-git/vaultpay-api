# app/main.py
from fastapi import FastAPI
from app.core.config import settings
from app.db.session import engine

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.get("/")
def root():
    return {"msg": "VaultPay is up"}
