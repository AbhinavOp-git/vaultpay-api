# app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# SQLite for now
engine = create_engine(
    settings.DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal → each request gets a DB session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency (FastAPI will use this in routes)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
