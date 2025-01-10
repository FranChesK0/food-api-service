from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .database import Model


class Restaurant(Model):
    """
    Restaurant model.

    Attributes:
        title (str): Restaurant title.
        address (str): Restaurant address.
    """

    _repr_columns_number = 3

    title: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    address: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)


class Schedule(Model):
    """
    Schedule model.

    Attributes:
        restaurant_id (int): Restaurant id.
        start (str): Schedule start time.
        end (str): Schedule end time.
    """

    _repr_columns_number = 5

    restaurant_id: Mapped[int] = mapped_column(
        ForeignKey("restaurants.id"), nullable=False
    )
    start: Mapped[str] = mapped_column(nullable=False)
    end: Mapped[str] = mapped_column(nullable=False)


class Category(Model):
    """
    Category model.

    Attributes:
        name (str): Category name.
    """

    _repr_columns_number = 2

    name: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)


class MenuItem(Model):
    """
    Menu item model.

    Attributes:
        category_id (int): Category id.
        name (str): Menu item name.
        price (float): Menu item price.
        description (str): Menu item description.
    """

    _repr_columns_number = 5

    category_id: Mapped[int] = mapped_column(ForeignKey("categorys.id"), nullable=False)
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
