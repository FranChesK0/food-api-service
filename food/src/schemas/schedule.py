from datetime import time

from pydantic import BaseModel


class ScheduleAddSchema(BaseModel):
    """
    Schedule add schema.

    Attributes:
        restaurant_id (int): Restaurant id.
        start (str): Schedule from.
        end (str): Schedule to.
    """

    restaurant_id: int
    start: time
    end: time


class ScheduleSchema(ScheduleAddSchema):
    """
    Schedule schema.

    Attributes:
        id (int): Schedule id.
        restaurant_id (int): Restaurant id.
        start (str): Schedule from.
        end (str): Schedule to.
    """

    id: int
