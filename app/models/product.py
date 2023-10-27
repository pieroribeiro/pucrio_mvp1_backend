from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from app.models import Base

class Product(Base):
    __tablename__ = 'products'

    id           = Column("id", Integer, primary_key=True, autoincrement=True)
    name         = Column("name", String(255), nullable=False, unique=True)
    value        = Column("value", Float, nullable=False, default=0)
    created_at   = Column("created_at", DateTime, default=datetime.now())
    updated_at   = Column("updated_at", DateTime, default=datetime.now())

    def __init__ (self, name: str, value: float):
        """
        Arguments:
            name: Name of Product. Example: Orange
            value: Value of Product. Example: 10.50
        """

        self.name = name
        self.value = value


