from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime
from typing import List
from app.models import Base
from app.models.sales_items import Sales_Items

class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int]                 = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str]               = mapped_column(String, nullable=False, unique=True)
    value: Mapped[float]            = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime]    = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime]    = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    sales_items: Mapped[List["Sales_Items"]] = relationship()

    def __init__ (self, name: str, value: float):
        """
        Arguments:
            name: Name of Product. Example: Orange
            value: Value of Product. Example: 10.50
        """

        self.name = name
        self.value = value


