from asyncio import current_task

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker, async_scoped_session
from app.core.config import settings


class DatabaseManager:
    def __init__(self, url: str, db_echo: bool = False):
        self.engine = create_async_engine(url, future=True, echo=db_echo)
        self.async_session = async_sessionmaker(self.engine, expire_on_commit=False, class_=AsyncSession)

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.async_session,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self.async_session() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.close()

db_manager = DatabaseManager(settings.DATABASE_URL, db_echo=settings.DB_ECHO)
