from pydantic import BaseModel

from schemas import OrderSchema


class OrderResponse(BaseModel):
    ok: bool
    msg: str
    order: OrderSchema
