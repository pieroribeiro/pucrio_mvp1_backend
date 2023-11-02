from pydantic import BaseModel

class ViewSalesSchema (BaseModel):
    """
    Define as sales will be returned.
    """
    id: int
    product_id: int
    product_value: float
    created_at: str
    updated_at: str
