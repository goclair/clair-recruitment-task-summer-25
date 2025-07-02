from sqlalchemy.ext.asyncio import AsyncSession

from src.db.queries.project import fetch_project
from src.models.project import Project


class ProjectService:
    """Service for managing project-related operations.

    This service handles all project-related logic and data access.
    """

    async def get_project(self, project_id: int, session: AsyncSession) -> Project:
        """Get a project by ID.

        Args:
            project_id: The ID of the project to fetch.

        Returns:
            Project: A project object.
        """
        result = await fetch_project(session, project_id)
        return Project.model_validate(result)
