import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    DB_ECHO: bool = os.getenv('DB_ECHO')
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MIN')
    REFRESH_TOKEN_EXPIRE_DAYS:  int = os.getenv('REFRESH_TOKEN_EXPIRE_DAYS')

settings = Settings()
