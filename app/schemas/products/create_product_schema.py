from pydantic import BaseModel

class CreateProductSchema (BaseModel):
    """
    Define the representation of new product
    """
    name: str
    value: float
