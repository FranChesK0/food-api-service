from pydantic import BaseModel, ConfigDict


class Interval(BaseModel):
    start: str
    end: str

    model_config = ConfigDict(from_attributes=True)


class RestaurantScheduleResponse(BaseModel):
    fri: Interval
    mon: Interval
    sat: Interval
    sun: Interval
    thu: Interval
    tue: Interval
    wed: Interval

    model_config = ConfigDict(from_attributes=True)
