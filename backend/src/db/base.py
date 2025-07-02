from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.schema import Table


class BaseMixin:
    __table__: Table

    def to_dict(self, exclude: set[str] | None = None) -> dict:
        exclude = exclude or set()
        return {
            col.name: getattr(self, col.name)
            for col in self.__table__.columns
            if col.name not in exclude
        }


Base = declarative_base(cls=BaseMixin)
