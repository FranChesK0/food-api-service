from fastapi import APIRouter

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


@router.get("", summary="Returns list of restaurants")
async def get_restaurants_list() -> None:
    return None
