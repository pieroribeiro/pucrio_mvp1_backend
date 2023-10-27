from pydantic import BaseModel

class SearchProductSchema (BaseModel):
    """
    Define structure of search with base in ID or Name of Product.
    """
    id: int
