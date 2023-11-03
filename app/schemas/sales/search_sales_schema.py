from pydantic import BaseModel, Field

class SearchSalesSchema (BaseModel):
    """
    Define structure of search with base in ID of Sale.
    """
    id: int = Field(..., description='sale id')
