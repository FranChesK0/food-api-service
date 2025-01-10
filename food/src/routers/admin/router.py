from fastapi import APIRouter

from schemas import (
    ScheduleSchema,
    RestaurantSchema,
    ScheduleAddSchema,
    RestaurantAddSchema,
)
from repository import SessionDep, ScheduleRepository, RestaurantRepository

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


@router.post("/schedule", summary="Add a new schedule")
async def add_schedule(
    schedule: ScheduleAddSchema, session: SessionDep
) -> ScheduleSchema:
    return await ScheduleRepository.add_one(schedule, session)


@router.post("/schedule_many", summary="Add new schedules")
async def add_schedules(
    schedules: list[ScheduleAddSchema], session: SessionDep
) -> list[ScheduleSchema]:
    return await ScheduleRepository.add_many(schedules, session)
