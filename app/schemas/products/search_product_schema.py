from pydantic import BaseModel, Field

class SearchProductSchema (BaseModel):
    """
    Define structure of search with base in ID or Name of Product.
    """
    id: int = Field(..., description='product id')
