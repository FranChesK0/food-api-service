import ujson

from schemas import (
    CategorySchema,
    RestaurantSchema,
    CategoryAddSchema,
    MenuItemAddSchema,
    ScheduleAddSchema,
    RestaurantAddSchema,
)


def load_restaurants(file_path: str) -> list[RestaurantAddSchema]:
    with open(file_path, "r", encoding="utf-8") as file:
        data = ujson.load(file)
    return [RestaurantAddSchema.model_validate(r) for r in data]


def load_schedules(
    file_path: str, restaursnts: list[RestaurantSchema]
) -> list[ScheduleAddSchema]:
    with open(file_path, "r", encoding="utf-8") as file:
        data = ujson.load(file)

    schedules: list[ScheduleAddSchema] = []
    for schedule in data:
        restaurant_id = [r.id for r in restaursnts if r.title == schedule["title"]][0]
        schedules.append(
            ScheduleAddSchema.model_validate(
                {
                    "restaurant_id": restaurant_id,
                    "start": schedule["start"],
                    "end": schedule["end"],
                }
            )
        )
    return schedules


def load_categories(file_path: str) -> list[CategoryAddSchema]:
    with open(file_path, "r", encoding="utf-8") as file:
        data = ujson.load(file)

    categories: list[str] = []
    for restaurant in data:
        for category in restaurant["menu"]:
            category_name = category["category"]
            if category_name not in categories:
                categories.append(category_name)
    return [CategoryAddSchema.model_validate({"name": name}) for name in categories]


def load_menus(
    file_path: str, restaurants: list[RestaurantSchema], categories: list[CategorySchema]
) -> list[MenuItemAddSchema]:
    with open(file_path, "r", encoding="utf-8") as file:
        data = ujson.load(file)

    menus: list[MenuItemAddSchema] = []
    for restaurant in data:
        resturant_id = [r.id for r in restaurants if r.title == restaurant["restaurant"]][
            0
        ]
        for category in restaurant["menu"]:
            category_id = [c.id for c in categories if c.name == category["category"]][0]
            for item in category["items"]:
                menus.append(
                    MenuItemAddSchema(
                        restaurant_id=resturant_id,
                        category_id=category_id,
                        name=item["name"],
                        price=item["price"],
                        description=item["description"],
                    )
                )
    return menus
