from pydantic import BaseModel


class CategoryAddSchema(BaseModel):
    """
    Category add schema.

    Attributes:
        name (str): Category name.
    """

    name: str


class CategorySchema(CategoryAddSchema):
    """
    Category schema.

    Attributes:
        id (int): Category id.
        name (str): Category name.
    """

    id: int
