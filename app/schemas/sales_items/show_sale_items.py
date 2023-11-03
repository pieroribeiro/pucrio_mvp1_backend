from typing import List
from app.models.sales_items import Sales_Items

def show_sale_items (sale_items: List[Sales_Items]):
    """
    Return an Array of Sale Items.
    """
    results = []
    for sale_item in sale_items:
        results.append({
            "id": sale_item.id,
            "name": sale_item.name,
            "value": sale_item.value,
            "created_at": sale_item.created_at,
            "updated_at": sale_item.updated_at
        })

    return {"sale_items": results}