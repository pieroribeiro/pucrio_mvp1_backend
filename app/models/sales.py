from sqlalchemy import DateTime, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime
from app.models import Base
from app.models.sales_items import Sales_Items
from typing import List

class Sales(Base):
    __tablename__ = 'sales'

    id: Mapped[int]                         = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at: Mapped[datetime]            = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    sales_items: Mapped[List["Sales_Items"]] = relationship()

    def __init__ (self):
        pass
