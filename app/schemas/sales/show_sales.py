from typing import List
from app.models.sales import Sales

def show_sales (sales: List[Sales]):
    """
    Return an Array of Sale.
    """
    results = []
    for sale in sales:
        results.append({
            "id": sale.id,
            "created_at": sale.created_at
        })

    return {"sales": results}