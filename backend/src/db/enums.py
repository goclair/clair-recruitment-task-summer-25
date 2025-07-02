from sqlalchemy import Enum as SQLEnum

from src.models.project import ProjectStatus

project_status_enum = SQLEnum(ProjectStatus, name="project_status_enum")
