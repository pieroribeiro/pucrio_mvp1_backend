from typing import List
from app.models.tables import Sales_Items

def show_sale_items (sale_items: List[Sales_Items]):
    """
    Return an Array of Sale Items.
    """
    results = []
    for sale_item in sale_items:
        results.append({
            "sale_id": sale_item.sale_id,
            "product_id": sale_item.product_id,
            "product_quantity": sale_item.product_quantity
        })

    return {"sale_items": results}