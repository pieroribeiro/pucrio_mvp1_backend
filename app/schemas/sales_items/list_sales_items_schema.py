from pydantic import BaseModel
from typing import List
from app.schemas.sales_items.view_sales_items_schema import ViewSalesItemsSchema

class ListSalesItemsSchema (BaseModel):
    """
    Define the return with list of sales.
    """
    sales: List[ViewSalesItemsSchema]
