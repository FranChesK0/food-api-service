from pydantic import BaseModel

from .category import CategorySchema
from .schedule import ScheduleSchema
from .menu_composition_item import MenuCompositionItemSchema


class CompositionAddSchema(BaseModel):
    """
    Composition add schema.

    Attributes:
        category (CategorySchema): Category.
        items (list[MenuCompositionItemAddSchema]): Composition items.
        schedule (ScheduleSchema): Schedule.
    """

    category: CategorySchema
    items: list[MenuCompositionItemSchema]
    schedule: ScheduleSchema


class CompositionSchema(CompositionAddSchema):
    """
    Composition schema.

    Attributes:
        id (int): Composition id.
    """

    id: int
