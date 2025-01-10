from pydantic import BaseModel


class MenuCompositionItemAddSchema(BaseModel):
    """
    Menu composition item add schema.

    Attributes:
        category_id (int): Category id.
        measure (int): Composition item measure.
        name (str): Composition item name.
        price (float): Composition item price.
        description (str): Composition item description.
        sort_order (int): Composition item sort order.
    """

    category_id: int
    measure: int
    name: str
    price: float
    description: str
    sort_order: int


class MenuCompositionItemSchema(MenuCompositionItemAddSchema):
    """
    Menu composition item schema.

    Attributes:
        id (int): Composition item id.
        category_id (int): Category id.
        measure (int): Composition item measure.
        name (str): Composition item name.
        price (float): Composition item price.
        description (str): Composition item description.
        sort_order (int): Composition item sort order.
    """

    id: int
