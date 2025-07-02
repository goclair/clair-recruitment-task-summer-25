from decimal import Decimal

from src.models.utils import CamelModel


class Product(CamelModel):
    id: int
    name: str
    price: Decimal
    image_url: str
    predicted_sales_quantity: int
