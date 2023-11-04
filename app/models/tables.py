from sqlalchemy import String, Integer, DateTime, Float, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime
from app.models import Base

# -------------------- Table Products Definition ---------------------------

class Products(Base):
    __tablename__ = 'products'

    id: Mapped[int]                         = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str]                       = mapped_column(String, nullable=False, unique=True)
    value: Mapped[float]                    = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime]            = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime]            = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def __init__ (self, name: str, value: float):
        """
        Arguments:
            name: Name of Product. Example: Orange
            value: Value of Product. Example: 10.50
        """

        self.name = name
        self.value = value


# -------------------- Table Sales Definition ---------------------------


class Sales(Base):
    __tablename__ = 'sales'

    id: Mapped[int]                         = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    created_at: Mapped[datetime]            = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    total: Mapped[float]                    = mapped_column(Numeric(12, 2), default=0, nullable=False)

    items: Mapped["Sales_Items"]            = relationship("Sales_Items", back_populates="sale")

    def __init__ (self):
        pass


# -------------------- Table Sales Items Definition ---------------------------


class Sales_Items(Base):
    __tablename__ = 'sales_items'

    sale_id: Mapped[int]                    = mapped_column(Integer, ForeignKey("sales.id"), nullable=False, primary_key=True)
    product_id: Mapped[int]                 = mapped_column(Integer, ForeignKey("products.id"), nullable=False, primary_key=True)
    product_quantity: Mapped[float]         = mapped_column(Numeric(12, 2), default=0, nullable=False)

    sale: Mapped["Sales"]                   = relationship("Sales", back_populates="items")
    product: Mapped["Products"]             = relationship("Products")

    def __init__ (self, sale_id: int, product_id: int):
        self.sale_id = sale_id
        self.product_id = product_id
