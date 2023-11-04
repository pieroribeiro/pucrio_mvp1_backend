from app.models.tables import Sales_Items

def show_sale_item (sale_item: Sales_Items):
    """
    Return an representation of One Sale.
    """
    return {
        "sale_id": sale_item.sale_id,
        "product_id": sale_item.product_id
    }