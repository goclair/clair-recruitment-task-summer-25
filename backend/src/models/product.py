from decimal import Decimal

from src.models.utils import CamelModel


class Product(CamelModel):
    id: int
    external_id: str
    category: str
    name: str
    price: Decimal
    color: str
    image_url: str | None
    predicted_sales_quantity: int
