from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class User(Base):
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
