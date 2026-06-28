from functools import lru_cache
import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


class Settings:
    PROJECT_NAME = os.getenv("PROJECT_NAME", "Dynamic Portfolio")
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-development-secret")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "480"))
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./portfolio.db")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@example.com")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "ChangeMe123!")
    MAX_UPLOAD_SIZE_MB = int(os.getenv("MAX_UPLOAD_SIZE_MB", "10"))
    BASE_DIR = Path(__file__).resolve().parents[1]
    UPLOAD_DIR = BASE_DIR / "static" / "uploads"


@lru_cache
def get_settings() -> Settings:
    return Settings()
