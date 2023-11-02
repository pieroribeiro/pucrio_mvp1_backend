from app.models.sales import Sales

def show_sales (sales: Sales):
    """
    Return an representation of One Product.
    """
    return {
        "id": sales.id,
        "product_id": sales.product_id,
        "product_value": sales.product_value,
        "created_at": sales.created_at,
        "updated_at": sales.updated_at
    }