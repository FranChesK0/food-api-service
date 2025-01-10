from fastapi import APIRouter

from schemas import RestaurantSchema, RestaurantAddSchema
from repository import SessionDep, RestaurantRepository

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.post("/restaurant", summary="Add a new restaurant")
async def add_restaurant(
    restaurant: RestaurantAddSchema, session: SessionDep
) -> RestaurantSchema:
    return await RestaurantRepository.add_one(restaurant, session)


@router.post("/restaurant_many", summary="Add new restaurants")
async def add_restaurants(
    restaurants: list[RestaurantAddSchema], session: SessionDep
) -> list[RestaurantSchema]:
    return await RestaurantRepository.add_many(restaurants, session)
