from pydantic import BaseModel

from .composition import CompositionSchema


class PlaceAddSchema(BaseModel):
    """
    Place add schema.

    Attributes:
        title (str): Place title.
        address (str): Place address.
        menu (CompositionSchema): Composition.
    """

    title: str
    address: str
    menu: CompositionSchema


class PlaceSchema(PlaceAddSchema):
    """
    Place schema.

    Attributes:
        id (int): Place id.
        title (str): Place title.
        address (str): Place address.
        menu (CompositionSchema): Composition.
    """

    id: int
