from pydantic import BaseModel, ConfigDict


class ScheduleAddSchema(BaseModel):
    """
    Schedule add schema.

    Attributes:
        restaurant_id (int): Restaurant id.
        start (str): Schedule from.
        end (str): Schedule to.
    """

    restaurant_id: int
    start: str
    end: str

    model_config = ConfigDict(from_attributes=True)


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

    model_config = ConfigDict(from_attributes=True)
