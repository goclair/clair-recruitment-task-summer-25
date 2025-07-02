import logging
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.db.session import get_async_session
from src.services import ProjectService
from src.services.factory import ServiceFactory

logger = logging.getLogger(__name__)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with get_async_session() as session:
        yield session


async def get_project_service() -> ProjectService:
    return ServiceFactory.get_project_service()
