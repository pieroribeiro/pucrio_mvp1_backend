from pydantic import BaseModel

class ViewProductSchema (BaseModel):
    """
    Define as product will be returned.
    """
    id: int
    name: str
    value: float
    created_at: str
    updated_at: str
