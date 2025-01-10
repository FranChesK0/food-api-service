from pydantic import BaseModel


class RestaurantAddSchema(BaseModel):
    """
    Restaurant add schema.

    Attributes:
        title (str): Restaurant title.
        address (str): Restaurant address.
    """

    title: str
    address: str


class RestaurantSchema(RestaurantAddSchema):
    """
    Restaurant schema.

    Attributes:
        id (int): Restaurant id.
        title (str): Restaurant title.
        address (str): Restaurant address.
    """

    id: int
