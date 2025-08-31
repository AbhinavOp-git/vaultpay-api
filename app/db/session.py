from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# PostgreSQL engine (no check_same_thread here!)
engine = create_engine(
    settings.DATABASE_URL,
    echo=True,  # optional, logs SQL queries
)

# SessionLocal → each request gets its own DB session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency (FastAPI will use this in routes)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
