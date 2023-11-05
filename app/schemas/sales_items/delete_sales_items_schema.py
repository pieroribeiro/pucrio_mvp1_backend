from pydantic import BaseModel, Field

class DeleteSalesItemsSchema (BaseModel):
    """
    Define structure of search with base in ID of Sale Item.
    """
    sale_id: int = Field(..., description='sale id')
    product_id: int = Field(..., description="product id")
