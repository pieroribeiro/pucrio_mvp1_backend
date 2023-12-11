from pydantic import BaseModel, Field

class SearchSalesItemsSchema (BaseModel):
    """
    Define structure of search with base in ID of Sale Item.
    """
    sale_id: int = Field(..., description='sale id')