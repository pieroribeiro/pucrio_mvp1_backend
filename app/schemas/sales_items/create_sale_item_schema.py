from pydantic import BaseModel

class CreateSaleItemSchema (BaseModel):
    """
    Define the representation of new Sale Item
    """
    sale_id: int
    product_id: int
