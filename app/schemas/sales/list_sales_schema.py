from pydantic import BaseModel
from typing import List
from app.schemas.sales.view_sales_schema import ViewSalesSchema

class ListSalesSchema (BaseModel):
    """
    Define the return with list of sales.
    """
    sales: List[ViewSalesSchema]
