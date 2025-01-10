from datetime import time

from pydantic import BaseModel


class ScheduleAddSchema(BaseModel):
    """
    Schedule add schema.

    Attributes:
        restaurant_id (int): Restaurant id.
        start (str): Schedule from.
        end (str): Schedule to.
        days (tuple[bool, ...]): Schedule days.
    """

    restaurant_id: int
    start: time
    end: time
    days: tuple[bool, ...]


class ScheduleSchema(ScheduleAddSchema):
    """
    Schedule schema.

    Attributes:
        id (int): Schedule id.
        restaurant_id (int): Restaurant id.
        start (str): Schedule from.
        end (str): Schedule to.
        days (tuple[bool, ...]): Schedule days.
    """

    id: int
