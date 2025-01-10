from pydantic import BaseModel


class CategoryAddSchema(BaseModel):
    """
    Category add schema.

    Attributes:
        name (str): Category name.
        sort_order (int): Category sort order.
    """

    name: str
    sort_order: int


class CategorySchema(CategoryAddSchema):
    """
    Category schema.

    Attributes:
        id (int): Category id.
        name (str): Category name.
        sort_order (int): Category sort order.
    """

    id: int
