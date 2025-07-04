from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.db.queries.utils import DataObject
from src.db.tables import Project


async def fetch_project(session: AsyncSession, project_id: int) -> DataObject:
    """Fetch a project by ID.

    Args:
        session: Async SQLAlchemy session
        project_id: ID of the project to fetch

    Returns:
        DataObject containing project data with nested products

    Raises:
        ValueError: If the project is not found
    """
    query = select(Project).options(selectinload(Project.products)).where(Project.id == project_id)
    result = (await session.execute(query)).scalar_one_or_none()

    if not result:
        raise ValueError(f"Project with id {project_id} not found")

    project_dict = result.to_dict()
    project_dict["products"] = [product.to_dict() for product in result.products]
    return project_dict
