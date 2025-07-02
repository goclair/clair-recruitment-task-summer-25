import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies import get_db_session, get_project_service
from src.models.project import Project
from src.services import ProjectService

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/{project_id}")
async def get_project(
    project_id: int,
    project_service: ProjectService = Depends(get_project_service),
    session: AsyncSession = Depends(get_db_session),
) -> Project:
    try:
        return await project_service.get_project(project_id, session)
    except Exception as e:
        logger.error(f"An unexpected error occurred while getting project: {e}")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred while getting project",
        )
