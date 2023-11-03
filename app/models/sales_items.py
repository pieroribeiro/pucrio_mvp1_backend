from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models import Base

class Sales_Items(Base):
    __tablename__ = 'sales_items'

    id: Mapped[int]             = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    sale_id: Mapped[int]        = mapped_column(ForeignKey("sales.id"), nullable=False)
    product_id: Mapped[int]     = mapped_column(ForeignKey("products.id"), nullable=False)

    def __init__ (self):
        pass
