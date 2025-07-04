import datetime
from decimal import Decimal

from sqlalchemy import (
    DateTime as SQLDateTime,
)
from sqlalchemy import (
    ForeignKey,
    Numeric,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from src.db.base import Base
from src.db.enums import project_status_enum
from src.models.project import ProjectStatus


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    name: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[ProjectStatus] = mapped_column(
        project_status_enum, nullable=False, default=ProjectStatus.CREATED
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        SQLDateTime(timezone=True), nullable=False, server_default=func.now()
    )

    products: Mapped[list["Product"]] = relationship("Product", back_populates="project")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False, autoincrement=True)

    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )

    external_id: Mapped[str] = mapped_column(nullable=False, unique=True)
    category: Mapped[str] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    color: Mapped[str] = mapped_column(nullable=False)
    image_url: Mapped[str | None] = mapped_column()
    predicted_sales_quantity: Mapped[int] = mapped_column(nullable=False)

    project: Mapped["Project"] = relationship("Project", back_populates="products")
