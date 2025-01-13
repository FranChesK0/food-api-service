from pydantic import BaseModel, ConfigDict

from .db_types import OrderStatus


class OrderAddSchema(BaseModel):
    restaurant_id: int
    items: list[int]
    address: str
    comment: str | None

    model_config = ConfigDict(from_attributes=True)


class OrderSchema(OrderAddSchema):
    id: int
    status: OrderStatus

    model_config = ConfigDict(from_attributes=True)
