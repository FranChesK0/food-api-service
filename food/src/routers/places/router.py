from fastapi import APIRouter

from .responses import RestaurantScheduleResponse

router = APIRouter(prefix="/places", tags=["Places"])


@router.get("/{restaurant_id}/schedule", summary="")
async def get_restaurant_schedule(restaurant_id: int) -> RestaurantScheduleResponse:
    _ = restaurant_id
    schedule = {
        "mon": {"start": "10:00", "end": "22:00"},
        "tue": {"start": "10:00", "end": "22:00"},
        "wed": {"start": "10:00", "end": "22:00"},
        "thu": {"start": "10:00", "end": "22:00"},
        "fri": {"start": "10:00", "end": "22:00"},
        "sat": {"start": "10:00", "end": "22:00"},
        "sun": {"start": "10:00", "end": "22:00"},
    }
    return RestaurantScheduleResponse.model_validate(schedule)
