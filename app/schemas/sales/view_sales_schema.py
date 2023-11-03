from pydantic import BaseModel

class ViewSalesSchema (BaseModel):
    """
    Define as sales will be returned.
    """
    id: int
    created_at: str
