from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models import Base

class Sales_Items(Base):
    __tablename__ = 'sales_items'

    sale_id: Mapped[int]        = mapped_column(ForeignKey("sales.id"), nullable=False, primary_key=True)
    product_id: Mapped[int]     = mapped_column(ForeignKey("products.id"), nullable=False, primary_key=True)

    sales                       = relationship("Sales", back_populates="sales_items")
    products                    = relationship("Products", back_populates="sales_items")

    def __init__ (self, sale_id: int, product_id: int):
        self.sale_id = sale_id
        self.product_id = product_id
