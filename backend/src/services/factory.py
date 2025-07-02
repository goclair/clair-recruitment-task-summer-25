from src.services import ProjectService


class ServiceFactory:
    """Factory for managing service instances.

    This class manages the lifecycle of service instances and provides
    a way to access them through dependency injection.
    """

    _project_service: ProjectService | None = None

    @classmethod
    def get_project_service(cls) -> ProjectService:
        if cls._project_service is None:
            cls._project_service = ProjectService()
        return cls._project_service
