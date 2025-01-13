import random
from itertools import count

from fastapi import APIRouter

from schemas import OrderSchema, OrderStatus, OrderAddSchema

from .response import OrderResponse

router = APIRouter(prefix="/order", tags=["Orders"])

get_next_id = count(start=1)
orders: dict[int, OrderSchema] = {}


@router.post("", summary="Create a new order")
async def create_order(order: OrderAddSchema) -> OrderResponse:
    order_id = next(get_next_id)
    new_order = OrderSchema(
        restaurant_id=order.restaurant_id,
        items=order.items,
        address=order.address,
        comment=order.comment,
        id=order_id,
        status=OrderStatus.CREATING,
    )
    orders[order_id] = new_order
    return OrderResponse(
        ok=True,
        msg="order created",
        order=new_order,
    )


@router.get("/{order_id}", summary="Get order info")
async def get_order(order_id: int) -> OrderSchema:
    if order_id in orders:
        order = orders[order_id]
        order.status = random.choice(
            (OrderStatus.COOKING, OrderStatus.DELIVERING, OrderStatus.DONE)
        )
        orders[order_id] = order
        return orders[order_id]
    else:
        raise ValueError("No such order")
