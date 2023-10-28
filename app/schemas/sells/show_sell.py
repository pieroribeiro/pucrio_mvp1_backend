from app.models.sells import Sells

def show_sell (sell: Sells):
    """
    Return an representation of One Product.
    """
    return {
        "id": sell.id,
        "product_id": sell.product_id,
        "product_value": sell.product_value,
        "created_at": sell.created_at,
        "updated_at": sell.updated_at
    }