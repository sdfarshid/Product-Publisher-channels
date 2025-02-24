from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.infrastructure.config import settings
import logging


logger = logging.getLogger(__name__)

try:
    engine = create_async_engine(settings.DATABASE_URL, echo=True)
    logger.info("Database engine created successfully")
except Exception as e:
    logger.critical(f"Database connection failed: {str(e)}")
    raise



AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


Base = declarative_base()
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


