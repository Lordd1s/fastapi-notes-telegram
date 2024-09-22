import os

from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('ACCESS_TOKEN_EXPIRE_MIN')
    REFRESH_TOKEN_EXPIRE_DAYS:  int = os.getenv('REFRESH_TOKEN_EXPIRE_DAYS')

settings = Settings()
