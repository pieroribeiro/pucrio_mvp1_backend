from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from app.models import Base

class Sales(Base):
    __tablename__ = 'sales'

    id           = Column("id", Integer, primary_key=True, autoincrement=True)
    created_at   = Column("created_at", DateTime, default=datetime.now())

    def __init__ (self):
        pass


