from fastapi import FastAPI
from app.core.config import settings
from app.core.database import engine, Base
from app.models import user

app = FastAPI(
    title=settings.PROJECT_NAME,
)

# Crear tablas
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the CRM system"}

