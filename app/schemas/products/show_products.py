from typing import List
from app.models.tables import Products

def show_products (products: List[Products]):
    """
    Return an Array of Products.
    """
    results = []
    for product in products:
        results.append({
            "id": product.id,
            "name": product.name,
            "value": product.value,
            "created_at": product.created_at,
            "updated_at": product.updated_at
        })

    return {"products": results}