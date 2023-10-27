from pydantic import BaseModel
from typing import List
from app.schemas.products.view_product_schema import ViewProductSchema

class ListProductsSchema (BaseModel):
    """
    Define the return with list of products.
    """
    products: List[ViewProductSchema]
