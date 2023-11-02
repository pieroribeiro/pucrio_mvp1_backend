from pydantic import BaseModel

class CreateSellSchema (BaseModel):
    """
    Define the representation of new sell
    """
    product_id: int
    product_value: float
