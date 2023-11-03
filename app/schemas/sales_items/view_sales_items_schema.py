from pydantic import BaseModel

class ViewSalesItemsSchema (BaseModel):
    """
    Define as sales will be returned.
    """
    sale_id: int
    product_id: int
    