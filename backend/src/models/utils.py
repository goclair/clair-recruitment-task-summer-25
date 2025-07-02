from typing import Any

from pydantic import BaseModel, ConfigDict, field_serializer
from pydantic.alias_generators import to_camel


class CamelModel(BaseModel):
    """Base model that uses camelCase aliases for frontend communication and stringifies int IDs."""

    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
    )

    @field_serializer("*", when_used="always")
    def convert_ids_to_str(self, value: Any, info: Any) -> Any:
        """Convert integer ID fields to strings during serialization."""
        if info.field_name.endswith("id") and isinstance(value, int):
            return str(value)
        if info.field_name.endswith("ids") and isinstance(value, list):
            return [str(id) for id in value]
        return value
