from datetime import datetime
from enum import Enum

from src.models.product import Product
from src.models.utils import CamelModel


class ProjectStatus(Enum):
    INITIALIZING = "initializing"
    READY = "ready"


class Project(CamelModel):
    id: int
    name: str
    status: ProjectStatus
    products: list[Product]
    created_at: datetime
