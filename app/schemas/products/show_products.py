from typing import List
from app.models.product import Product

def show_products (products: List[Product]):
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