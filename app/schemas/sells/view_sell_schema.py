from pydantic import BaseModel

class ViewSellSchema (BaseModel):
    """
    Define as sell will be returned.
    """
    id: int
    product_id: int
    product_value: float
    created_at: str
    updated_at: str
