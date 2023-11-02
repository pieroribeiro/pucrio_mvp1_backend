from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from app.models import Base

class Sales(Base):
    __tablename__ = 'sales'

    id           = Column("id", Integer, primary_key=True, autoincrement=True)
    name         = Column("product_id", Integer, nullable=False, unique=True)
    value        = Column("product_value", Float, nullable=False)
    created_at   = Column("created_at", DateTime, default=datetime.now())

    def __init__ (self, product_id: str, product_value: float):
        """
        Arguments:
            product_id: Id of product
            product_value: Value of product
        """

        self.product_id = product_id
        self.product_value = product_value


