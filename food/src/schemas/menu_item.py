from pydantic import BaseModel


class MenuItemAddSchema(BaseModel):
    """
    Menu item add schema.

    Attributes:
        restaurant_id (int): Restaurant id.
        category_id (int): Category id.
        name (str): Menu item name.
        price (float): Menu item price.
        description (str): Menu item description.
    """

    restaurant_id: int
    category_id: int
    name: str
    price: float
    description: str


class MenuItemSchema(MenuItemAddSchema):
    """
    Menu item schema.

    Attributes:
        id (int): Menu item id.
        category_id (int): Category id.
        name (str): Menu item name.
        price (float): Menu item price.
        description (str): Menu item description.
    """

    id: int
