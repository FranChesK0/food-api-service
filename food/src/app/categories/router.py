from fastapi import APIRouter

from schemas import CategorySchema, RestaurantSchema
from repository import (
    SessionDep,
    CategoryRepository,
    MenuItemRepository,
    RestaurantRepository,
)

router = APIRouter(prefix="/category", tags=["Categories"])


@router.get("", summary="Get all categories")
async def get_categories(session: SessionDep) -> list[CategorySchema]:
    return await CategoryRepository.find_all(session)


@router.get("/{category_id}/restaurants", summary="Get all restaurants by category id")
async def get_restaurants(
    category_id: int, session: SessionDep
) -> list[RestaurantSchema]:
    restaurants = await RestaurantRepository.find_all(session)
    resaturants = {restaurant.id: restaurant for restaurant in restaurants}
    items = await MenuItemRepository.find_by_category(category_id, session)

    result: list[RestaurantSchema] = []
    for item in items:
        if item.restaurant_id not in [i.id for i in result]:
            result.append(resaturants[item.restaurant_id])
    return result
