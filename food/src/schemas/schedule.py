from datetime import datetime

from pydantic import BaseModel


class ScheduleAddSchema(BaseModel):
    """
    Schedule add schema.

    Attributes:
        from_ (datetime): Schedule from.
        to (datetime): Schedule to.
        days (tuple[bool, ...]): Schedule days.
    """

    from_: datetime
    to: datetime
    days: tuple[bool, ...]


class ScheduleSchema(ScheduleAddSchema):
    """
    Schedule schema.

    Attributes:
        id (int): Schedule id.
        from_ (datetime): Schedule from.
        to (datetime): Schedule to.
        days (tuple[bool, ...]): Schedule days.
    """

    id: int
