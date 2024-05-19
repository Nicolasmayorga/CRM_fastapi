from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = os.getenv("API_V1_STR")
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    PROJECT_NAME: str = os.getenv("PROJECT_NAME")
    SQLALCHEMY_DATABASE_URI: str = os.getenv("SQLALCHEMY_DATABASE_URI")
    
    class Config:
        case_sensitive = True

settings = Settings()
